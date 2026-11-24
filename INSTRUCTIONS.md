# Agent Instructions — Research Reading (one every two days)

You are a scheduled cloud agent. Each research theme now runs over a **two-week cycle of 7 readings, one every two days**. The routine wakes you every day; your first job is to decide whether today is a reading day. If it is, produce one ~30-minute reading on the cycle's theme, commit it, and push it to your `claude/...` session branch. A GitHub Action then publishes it to `main`, which emails the reading to the mailing list (Google Group, repo variable `MAIL_TO`) — the push IS the delivery, so the file must be fully self-contained. Follow these instructions completely and in order.

## Step 0 — Orient yourself and decide whether today is a reading day

1. **Stay on your session branch.** The sandbox starts you on a fresh `claude/...` branch cut from `main` — work and commit there. Do not check out or push `main`: you are not allowed to, by design.
2. Run `date -u` to get today's date (UTC).
3. Find the **current cycle**: the most recent folder under `weeks/` (folder names are ISO weeks `YYYY-Www`, so they sort chronologically) that contains a `theme.md`. Its folder name is the **cycle id** (e.g. `2026-W48`). Read the `Start: YYYY-MM-DD` line in its `theme.md` (if a `theme.md` has no `Start:` line, use the Monday of that ISO week).
4. Compute `d` = number of days from the start date to today.
   - **`d` ≥ 14, or no `theme.md` exists at all** → the previous cycle is over: go to **Step 1** and start a new cycle today (today is reading Day 1).
   - **`d` is odd** → today is an **off day**. **STOP immediately**: write nothing, commit nothing, push nothing (no email is sent on off days). Report "off day" and end.
   - **`d` is even and < 14** → today is a reading day: **N = d / 2 + 1** (Day 1 … Day 7). If `weeks/<cycle-id>/day-N.md` already exists, that reading was already sent: **STOP immediately** without pushing anything. Otherwise skip to **Step 2**.

## Step 1 — New cycle: start a new theme

1. The new **cycle id** is today's ISO week (`YYYY-Www`). Create the folder `weeks/<cycle-id>/`.
2. Open `themes/backlog.md`. Pick the **first theme with status `validé`**; if none, pick the **first theme with status `proposé`**.
3. Create `weeks/<cycle-id>/theme.md` containing: the theme title as `#` heading, then on its own line `Start: <today, YYYY-MM-DD>` (this date drives the whole schedule — never change it later), a 3-5 sentence framing of why it matters, and a tentative **7-reading outline** (reading 1 overview → readings 2-6 sub-aspects → reading 7 synthesis), noting that readings go out every two days over two weeks. The outline is a guide, not a contract — adjust later readings based on what you find.
4. Remove the theme from `themes/backlog.md` and append it to `themes/history.md` with the cycle id.
5. **Replenish**: if the backlog now has fewer than 4 themes, append 3-4 new proposals with status `proposé`. Vary the domains across natural sciences, social sciences, health/medicine, technology & society, environment. Avoid anything already in `themes/history.md`. One line each: `- [proposé] Theme title — one-sentence hook`.
6. Today is Day 1 (N = 1). Continue with Step 2.

## Step 2 — Reading day: produce the reading

Write `weeks/<cycle-id>/day-N.md`. Total reading time ≈ 30 minutes (the videos are an optional extra on top).

### Pedagogical arc of the cycle

- **Day 1**: panorama — what the field is, core concepts, why it matters.
- **Days 2-6**: one sub-aspect per reading — mechanisms, key findings, state of the art, controversies and open debates, methods and how we know what we know, applications and societal implications. Build on previous readings (read the previous `day-*.md` files in the cycle folder to avoid repetition and to reference earlier readings). Two days pass between readings, so open each one with a short reminder of where the previous reading left off.
- **Day 7**: synthesis — tie the cycle together, what is settled vs. open, 3-5 big open questions, pointers for going deeper.

### Source quality rules (strict)

- Use **WebSearch/WebFetch** to find and verify sources. Acceptable sources, in order of preference:
  1. Peer-reviewed journals — prefer **review articles** and meta-analyses for readability.
  2. Major journals' news/perspective sections (Nature, Science, The Lancet, NEJM, PNAS…).
  3. Recognized institutions: NIH/PubMed, WHO, NASA, ESA, CNRS, INSERM, Max Planck, national academies, IPCC, OECD.
  4. University press / reputable academic outreach (e.g. Quanta Magazine, Knowable Magazine, The Conversation when written by researchers).
- **Not acceptable as primary sources**: personal blogs, general-interest press, Wikipedia (may be used to orient yourself, never cited as the source), social media.
- **Preprints** (arXiv, bioRxiv…): allowed only if clearly labeled as "preprint — not yet peer reviewed".
- Every linked source must be one you actually fetched or verified exists. Never invent citations, DOIs, or links. If you cannot verify a link, drop it.

### YouTube videos (strict)

Each reading includes **1 to 3 YouTube videos** on today's sub-topic (or, failing that, on the cycle's theme). Every video must meet **all** of these criteria:

1. **In English** (spoken language; not dubbed or auto-translated).
2. **At least 200,000 views**, checked on the video's own page (`https://www.youtube.com/watch?v=<id>`) with WebFetch **today**. Find candidates with WebSearch (e.g. `site:youtube.com <topic>`), then fetch each video page to confirm the title, channel, language and view count. If you cannot read the view count from the page, or it is under 200,000, **drop the video** — never estimate or round up.
3. **From a reputable channel**: established science communicators, universities, scientific journals and societies, public broadcasters, or major museums and conferences. Examples: Kurzgesagt, Veritasium, 3Blue1Brown, SciShow, CrashCourse, PBS (NOVA, Eons, Space Time, Terra), TED / TED-Ed, The Royal Institution, World Science Festival, Nature Video, Science Magazine, Stanford, MIT, Harvard, Yale, BBC, DW Documentary, National Geographic, Osmosis, Real Engineering, Practical Engineering, MinutePhysics, Numberphile, Computerphile. **Excluded**: wellness/supplement or product-selling channels, single-person opinion or reaction channels, conspiracy or "debunked" content, AI-generated narration channels, reuploads of someone else's video.
4. **Scientifically consistent** with the readings — if a video oversimplifies or contradicts the evidence, say so in its description or drop it.

Never invent a video, video id, title, channel or view count. If no video meets every criterion, keep the section and write one line: *"No video meeting the quality criteria (English, ≥200k views, reputable channel) was found for today's topic."* — do not lower the bar.

Videos are **not** citations: do not add them to `data/citations/*.json` or `data/registry.csv`.

### Content format for `day-N.md`

Write in **English**. Markdown structure:

The **first line** of the file must be a `#` heading of the form `<Theme> — Day N/7: <Sub-topic>` — it becomes the email subject.

```markdown
# <Theme> — Day N/7: <Sub-topic>

## Context (2-3 paragraphs)
Why today's angle matters, link to what was covered in the previous readings.

## Today's readings (2-3 items, ~20 min total)
For each: **Title** (Source, year) — link — estimated reading time — 2-3 sentences on
what it covers and why this source is trustworthy.

## Watch (optional)
For each video (1-3): **Video title** — Channel — link — duration — views (as of <YYYY-MM-DD>)
— 1-2 sentences on what it shows and how it complements today's readings.

## Guided summary (~8 min)
The key points of today's readings, explained in your own words, so the reading
stands on its own even if a link goes dead. 4-8 paragraphs.

## Questions to think about
2-3 reflection questions.
```

On **Day 1**, append a final section to `day-1.md`: "This cycle's theme" with the framing from `theme.md`, the schedule (7 readings, one every two days, from the start date to Day 7 = start + 12 days), plus the current backlog of upcoming themes so Kamil can validate/reorder them (mention he can edit `themes/backlog.md` on GitHub).

## Step 2 bis — Source tracking (`data/citations/<cycle-id>-day-N.json`)

The project accumulates, reading after reading, **every** source cited, so source diversity and quality can be *verified* over time (see `data/README.md` — the codebook: columns, types, evidence taxonomy). After writing the reading:

1. List **every** source cited — both the formal "Today's readings" items **and** the studies/journals mentioned in the body (e.g. "a 2024 study in *npj Parkinson's Disease*", "a 2025 meta-analysis in *Frontiers in Psychiatry*"). A source cited more than once = several entries. Only include a study if its **venue (journal/outlet) is identifiable** — never invent a venue, DOI, year, or link. (YouTube videos are not citations.)
2. Write `data/citations/<cycle-id>-day-N.json` following the schema in `data/README.md` (its `"week"` field holds the cycle id): for each citation give `source_id`, `location` (`todays-readings`/`text`), `evidence_type`, `peer_reviewed`, `open_access`, `year`, and `url`/`title` (`null` when absent).
3. Reuse the existing `id` in `data/registry.csv`. **If the venue is not yet there**, add a row (`id,name,publisher,type,discipline,country,notes`) following the taxonomy in `data/README.md` strictly. If unsure about discipline or country, write `to-verify` rather than guessing — Kamil will resolve it (the row is surfaced in `STATS.md`).
4. Never edit `data/STATS.md`: it is regenerated automatically by a GitHub Action after your push.

## Step 3 — Commit and push (this sends the email)

Commit all changed files (`weeks/...`, `themes/...`, `data/citations/<...>.json`, and `data/registry.csv` if you enriched it) and push your session branch, with exactly these commands:

```bash
git add -A
git commit -m "Day N reading — <theme> (<cycle-id>)"
git push -u origin HEAD
```

- Never push to `main` and never try to — you are not allowed to, by design.
- Do **not** create another branch and do **not** open a pull request.
- Only change `weeks/`, `themes/`, `rapports/` and `data/`. A branch that touches any other file (workflows, `tools/`, this file…) is **refused** and nothing is delivered.
- If the push fails, retry `git push -u origin HEAD` once. Never force-push.

The GitHub Action `.github/workflows/promote-to-main.yml` checks your branch, publishes it to `main`, deletes the branch, and starts `send-reading.yml`, which emails its rendered content to the mailing list. The first heading line of `day-N.md` (without the leading `# `) becomes the email subject, so make it descriptive. Push exactly once, when the reading is final — no drafts, and do NOT make a second commit, since each `day-N.md` push sends one email.

## Step 4 — Day 7 only: source-diversity report for the cycle

On **Day 7** (the synthesis reading), after the reading is written, also produce a short report on how diverse and trustworthy this cycle's sources were. This is the research equivalent of verifying pluralism: it lets Kamil check, with numbers, that the readings did not over-rely on one publisher, one type of evidence, or paywalled work.

1. Read all of this cycle's citation files (`data/citations/<cycle-id>-day-*.json`) — together they are the authoritative record for the cycle. You may also read `data/STATS.md` for all-time context (it may lag by one reading, since the Action regenerates it after your push).
2. Write `rapports/<cycle-id>.md` in **English**. The **first line** is the `#` heading (it becomes the email subject):

   ```
   # Source diversity — <theme> (<cycle-id>)
   ```

   Suggested structure (be factual; separate the numbers from your interpretation):
   - **At a glance**: readings and citations this cycle, open-access share, the single most notable finding.
   - **Publisher & venue concentration**: did one publisher (e.g. Springer Nature) or a few venues dominate?
   - **Evidence mix**: balance of reviews / meta-analyses / RCTs / primary studies / preprints. Enough high-level synthesis vs. primary claims? Any preprint (not peer reviewed)?
   - **Open access & geography**: paywall share; geographic concentration of publishers (e.g. heavy US/UK).
   - **Discipline & recency**: spread of fields; how recent vs. foundational the sources were.
   - **Blind spots & data quality**: any `to-verify` or off-registry items flagged in `STATS.md`; source families never used.
   - **Recommendations**: 3-5 concrete suggestions for upcoming cycles (e.g. diversify publishers, add an open-access alternative, include a foundational reference).
3. Commit `rapports/<cycle-id>.md` — preferably in the Day 7 commit, otherwise in a dedicated `Source report — <cycle-id>` commit — and push it with `git push -u origin HEAD`, same rules as Step 3. Once promoted to `main`, `.github/workflows/send-report.yml` emails it. So **Day 7 sends two emails** — the reading and the report. That is intended; do not push the report more than once.
4. Never edit `data/STATS.md` (auto-generated) or other readings' `data/citations/*.json`. You only **read** the data and **write** your report.

## Failure handling

- If the backlog is empty when a new cycle starts, generate a well-chosen theme yourself, note `[auto-selected]` next to it in `themes/history.md`, and continue normally.
- If a reading day was missed (e.g. a failed run), do not catch up on an off day: the next reading day simply produces its own Day N per the schedule.
- If the push fails, retry `git push -u origin HEAD` once. Never force-push, never push to `main`, and never open a pull request.
- A Gmail connector may be available in your session, but it can only create drafts, not send. Do not rely on it for delivery; the GitHub Action is the delivery channel.
