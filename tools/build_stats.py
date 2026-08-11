#!/usr/bin/env python3
"""Aggregate cited sources across readings into deterministic statistics,
written to data/STATS.md.

Standard library only — no pip dependency.
Usage: python tools/build_stats.py

Computation is exposed via `compute_stats()` so it can be reused (e.g. the HTML
preview in tools/preview_stats.py) without duplicating logic.
"""

import csv
import glob
import json
import os
from collections import Counter, defaultdict
from datetime import datetime, timezone

# --- Alert thresholds (documented) ----------------------------------------
PUBLISHER_CONCENTRATION = 50.0  # % : a publisher above this is flagged
COUNTRY_CONCENTRATION = 60.0    # % : a publisher-country above this is flagged
OPEN_ACCESS_MIN = 50.0          # % : open-access share below this is flagged
TOP_VENUES = 15                 # number of venues in the ranking

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(REPO_ROOT, "data")
REGISTRY = os.path.join(DATA_DIR, "registry.csv")
CITATIONS_GLOB = os.path.join(DATA_DIR, "citations", "*.json")
OUT = os.path.join(DATA_DIR, "STATS.md")

PEER_LABEL = {True: "peer-reviewed", False: "not peer-reviewed"}


def load_registry():
    reg = {}
    with open(REGISTRY, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            sid = (row.get("id") or "").strip()
            if sid:
                reg[sid] = {k: (v or "").strip() for k, v in row.items()}
    return reg


def load_citations():
    readings = []
    for path in sorted(glob.glob(CITATIONS_GLOB)):
        with open(path, encoding="utf-8") as f:
            readings.append(json.load(f))
    return readings


def pct(n, total):
    return (100.0 * n / total) if total else 0.0


def compute_stats(reg, readings):
    """Return a dict of counters/aggregates — single source of truth."""
    total = 0
    by_publisher = Counter()
    by_venue = Counter()        # (source_id, name) -> count
    by_type = Counter()
    by_discipline = Counter()
    by_country = Counter()
    by_evidence = Counter()
    by_open = Counter()
    by_peer = Counter()
    by_year = Counter()
    by_location = Counter()
    by_week = Counter()              # week -> citations
    week_theme = {}
    week_days = defaultdict(set)
    week_publishers = defaultdict(set)
    off_registry = Counter()
    to_verify_venue = set()          # venue ids with discipline/country to-verify
    to_verify_evidence = 0

    for r in readings:
        week = r.get("week", "")
        if week:
            by_week[week] += 0  # ensure key exists even if 0
            week_theme.setdefault(week, r.get("theme", ""))
            week_days[week].add(r.get("day"))
        for c in r.get("citations", []):
            total += 1
            sid = c.get("source_id", "")
            meta = reg.get(sid)
            if meta is None:
                off_registry[sid] += 1
                publisher = typ = discipline = country = "(off-registry)"
                name = sid
            else:
                publisher = meta.get("publisher", "")
                typ = meta.get("type", "")
                discipline = meta.get("discipline", "")
                country = meta.get("country", "")
                name = meta.get("name", sid)
                if discipline == "to-verify" or country == "to-verify":
                    to_verify_venue.add(sid)
            ev = c.get("evidence_type", "?")
            if ev == "to-verify":
                to_verify_evidence += 1
            peer = c.get("peer_reviewed", None)
            oa = c.get("open_access", "unknown")
            year = c.get("year", None)

            by_publisher[publisher] += 1
            by_venue[(sid, name)] += 1
            by_type[typ] += 1
            by_discipline[discipline] += 1
            by_country[country] += 1
            by_evidence[ev] += 1
            by_open[oa] += 1
            by_peer[PEER_LABEL.get(peer, "unknown")] += 1
            by_year[str(year) if year is not None else "unknown"] += 1
            by_location[c.get("location", "?")] += 1
            if week:
                by_week[week] += 1
                week_publishers[week].add(publisher)

    weeks = sorted(by_week)
    return {
        "total": total,
        "by_publisher": by_publisher,
        "by_venue": by_venue,
        "by_type": by_type,
        "by_discipline": by_discipline,
        "by_country": by_country,
        "by_evidence": by_evidence,
        "by_open": by_open,
        "by_peer": by_peer,
        "by_year": by_year,
        "by_location": by_location,
        "by_week": by_week,
        "week_theme": week_theme,
        "week_days": week_days,
        "week_publishers": week_publishers,
        "off_registry": off_registry,
        "to_verify_venue": to_verify_venue,
        "to_verify_evidence": to_verify_evidence,
        "reg": reg,
        "n_readings": len(readings),
        "weeks": weeks,
    }


def alerts_list(s):
    """Quality + concentration alerts, reusable by the HTML preview."""
    total, reg = s["total"], s["reg"]
    out = []
    for sid, n in s["off_registry"].items():
        out.append(f"⚠️ Off-registry source: `{sid}` ({n} citation(s)) — add a row to registry.csv.")
    for sid in sorted(s["to_verify_venue"]):
        name = reg.get(sid, {}).get("name", sid)
        out.append(f"🔎 Venue to verify: {name} (`{sid}`) — discipline/country marked to-verify in registry.csv.")
    if s["to_verify_evidence"]:
        out.append(f"🔎 {s['to_verify_evidence']} citation(s) with evidence_type `to-verify` — classify them.")
    for publisher, n in s["by_publisher"].most_common():
        p = pct(n, total)
        if publisher != "(off-registry)" and p > PUBLISHER_CONCENTRATION:
            out.append(f"🏢 Publisher concentration: `{publisher}` = {p:.1f} % of citations (threshold {PUBLISHER_CONCENTRATION:.0f} %).")
    for country, n in s["by_country"].most_common():
        p = pct(n, total)
        if country != "(off-registry)" and p > COUNTRY_CONCENTRATION:
            out.append(f"🌍 Geographic concentration: publishers based in `{country}` = {p:.1f} % (threshold {COUNTRY_CONCENTRATION:.0f} %).")
    open_share = pct(s["by_open"].get("open", 0), total)
    if total and open_share < OPEN_ACCESS_MIN:
        out.append(f"🔓 Open-access share is {open_share:.1f} % (below {OPEN_ACCESS_MIN:.0f} %) — many readings sit behind paywalls.")
    not_peer = s["by_peer"].get("not peer-reviewed", 0)
    preprints = s["by_evidence"].get("preprint", 0)
    if preprints:
        out.append(f"📄 {preprints} preprint(s) cited ({pct(preprints, total):.1f} %) — not peer reviewed, keep an eye on the share.")
    if not_peer:
        out.append(f"📄 {not_peer} non-peer-reviewed citation(s) ({pct(not_peer, total):.1f} %).")
    return out


def _bar(p):
    return "█" * int(round(p / 5.0))  # 1 block ≈ 5 %


def _table(title, counter, total, order=None):
    items = list(counter.most_common())
    if order:
        items.sort(key=lambda kv: order.index(kv[0]) if kv[0] in order else 999)
    lines = [f"### {title}", "", "| Value | Citations | Share | |", "|---|---:|---:|---|"]
    for value, n in items:
        p = pct(n, total)
        lines.append(f"| {value or '—'} | {n} | {p:.1f} % | {_bar(p)} |")
    lines.append("")
    return "\n".join(lines)


def render_markdown(s):
    total = s["total"]
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    out = []
    out.append("# Source statistics")
    out.append("")
    out.append(f"*Auto-generated by `tools/build_stats.py` — do not edit by hand. Last generated: {generated}.*")
    out.append("")
    out.append("## Summary")
    out.append("")
    out.append(f"- **Readings analysed**: {s['n_readings']}")
    out.append(f"- **Weeks / themes**: {len(s['weeks'])}")
    out.append(f"- **Total citations**: {total}")
    out.append(f"- **Distinct venues**: {len({sid for (sid, _) in s['by_venue']})}")
    out.append(f"- **Distinct publishers**: {len(s['by_publisher'])}")
    out.append(f"- **Open-access share**: {pct(s['by_open'].get('open', 0), total):.1f} %")
    out.append("")
    out.append("## Alerts")
    out.append("")
    al = alerts_list(s)
    if al:
        out.extend(f"- {a}" for a in al)
    else:
        out.append("No alerts: no off-registry or to-verify sources, no concentration beyond thresholds, healthy open-access and peer-review shares.")
    out.append("")
    out.append(f"*Thresholds: publisher > {PUBLISHER_CONCENTRATION:.0f} %, publisher-country > {COUNTRY_CONCENTRATION:.0f} %, open-access < {OPEN_ACCESS_MIN:.0f} % flagged; any preprint reported.*")
    out.append("")
    out.append("## Distributions")
    out.append("")
    out.append(_table("By publisher", s["by_publisher"], total))
    out.append(_table("By type of evidence", s["by_evidence"], total))
    out.append(_table("By open access", s["by_open"], total, order=["open", "paywall", "unknown"]))
    out.append(_table("By peer review", s["by_peer"], total, order=["peer-reviewed", "not peer-reviewed", "unknown"]))
    out.append(_table("By discipline", s["by_discipline"], total))
    out.append(_table("By publisher country", s["by_country"], total))
    out.append(_table("By venue type", s["by_type"], total))
    out.append(_table("By publication year", s["by_year"], total, order=sorted(s["by_year"], reverse=True)))
    out.append(_table("By location (reading list / in-text)", s["by_location"], total))
    out.append(f"## Most-cited venues (top {TOP_VENUES})")
    out.append("")
    out.append("| Venue | Citations | Share |")
    out.append("|---|---:|---:|")
    for (sid, name), n in s["by_venue"].most_common(TOP_VENUES):
        out.append(f"| {name} | {n} | {pct(n, total):.1f} % |")
    out.append("")
    out.append("## Weekly evolution (by theme)")
    out.append("")
    out.append("| Week | Theme | Days | Citations | Distinct publishers |")
    out.append("|---|---|---:|---:|---:|")
    for w in s["weeks"]:
        out.append(f"| {w} | {s['week_theme'].get(w, '')} | {len(s['week_days'][w])} | {s['by_week'][w]} | {len(s['week_publishers'][w])} |")
    out.append("")
    return "\n".join(out)


def main():
    s = compute_stats(load_registry(), load_citations())
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render_markdown(s))
    print(f"STATS.md generated: {s['total']} citations, {s['n_readings']} reading(s) -> {OUT}")


if __name__ == "__main__":
    main()
