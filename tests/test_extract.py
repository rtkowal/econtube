import pytest

from econtube.extract import extract_refs, parse_podcast, parse_youtube

V = "dQw4w9WgXcQ"


@pytest.mark.parametrize("url", [
    f"https://www.youtube.com/watch?v={V}",
    f"http://youtube.com/watch?v={V}&feature=share",
    f"https://m.youtube.com/watch?app=desktop&v={V}",
    f"https://music.youtube.com/watch?v={V}",
    f"https://youtu.be/{V}",
    f"https://youtu.be/{V}?si=abc123",
    f"https://www.youtube.com/embed/{V}",
    f"https://www.youtube.com/embed/{V}?rel=0&start=30",
    f"//www.youtube.com/embed/{V}",
    f"https://www.youtube-nocookie.com/embed/{V}",
    f"https://www.youtube.com/shorts/{V}",
    f"https://www.youtube.com/live/{V}?feature=shared",
    f"https://www.youtube.com/v/{V}",
    f"https://www.youtube.com/watch?v={V}&amp;t=1m30s",
])
def test_video_shapes(url):
    refs = parse_youtube(url.replace("&amp;", "&"))
    assert [r.id for r in refs if r.kind == "youtube_video"] == [V]


def test_timestamp():
    assert parse_youtube(f"https://youtu.be/{V}?t=90")[0].start == 90
    assert parse_youtube(f"https://www.youtube.com/watch?v={V}&t=1h2m3s")[0].start == 3723


def test_playlist_shapes():
    pl = "PL01nDImtijMBKaj8K3QaCKX81OtTosVL4"
    for u in [f"https://www.youtube.com/playlist?list={pl}",
              f"https://www.youtube.com/embed/videoseries?list={pl}"]:
        refs = parse_youtube(u)
        assert [(r.kind, r.id) for r in refs] == [("youtube_playlist", pl)]
    refs = parse_youtube(f"https://www.youtube.com/watch?v={V}&list={pl}")
    assert {r.kind for r in refs} == {"youtube_video", "youtube_playlist"}


def test_mix_playlist_ignored():
    refs = parse_youtube(f"https://www.youtube.com/watch?v={V}&list=RD{V}")
    assert [r.kind for r in refs] == ["youtube_video"]


@pytest.mark.parametrize("url", [
    "https://www.youtube.com/@UnHerd",
    "https://www.youtube.com/channel/UCjB5Zb0i5q37j3yHDUECyxw",
    "https://www.youtube.com/watch?v=short",
    "https://youtu.be/",
    "https://notyoutube.com/watch?v=dQw4w9WgXcQ",
    "https://www.youtube.com/results?search_query=hayek",
])
def test_non_video(url):
    assert [r for r in parse_youtube(url) if r.kind == "youtube_video"] == []


def test_attribution_link():
    u = f"https://www.youtube.com/attribution_link?u=/watch%3Fv%3D{V}%26feature%3Dshare"
    assert parse_youtube(u)[0].id == V


def test_extract_html_iframe_and_dedupe():
    html = f'''
      <p>Watch <a href="https://youtu.be/{V}">this</a>.</p>
      <iframe src="https://www.youtube.com/embed/{V}?feature=oembed"></iframe>
      <iframe data-src="//www.youtube-nocookie.com/embed/abcdefghijk"></iframe>
      <a href="https://www.youtube.com/watch?v=ZZZZZZZZZZZ&amp;t=10s">x</a>.
      <a href="https://vimeo.com/123456789">v</a>
      <a href="https://podcasts.apple.com/us/podcast/econtalk/id135066958?i=1000">p</a>
      <a href="https://open.spotify.com/episode/4rOoJ6Egrf8K2IrywzwOMk?si=x">s</a>
      <enclosure url="https://cdn.example.com/ep1.mp3" />
    '''
    refs = extract_refs(html)
    vids = [r.id for r in refs if r.kind == "youtube_video"]
    assert vids == [V, "abcdefghijk", "ZZZZZZZZZZZ"]
    kinds = [r.kind for r in refs]
    assert kinds.count("vimeo") == 1 and kinds.count("audio_file") == 1
    plats = sorted(r.platform for r in refs if r.kind == "podcast")
    assert plats == ["apple", "spotify"]


def test_trailing_punctuation():
    assert extract_refs(f"see https://youtu.be/{V}.")[0].id == V


def test_podcast_non_episode_links_ignored():
    assert parse_podcast("https://open.spotify.com/track/abc") is None
    assert parse_podcast("https://podcasts.apple.com/us/browse") is None
