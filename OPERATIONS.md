# Operations

How EconTube runs, and the routine changes you'll make. Product decisions and their reasons are in `DECISIONS.md`.

## How it runs

```
GitHub Actions "refresh" (every 6 h, 00:17/06:17/12:17/18:17 UTC; also manual: Actions → refresh → Run workflow)
  ingest.py      curator posts: newest 2 feed pages + 40 archive pages per blog (resumes from a cursor)
  build_data.py  YouTube channels/playlists (full archives, incremental) + post links + podcasts
                 → relevance gate (OpenAI) → videos.list enrichment → classification → score
  commit data/*.json  →  Vercel rebuilds the static site (site/build_site.py, ~seconds)
```

Caches (`.cache/`: raw posts, LLM decisions, YouTube lists and metadata) live in the Actions cache, not in git.
If the cache is ever lost, the next runs rebuild it; the cost is paying for LLM decisions again.

## Add a source

1. Add an entry to `sources.yaml`:
   ```yaml
   - id: my-source            # lowercase, unique
     name: My Source
     url: https://example.com/
     type: rss                # rss | sitemap | html | youtube_channel | curated_list
     weight: 1.0              # 0.25 seed … 3.0 top curator
     feeds: [https://example.com/feed/]
     backfill: paged_feed     # only if <feed>?paged=2 returns older posts (WordPress)
     youtube_channels: [{id: UC..., handle: "@x", verified: true, filter: economics_only}]
     podcast_feeds: [{name: Show, rss: "https://...", verified: true}]
   ```
   Use `filter: economics_only` for general-interest channels. Only `verified: true` channels are ingested.
2. Optional check: `python pipeline/probe.py --only my-source`.
3. Commit. The next refresh picks it up.

To find a channel ID from a handle, open `https://www.youtube.com/@handle`; the page source contains
`"externalId":"UC…"`. Or let the YouTube API do it: `channels.list?forHandle=@handle`.

## Remove or pause a source
Set `status: disabled` and add a `status_reason`. Its items drop out at the next refresh.

## Retune ranking
All constants are in `pipeline/econtube/score.py`, with tests in `tests/test_score.py`:

| constant | default | meaning |
|---|---|---|
| `EDITORIAL_MULT` | 1.5 | a third-party video linked in a curator's post |
| `SELF_MULT` | 1.0 | a source's own channel or podcast |
| `HALF_LIFE_DAYS` | 730 | recommendation recency half-life |
| `DECAY_FLOOR` | 0.25 | old recommendations never decay below this |
| `VIEWS_COEF` | 0.05 | weight of log10(views) |

Source weights are in `sources.yaml`. Run `pytest -q` after changing anything.

## Fix a classification
Add the item to `overrides.yaml`; it always wins over the model:
```yaml
dQw4w9WgXcQ:
  topics: [inflation, the-fed]
  schools: [chicago-monetarist]
  format: lecture
```

## Change the taxonomy
Edit `taxonomy.yaml`. **Adding** a topic is cheap. Existing items keep their tags until reclassified.
To reclassify everything, bump `CLASSIFY_CACHE` in `pipeline/econtube/classify.py`; that pays for every item again.
Values the model wanted but couldn't use are logged to `taxonomy_suggestions.jsonl` in the Actions cache.

## Keys and secrets

| name | where | used by |
|---|---|---|
| `YOUTUBE_API_KEY` | GitHub → Settings → Secrets → Actions | refresh, sample |
| `OPENAI_API_KEY` | same | refresh (only when `CLASSIFY=on`), sample |
| `CLASSIFY` (variable) | GitHub → Settings → Variables → Actions | `on` enables LLM gate and classification |
| `OPENAI_MODEL` (variable, optional) | same | pins a model; otherwise the cheapest suitable one is picked automatically |

**Rotate a key:** create a new key at the provider (Google Cloud Console → Credentials; platform.openai.com → API keys),
paste it over the GitHub secret, run "refresh" once to confirm, then delete the old key at the provider.
Vercel needs no keys.

## Monthly costs

| item | cost | notes |
|---|---|---|
| Vercel | $0 (Hobby) / $20 (Pro) | Pro is required once the site carries sponsors or affiliate links. The site is static. |
| OpenAI | backfill once, then small | about 1,100 input + 350 output tokens per new item (measured, gpt-5.4-nano). Multiply by current prices. Daily new items: tens. |
| YouTube Data API | $0 | free quota of 10,000 units/day. A run uses at most `QUOTA_BUDGET` (3,000). |
| GitHub Actions | $0 | public repository |
| Domain | ~$20/yr | GoDaddy |

Watch spend in the "usage summary" step of each refresh run, and set a monthly budget cap in the OpenAI dashboard.

## When something breaks
- **A refresh fails:** open the run log. Each source fails on its own; a red run is usually a commit or push conflict, and the next run recovers.
- **A source starts returning 403:** that's its bot protection. Don't work around it; set `status: disabled` with the reason.
- **Site build fails on Vercel:** `site/build_site.py` uses only the Python standard library, so a failure means bad data. Check the last data commit.
- **DNS:** econtube.org has A records `216.150.1.1` and `216.150.16.1`; www is a CNAME to `7e64eb5551f3c553.vercel-dns-016.com`, redirecting 301 to the apex.
