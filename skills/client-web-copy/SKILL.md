---
name: client-web-copy
description: Write, rewrite or review website copy for agency clients — service pages, landing pages, homepages, industry/vertical pages, case studies, About pages, headlines and CTAs — so it reads as a company that works in the client's industry, not as generic AI marketing copy. Use whenever writing or editing any page a business will publish to win customers, especially B2B (exporters, manufacturers, traders, clinics, professional services), and whenever copy is described as sounding "too AI", "generic", "like ChatGPT wrote it", or needs to match a client's or competitor's tone. Also use to audit existing copy without rewriting it. Trigger even if the user doesn't name this skill. Covers pre-writing questions, register and industry vocabulary, pain points, headline and CTA tests, stripping AI tells by severity, never inventing facts, keyword restraint, E-E-A-T proof, and when statistics help versus hurt.
---

# Client Web Copy

## Why AI copy sounds like AI

A language model writes whatever is most likely to come next, so by default it makes the choice that suits the widest range of readers. A person writing for a client makes choices for one reader in one industry, so their writing is uneven and specific. Every AI tell is a version of that safe default: the contrast that adds weight instead of a fact, the list of three because three sounds complete, the dash that avoids deciding how two ideas relate, the invented person who makes a point vivid.

Business buyers are not reading for prose quality. They are scanning for evidence that you understand their business, and they decide that from **vocabulary and problems**. That is why AI copy fails in a way that is hard to name: it is often well written, just not written by anyone in the trade. The client says "it's good, but it doesn't sound like us", and they are right.

The fix is to write from inside the reader's business, for one reader.

## Modes

Pick the mode from the request. It decides how much you are allowed to change.

- **Write** — a new page or section. Run the full process below.
- **Rewrite** — improve existing copy. Keep every claim that is supported. Change wording and, if asked, structure.
- **Detect** — report problems only, change nothing. Use this for copy the client wrote themselves, for any page on a protect-list (pages that already rank), and whenever the user asks for a review or audit. Finding a problem never by itself authorises changing it.

## Two rules that override everything

**1. Never add a fact.** When writing or rewriting, do not introduce a number, name, date, location, client, certification, quote, statistic or claim that is not in the source material or given by the user. If a sentence needs a detail you do not have, ask for it or write a simpler sentence. Check claims about the client's own site against the live site. A plausible guess published as fact is worse than any AI tell.

**2. Never inject a fake human voice.** Removing AI tells tends to install a different fingerprint: an invented speaker ("in my experience", "I've seen this a hundred times"), manufactured stakes ("now more than ever", "in a world where"), forced contrarianism ("everyone says X, but they're wrong"), performed candour ("let's be honest", "here's the thing", "real talk"), and choppy one-line fragments used for rhythm. None of these may be added to copy that did not already contain them. The goal is plain, specific writing, not a personality.

## Before writing

Read `references/before-writing.md` and work through it. In short:

1. **Load the client context file** if one exists (`.claude/client-context.md` in the client's repo). If not, create it from `assets/client-context.template.md` and ask only for what is missing. It saves every future page from starting from zero.
2. **Answer the pre-writing questions**: the one action the page should produce, who the reader is, what words they use for their problem, their objections, where the traffic comes from and what the visitor already knows.
3. **Get a writing sample** if you can — the client's own emails, brochure, proposals or a page they like. A sample sets the voice and overrides the defaults in this skill, including the dash rule.
4. **Load the house style** if the client has one (`.claude/house-style.json`, template in `assets/`): spelling, banned words, dash policy, formality.
5. **Read the top 3 ranking pages** for the target term. Learn what vocabulary is table stakes, what every page does, and the one thing none of them says. That gap is your angle.
6. **Collect 20–30 real industry terms.** See `references/register.md`.

## Process

1. **Write the pain points first.** Usually the strongest section and the easiest to get wrong (see below).
2. **Draft in plain declaratives.** One idea per sentence, one argument per section, varied sentence length.
3. **Run the claim tests** from `references/before-writing.md` on every headline, benefit line and CTA:
   - *So what?* — every claim answers why the reader should care, usually via a "which means…" bridge
   - *Now you can…* — prefix the headline; if the result is compelling **and** true, it works
   - *CTA formula* — action verb + what they get + qualifier if needed ("Get a keyword report for your markets", not "Submit")
   - *Zero risk* — near each CTA, are objections answered, trust signals visible, costs and next steps clear?
4. **Strip the AI tells.** Read `references/ai-tells.md`. Fix P0 and strong tells on one sighting; act on weak tells only where several cluster. Then run `scripts/copycheck.py <file>` (add `--list` to see each hit, `--style <house-style.json>` for client rules).
5. **Survivor check.** After rewriting, look again for the five tells that most often survive a rewrite: a contrast (including "rather than"), a one-line closer, a dash, a list of three, a bold label.
6. **Check fidelity.** Compare the draft against the source. Any added fact is an error. Any lost claim is an error unless a rule told you to cut it.
7. **Check keyword restraint** (below), and on protected pages confirm the earning phrases are still at or above their previous counts.
8. **Read it as the client.** Would they forward this to a customer? Would any line embarrass them?

## What to deliver

- **Write / rewrite:** the copy, plus 2–3 alternatives for the H1 and primary CTA, a one-line note on why each works, and the title and meta description. The client chooses; you do not decide alone.
- **Detect:** findings grouped by severity (P0, P1, P2) with the exact text and a suggested fix, and no changes to the file.
- **Editing a file:** change prose only. Leave code, class names, URLs, schema and data untouched.

## Pain points in the customer's own words

A bare list of problems the reader already has is the most persuasive section on most B2B pages, because recognition beats persuasion. Write them the way the customer would say them out loud, not the way a marketer would categorise them.

- Weak: "Suboptimal lead quality and inefficient budget allocation"
- Strong: "Most leads are traders or students, not buyers"
- Weak: "Over-reliance on third-party platforms"
- Strong: "All your buyers come from one portal, and the portal keeps raising its price"

No prose around the list. The list is the argument.

## Keyword restraint

Put the exact-match term in four places and stop: the `<title>`, the meta description, the H1, and at most one FAQ question where it reads naturally. Everything else uses the reader's words. The audience noun (exporter, clinic, manufacturer) should be the most frequent term on the page; if the service phrase is winning, the page is written for the algorithm.

Do not write to a word count. Google's own guidance treats content written to a length target as a sign it exists for search rather than for people.

## Proof, statistics and E-E-A-T

Ask who a number is about.

- **About the client's results** — belongs on a case study, where the reader has opted in to evidence.
- **About your agency, on a service page** — makes the page about you while the reader is checking whether you understand them, and invites scrutiny.
- **An industry statistic** — fine if sourced and load-bearing, filler otherwise. Never "experts say" or "studies show" without naming the source.

Default to no statistics on service pages. Put proof in case studies, and make it **first-hand**: before/after results, the actual process, real screenshots and photos, named clients. Google now weighs this experience signal heavily. Every page should also pass Google's *Who / How / Why* test — who wrote it, how it was made, and whether it exists to help people or to catch clicks. Details in `references/before-writing.md`.

Never publish a figure you have not checked against its source that day.

## Page structure that works for B2B service pages

Deviate with reason, not by default.

1. Plain H1 naming what this is and who it is for
2. One paragraph of what you do, in their vocabulary
3. Client names or logos
4. Why this industry is different from general work
5. The pain-point list
6. How their buyers actually decide, with real search or evaluation examples
7. Services, each with a plain heading and a short list of what is included
8. Client work, described without metrics (link to the case study)
9. Why clients choose you — plain claims, no superlatives
10. FAQ answering what a real prospect asks before enquiring
11. CTA that asks for the conversation, not the sale

Guides and blog posts are different: they are read rather than evaluated, so longer prose and more characterful headings are fine there. The AI-tell rules still apply.

## Deliberately excluded

These are common in other copywriting skills and do not fit our clients:

- Stat-led persuasion ("+81% conversions") on service pages
- Humour and rhetorical questions as default devices — wrong register for most Indian B2B buyers
- Adding opinions or reactions to "sound human" (see rule 2)
- Word-count targets
- Simulated "expert panel" scores

## Files

- `references/before-writing.md` — pre-writing questions, the claim tests, Who/How/Why and E-E-A-T, delivery format.
- `references/ai-tells.md` — every AI pattern by severity, with before/after rewrites. Read before reviewing any draft.
- `references/register.md` — researching an industry's vocabulary, writing samples, house styles.
- `references/examples.md` — real before/after passages from client work.
- `assets/client-context.template.md` — per-client context file.
- `assets/house-style.template.json` — per-client style rules the checker can enforce.
- `scripts/copycheck.py` — mechanical review by severity. Catches what a tired reader misses; it cannot tell whether the copy is good.
