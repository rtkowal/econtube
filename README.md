# EconTube

A minimalist, YouTube-style index of economics and finance videos and podcast
episodes, ranked by how many serious curators (blogs, think tanks, institutions)
link to or embed them. Modeled on Karpathy's
[HackerTube](https://karpathy.bearblog.dev/hacker-tube/), but the signal is
editorial curation, not comments.

**Status:** live preview at https://econtube.org. Classification switches on when `OPENAI_API_KEY` is set. Choices are logged in `DECISIONS.md`.

## Layout

| path | what |
|---|---|
| `sources.yaml` | every curator source, with candidate feeds, weights, filters |
| `seeds.yaml` | low-weight YouTube search seeds, with a quota budget |
| `pipeline/econtube/extract.py` | YouTube/podcast/Vimeo URL extractor (all URL shapes) |
| `pipeline/econtube/score.py` | ranking formula, all constants documented |
| `pipeline/econtube/http.py` | polite client: honest UA, robots.txt, 1 req/s/host, ETag cache |
| `pipeline/probe.py` | step 1: verifies sources, writes `reports/probe.md` |
| `pipeline/ingest.py` | fetches curator posts (sitemap or WordPress paged feed), extracts links |
| `pipeline/build_data.py` | feeds + posts + podcasts → gate → classify → score → `data/videos.json` |
| `pipeline/econtube/llm.py`, `classify.py` | OpenAI relevance gate + facet classifier (validated against `taxonomy.yaml`) |
| `taxonomy.yaml`, `overrides.yaml` | controlled vocabularies; hand overrides that always win |
| `site/build_site.py`, `site/facets.py` | static site (stdlib only): home, item pages, topic/field/school/person/tag pages, /browse/, RSS |
| `pipeline/econtube/youtube.py` | YouTube Data API: full channel archives, video metadata, quota budget |
| `books.yaml`, `site.yaml` | book links (Amazon tag), sponsor line, support URL, contact |
| `OPERATIONS.md` | adding sources, retuning, keys, costs |
| `.github/workflows/` | tests on push; `probe-sources` (manual) |

## Run locally

```bash
pip install -r requirements.txt
```

```bash
pytest -q
```

```bash
OPENAI_API_KEY=... YOUTUBE_API_KEY=... python pipeline/build_data.py && python site/build_site.py
```

Secrets (GitHub → Settings → Secrets and variables → Actions): `OPENAI_API_KEY`, `YOUTUBE_API_KEY`.
Optional variable: `OPENAI_MODEL` to pin a model.

## Licence

Code: MIT. Dataset export (`data/econtube-export.json`): metadata and links
only. No video, audio or article text is rehosted.
