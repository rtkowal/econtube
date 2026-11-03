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
9. **Apify discovery report (2026-11-03) merged into `sources.yaml`.** Every feed it named was re-tested from
   our own client. Working: prywatyzacja.com/feed.xml (107 items, one shared feed for all three Polish
   sections, with items routed by URL path), weusecoins feed.xml, the DoubleLine feed, and the
   LSE Business Review /home/feed/ path. Not working: cato.org/rss (403), cepr.org/rss (403),
   hoover.org/rss (404), unchained /blog/rss.xml (404). The channels it found are recorded as
   `verified: false` until they are resolved through the YouTube API.
10. **Extractor reads only the post body.** It skips `header`, `footer`, `aside`, `nav`, sidebars and widgets,
    because a channel in a blogroll is not an editorial pick (the example is Naked Capitalism's sidebar). It also
    unwraps embed proxies (iframe.ly and Drupal `/media/oembed?url=`) and ignores music.youtube.com.
11. **Disabled sources:** Naked Capitalism (returns 403 to our User-Agent) and Calculated Risk (its feed host is
    unreachable and it has almost no videos). They stay in the file with `status: disabled` so the decision is visible.
12. **Rejected matches:** the Lyn Alden iTunes hits (shows she guests on; confirmed by owner),
    @drmatthewgoodwin on Niall Ferguson's page, and the iTunes "Unchained" show (Laura Shin's, not the company's).
13. **Marginal Revolution's archive is read through its own feed (`/feed?paged=N`), not post pages.** After about 1,500
    post fetches at 1 req/s, Cloudflare began challenging post pages and the sitemap, and the WordPress REST
    API requires login. Per the no-bypass rule we stopped. The public paged feed returns full post content 15 posts
    at a time back to at least 2010, so the backfill needs about 2,700 requests instead of about 40,000. It runs with
    an extra 4s delay between pages and stops for good on any 403 or 429. The same route applies to every
    WordPress source (Cafe Hayek, Ritholtz, Conversable Economist, IEA, etc.).
14. **The Nobel `/summary/` pages contain no YouTube embeds** (0 in 57 prize years). Nobel lectures come from the
    official @thenobelprize channel, filtered to "Economic Sciences", which needs the YouTube API key.
15. **Channels added by owner (2026-11-03), IDs taken from the handle pages and checked against each channel's RSS feed:**
    @NobelPrize = UC-V6odR7HzLCuqjYeowPjLA (the old @thenobelprize handle now returns 404), @EconomicsExplained =
    UCZ4AMrDcNrfy3X6nsU8-rPg, @CowenConvos = UC_AnpBvnhXTcipgGEHLWoOg (attached to Conversations with Tyler and
    related to Marginal Revolution), @HooverInstitution = UCzWwWbbKHg4aodl0S35R6XA, and the GoodFellows playlist
    PLKruweaZqDNetb7uwJF1vS0mzmaTe8Kzg. **@UncommonKnowledge is not Peter Robinson's show** (an unrelated channel with 1 video),
    so it is rejected. Uncommon Knowledge episodes are on the Hoover channel in yearly playlists. uncommonknowledge.org
    fails TLS. On hoover.org/plus only the economics playlists and podcasts are kept (trade, socialism vs capitalism,
    healthcare, China model; Capitalism and Freedom, Economics Applied, The Grumpy Economist, The Libertarian). The
    general-policy ones (Iran, Taiwan, AI, free speech, the Classicist, and so on) are skipped. The Hoover channel and GoodFellows go
    through the economics_only gate. The Sowell playlist skips the gate.
16. **YouTube channel RSS (`/feeds/videos.xml?channel_id=` or `playlist_id=`) works without a key** but returns only the
    newest 15 videos. It is good for the daily incremental run. A full backfill still needs the Data API (`playlistItems.list`).
