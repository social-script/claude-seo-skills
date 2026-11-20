# Claude SEO skills from Social Script

Two Agent Skills for Claude Code, Claude.ai and other agents that read `SKILL.md`:

- **seo-content** plans, writes, rewrites and audits web pages that need to rank in Google and be cited by AI answers (Google AI Overviews, ChatGPT, Perplexity, Claude).
- **client-web-copy** sets the sentence-level rules for website copy: industry register, pain points in the customer's words, headline and CTA tests, removing AI tells, and never inventing facts.

They are the skills [Social Script](https://www.socialscript.in), a web and SEO agency in Bengaluru, uses on its own site and on client sites. The rules come from our own data, not from a tips list.

## What the rules are based on

In November 2026 we checked 150 pages against three months of Google Search Console data: 76 pages on socialscript.in and 74 pages from the six client sites with the most search traffic. What we found:

| Finding | Data |
|---|---|
| The page type matters more than the writing | Price pages, free tools and product pages for a specific job won on every site. 13 of our 36 blog posts were not indexed, all of them generic. |
| First-hand material separates indexed from ignored | Every guide with our own prices was indexed; every trend and tips post without them was skipped. |
| Writing style alone does not predict ranking | Our top pages had longer sentences (median 20.9 words) than the posts Google skipped (15.6). |
| Hype words go with weaker pages | 0.3 per 1,000 words on strong client pages against 1.1 on weak ones. |
| Question headings and FAQ schema go with stronger pages | Median question headings 3 against 0; FAQ schema on 81% against 69%. |
| Ranking for the wrong searcher earns nothing | Our Bangalore SEO cost guide ranks first for worldwide "seo service price" searches and gets no clicks. |

The full evidence, with the external research (Google's guidance, the Ahrefs readability study, the GEO paper), is in [`skills/seo-content/references/evidence.md`](skills/seo-content/references/evidence.md). The write-up: [How to write SEO content: what ranked across 150 of our pages](https://www.socialscript.in/blog/how-to-write-seo-content-that-ranks-2026).

## What seo-content does

It works in four modes:

| Mode | Use it for | You get |
|---|---|---|
| Plan | "Should we write about X?" | A go / no-go with the evidence, the page type, and a content brief |
| Write | A new page | Research, brief, the page, the on-page checklist, indexing steps |
| Rewrite | An existing page | The same, after recording what the page already ranks for so the rewrite does not lose it |
| Audit | "Why isn't this ranking?" | Findings per page with data and ranked fixes |

It picks the page type from the search intent (price answer, free tool, product or segment page, service page, industry case study, local page, guide), puts the answer first, turns People Also Ask into question headings, requires a named, linked source for every statistic, and covers schema, internal links, llms.txt and indexing.

Two scripts run without any API keys:

```bash
# Pre-publish check of one page: title, meta, H1, canonical, schema, question headings,
# hype words, unsourced statistics, dashes, internal and outbound links
python3 -I skills/seo-content/scripts/content_check.py https://example.com/page --term "target term"

# Score many pages for an audit
python3 -I skills/seo-content/scripts/style_score.py urls.txt scores.json
```

## Install

**Claude Code (plugin)**

```
/plugin marketplace add social-script/claude-seo-skills
/plugin install seo-skills@social-script
```

**Any agent that supports Agent Skills**

```bash
npx skills add social-script/claude-seo-skills
```

**By hand:** copy `skills/seo-content` and `skills/client-web-copy` into `~/.claude/skills/` (personal) or `.claude/skills/` in a project.

**Claude.ai:** download the zip files from the [latest release](https://github.com/social-script/claude-seo-skills/releases/latest) and upload them in Settings → Capabilities → Skills.

## Use

Ask in plain words. For example:

- "Should we write a page about root canal cost in Pune? Plan it."
- "Rewrite /services/web-design so it ranks for web design company in Chennai."
- "Audit our blog. Why are half the posts not indexed?"
- "Review the copy on this landing page. It sounds like AI wrote it."

Keyword and results-page data are optional. The skill works with whatever you have: DataForSEO, Ahrefs, Semrush, Search Console, or a manual search from the right location.

## Free checks

Optional tools from Social Script that pair with the skill:

- [AI visibility checker](https://www.socialscript.in/ai-visibility-checker): are Google AI Overviews citing your site for 5 searches, and who is cited instead
- [Schema checker](https://www.socialscript.in/schema-audit): validates structured data against Google's rich-result rules
- [SEO audit](https://www.socialscript.in/seo-audit): full-site technical check with a fix list

## Notes

- Client sites in the evidence are described by type ("a dental clinic", "a phone repair company"), not named.
- Some examples are Indian (rupee prices, Bengaluru, Indian dental advertising rules). The method is not tied to a country.
- Re-run the audit every six months; we will update the evidence when we do.

## Licence

MIT. Built by [Social Script](https://www.socialscript.in). Issues and pull requests are welcome.
