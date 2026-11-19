#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "requests>=2.28.0",
#   "tomli-w>=1.0.0",
#   "pytest>=8.0",
# ]
# ///

"""Tests for sync-videos.py."""

import json
import sys
from pathlib import Path

import pytest
import tomli_w

sys.path.insert(0, str(Path(__file__).resolve().parent))

from videotesting import FakeHttp, load_script, make_repo, write  # noqa: E402

s = load_script("sync-videos.py")


def video(vid="abcdefghijk", title="Intro to Quarto with Hadley Wickham", **overrides):
    v = {
        "url": f"https://www.youtube.com/watch?v={vid}",
        "title": title,
        "slug": f"2026-10-01_{title.lower().replace(' ', '-')}",
        "date": "2026-10-01T12:00:00Z",
        "description": "Learn Quarto and Shiny. #quarto",
        "duration": 600,
        "channel": "Posit PBC",
        "playlist": "",
        "tags": ["#quarto", "R/Python", "?", "data"],
        "view_count": 1,
        "like_count": 1,
        "comment_count": 0,
        "thumbnail": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
        "language": "en",
        "has_captions": False,
        "definition": "hd",
        "publish": True,
        "last_updated": "2026-11-01T00:00:00+00:00",
    }
    v.update(overrides)
    return v


def write_videos(repo, videos):
    (repo / "data/videos.toml").write_text(tomli_w.dumps({"videos": videos}))


def run(repo, http=None, *args):
    summary = repo / "summary.json"
    code = s.main(
        ["--project-root", str(repo), "--summary-json", str(summary), *args],
        http_get=http or FakeHttp(),
    )
    return code, json.loads(summary.read_text())


def items(data, status):
    return [i for i in data["items"] if i["status"] == status]


@pytest.fixture
def repo(tmp_path):
    return make_repo(tmp_path)


# --- Pure helpers ---


class TestComputeTopLevelKeys:
    def test_external_only(self):
        assert s.compute_top_level_keys({"title": "T", "people": ["A"]}, {}, {}, {}) == {
            "title": "T",
            "people": ["A"],
        }

    def test_include_dedupes(self):
        result = s.compute_top_level_keys({"software": ["quarto"]}, {"software": ["shiny", "quarto"]}, {}, {})
        assert result["software"] == ["quarto", "shiny"]

    def test_include_without_external_value(self):
        assert s.compute_top_level_keys({}, {"people": ["A"]}, {}, {})["people"] == ["A"]

    def test_exclude(self):
        result = s.compute_top_level_keys({"people": ["A", "B"]}, {}, {"people": ["B"]}, {})
        assert result["people"] == ["A"]

    def test_override_wins(self):
        result = s.compute_top_level_keys({"title": "T"}, {"title": ["x"]}, {}, {"title": "Better"})
        assert result["title"] == "Better"


class TestDetection:
    def test_people_word_boundaries(self):
        v = {"title": "Talk by Hadley Wickham", "description": "Not Hadley Wickhamson"}
        assert s.detect_people(v, ["Hadley Wickham", "Wickham Hadley"]) == ["Hadley Wickham"]

    def test_people_case_insensitive_and_unicode(self):
        v = {"title": "mine çetinkaya-rundel on teaching", "description": ""}
        assert s.detect_people(v, ["Mine Çetinkaya-Rundel"]) == ["Mine Çetinkaya-Rundel"]

    def test_no_partial_word_match(self):
        assert s.find_matches("Shinylive apps", ["Shiny"]) == []
        assert s.find_matches("Shiny, live", ["Shiny"]) == ["Shiny"]

    def test_software_returns_slugs(self):
        v = {"title": "Quarto tips", "description": "with shiny"}
        assert s.detect_software(v, {"quarto": "Quarto", "shiny": "Shiny", "gt": "gt"}) == ["quarto", "shiny"]


def test_build_external_cleans_tags():
    ext = s.build_external(video(), ["Hadley Wickham"], ["quarto"])
    assert ext["tags"] == ["quarto", "RPython", "data"]
    assert ext["people"] == ["Hadley Wickham"]
    assert ext["software"] == ["quarto"]
    assert "publish" not in ext and "slug" not in ext


def test_changed_keys():
    old = {"title": "A", "external": {"url": "u", "view_count": 1}, "tags": []}
    new = {"title": "B", "external": {"url": "u", "view_count": 2, "people": ["X"]}, "tags": []}
    assert s.changed_keys(old, new) == ["external.people", "external.view_count", "title"]


# --- main ---


class TestMain:
    def test_create(self, repo):
        write_videos(repo, [video()])
        http = FakeHttp()
        code, data = run(repo, http)
        assert code == 0
        d = repo / "content/resources/videos/2026-10-01_intro-to-quarto-with-hadley-wickham"
        fm, _, _ = s.parse_frontmatter((d / "_index.md").read_text())
        assert fm["title"] == "Intro to Quarto with Hadley Wickham"
        assert fm["date"] == "2026-10-01"
        assert fm["people"] == ["Hadley Wickham"]
        assert fm["software"] == ["quarto", "shiny"]  # "commons" is in the ignore list
        assert fm["image"] == "thumbnail.jpg"
        assert fm["resources"] == []
        assert fm["external"]["url"] == video()["url"]
        assert (d / "thumbnail.jpg").read_bytes() == b"JPEG:" + video()["thumbnail"].encode()
        (created,) = items(data, "created")
        assert created["video_id"] == "abcdefghijk"
        assert created["thumbnail"] == "downloaded (missing)"

    def test_second_run_unchanged_and_untouched(self, repo):
        write_videos(repo, [video()])
        run(repo)
        index = next((repo / "content/resources/videos").glob("*/_index.md"))
        mtime = index.stat().st_mtime_ns
        http = FakeHttp()
        code, data = run(repo, http)
        assert code == 0
        assert data["counts"] == {"unchanged": 1, "unpublished": 0}
        assert data["items"] == []
        assert index.stat().st_mtime_ns == mtime
        assert http.requested == []  # no thumbnail download

    def test_update_reports_changed_keys(self, repo):
        write_videos(repo, [video()])
        run(repo)
        write_videos(repo, [video(view_count=99, description="Nothing else here")])
        code, data = run(repo)
        (updated,) = items(data, "updated")
        assert updated["changes"] == [
            "description",
            "external.description",
            "external.software",
            "external.view_count",
            "software",
        ]

    def test_manual_blocks_and_body_preserved(self, repo):
        write_videos(repo, [video()])
        run(repo)
        index = next((repo / "content/resources/videos").glob("*/_index.md"))
        text = index.read_text().replace("---\n", "---\noverride:\n  title: Custom\nexclude:\n  software:\n  - shiny\n", 1)
        index.write_text(text + "Some body text.\n")
        run(repo)
        fm, _, body = s.parse_frontmatter(index.read_text())
        assert fm["title"] == "Custom"
        assert fm["software"] == ["quarto"]
        assert "Some body text." in body

    def test_override_date(self, repo):
        write_videos(repo, [video()])
        run(repo)
        index = next((repo / "content/resources/videos").glob("*/_index.md"))
        index.write_text(index.read_text().replace("---\n", "---\noverride:\n  date: 2025-09-17\n", 1))
        run(repo)
        assert s.parse_frontmatter(index.read_text())[0]["date"] == "2025-09-17"

    def test_unpublished_skipped(self, repo):
        write_videos(repo, [video(publish=False)])
        code, data = run(repo)
        assert data["counts"] == {"unpublished": 1}
        assert list((repo / "content/resources/videos").iterdir()) == []

    def test_rename_moves_dir_and_updates_references(self, repo):
        write_videos(repo, [video()])
        run(repo)
        videos_dir = repo / "content/resources/videos"
        old = videos_dir / "2026-10-01_intro-to-quarto-with-hadley-wickham"
        write(old / "transcription.vtt", "WEBVTT\n")
        post = write(
            repo / "content/blog/post/index.md",
            "See [talk](/resources/videos/2026-10-01_intro-to-quarto-with-hadley-wickham/) "
            "but not videos/2026-10-01_intro-to-quarto-with-hadley-wickham-part-2.\n",
        )
        write_videos(repo, [video(title="Quarto deep dive", slug="2026-10-01_quarto-deep-dive")])
        code, data = run(repo)
        assert code == 0
        assert not old.exists()
        assert (videos_dir / "2026-10-01_quarto-deep-dive/transcription.vtt").exists()
        assert post.read_text() == (
            "See [talk](/resources/videos/2026-10-01_quarto-deep-dive/) "
            "but not videos/2026-10-01_intro-to-quarto-with-hadley-wickham-part-2.\n"
        )
        (renamed,) = items(data, "renamed")
        assert renamed["action"] == "renamed"
        assert renamed["old_slug"] == "2026-10-01_intro-to-quarto-with-hadley-wickham"
        assert renamed["slug"] == "2026-10-01_quarto-deep-dive"
        assert renamed["updated_references"] == ["content/blog/post/index.md"]

    def test_merge_into_existing_dir(self, repo):
        videos_dir = repo / "content/resources/videos"
        write_videos(repo, [video()])
        run(repo)
        old = videos_dir / "2026-10-01_intro-to-quarto-with-hadley-wickham"
        write(old / "transcription.vtt", "WEBVTT\n")
        index = old / "_index.md"
        index.write_text(index.read_text().replace("---\n", "---\ninclude:\n  people:\n  - Someone\n", 1))
        # A directory for the new slug already exists (e.g. created by hand).
        write(videos_dir / "2026-10-01_new/_index.md", "---\ntitle: placeholder\n---\n")
        write_videos(repo, [video(title="New", slug="2026-10-01_new")])
        code, data = run(repo)
        assert not old.exists()
        new = videos_dir / "2026-10-01_new"
        assert (new / "transcription.vtt").exists()
        fm, _, _ = s.parse_frontmatter((new / "_index.md").read_text())
        assert fm["include"] == {"people": ["Someone"]}
        assert "Someone" in fm["people"]
        (renamed,) = items(data, "renamed")
        assert renamed["action"] == "merged"
        assert "transcription.vtt" in renamed["moved_files"]

    def test_orphan_reported(self, repo):
        write(
            repo / "content/resources/videos/2020-01-01_gone/_index.md",
            "---\ntitle: Gone\nexternal:\n  url: https://www.youtube.com/watch?v=gonegonegon\n---\n",
        )
        write_videos(repo, [video()])
        code, data = run(repo)
        assert code == 0
        (orphan,) = items(data, "orphan")
        assert orphan["slug"] == "2020-01-01_gone"
        assert (repo / "content/resources/videos/2020-01-01_gone").exists()

    def test_thumbnail_redownloaded_when_url_changes(self, repo):
        write_videos(repo, [video()])
        run(repo)
        new_url = "https://i.ytimg.com/vi/abcdefghijk/maxresdefault.jpg"
        write_videos(repo, [video(thumbnail=new_url)])
        http = FakeHttp()
        code, data = run(repo, http)
        assert http.requested == [new_url]
        thumb = next((repo / "content/resources/videos").glob("*/thumbnail.jpg"))
        assert thumb.read_bytes() == b"JPEG:" + new_url.encode()
        (updated,) = items(data, "updated")
        assert updated["thumbnail"] == "downloaded (url changed)"

    def test_thumbnail_failure_is_partial(self, repo, monkeypatch):
        monkeypatch.setattr(s.time, "sleep", lambda _: None)
        write_videos(repo, [video(), video("zyxwvutsrqp", "Second")])
        http = FakeHttp(fail_urls={video()["thumbnail"]})
        code, data = run(repo, http)
        assert code == 2
        (error,) = items(data, "error")
        assert error["reason"] == "thumbnail_failed"
        assert "connection refused" in error["detail"]
        assert http.requested.count(video()["thumbnail"]) == 2  # retried once
        # The page itself and the other video were still written.
        assert len(list((repo / "content/resources/videos").glob("*/_index.md"))) == 2
        # The next run tries again because the file is still missing.
        http2 = FakeHttp()
        code, _ = run(repo, http2)
        assert code == 0 and http2.requested == [video()["thumbnail"]]

    def test_dry_run_writes_nothing(self, repo):
        write_videos(repo, [video()])
        http = FakeHttp()
        code, data = run(repo, http, "--dry-run")
        assert code == 0
        assert list((repo / "content/resources/videos").iterdir()) == []
        assert http.requested == []
        (created,) = items(data, "created")
        assert created["thumbnail"] == "would download (missing)"

    def test_missing_videos_toml_is_fatal(self, repo):
        code, data = run(repo)
        assert code == 1
        assert "videos TOML not found" in data["fatal"]

    def test_logging(self, repo, capsys, monkeypatch):
        monkeypatch.setenv("CI", "true")
        write_videos(repo, [video()])
        run(repo)
        err = capsys.readouterr().err
        assert "Created 2026-10-01_intro-to-quarto-with-hadley-wickham (abcdefghijk)" in err
        assert "Summary: created=1, unpublished=0" in err


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-p", "no:cacheprovider", *sys.argv[1:]]))
