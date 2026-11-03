# EconTube

A minimalist, YouTube-style index of economics and finance videos and podcast
episodes, ranked by how many serious curators (blogs, think tanks, institutions)
link to or embed them. Modeled on Karpathy's
[HackerTube](https://karpathy.bearblog.dev/hacker-tube/), but the signal is
editorial curation, not comments.

**Status: step 1 of 5 (scaffold + source probe).** See the build order in `DECISIONS.md`.

## Layout

| path | what |
|---|---|
| `sources.yaml` | every curator source, with candidate feeds, weights, filters |
| `seeds.yaml` | low-weight YouTube search seeds, with a quota budget |
| `pipeline/econtube/extract.py` | YouTube/podcast/Vimeo URL extractor (all URL shapes) |
| `pipeline/econtube/score.py` | ranking formula, all constants documented |
| `pipeline/econtube/http.py` | polite client: honest UA, robots.txt, 1 req/s/host, ETag cache |
| `pipeline/probe.py` | step 1: verifies sources, writes `reports/probe.md` |
| `.github/workflows/` | tests on push; `probe-sources` (manual) |

## Run locally

```bash
pip install -r requirements.txt
```

```bash
pytest -q
```

```bash
YOUTUBE_API_KEY=... python pipeline/probe.py
```

## Licence

Code: MIT. Dataset export (`data/econtube-export.json`): metadata and links
only. No video, audio or article text is rehosted.
