# Evidence behind the rules

Use this to explain a recommendation to a client, or to decide whether a rule applies to an unusual page. Our own data comes first; external research second. Re-run the audit (SKILL.md → Audit mode) every six months and update this file.

## Our audit, November 2026

Data: Google Search Console, 3 months to 18 Nov 2026; style scores of the live copy.

**socialscript.in (76 pages; 206 clicks, 24.1k impressions in 3 months)**

| Finding | Data |
|---|---|
| Generic posts are not indexed | 13 of 36 blog posts not indexed; all general AI/design/dev topics with no sources and few internal links; 12 by one author with no author page |
| Local, commercial guides are indexed | Every Bangalore guide with our own prices is indexed (5–8 internal links each) |
| Curated list with outbound links wins | design-inspiration post: 52 clicks, 3,963 impressions, position 6.4; the only post linking out (13 sites) |
| Price answer wins its local intent | SEO cost guide: #1 for "seo pricing in bangalore", "seo cost in bangalore" |
| Wrong geography = no clicks | Same guide: #1 for "seo service price" (585 impressions) and "search engine optimization services cost" (719) with 0 clicks |
| A tool wins | /schema-audit: 35 clicks, 3,078 impressions |
| Thin service pages rank low | /services/* at 300–460 words, no proof: positions 27–66 |
| Style does not separate winners | Top pages: 20.9-word sentences, 24 dashes/1k; not-indexed posts: 15.6 and 17.3 |

**Client sites (74 pages from the 6 sites with most clicks)**

| Finding | Data |
|---|---|
| Price pages win | Dental clinic (Bengaluru): price list 308 clicks, 38.6k impressions; treatment cost pages next; 17 #1 and 6 #2 Bengaluru positions, all cost or treatment queries |
| Tools win | Phone repair company: 4 of its top 8 pages are phone-test tools (~450 words, ~10% CTR) |
| Segment pages with price win | Billing-machine seller: top 5 pages are segment collections; a product page with the one-time price in the title at position 2.2 |
| Hype goes with weak pages | Hype words/1k, best vs weak: pooled 0.3 vs 1.1; dental clinic 1.0 vs 2.5; CAD services firm 0.9 vs 2.8 |
| Question headings and FAQ go with strong pages | Pooled question headings 3 vs 0; B2B trading company: FAQ schema on 7 of 8 best pages, 1 of 6 weak |
| Templated area pages fail | Dental clinic's area pages: 580 impressions, 0 clicks; 256, 0 |
| Generic guides fail on client sites too | B2B trading company's "complete guide" and "X vs Y" posts not indexed |

Caveats: samples are small (48 best, 26 weak); pooled comparisons mix site types; differences under ~1.5x may be noise. Within-site comparisons are more reliable.

## External research

| Claim | Source |
|---|---|
| Readability is not a Google ranking factor | John Mueller, Google Webmaster Office Hours, Jan 2018, reported by Search Engine Journal: https://www.searchenginejournal.com/ranking-factors/reading-level-ranking-factor/ |
| Readability scores do not correlate with rankings | Ahrefs, 15,000 keywords: https://ahrefs.com/blog/flesch-reading-ease ; Portent: https://portent.com/blog/content/study-how-content-readability-affects-seo-and-rankings.htm |
| Sources, statistics and quotations raise AI-answer visibility most; fluency and simple language help; keyword stuffing hurts | GEO, Aggarwal et al., KDD 2024: https://arxiv.org/abs/2311.09735 |
| Concise, scannable, objective writing improved measured usability by 124% (1997, one site) | Nielsen Norman Group: https://www.nngroup.com/papers/webwriting/rewriting.html |
| Controlled English improves comprehension and translation | Holmback & Spyridakis 1996; Roturier 2004; Preux 2005 (ACL Anthology) |
| No published evidence that ASD-STE100 itself improves rankings | Searched Nov 2026; none found |
| Google asks who created content and why (E-E-A-T) | Google, Creating helpful, reliable, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content |
