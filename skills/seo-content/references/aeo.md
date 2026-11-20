# AEO: being quoted by AI answers

AEO (answer engine optimisation, also called GEO) is making a page easy for Google AI Overviews, ChatGPT, Perplexity and Claude to understand, quote and cite. Most of it is the same as good SEO structure; a few things matter more.

## What the research measured

The GEO paper (Aggarwal et al., KDD 2024, arXiv 2311.09735) rewrote pages in different ways and measured how much of each page generative engines used (position-adjusted word count, computed from its Table 1):

| Change | Visibility |
|---|---|
| Adding quotations from relevant sources | +41% |
| Adding statistics | +31% |
| More fluent wording | +28% |
| Citing sources | +28% |
| Technical terms | +18% |
| Simpler, easy-to-understand language | +14% |
| Keyword stuffing | −8% |

So: checkable facts with named sources help most; clear wording helps; stuffing hurts. Our own data could not test citations (almost no page on our sites cites anything), so the playbook follows the research here.

## Rules

1. **Answer first.** The first one or two sentences of the page, and of each section, answer the question directly. Definition questions get a one-sentence definition ("Digital marketing for dental clinics is…").
2. **Question headings.** Use the People Also Ask questions and Search Console queries as H2/H3s, each answered in its first sentence. Our stronger pages have more question headings.
3. **Lists and tables** for steps, options and prices. AI answers lift numbered lists and tables.
4. **Named sources with links** for every statistic, rule or claim that is not our own. Quote the exact clause or figure where it matters.
5. **Consistent facts everywhere.** Prices, hours, address and phone must match across the site, Google Business Profile and directories. Conflicting facts make engines unsure which to quote.
6. **Server-rendered HTML.** Crawlers and most AI fetchers read the raw HTML. Content that appears only after JavaScript runs may not be read.
7. **Schema** that describes the page truthfully: FAQPage for real FAQs, Article/BlogPosting with author and dates, Service, Product with offers, LocalBusiness or a specific type (Dentist), BreadcrumbList. Never mark up content that is not visible.
8. **llms.txt.** Add the page to the site's `llms.txt` (and `llms-full.txt` if it exists) with a two- or three-sentence factual summary.
9. **Off-site presence.** AI answers often cite YouTube, LinkedIn, Reddit and directories more than agency sites. For important topics, plan a short video, LinkedIn posts linking to the page, and directory profiles. Check who is cited for your questions with an AI visibility tool, such as our free [AI visibility checker](https://www.socialscript.in/ai-visibility-checker).

## Check

After launch, search the target questions in Google (AI Overview), ChatGPT and Perplexity and note whether the page or site is cited. Repeat monthly with `check_ai_visibility` for the site's main topics.
