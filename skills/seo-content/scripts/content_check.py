#!/usr/bin/env python3
"""Pre-publish check for one page (local dev URL or live URL).

Usage:
  python3 -I content_check.py <url> [--term "target term"]

Prints PASS / WARN / INFO lines. WARN items need a fix or a reason.
Reuses the copy metrics from style_score.py in the same folder.
"""
import argparse
import html as htmllib
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from style_score import HYPE, score  # noqa: E402

STAT = re.compile(r"\b\d+(\.\d+)?\s?(%|per ?cent)|\b\d+x\b|\b(study|studies|survey|research|report|data)\s+(shows?|found|suggests?)", re.I)
VAGUE = re.compile(r"\b(studies show|research shows|experts say|industry (data|studies)|according to (experts|studies|research))\b", re.I)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; SeoContentCheck/1.0)"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "replace")


def text_of(fragment):
    return re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--term", default="", help="exact target term to check in title, meta and H1")
    a = ap.parse_args()

    raw = fetch(a.url)
    s = score(a.url)
    if "error" in s:
        print("ERROR", s["error"])
        sys.exit(1)

    out = []

    def add(level, msg):
        out.append((level, msg))

    # Title, meta, H1, canonical, robots, OG
    t = s["title"]
    add("PASS" if 0 < s["title_len"] <= 60 else "WARN", f"title {s['title_len']} chars: {t}")
    add("PASS" if 50 <= s["meta_desc_len"] <= 155 else "WARN", f"meta description {s['meta_desc_len']} chars (aim 120–155)")
    h1s = s["h1"]
    add("PASS" if len(h1s) == 1 else "WARN", f"H1 count {len(h1s)}: {h1s[:2]}")
    canon = re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', raw) or re.search(r'<link[^>]+href="([^"]+)"[^>]+rel="canonical"', raw)
    add("PASS" if canon else "WARN", f"canonical: {canon.group(1) if canon else 'missing'}")
    noindex = re.search(r'<meta[^>]+name="robots"[^>]+content="[^"]*noindex', raw, re.I)
    add("WARN" if noindex else "PASS", "robots: noindex" if noindex else "robots: indexable")
    og = re.search(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', raw)
    add("PASS" if og and "logo" not in og.group(1) else "WARN", f"og:image: {og.group(1) if og else 'missing'}{' (generic logo, use a page-specific image)' if og and 'logo' in og.group(1) else ''}")

    # Target term placement
    if a.term:
        term = a.term.lower()
        meta = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]*)"', raw)
        meta_txt = (meta.group(1) if meta else "").lower()
        for where, txt in (("title", t.lower()), ("meta description", meta_txt), ("H1", " ".join(h1s).lower())):
            add("PASS" if term in txt else "WARN", f"term in {where}: {'yes' if term in txt else 'no'}")
        visible = re.sub(r"<(head|script|style|noscript)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
        body_count = len(re.findall(re.escape(term), text_of(visible).lower()))
        add("INFO", f"term appears {body_count}x in the page text (keep it to title, meta, H1, one FAQ on purpose)")

    # Structure and schema
    add("PASS" if s["question_headings"] >= 2 else "WARN", f"question headings: {s['question_headings']}")
    add("INFO", f"schema: {', '.join(s['schema']) or 'none'}")
    if "FAQPage" not in s["schema"]:
        add("WARN", "no FAQPage schema (add if the page has real FAQs)")
    if s["dates"]:
        add("INFO", f"dates in schema: {s['dates']}")
    add("INFO", f"words {s['words']}, avg sentence {s['avg_sentence']}, long sentences {s['pct_long_sentences']}%")

    # Copy quality signals
    add("PASS" if not s["hype"] else "WARN", f"hype words: {s['hype'] or 'none'}")
    add("PASS" if s["em_en_dashes_per_k"] <= 5 else "WARN", f"dashes per 1k words: {s['em_en_dashes_per_k']} (run client-web-copy copycheck)")
    if s["ai_tells"]:
        add("WARN", f"AI-tell phrases: {s['ai_tells']}")

    # Unsourced statistics: paragraphs/list items with a statistic or study claim and no link
    flagged = []
    for frag in re.findall(r"<(p|li|td)[^>]*>(.*?)</\1>", raw, re.S | re.I):
        inner = frag[1]
        txt = text_of(inner)
        if len(txt.split()) < 6:
            continue
        if (STAT.search(txt) or VAGUE.search(txt)) and "<a " not in inner:
            flagged.append(txt[:160])
    if flagged:
        add("WARN", f"{len(flagged)} block(s) with a statistic or study claim and no link (check each has a source):")
        for f in flagged[:8]:
            out.append(("    ", f))
    else:
        add("PASS", "no unsourced statistics found")

    # Links
    social = {"linkedin.com", "twitter.com", "x.com", "wa.me", "facebook.com", "instagram.com", "maps.google.com", "youtube.com"}
    ext = [d for d in s["external_domains"] if d not in social]
    add("PASS" if s["internal_links"] >= 3 else "WARN", f"internal links (body): {s['internal_links']}")
    add("INFO", f"outbound domains (excl. social): {ext or 'none'}")
    add("INFO", f"opening paragraph ({s['first_para_words']} words): {s['first_para'][:200]}")

    for level, msg in out:
        print(f"{level:5} {msg}")
    warns = sum(1 for lvl, _ in out if lvl == "WARN")
    print(f"\n{warns} warning(s).")


if __name__ == "__main__":
    main()
