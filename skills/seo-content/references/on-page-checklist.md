# Pre-publish checklist

Run this before calling a page done. `scripts/content_check.py <url> --term "<target term>"` checks the items marked (auto).

## Search basics
- [ ] Title is 60 characters or fewer, contains the target term, and carries the answer where possible (auto)
- [ ] Meta description is 155 characters or fewer, contains the term, says what the page gives (auto)
- [ ] Exactly one H1, the searcher's query in their words (auto)
- [ ] Canonical points to the page's own final URL (www vs non-www correct) (auto)
- [ ] The page is indexable: no stray noindex; not blocked in robots.txt (auto: noindex)
- [ ] The URL is short and descriptive; old URLs redirect to it if it replaces a page

## Content
- [ ] The first one or two sentences answer the main question (auto: first paragraph shown for review)
- [ ] H2/H3 questions match People Also Ask and Search Console queries (auto: counts question headings)
- [ ] Every statistic has a named, linked source (auto: flags unsourced numbers for review)
- [ ] No hype words; no "best/first/leading" claims (auto)
- [ ] client-web-copy's copycheck passes, for prose quality
- [ ] Facts match the client's material and are dated where they can change
- [ ] Real screenshots or photos, with useful alt text and captions
- [ ] The CTA asks for the next step that fits the intent

## Structure and schema
- [ ] Schema matches visible content: FAQPage, Article/BlogPosting (author, datePublished, dateModified), Service, Product/Offer, LocalBusiness/Dentist, BreadcrumbList as fits (auto: lists types)
- [ ] OG and Twitter image, 1200×630, specific to the page (auto: og:image present)
- [ ] Author page exists for guides and posts

## Links
- [ ] At least 3 internal links out to related pages (auto: counts)
- [ ] At least 5 related pages link in, in the body text where it reads naturally (navigation and footer count for little)
- [ ] Outbound links to the things the page discusses: tools, rules, the client's site (auto: lists external domains)
- [ ] No broken links

## Ship
- [ ] Added to the sitemap; sitemap lastmod updates
- [ ] Added to llms.txt (and llms-full.txt) with a factual summary
- [ ] Deployed; live URL returns 200 and shows the new content
- [ ] IndexNow submitted for new and changed URLs (if the site has a key)
- [ ] Search Console: sitemap resubmitted; Request indexing for the page and the main pages linking to it
- [ ] Change logged (date, URL, target term, what changed)
- [ ] A check date set for 2–4 weeks out
