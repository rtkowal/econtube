"""Step-2 report: classify the current catalogue, then write reports/sample.md with
50 sample rows (Marginal Revolution, Hoover, Nobel first), facet/topic frequencies, tag vocabulary,
out-of-vocabulary suggestions, gate rejections and measured LLM cost. Reads data/videos.json
(already gated+classified by build_data.py when OPENAI_API_KEY is set) and .cache/*.json.
"""
from __future__ import annotations

import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
C = ROOT / ".cache"


def main() -> None:
    items = json.loads((ROOT / "data/videos.json").read_text())["items"]
    cls = [i for i in items if i.get("classified")]
    pri = ("marginal-revolution", "hoover", "nobel-economics")
    rank = lambda i: min((pri.index(s["id"]) for s in i["sources"] if s["id"] in pri), default=9)  # noqa: E731
    sample = sorted(cls, key=lambda i: (rank(i), -i["score"]))[:50]

    L = ["# Step 2 sample: classification report\n",
         f"Items in catalogue: {len(items)}; classified: {len(cls)}.\n"]
    # cost
    logp = C / "llm_cost.jsonl"
    if logp.exists():
        rows = [json.loads(x) for x in logp.read_text().splitlines() if x.strip()]
        by = collections.defaultdict(lambda: [0, 0, 0])
        for r in rows:
            b = by[(r["model"], r["tag"])]
            b[0] += 1
            b[1] += r.get("in") or 0
            b[2] += r.get("out") or 0
        L.append("## LLM usage this run\n\n| model | step | calls | input tok | output tok |\n|---|---|---:|---:|---:|")
        L += [f"| {m} | {t} | {n} | {i:,} | {o:,} |" for (m, t), (n, i, o) in sorted(by.items())]
        L.append("\nMultiply by the model's current per-token price to get cost; per-item cost × expected catalogue size = backfill cost.\n")
    # gate
    gp = C / "gate.json"
    if gp.exists():
        g = json.loads(gp.read_text())
        rej = [(k, v) for k, v in g.items() if not (v.get("relevant") and float(v.get("confidence", 0)) >= 0.7)]
        L.append(f"## Relevance gate\n\n{len(g)} gated items, {len(rej)} rejected. Rejection reasons (first 25):\n")
        L += [f"- `{k}`: {v.get('reason','')} (conf {v.get('confidence')})" for k, v in rej[:25]]
        L.append("")
    # sample rows
    L.append("## 50 sample rows\n")
    for i in sample:
        f = i.get("facets", {})
        p = i.get("people") or {}
        L.append(f"**{i['title']}** — {i['channel']} · via {', '.join(sorted({s['name'] for s in i['sources']}))}  ")
        L.append(f"why: _{i.get('why','')}_  ")
        L.append(f"field: {', '.join(f.get('fields') or []) or '—'} · topic: {', '.join(f.get('topics') or []) or '—'} · "
                 f"school: {', '.join(f.get('schools') or []) or '—'} · format: {f.get('format') or '—'} · level: {f.get('level') or '—'} · "
                 f"era: {', '.join(f.get('eras') or []) or '—'} · region: {', '.join(f.get('regions') or []) or '—'}  ")
        L.append(f"speakers: {', '.join(p.get('speakers') or []) or '—'} · discussed: {', '.join(p.get('discussed') or []) or '—'}  ")
        L.append(f"tags: {', '.join(i.get('tags') or [])}\n")
    # frequencies
    for facet in ("topics", "fields", "schools", "format", "level"):
        cnt = collections.Counter()
        for i in cls:
            v = (i.get("facets") or {}).get(facet)
            cnt.update(v if isinstance(v, list) else ([v] if v else []))
        L.append(f"## {facet} frequency\n\n" + ", ".join(f"{k} ({n})" for k, n in cnt.most_common()) + "\n")
    tags = collections.Counter(t for i in cls for t in i.get("tags") or [])
    L.append(f"## Tag vocabulary ({len(tags)} distinct; ≥2 uses shown)\n\n" +
             ", ".join(f"{t} ({n})" for t, n in tags.most_common() if n >= 2) + "\n")
    sp = ROOT / "taxonomy_suggestions.jsonl"
    if sp.exists():
        s = collections.Counter((json.loads(x)["facet"], json.dumps(json.loads(x)["value"])[:60])
                                for x in sp.read_text().splitlines() if x.strip())
        L.append("## Out-of-vocabulary values the model wanted (candidates for new topics)\n")
        L += [f"- {f}: {v} ×{n}" for (f, v), n in s.most_common(60)]
    (ROOT / "reports").mkdir(exist_ok=True)
    (ROOT / "reports/sample.md").write_text("\n".join(L) + "\n")
    print("wrote reports/sample.md;", len(sample), "rows")


if __name__ == "__main__":
    main()
