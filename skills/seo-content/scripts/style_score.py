#!/usr/bin/env python3
"""Fetch live pages and score their copy against our content style rules.

Usage: python3 -I style_score.py <urls.txt> <out.json>
Each line of urls.txt is a URL. Output: list of dicts with metrics per URL.
"""
import concurrent.futures as cf
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urlparse

HYPE = [
    "best", "leading", "cutting-edge", "cutting edge", "world-class", "seamless", "seamlessly", "robust",
    "unlock", "unleash", "elevate", "empower", "revolutionize", "revolutionise", "game-changer", "game changer",
    "supercharge", "ultimate", "next-level", "state-of-the-art", "innovative", "top-notch", "premier",
    "unparalleled", "unmatched", "stunning", "transformative", "skyrocket", "effortless", "effortlessly",
    "magic", "secret", "powerful", "incredible", "amazing", "perfect", "guaranteed",
]
AI_TELLS = [
    r"in today'?s (fast-paced |digital |competitive )?(world|landscape|age|market)", r"\blet'?s dive\b", r"\bdive into\b",
    r"\bdelve\b", r"\blandscape\b", r"\bnavigat(e|ing) the\b", r"\bharness(ing)? the power\b", r"\bin conclusion\b",
    r"\bwhether you'?re\b", r"\bit'?s not just\b", r"\bnot only\b.{0,60}\bbut also\b", r"\btapestry\b", r"\brealm\b",
    r"\bever-evolving\b", r"\bfast-paced\b", r"\bat the end of the day\b", r"\bthe key to\b", r"\bunlock(ing)? the\b",
    r"\bhere'?s the thing\b", r"\bgame[- ]chang", r"\bnow more than ever\b", r"\bin the world of\b",
    r"\bplays a (crucial|vital|pivotal) role\b", r"\bcrucial\b", r"\bpivotal\b", r"\bvital\b", r"\bseamless\b",
]
PASSIVE = re.compile(r"\b(is|are|was|were|be|been|being)\s+(\w+ly\s+)?\w+(ed|en)\b", re.I)
NUMBER = re.compile(r"(₹|\$|£|€)\s?\d|\b\d+(\.\d+)?\s?(%|per ?cent|x\b|k\b|lakh|crore|ms\b|s\b|seconds|days|weeks|months|hours|minutes)|\b\d{2,}\b")


class Extract(HTMLParser):
    SKIP = {"head", "script", "style", "noscript", "svg", "nav", "footer", "header", "form", "button", "select", "option"}

    def __init__(self):
        super().__init__()
        self.depth_skip = 0
        self.stack = []
        self.blocks = []  # (tag, text)
        self.cur = []
        self.links = []
        self.jsonld = []
        self.in_jsonld = False
        self.title = ""
        self.in_title = False
        self.meta = {}
        self.h = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "script" and a.get("type") == "application/ld+json":
            self.in_jsonld = True
            self.jsonld.append("")
            return
        if tag == "title":
            self.in_title = True
        if tag == "meta" and a.get("name") in ("description",):
            self.meta["description"] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical":
            self.meta["canonical"] = a.get("href", "")
        if tag in self.SKIP:
            self.depth_skip += 1
            return
        if tag == "a" and self.depth_skip == 0 and a.get("href"):
            self.links.append(a["href"])
        if tag in ("p", "li", "h1", "h2", "h3", "h4", "td", "dd", "dt", "blockquote", "figcaption"):
            self._flush()
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag == "script" and self.in_jsonld:
            self.in_jsonld = False
            return
        if tag == "title":
            self.in_title = False
        if tag in self.SKIP:
            self.depth_skip = max(0, self.depth_skip - 1)
            return
        if tag in ("p", "li", "h1", "h2", "h3", "h4", "td", "dd", "dt", "blockquote", "figcaption"):
            self._flush(tag)

    def handle_data(self, data):
        if self.in_jsonld:
            self.jsonld[-1] += data
            return
        if self.in_title:
            self.title += data
        if self.depth_skip:
            return
        self.cur.append(data)

    def _flush(self, tag=None):
        text = re.sub(r"\s+", " ", "".join(self.cur)).strip()
        self.cur = []
        if text:
            t = tag or (self.stack[-1] if self.stack else "div")
            self.blocks.append((t, text))
            if t in ("h1", "h2", "h3"):
                self.h.append((t, text))
        if tag and self.stack and self.stack[-1] == tag:
            self.stack.pop()


def ld_types(chunks):
    types, dates = set(), {}
    for c in chunks:
        try:
            data = json.loads(c)
        except Exception:
            continue
        stack = [data]
        while stack:
            x = stack.pop()
            if isinstance(x, dict):
                t = x.get("@type")
                if isinstance(t, str):
                    types.add(t)
                elif isinstance(t, list):
                    types.update(t)
                for k in ("datePublished", "dateModified"):
                    if k in x and isinstance(x[k], str):
                        dates[k] = x[k][:10]
                stack.extend(x.values())
            elif isinstance(x, list):
                stack.extend(x)
    return sorted(types), dates


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9“\"(])", text)
    return [p for p in parts if len(p.split()) >= 3]


def score(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; SocialScriptAudit/1.0)"})
        with urllib.request.urlopen(req, timeout=40) as r:
            html = r.read().decode("utf-8", "replace")
    except Exception as e:
        return {"url": url, "error": str(e)[:120]}
    p = Extract()
    p.feed(html)
    p._flush()
    host = urlparse(url).netloc.replace("www.", "")
    body_blocks = [(t, x) for t, x in p.blocks if t not in ("h1", "h2", "h3", "h4")]
    text = " ".join(x for _, x in body_blocks)
    words = re.findall(r"[A-Za-z][A-Za-z'’-]*", text)
    wc = len(words)
    sents = sentences(" ".join(x for t, x in body_blocks if t in ("p", "li", "dd", "td", "blockquote")))
    slen = [len(s.split()) for s in sents]
    low = text.lower()
    hype_hits = {w: len(re.findall(r"\b" + re.escape(w) + r"\b", low)) for w in HYPE}
    hype_hits = {k: v for k, v in hype_hits.items() if v}
    tells = {}
    for pat in AI_TELLS:
        n = len(re.findall(pat, low))
        if n:
            tells[pat.strip("\\b")] = n
    ext = sorted({urlparse(l).netloc.replace("www.", "") for l in p.links if l.startswith("http") and host not in urlparse(l).netloc})
    internal = [l for l in p.links if l.startswith("/") or host in l]
    types, dates = ld_types(p.jsonld)
    h2 = [x for t, x in p.h if t == "h2"]
    q_heads = [x for t, x in p.h if t in ("h2", "h3") and x.strip().endswith("?")]
    first_p = next((x for t, x in body_blocks if t == "p" and len(x.split()) >= 8), "")
    per_k = lambda n: round(1000 * n / wc, 1) if wc else 0
    return {
        "url": url,
        "title": p.title.strip(),
        "title_len": len(p.title.strip()),
        "meta_desc_len": len(p.meta.get("description", "")),
        "h1": [x for t, x in p.h if t == "h1"][:2],
        "words": wc,
        "h2_count": len(h2),
        "question_headings": len(q_heads),
        "avg_sentence": round(sum(slen) / len(slen), 1) if slen else 0,
        "pct_long_sentences": round(100 * sum(1 for n in slen if n > 25) / len(slen)) if slen else 0,
        "em_en_dashes_per_k": per_k(text.count("—") + text.count(" – ")),
        "hype_per_k": per_k(sum(hype_hits.values())),
        "hype": hype_hits,
        "ai_tells_per_k": per_k(sum(tells.values())),
        "ai_tells": tells,
        "passive_per_k": per_k(len(PASSIVE.findall(text))),
        "numbers_per_k": per_k(len(NUMBER.findall(text))),
        "external_domains": ext[:15],
        "external_count": len(ext),
        "internal_links": len(internal),
        "schema": types,
        "dates": dates,
        "first_para_words": len(first_p.split()),
        "first_para": first_p[:220],
    }


def main():
    urls = [u.strip() for u in open(sys.argv[1]) if u.strip()]
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        res = list(ex.map(score, urls))
    json.dump(res, open(sys.argv[2], "w"), indent=1, ensure_ascii=False)
    ok = [r for r in res if "error" not in r]
    print(f"scored {len(ok)}/{len(res)}")
    for r in res:
        if "error" in r:
            print("ERR", r["url"], r["error"])


if __name__ == "__main__":
    main()
