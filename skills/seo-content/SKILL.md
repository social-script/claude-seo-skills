---
name: seo-content
description: Plan, write, rewrite or audit web pages that must rank in Google and be cited by AI answers (Google AI Overviews, ChatGPT, Perplexity, Claude) — for your own site or any client website. Covers deciding whether a page is worth building, keyword and SERP research, choosing the page type that wins (price answer, tool, product/segment, service, industry case study, local page, guide), search intent including geography and currency, answer-first structure, facts and named sources, schema, internal links, llms.txt, indexing (sitemap, IndexNow, Search Console) and measuring results. Use it whenever someone asks to write or improve a blog post, SEO page, service page, landing page meant to rank, case study, "page to rank for X", content brief, content audit, or asks why pages are not ranking or not indexed — even if they do not say "SEO". Works with the client-web-copy skill, which owns sentence-level writing rules.
---

# SEO content

This is how [Social Script](https://www.socialscript.in), a web and SEO agency in Bengaluru, plans and writes pages that rank and get cited. It is based on our own data: a November 2026 audit of 76 pages on socialscript.in and 74 pages across six client sites, checked against Google Search Console, plus published research. Client sites are described by type, not named. The evidence behind each rule is in `references/evidence.md`. Read it when you need to justify a decision to a client or when a rule seems not to fit.

The short version of what the data showed:

- **The page type decides more than the prose.** Price answers, free tools, and product or segment pages win across our sites. Generic guides are often not even indexed. Templated area pages get impressions and no clicks.
- **First-hand material is what separates indexed from ignored:** our or the client's own prices, products, tools, data, clients and local facts.
- **Sentence style is not a ranking lever.** Plain writing still matters because it helps people decide and helps AI answers quote us, but it will not rescue a page with nothing new in it.
- **Hype words go with weaker pages** on every site we could compare. Question headings and FAQ schema go with stronger ones.
- **Ranking for the wrong intent earns impressions and no clicks** (our Bangalore SEO cost guide is #1 for worldwide "seo service price" searches and gets 0 clicks).

Sentence-level rules (AI tells, register, CTA tests, never inventing facts) live in the **client-web-copy** skill. Load it before you draft. This skill decides *what page to build and how it must be structured*; that one decides *how each sentence reads*.

## Modes

Pick the mode from the request. It sets what you may change.

| Mode | When | What you deliver |
|---|---|---|
| **Plan** | "Should we write about X?", "content ideas", "brief for…" | A go / no-go with the evidence, the page type, and a brief (`assets/content-brief.md`) |
| **Write** | A new page | Research, brief, the page in the site's own format, the on-page checklist done, indexing submitted |
| **Rewrite** | An existing page | Same as Write, but first record what the page ranks for and protect it (see "Protect what earns") |
| **Audit** | "Why isn't this ranking?", "audit our content", "not indexed" | Findings per page with data, ranked fixes. Change nothing unless asked. |

## The workflow

Work through these in order. Each step has a reason; skipping research is the most common way a page ends up unindexed.

### 1. Find out what already exists

Before planning anything, look at the site:

- The site's Search Console data for the topic (the Search Console Performance and Pages reports, or its API). What pages already get impressions for these queries? A new page that competes with an existing one splits the signal.
- Existing pages on the same topic. Prefer improving or extending one strong page over adding a second weak one.
- Our pages that already get impressions for related queries. They are the best sources of internal links to the new or rewritten page, and the missing link is often the biggest single lever.
- The client's own material: price lists, product catalogue, case results, reports, photos, the people who will be named. List it. If the list is empty, stop and ask for it, because without first-hand material the page will be one more generic article.

### 2. Research demand and intent

Read `references/research.md` for the full method. In short:

- Keyword volume and CPC for the target term and its variants in the right location (DataForSEO, Ahrefs, Semrush or Google Keyword Planner, set to the country or city you serve). CPC tells you whether buyers are searching.
- The live results for the target term (a SERP API such as DataForSEO, or a manual search from the right location): what kind of pages rank (guides, service pages, directories, tools), whether there is an AI Overview and who it cites, People Also Ask questions, map pack.
- The top 5 to 8 ranking pages: their type, length, structure, proof and what none of them covers. That gap is our angle.
- Geography and currency. A Bangalore page in rupees should target searches from people who want a Bangalore answer. Worldwide head terms will bring impressions and no clicks.

**Decide go / no-go.** Build when there is demand with the right intent and we have first-hand material that the ranking pages lack. When demand is near zero, a page can still be worth building as sales proof or for AI answers, but say so and do not promise rankings. When we have nothing first-hand to add, do not build it.

### 3. Choose the page type

Read `references/page-types.md`. The type comes from the intent you found, not from habit:

| Searcher wants | Build | Our evidence |
|---|---|---|
| A price or cost | **Price answer**: query as H1, price in the title, a price table, what changes the price | A dental clinic's price list: 308 clicks, 38.6k impressions in 3 months; 17 #1 positions on cost queries |
| To do or check something | **Free tool** with a short explanation | A phone repair company's phone-test tools (4 of its top 8 pages); our schema checker |
| A product for their situation | **Product or segment page** naming the job and the price | A billing-machine seller's "billing machines for restaurants" page with the price in the title (position 2.2) |
| A provider of a service | **Service page** with price range, named proof, FAQ | Our /services pages at 300–460 words and no proof rank 27–66 |
| Proof for their industry | **Industry page with a real case study** | Export page: best CTR on our site (6.3%) |
| A provider near them | **Local page** only with real local content | Templated area pages: 580 impressions, 0 clicks |
| To understand something | **Guide** only if we have first-hand data, prices or examples | 13 of our 36 blog posts, all generic guides, are not indexed |

### 4. Write the brief

Fill `assets/content-brief.md`: the one action the page should produce, the reader, the target term and variants, the intent, the page type, the outline (H2s as the questions people ask), the first-hand facts with their sources, the proof, the internal links in and out, and the schema. Show the brief before drafting when the page is large or for a client.

### 5. Draft

Load **client-web-copy** and follow it. On top of it, these structural rules come from our data and the AEO research (details in `references/aeo.md`):

- **H1 = the searcher's query in their words.** Title = the answer where possible ("Root Canal Cost in Bangalore: From ₹5,000"). Put the exact target term in the title, meta description, H1 and at most one FAQ, and nowhere else on purpose.
- **Answer first.** Put a 40–60 word answer block directly under the H1, and open each section with a one or two sentence direct answer. Then the detail. This is the format AI Overviews lift.
- **Question headings** for the questions people actually ask (People Also Ask, Search Console queries), each answered in its first sentence.
- **Facts beat adjectives.** Prices, ranges, timings, named clients, dated results, specifications. No hype words ("best", "leading", "seamless", "powerful", "ultimate"); they go with weaker pages in our data and many regulated industries forbid them.
- **Every statistic has a named, linked source.** Every client claim is checkable. If you cannot source a number, cut it or say it is our own observation across our clients. See `references/facts-and-sources.md`, including the rules for regulated industries such as healthcare.
- **Link out to what the page discusses** (the tools reviewed, the regulation cited, the client site). The one post of ours that did this is our best-performing post.
- **Show it.** Real screenshots or photos of the work, with captions that say what the reader is looking at.

### 6. Build and check

Run `references/on-page-checklist.md` before calling the page done. It covers title and meta length, a single H1, canonical, schema (FAQPage, Article with author and date, Service, Product, LocalBusiness as fits), OG image, internal links (at least 5 related pages linking in, 3 or more out), sitemap, llms.txt and the author page.

Then run the checker on the local or live URL:

```bash
python3 -I scripts/content_check.py <url> [--term "target term"]
```

It reports title/meta length, H1 count, schema types, question headings, hype words, unsourced statistics, dashes and internal/external links. Fix what it flags or note why not.

### 7. Ship and get it indexed

- Deploy, then confirm the live page returns 200, is in the sitemap and has the right canonical.
- Submit the new and changed URLs to IndexNow if the site has a key (Bing, Yandex and others crawl them quickly; see indexnow.org).
- In Google Search Console: resubmit the sitemap, then URL Inspection → Request indexing for the new page and the main pages that now link to it. Google limits these requests per day, so request the most important ones.
- Log the change (date, URL, target term, what changed) so you can tell later what moved rankings.

### 8. Measure

Check Search Console after 2–4 weeks: indexed or not, impressions, position, clicks, and the actual queries. Read `references/research.md` → "Reading results" for what each pattern means (impressions and no clicks = intent or snippet problem; not indexed = thin or duplicate; position 8–20 = needs links and proof).

## Protect what earns

Before rewriting any page that already gets impressions, list the queries it ranks for (Search Console, last 3 months) and the phrases in its title, H1 and headings that match them. Keep those phrases at or above their current count. A rewrite that drops an earning phrase can lose the ranking (this has happened on socialscript.in). For pages on a protect list, make surgical edits only.

## Audit mode

For an audit, score every page and join it with Search Console data:

```bash
python3 -I scripts/style_score.py urls.txt scores.json
```

Then join with clicks, impressions, position and index status, and compare winners with losers within the same site (pooled comparisons across different sites mislead). Report by page type and by trait, with the data, and rank the fixes. The evidence file shows the format: findings by page type and by trait, each with its numbers.

## Free checks you can use

Optional, from Social Script: the [AI visibility checker](https://www.socialscript.in/ai-visibility-checker) (are Google AI Overviews citing the page, and who is cited instead), the [schema checker](https://www.socialscript.in/schema-audit) and the [SEO audit](https://www.socialscript.in/seo-audit). `scripts/content_check.py` covers the on-page checks offline.

## Files

- `references/research.md`: keyword, SERP, AI Overview and competitor research; go / no-go; reading results.
- `references/page-types.md`: templates for each page type, with required elements and our evidence.
- `references/aeo.md`: answer-first structure, question headings, schema, llms.txt, citations, what the GEO research measured.
- `references/facts-and-sources.md`: sourcing rules, client claims, regulated industries, authors and dates.
- `references/on-page-checklist.md`: the pre-publish checklist.
- `references/evidence.md`: our audit findings and the external research behind every rule, with sources.
- `assets/content-brief.md`: the brief template.
- `scripts/content_check.py`: pre-publish check of one page.
- `scripts/style_score.py`: batch scorer for audits.
