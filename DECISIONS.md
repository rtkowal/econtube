# Decisions log

Product and engineering choices made without explicit instruction. Simplest option wins.

1. **Feed URLs in `sources.yaml` are candidates, not facts.** They are standard conventions
   (WordPress `/feed`, Substack `/feed`, Blogger `/feeds/posts/default`). `probe.py` confirms
   each one. The EconTalk Simplecast URL came from memory and is flagged for the probe to confirm.
2. **Probe runs in GitHub Actions**, not in the build sandbox. The sandbox's egress policy
   blocks the source hosts, the YouTube API and iTunes. Actions runners have open egress.
3. **Added sources that the brief implied but didn't list:** `econtalk`,
   `conversations-with-tyler`, `free-to-choose-network`. Each gets its own row so weights can
   be tuned separately from the parent institution.
4. **Scoring dedup:** a source counts once per video and keeps its single best (most recent)
   recommendation. `DECAY_FLOOR = 0.25` stops 1970s Friedman lectures from decaying to zero:
   a classic recommended by four curators should still beat a new video recommended by one.
5. **Recency half-life: 2 years.** Econ videos age slowly. Tunable in `score.py`.
6. **Auto-generated YouTube "Mix" playlists (`list=RD…`) are ignored.** They are per-user and not
   editorial picks.
7. **Channels found on a homepage are `verified: false`** until reviewed. Only IDs and handles
   given in config are `verified: true`.
8. **Site generator: plain HTML + a Python build script (decision pending step 3).** It can use
   the pipeline's language, so we don't need a Node toolchain to keep the client JS under 50KB.
   If Astro turns out simpler for the per-topic pages, this entry gets revised.
