# Agent Instructions — Daily Research Reading

You are a scheduled cloud agent. Your job today: produce one ~30-minute reading on this week's research theme, commit it, and push it **to `main`**. Pushing a new `day-N.md` to `main` automatically triggers a GitHub Action that emails the reading to the mailing list (Google Group, repo variable `MAIL_TO`) — the push to `main` IS the delivery, so the file must be fully self-contained and must not be left on a branch. Follow these instructions completely and in order.

## Step 0 — Orient yourself

1. **Work on `main`.** The sandbox may drop you on a `claude/...` branch — ignore it and switch:
   `git checkout main && git pull --ff-only`. Everything you write today belongs on `main`.
2. Run `date -u` to get today's date. Compute the ISO week identifier (`YYYY-Www`, e.g. `2026-W24`) and the day of week (Monday = day 1 … Sunday = day 7).
3. Check whether `weeks/<current-ISO-week>/theme.md` exists.

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

The **first line** of the file must be a `#` heading of the form `<Week theme> — Day N/7: <Sub-topic>` — it becomes the email subject.

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

On **Monday**, append a final section to `day-1.md`: "This week's theme" with the framing from `theme.md`, plus the current backlog of upcoming themes so Kamil can validate/reorder them (mention he can edit `themes/backlog.md` on GitHub).

## Step 2 bis — Source tracking (`data/citations/<YYYY-Www>-day-N.json`)

The project accumulates, reading after reading, **every** source cited, so source diversity and quality can be *verified* over time (see `data/README.md` — the codebook: columns, types, evidence taxonomy). After writing the reading:

1. List **every** source cited — both the formal "Today's readings" items **and** the studies/journals mentioned in the body (e.g. "a 2024 study in *npj Parkinson's Disease*", "a 2025 meta-analysis in *Frontiers in Psychiatry*"). A source cited more than once = several entries. Only include a study if its **venue (journal/outlet) is identifiable** — never invent a venue, DOI, year, or link.
2. Write `data/citations/<YYYY-Www>-day-N.json` following the schema in `data/README.md`: for each citation give `source_id`, `location` (`todays-readings`/`text`), `evidence_type`, `peer_reviewed`, `open_access`, `year`, and `url`/`title` (`null` when absent).
3. Reuse the existing `id` in `data/registry.csv`. **If the venue is not yet there**, add a row (`id,name,publisher,type,discipline,country,notes`) following the taxonomy in `data/README.md` strictly. If unsure about discipline or country, write `to-verify` rather than guessing — Kamil will resolve it (the row is surfaced in `STATS.md`).
4. Never edit `data/STATS.md`: it is regenerated automatically by a GitHub Action after your push.

## Step 3 — Commit and push (this sends the email)

Commit all changed files (`weeks/...`, `themes/...`, `data/citations/<...>.json`, and `data/registry.csv` if you enriched it) and publish them **to `main`**, with exactly these commands:

```bash
git add -A
git commit -m "Day N reading — <theme> (<YYYY-Www>)"
git push origin HEAD:main
```

- Do **not** run a bare `git push` — from a `claude/...` branch it pushes that branch, not `main`.
- Do **not** create a branch and do **not** open a pull request.
- Do **not** leave the reading on a `claude/...` branch: the email fires only on a push to `main`, so a reading left on a branch is silently never delivered.
- If the push is rejected as non-fast-forward, run `git pull --rebase origin main` and push again. Never force-push.

The GitHub Action `.github/workflows/send-reading.yml` detects the new `day-N.md` on `main` and emails its rendered content to the mailing list. The first heading line of `day-N.md` (without the leading `# `) becomes the email subject, so make it descriptive. Push exactly once, when the reading is final — no drafts, and do NOT make a second commit, since each `day-N.md` push sends one email.

## Step 4 — Day 7 only: weekly source-diversity report

On **day 7** (the synthesis day), after the reading is written, also produce a short report on how diverse and trustworthy this week's sources were. This is the research equivalent of verifying pluralism: it lets Kamil check, with numbers, that the readings did not over-rely on one publisher, one type of evidence, or paywalled work.

1. Read all of this week's citation files (`data/citations/<YYYY-Www>-day-*.json`) — together they are the authoritative record for the week. You may also read `data/STATS.md` for all-time context (it may lag by one reading, since the Action regenerates it after your push).
2. Write `rapports/<YYYY-Www>.md` in **English**. The **first line** is the `#` heading (it becomes the email subject):

   ```
   # Source diversity — <week theme> (<YYYY-Www>)
   ```

   Suggested structure (be factual; separate the numbers from your interpretation):
   - **At a glance**: readings and citations this week, open-access share, the single most notable finding.
   - **Publisher & venue concentration**: did one publisher (e.g. Springer Nature) or a few venues dominate?
   - **Evidence mix**: balance of reviews / meta-analyses / RCTs / primary studies / preprints. Enough high-level synthesis vs. primary claims? Any preprint (not peer reviewed)?
   - **Open access & geography**: paywall share; geographic concentration of publishers (e.g. heavy US/UK).
   - **Discipline & recency**: spread of fields; how recent vs. foundational the sources were.
   - **Blind spots & data quality**: any `to-verify` or off-registry items flagged in `STATS.md`; source families never used.
   - **Recommendations**: 3-5 concrete suggestions for upcoming weeks (e.g. diversify publishers, add an open-access alternative, include a foundational reference).
3. Commit `rapports/<YYYY-Www>.md` (it can be part of the day-7 commit or a dedicated `Weekly source report — <YYYY-Www>` commit) and push it **to `main`** with `git push origin HEAD:main` — same rules as Step 3, a report left on a branch is never delivered. Its arrival on `main` triggers `.github/workflows/send-report.yml`, which emails it. So **day 7 sends two emails** — the reading and the report. That is intended; do not push the report more than once.
4. Never edit `data/STATS.md` (auto-generated) or other days' `data/citations/*.json`. You only **read** the data and **write** your report.

## Failure handling

- If the backlog is empty on a Monday, generate a well-chosen theme yourself, note `[auto-selected]` next to it in `themes/history.md`, and continue normally.
- If the push to `main` fails, retry once after `git pull --rebase origin main`, then `git push origin HEAD:main` again. Never force-push, and never fall back to pushing a branch or opening a pull request — that would deliver nothing.
- A Gmail connector may be available in your session, but it can only create drafts, not send. Do not rely on it for delivery; the GitHub Action is the delivery channel.
