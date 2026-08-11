# Source tracking data

This folder turns **every source cited** in the weekly readings into **structured data**,
so we can *verify* — not merely hope — that the readings stay diverse and trustworthy over
time (publisher, venue, evidence type, open access, discipline, geography, recency).

## Files

| File | Role | Written by |
|---|---|---|
| `registry.csv` | Canonical registry of **venues** (journals / outlets) and their attributes. **This is the file Kamil audits and corrects.** | Agent (additions), Kamil (corrections) |
| `citations/<YYYY-Www>-day-N.json` | Every source cited in one reading (one file per reading). | Agent, on the day of the reading |
| `STATS.md` | **Deterministic** statistics, regenerated on every push. **Do not edit by hand.** | `tools/build_stats.py` (GitHub Action) |

The split is deliberate: the **agent** (judgement) *extracts and labels*; the **script**
(precision) *aggregates and counts*. The numbers are therefore reproducible and verifiable,
independent of the model.

## `registry.csv` — one row per venue (the recurring entity over time)

`id,name,publisher,type,discipline,country,notes`

- **id** — unique `kebab-case` slug, the join key with citations (`jama-neurology`, `cell`, `nature-communications`). Never rename an existing `id` (it would break history).
- **name** — display name of the venue.
- **publisher** — e.g. `Springer Nature`, `Elsevier (Cell Press)`, `Oxford University Press`, `American Medical Association`, `Frontiers`, `Wiley`, `PLOS`.
- **type** — one of:
  - `journal` — peer-reviewed scholarly journal
  - `megajournal` — large multidisciplinary journal (Nature Communications, PNAS, PLOS ONE, Scientific Reports)
  - `news-perspective` — news/perspective section of a major journal (Nature News, Science News)
  - `preprint-server` — arXiv, bioRxiv, medRxiv… (**not peer reviewed**)
  - `institution` — official body / agency (NIH, WHO, IPCC, OECD, national academies)
  - `outreach` — reputable academic outreach (Quanta, Knowable, The Conversation)
- **discipline** — dominant field of the venue: `neurology`, `psychiatry`, `nutrition`, `general-medicine`, `microbiology`, `multidisciplinary`, `physics`, `climate`, `technology`… (use `multidisciplinary` for Nature/Science/PNAS/Cell-type venues).
- **country** — country of the publisher's headquarters (`United States`, `United Kingdom`, `Germany`, `Netherlands`, `Switzerland`…). Use `to-verify` if unsure.
- **notes** — short justification of the classification (optional). Wrap in **double quotes** if it contains commas.

Special value **`to-verify`** (in `discipline` or `country`, or `evidence_type` in citations):
the agent was **unsure**. These are surfaced at the top of `STATS.md` so Kamil can decide.
Prefer `to-verify` over guessing.

## Audit (Kamil)

Labelling is fallible. The registry is built to be reviewed: open `registry.csv` (spreadsheet
or editor), fix any `publisher` / `discipline` / `country` you judge wrong, resolve `to-verify`
rows, then push. On the next push, `STATS.md` recomputes with your corrections. **You have the
final say.**

## `citations/<YYYY-Www>-day-N.json` — per-article attributes (non-recurring)

```json
{
  "week": "2026-W24",
  "day": 4,
  "theme": "The gut microbiome and the brain",
  "citations": [
    {
      "source_id": "jama-neurology",
      "location": "todays-readings",
      "evidence_type": "rct",
      "peer_reviewed": true,
      "open_access": "paywall",
      "year": 2024,
      "url": "https://jamanetwork.com/...",
      "title": "Fecal Microbiota Transplantation for Treatment of Parkinson Disease: A Randomized Clinical Trial"
    }
  ]
}
```

- **source_id** — must exist in `registry.csv` (otherwise the citation is still counted but flagged "off-registry" in `STATS.md`).
- **location** — `todays-readings` (a formal reading-list item) or `text` (a study mentioned in the body).
- **evidence_type** — `review` · `meta-analysis` · `umbrella-review` · `rct` · `cohort` · `primary-study` · `preprint` · `perspective` · `guideline` · `book` · `to-verify`.
- **peer_reviewed** — `true` / `false` (false for preprints, institutional reports, outreach).
- **open_access** — `open` · `paywall` · `unknown`.
- **year** — integer publication year (`null` if genuinely unknown).
- **url / title** — `null` if the study is only mentioned in passing without a link.

A source cited several times yields **several entries** (each mention counts).
