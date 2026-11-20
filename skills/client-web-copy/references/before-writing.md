# Before writing, and the tests every page must pass

## 1. The client context file

Every client repo should have `.claude/client-context.md`. Read it first. If it does not exist, copy `assets/client-context.template.md` into place, fill in what you already know from the site and conversation, and ask the user only for the gaps.

This matters because most bad copy comes from missing context rather than weak writing. Answering these questions once per client means every later page starts from the same understanding instead of guessing again.

## 2. Pre-writing questions

Answer these for the page in front of you. Ask the user for anything the context file and site do not cover.

**The page**
- What type of page is it? (service, landing, homepage, about, case study)
- What is the **one** action a visitor should take? A page with three primary actions has none.

**The reader**
- Who exactly reads this page? A job title and a situation, not a demographic.
- What problem brought them here, in their words?
- What words do they use for it? Get these from reviews, sales emails, enquiry forms, support tickets, forums. Copy their phrasing, not yours.
- What objections or doubts do they have? (price, trust, risk, switching cost, "we tried an agency before")

**The context**
- Where does the traffic come from? (organic search, Google Ads, referral, WhatsApp, email)
- What does the visitor already know when they arrive? A visitor from a specific ad needs less explanation than one from a broad search.

**The offer**
- What exactly is being sold, and what is included?
- What makes it different from the alternatives, including doing nothing?
- What proof exists that you are allowed to use? (named clients, case studies, certifications)

## 3. Writing samples and house style

If the client can give you something they wrote themselves — emails to customers, a brochure, a proposal, a page they like — read it before drafting. Match its sentence length, word choice, formality, punctuation and how it opens and closes. A sample overrides the defaults in this skill. If the client's own writing uses dashes, keep dashes at about the same rate.

If the client has a `.claude/house-style.json` (template in `assets/`), apply it. It holds spelling, banned words, dash policy and formality, and `scripts/copycheck.py --style` enforces the checkable parts.

Without a sample, take the voice from the page type: service pages plain and specific, guides can carry more personality, legal and technical text stays neutral.

## 4. The claim tests

Run these on every headline, benefit line and CTA.

### So what?

For each claim, ask "so what?" If the copy does not answer with something the reader cares about, it is not finished. The fix is usually a "which means…" bridge.

- Before: "We build on Next.js."
- After: "We build on Next.js, so the site loads on a mid-range phone on a slow connection."

### Now you can…

Mentally put "Now you can" in front of the headline or benefit.

- "Now you can… digital marketing agency in Bangalore, run by one team" — reads oddly, but it states a fact; fine for an H1 that names a service.
- "Now you can… unlock growth" — vague and unprovable. Rewrite.
- "Now you can… get enquiries from buyers in Latin America" — compelling and true. Keep.

If the result is vague, obvious or a stretch, rewrite it.

### CTA formula

**Action verb + what they get + qualifier if needed.**

- Weak: "Submit", "Learn more", "Get started", "Contact us"
- Strong: "Get a keyword report for your export markets", "Book a 20-minute site review", "Get a quote within one working day"

The button should tell the reader what happens when they click it.

### Zero risk

Look at the area around each CTA and ask:
- Is the main objection answered nearby?
- Is there a trust signal (named client, certification, case study) close to the ask?
- Are cost, timeline and the next step clear?
- Is anything hidden that will surprise them later?

Remove every reason not to click that you can.

## 5. Google's Who / How / Why test

From Google's helpful-content guidance. Every page should pass all three.

| Question | What to check |
|---|---|
| **Who** made it? | A real company, and for articles a named author with a bio. Required where readers would expect it. |
| **How** was it made? | First-hand evidence, real process, original data. Where readers would reasonably ask, say how it was produced. |
| **Why** does it exist? | To help the reader decide or act — not to catch search clicks, hit a word count, or enter a topic without expertise. |

## 6. E-E-A-T: what proof actually looks like

Google's quality raters weigh Experience, Expertise, Authoritativeness and Trust. For agency and client pages, **experience** is the one most often missing and the easiest to supply honestly:

- Before/after results from real projects
- The actual process, step by step, as it happened
- Real screenshots, photos and work samples rather than stock images
- Named clients and linked case studies
- Specific details only someone who did the work would know

Put this evidence on case study pages and link to it from service pages. Never fabricate any of it (see "Never add a fact" in SKILL.md).

## 7. What to deliver

For writing and rewriting:

1. **The copy**, section by section.
2. **Alternatives** for the H1 and the primary CTA — two or three of each, with a one-line note on what each is doing. The client picks.
3. **Title tag and meta description**, with the exact-match term placed once in each.
4. **Notes** on anything you could not verify, and questions for the client.

For detect mode: findings grouped P0 / P1 / P2, each with the exact text, why it is a problem, and a suggested fix. No edits.
