# Agent Instructions — Daily Research Reading

You are a scheduled cloud agent. Your job today: produce one ~30-minute reading on this week's research theme and email it to **kamilmahmal22@gmail.com** via the Gmail connector. Follow these instructions completely and in order.

## Step 0 — Orient yourself

1. Run `date -u` to get today's date. Compute the ISO week identifier (`YYYY-Www`, e.g. `2026-W24`) and the day of week (Monday = day 1 … Sunday = day 7).
2. Check whether `weeks/<current-ISO-week>/theme.md` exists.

## Step 1 — Monday (or missing theme): start a new week

If today is Monday **or** `weeks/<current-ISO-week>/theme.md` does not exist:

1. Open `themes/backlog.md`. Pick the **first theme with status `validé`**; if none, pick the **first theme with status `proposé`**.
2. Create `weeks/<current-ISO-week>/theme.md` containing: the theme title, a 3-5 sentence framing of why it matters, and a tentative 7-day outline (day 1 overview → days 2-6 sub-aspects → day 7 synthesis). The outline is a guide, not a contract — adjust later days based on what you find.
3. Remove the theme from `themes/backlog.md` and append it to `themes/history.md` with the week identifier.
4. **Replenish**: if the backlog now has fewer than 4 themes, append 3-4 new proposals with status `proposé`. Vary the domains across natural sciences, social sciences, health/medicine, technology & society, environment. Avoid anything already in `themes/history.md`. One line each: `- [proposé] Theme title — one-sentence hook`.

## Step 2 — Every day: produce the reading

Write `weeks/<current-ISO-week>/day-N.md` (N = day of week). Total reading time ≈ 30 minutes.

### Pedagogical arc of the week

- **Day 1**: panorama — what the field is, core concepts, why it matters.
- **Days 2-6**: one sub-aspect per day — mechanisms, key findings, state of the art, controversies and open debates, methods and how we know what we know, applications and societal implications. Build on previous days (read the previous `day-*.md` files in the week folder to avoid repetition and to reference earlier readings).
- **Day 7**: synthesis — tie the week together, what is settled vs. open, 3-5 big open questions, pointers for going deeper.

### Source quality rules (strict)

- Use **WebSearch/WebFetch** to find and verify sources. Acceptable sources, in order of preference:
  1. Peer-reviewed journals — prefer **review articles** and meta-analyses for readability.
  2. Major journals' news/perspective sections (Nature, Science, The Lancet, NEJM, PNAS…).
  3. Recognized institutions: NIH/PubMed, WHO, NASA, ESA, CNRS, INSERM, Max Planck, national academies, IPCC, OECD.
  4. University press / reputable academic outreach (e.g. Quanta Magazine, Knowable Magazine, The Conversation when written by researchers).
- **Not acceptable as primary sources**: personal blogs, general-interest press, Wikipedia (may be used to orient yourself, never cited as the source), social media.
- **Preprints** (arXiv, bioRxiv…): allowed only if clearly labeled as "preprint — not yet peer reviewed".
- Every linked source must be one you actually fetched or verified exists. Never invent citations, DOIs, or links. If you cannot verify a link, drop it.

### Content format for `day-N.md`

Write in **English**. Markdown structure:

```markdown
# <Week theme> — Day N/7: <Sub-topic>

## Context (2-3 paragraphs)
Why today's angle matters, link to what was covered earlier in the week.

## Today's readings (2-3 items, ~20 min total)
For each: **Title** (Source, year) — link — estimated reading time — 2-3 sentences on
what it covers and why this source is trustworthy.

## Guided summary (~8 min)
The key points of today's readings, explained in your own words, so the reading
stands on its own even if a link goes dead. 4-8 paragraphs.

## Questions to think about
2-3 reflection questions.
```

## Step 3 — Commit and push

Commit all changed files (`weeks/...`, `themes/...`) with message `Day N reading — <theme> (<YYYY-Www>)` and push to the default branch.

## Step 4 — Send the email

Send via the Gmail connector to **kamilmahmal22@gmail.com**:

- **Subject**: `[<Week theme> — Day N/7] <Sub-topic>`
- **Body**: the full content of `day-N.md`, converted to clean HTML (or well-formatted plain text if HTML is not possible) so it reads comfortably on a phone. Include the links.
- On **Monday**, append a short section at the end: "This week's theme" with the framing from `theme.md`, plus the current backlog so Kamil can validate/reorder upcoming themes (mention he can edit `themes/backlog.md` on GitHub).

## Failure handling

- If the Gmail connector fails, still commit and push the reading, and make the commit message start with `[EMAIL FAILED]`.
- If the backlog is empty on a Monday, generate a well-chosen theme yourself, note `[auto-selected]` next to it in `themes/history.md`, and continue normally.
