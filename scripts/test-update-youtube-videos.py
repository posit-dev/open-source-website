#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-api-python-client>=2.100.0",
#   "tomli-w>=1.0.0",
#   "python-dotenv>=1.0.0",
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "pytest>=8.0",
# ]
# ///

"""Tests for update-youtube-videos.py."""

import json
import sys
import tomllib
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from videotesting import FakeYouTube, load_script, make_repo, yt_item  # noqa: E402

u = load_script("update-youtube-videos.py")

NOW = "2026-11-12T05:00:00+00:00"
EARLIER = "2026-10-01T00:00:00+00:00"


# --- Pure helpers ---


@pytest.mark.parametrize(
    "title, slug",
    [
        ("Hello, World!", "hello-world"),
        ("Mine Çetinkaya-Rundel | Teaching R", "mine-cetinkaya-rundel-teaching-r"),
        ("posit::conf(2025) — keynote", "positconf2025-keynote"),
        ("  spaces   and--dashes ", "spaces-and-dashes"),
    ],
)
def test_slugify(title, slug):
    assert u.slugify(title) == slug


@pytest.mark.parametrize(
    "duration, seconds",
    [
        ("PT1H2M3S", 3723),
        ("PT45S", 45),
        ("PT10M", 600),
        ("P1DT2H", 93600),
        ("P0D", 0),  # live streams
        ("", 0),
        ("garbage", 0),
    ],
)
def test_parse_iso8601_duration(duration, seconds):
    assert u.parse_iso8601_duration(duration) == seconds


def test_best_thumbnail():
    assert u.best_thumbnail({"high": {"url": "h"}, "maxres": {"url": "m"}}) == "m"
    assert u.best_thumbnail({"default": {"url": "d"}}) == "d"
    assert u.best_thumbnail({}) == ""


def test_transform_video():
    item = yt_item("abcdefghijk", "My Talk", tags=["R", "#quarto"], views=5, duration="PT1M5S")
    v = u.transform_video(item, "Posit PBC", "PLx", NOW)
    assert v == {
        "url": "https://www.youtube.com/watch?v=abcdefghijk",
        "title": "My Talk",
        "slug": "2026-10-01_my-talk",
        "date": "2026-10-01T12:00:00Z",
        "description": "",
        "duration": 65,
        "channel": "Posit PBC",
        "playlist": "PLx",
        "tags": ["R", "#quarto"],
        "view_count": 5,
        "like_count": 10,
        "comment_count": 1,
        "thumbnail": "https://i.ytimg.com/vi/abcdefghijk/hqdefault.jpg",
        "language": "en",
        "has_captions": False,
        "definition": "hd",
        "publish": True,
        "last_updated": NOW,
    }


def test_transform_uses_channel_title_when_unknown():
    v = u.transform_video(yt_item("abcdefghijk", channel_title="Other"), "", "", NOW)
    assert v["channel"] == "Other"


# --- merge_video ---


def stored(**overrides):
    v = u.transform_video(yt_item("abcdefghijk", "My Talk"), "Posit PBC", "", EARLIER)
    v.update(overrides)
    return v


def fetched(**item_kwargs):
    return u.transform_video(yt_item("abcdefghijk", **{"title": "My Talk", **item_kwargs}), "Posit PBC", "", NOW)


class TestMergeVideo:
    def test_new(self):
        video, changed, stats = u.merge_video(None, fetched(), refresh_stats=False, now=NOW)
        assert video["last_updated"] == NOW and changed == [] and stats == []

    def test_unchanged_keeps_timestamp(self):
        video, changed, stats = u.merge_video(stored(), fetched(), refresh_stats=False, now=NOW)
        assert changed == [] and stats == []
        assert video["last_updated"] == EARLIER
        assert video == stored()

    def test_title_change_bumps_timestamp_and_slug(self):
        video, changed, _ = u.merge_video(stored(), fetched(title="New Title"), refresh_stats=False, now=NOW)
        assert changed == ["title", "slug"]
        assert video["slug"] == "2026-10-01_new-title"
        assert video["last_updated"] == NOW

    def test_stats_kept_without_refresh(self):
        video, changed, stats = u.merge_video(stored(), fetched(views=999), refresh_stats=False, now=NOW)
        assert changed == [] and stats == []
        assert video["view_count"] == 100
        assert video["last_updated"] == EARLIER

    def test_stats_refreshed(self):
        video, changed, stats = u.merge_video(stored(), fetched(views=999, likes=11), refresh_stats=True, now=NOW)
        assert changed == []
        assert stats == ["view_count", "like_count"]
        assert video["view_count"] == 999 and video["last_updated"] == NOW

    def test_refresh_without_stat_changes_keeps_timestamp(self):
        video, _, stats = u.merge_video(stored(), fetched(), refresh_stats=True, now=NOW)
        assert stats == [] and video["last_updated"] == EARLIER

    def test_publish_false_preserved(self):
        video, changed, _ = u.merge_video(stored(publish=False), fetched(), refresh_stats=False, now=NOW)
        assert video["publish"] is False and changed == []

    def test_manual_keys_preserved(self):
        video, changed, _ = u.merge_video(stored(note="keep me"), fetched(), refresh_stats=False, now=NOW)
        assert video["note"] == "keep me" and changed == []


# --- deduplicate_videos ---


class TestDeduplicate:
    def videos(self):
        a = {"slug": "s", "date": "2026-01-01T10:00:00Z"}
        b = {"slug": "s", "date": "2026-01-01T11:00:00Z"}
        c = {"slug": "other", "date": "2026-01-01T10:00:00Z"}
        return {"url-a": a, "url-b": b, "url-c": c}

    def test_prefers_existing_entry(self):
        result, discarded = u.deduplicate_videos(self.videos(), existing_urls={"url-a"})
        assert set(result) == {"url-a", "url-c"}
        assert discarded == [{"url": "url-b", "slug": "s", "kept": "url-a"}]

    def test_then_later_date(self):
        result, _ = u.deduplicate_videos(self.videos(), existing_urls=set())
        assert set(result) == {"url-b", "url-c"}

    def test_stable_across_runs(self):
        first, _ = u.deduplicate_videos(self.videos(), existing_urls={"url-a", "url-b"})
        second, _ = u.deduplicate_videos(self.videos(), existing_urls=set(first))
        assert set(first) == set(second)

    def test_preserves_order(self):
        result, _ = u.deduplicate_videos(self.videos(), existing_urls={"url-a"})
        assert list(result) == ["url-a", "url-c"]


# --- Fake API ---


def fake_api(**overrides) -> FakeYouTube:
    yt = FakeYouTube(
        channels={"PositPBC": ("UUposit", "Posit PBC")},
        playlists={"UUposit": ["video000001", "video000002", "video000003"], "PLtest": ["video000003"]},
        videos={
            "video000001": yt_item("video000001", "First talk", published="2026-10-01T10:00:00Z"),
            "video000002": yt_item("video000002", "Second talk", published="2026-10-02T10:00:00Z"),
            "video000003": yt_item("video000003", "Third talk", published="2026-10-03T10:00:00Z"),
            "indiv000001": yt_item("indiv000001", "Elsewhere", published="2025-01-01T10:00:00Z"),
        },
        page_size=2,  # exercise pagination
    )
    for k, v in overrides.items():
        setattr(yt, k, v)
    return yt


def run(repo, yt, *args):
    summary = repo / "summary.json"
    code = u.main(["--project-root", str(repo), "--summary-json", str(summary), *args], youtube=yt)
    data = json.loads(summary.read_text())
    return code, data


def read_videos(repo):
    with open(repo / "data/videos.toml", "rb") as f:
        return {v["url"].rsplit("=", 1)[1]: v for v in tomllib.load(f)["videos"]}


@pytest.fixture
def repo(tmp_path):
    return make_repo(tmp_path)


class TestMain:
    def test_first_run(self, repo):
        code, data = run(repo, fake_api())
        assert code == 0
        videos = read_videos(repo)
        assert set(videos) == {"video000001", "video000002", "video000003", "indiv000001"}
        assert videos["video000003"]["playlist"] == "PLtest"
        assert videos["video000003"]["channel"] == "Posit PBC"
        assert videos["indiv000001"]["channel"] == "Posit PBC"  # from snippet.channelTitle
        assert data["counts"] == {"new": 4}
        new = {i["video_id"]: i for i in data["items"]}
        assert new["video000001"]["slug"] == "2026-10-01_first-talk"
        assert new["video000001"]["title"] == "First talk"
        assert data["extra"]["quota_used"] > 0

    def test_second_run_is_byte_identical_and_not_rewritten(self, repo):
        run(repo, fake_api())
        path = repo / "data/videos.toml"
        before = path.read_bytes()
        mtime = path.stat().st_mtime_ns
        code, data = run(repo, fake_api())
        assert code == 0
        assert path.read_bytes() == before
        assert path.stat().st_mtime_ns == mtime
        assert data["counts"] == {"unchanged": 4}
        assert data["extra"]["written"] is False

    def test_stats_only_change_without_refresh(self, repo):
        run(repo, fake_api())
        before = (repo / "data/videos.toml").read_bytes()
        yt = fake_api()
        yt.videos_data["video000001"] = yt_item("video000001", "First talk", published="2026-10-01T10:00:00Z", views=5000)
        code, data = run(repo, yt)
        assert (repo / "data/videos.toml").read_bytes() == before
        assert data["counts"] == {"unchanged": 4}

    def test_stats_change_with_refresh(self, repo):
        run(repo, fake_api())
        yt = fake_api()
        yt.videos_data["video000001"] = yt_item("video000001", "First talk", published="2026-10-01T10:00:00Z", views=5000)
        code, data = run(repo, yt, "--refresh-stats")
        assert read_videos(repo)["video000001"]["view_count"] == 5000
        assert data["counts"] == {"stats_refreshed": 1, "unchanged": 3}
        assert data["extra"]["refresh_stats"] is True

    def test_title_change(self, repo):
        run(repo, fake_api())
        yt = fake_api()
        yt.videos_data["video000002"] = yt_item("video000002", "Renamed talk", published="2026-10-02T10:00:00Z")
        code, data = run(repo, yt)
        (item,) = data["items"]
        assert item["status"] == "changed"
        assert item["changed_fields"] == ["title", "slug"]
        assert item["old_slug"] == "2026-10-02_second-talk"
        assert item["slug"] == "2026-10-02_renamed-talk"

    def test_missing_and_unavailable(self, repo):
        run(repo, fake_api())
        yt = fake_api()
        yt.playlists_data["UUposit"] = ["video000002", "video000003"]  # 1 removed from channel
        del yt.videos_data["video000003"]  # 3 went private
        code, data = run(repo, yt)
        assert code == 0
        statuses = {i["video_id"]: i["status"] for i in data["items"]}
        assert statuses == {"video000001": "missing", "video000003": "unavailable"}
        # Nothing is removed automatically.
        assert set(read_videos(repo)) == {"video000001", "video000002", "video000003", "indiv000001"}

    def test_publish_false_survives(self, repo):
        run(repo, fake_api())
        path = repo / "data/videos.toml"
        path.write_text(path.read_text().replace("publish = true", "publish = false", 1))
        before = path.read_bytes()
        run(repo, fake_api())
        assert path.read_bytes() == before

    def test_one_source_fails_is_partial(self, repo):
        yt = fake_api()
        yt.fail_playlists = {"PLtest"}
        code, data = run(repo, yt)
        assert code == 2
        (error,) = [i for i in data["items"] if i["status"] == "error"]
        assert error["source"] == "playlist:PLtest"
        assert "PLtest" in error["detail"]
        # Everything else is still written.
        assert "video000001" in read_videos(repo)

    def test_all_sources_fail_is_fatal_and_writes_nothing(self, repo):
        yt = fake_api(channels_data={})
        yt.fail_playlists = {"PLtest"}
        code, data = run(repo, yt)
        assert code == 1
        assert "All 2 channels and playlists failed" in data["fatal"]
        assert not (repo / "data/videos.toml").exists()

    def test_videos_api_failure_is_fatal(self, repo):
        run(repo, fake_api())
        before = (repo / "data/videos.toml").read_bytes()
        yt = fake_api()
        yt.fail_videos = True
        code, data = run(repo, yt)
        assert code == 1
        assert "quotaExceeded" in data["fatal"]
        assert (repo / "data/videos.toml").read_bytes() == before

    def test_corrupt_videos_toml_is_fatal(self, repo):
        (repo / "data/videos.toml").write_text("this is [not toml")
        code, data = run(repo, fake_api())
        assert code == 1
        assert "Could not parse" in data["fatal"]
        assert (repo / "data/videos.toml").read_text() == "this is [not toml"

    def test_missing_config_is_fatal(self, repo):
        (repo / "data/youtube.toml").unlink()
        code, data = run(repo, fake_api())
        assert code == 1 and "Config file not found" in data["fatal"]

    def test_missing_api_key_is_fatal(self, repo, monkeypatch):
        monkeypatch.delenv("YOUTUBE_API_KEY", raising=False)
        summary = repo / "s.json"
        code = u.main(["--project-root", str(repo), "--summary-json", str(summary)])
        assert code == 1
        assert "YOUTUBE_API_KEY" in json.loads(summary.read_text())["fatal"]

    def test_dry_run_writes_nothing(self, repo):
        code, data = run(repo, fake_api(), "--dry-run")
        assert code == 0
        assert not (repo / "data/videos.toml").exists()
        assert data["counts"] == {"new": 4}

    def test_duplicate_slug_is_stable(self, repo):
        yt = fake_api()
        yt.playlists_data["UUposit"].append("video000004")
        yt.videos_data["video000004"] = yt_item("video000004", "First talk", published="2026-10-01T23:00:00Z")
        run(repo, yt)
        first = read_videos(repo)
        code, data = run(repo, yt)
        assert read_videos(repo) == first
        dupes = [i for i in data["items"] if i["status"] == "duplicate_slug"]
        assert len(dupes) == 1 and dupes[0]["slug"] == "2026-10-01_first-talk"

    def test_logs_changes(self, repo, capsys, monkeypatch):
        monkeypatch.setenv("CI", "true")
        run(repo, fake_api())
        err = capsys.readouterr().err
        assert "New: 2026-10-01_first-talk (video000001) 'First talk'" in err
        assert "API quota used" in err
        assert "Summary: new=4" in err


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-p", "no:cacheprovider", *sys.argv[1:]]))
