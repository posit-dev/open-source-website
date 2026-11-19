#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "pytest>=8.0",
# ]
# ///

"""Tests for video-sync-report.py."""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import videolib  # noqa: E402
from videotesting import load_script  # noqa: E402

r = load_script("video-sync-report.py")

ALL = list(r.STEPS)
RUN_URL = "https://github.com/posit-dev/open-source-website/actions/runs/1"


def summary(script, items=(), tallies=None, extra=None, fatal=None):
    s = videolib.RunSummary(script)
    for item in items:
        item = dict(item)
        s.add(item.pop("status"), **item)
    for status, n in (tallies or {}).items():
        s.tally(status, n)
    s.extra.update(extra or {})
    s.fatal = fatal
    return s.to_dict()


def quiet_night():
    return {
        "update-youtube-videos": summary("update-youtube-videos", tallies={"unchanged": 1750}, extra={"refresh_stats": False}),
        "sync-videos": summary("sync-videos", tallies={"unchanged": 1750}),
        "transcribe": summary("transcribe", tallies={"already_transcribed": 1750}),
        "format-transcriptions": summary("format-transcriptions", tallies={"already_formatted": 1750}),
    }


def typical_night():
    s = quiet_night()
    s["update-youtube-videos"] = summary(
        "update-youtube-videos",
        items=[
            {"status": "new", "url": "https://www.youtube.com/watch?v=aaaaaaaaaaa", "slug": "2026-11-11_new-talk", "title": "New | talk"},
            {"status": "changed", "slug": "2026-10-01_renamed", "changed_fields": ["title", "slug"], "old_slug": "2026-10-01_old"},
            {"status": "missing", "slug": "2025-01-01_gone", "url": "https://www.youtube.com/watch?v=ggggggggggg"},
        ],
        tallies={"unchanged": 1748},
        extra={"refresh_stats": False},
    )
    s["sync-videos"] = summary(
        "sync-videos",
        items=[
            {"status": "created", "slug": "2026-11-11_new-talk"},
            {
                "status": "renamed",
                "action": "renamed",
                "old_slug": "2026-10-01_old",
                "slug": "2026-10-01_renamed",
                "updated_references": ["content/blog/post/index.md"],
            },
        ],
        tallies={"unchanged": 1749},
    )
    s["transcribe"] = summary(
        "transcribe",
        items=[{"status": "transcribed", "slug": "2026-11-11_new-talk", "estimated_cost_usd": 0.12, "duration_s": 1200}],
        tallies={"already_transcribed": 1750},
        extra={"estimated_cost_usd": 0.12, "breaker_tripped": False},
    )
    s["format-transcriptions"] = summary(
        "format-transcriptions",
        items=[{"status": "formatted", "slug": "2026-11-11_new-talk", "estimated_cost_usd": 0.3, "warnings": None}],
        tallies={"already_formatted": 1750},
        extra={"estimated_cost_usd": 0.3},
    )
    return s


def blocked_night():
    s = typical_night()
    s["transcribe"] = summary(
        "transcribe",
        items=[
            {"status": "error", "slug": "2026-11-11_new-talk", "stage": "download", "reason": "bot_check", "detail": "ERROR: Sign in to confirm you’re not a bot"},
            {"status": "error", "slug": "2026-11-10_b", "stage": "download", "reason": "bot_check", "detail": "ERROR: Sign in"},
            {"status": "error", "slug": "2026-11-09_c", "stage": "download", "reason": "private", "detail": "ERROR: Private video"},
            {"status": "skipped", "slug": "2026-11-08_d", "reason": "download_blocked"},
        ],
        extra={"breaker_tripped": True},
    )
    s["format-transcriptions"] = summary("format-transcriptions", tallies={"already_formatted": 1750})
    return s


def build(summaries, expected=ALL):
    return r.build_report(summaries, expected=expected, run_url=RUN_URL)


def test_quiet_night():
    report, annotations = build(quiet_night())
    assert report == (
        "Nightly sync of [Posit's YouTube videos](https://www.youtube.com/@PositPBC) into "
        f"`content/resources/videos/` ([workflow run]({RUN_URL})).\n"
        "\n"
        "Review the changes below, then approve and merge to publish them.\n"
        "\n"
        "| Step | Result |\n"
        "| --- | --- |\n"
        "| YouTube metadata | 1,750 unchanged |\n"
        "| Video pages | 1,750 unchanged |\n"
        "| Transcription | nothing to do |\n"
        "| Formatting | nothing to do |\n"
        "\n"
        "---\n"
        "\n"
        "Adjust a video with `include`, `exclude`, or `override` blocks in its `_index.md`, hide it with "
        "`publish = false` in `data/videos.toml`, or skip its transcript with `transcribe: false`. "
        f"Logs and run summaries are attached to the [workflow run]({RUN_URL}).\n"
    )
    assert annotations == []


def test_typical_night():
    report, annotations = build(typical_night())
    assert "| YouTube metadata | 1 new, 1 changed, 1,748 unchanged |" in report
    assert "| Video pages | 1 created, 1 renamed, 1,749 unchanged |" in report
    assert "| Transcription | 1 transcribed (~$0.12) |" in report
    assert "| Formatting | 1 formatted (~$0.30) |" in report
    assert "### New videos (1)" in report
    assert "- [New \\| talk](https://www.youtube.com/watch?v=aaaaaaaaaaa) `2026-11-11_new-talk`" in report
    assert "- `2026-10-01_old` → `2026-10-01_renamed`; references updated in `content/blog/post/index.md`" in report
    assert "- `2026-10-01_renamed`: title, slug" in report
    assert "- `2026-11-11_new-talk`: transcribed and formatted" in report
    assert "### ⚠️ Problems" not in report
    assert "### Notes" in report and "no longer on the channel" in report
    assert annotations == []


def test_blocked_night():
    report, annotations = build(blocked_night())
    assert "| Transcription | ⚠️ 3 failed, downloads blocked |" in report
    assert "**YouTube blocked the downloads**" in report
    assert "1 more video skipped after repeated bot_check errors" in report
    assert "`just update-videos 15 chrome`" in report
    assert "`2026-11-10_b`: **bot_check**" in report
    assert "Fix: `just transcribe --video 2026-11-10_b --cookies-from-browser chrome`\n" in report
    assert "`2026-11-09_c`: **private**" in report and "or set `transcribe: false`" in report
    assert annotations == [
        "::warning title=YouTube blocked the downloads::1 item(s); see the step summary or PR description",
        "::warning title=Audio downloads failed::3 item(s); see the step summary or PR description",
    ]


def test_waiting_for_transcripts():
    s = quiet_night()
    del s["transcribe"]
    s["format-transcriptions"] = summary(
        "format-transcriptions",
        tallies={"already_formatted": 1700, "no_vtt": 2},
        extra={"needs_transcript": ["2026-11-11_b", "2026-11-10_a"]},
    )
    report, annotations = build(s, expected=["update-youtube-videos", "sync-videos", "format-transcriptions"])
    assert "Transcription" not in report  # the step didn't run and wasn't expected
    assert "**2 videos waiting for a transcript.**" in report
    assert "git switch -C automation/sync-videos origin/automation/sync-videos" in report
    assert "just transcribe --limit 15" in report
    assert "- `2026-11-11_b`\n- `2026-11-10_a`" in report
    assert annotations == []


def test_stats_refresh():
    s = quiet_night()
    s["update-youtube-videos"] = summary(
        "update-youtube-videos", tallies={"stats_refreshed": 1700, "unchanged": 50}, extra={"refresh_stats": True}
    )
    report, _ = build(s)
    assert "| YouTube metadata | 1,750 unchanged, stats refreshed |" in report


def test_formatting_errors_and_warnings():
    s = typical_night()
    s["format-transcriptions"] = summary(
        "format-transcriptions",
        items=[
            {"status": "error", "slug": "2026-11-11_new-talk", "reason": "low_coverage", "detail": "Only 80% of the words"},
            {"status": "formatted", "slug": "2026-11-01_x", "warnings": ["timestamp_overshoot: 44s"]},
        ],
    )
    report, annotations = build(s)
    assert "`2026-11-11_new-talk`: transcribed (not formatted yet)" in report
    assert "`2026-11-01_x`: ⚠️ timestamp_overshoot: 44s" in report
    assert "**Formatting failed**" in report
    assert "`just format-transcriptions --video 2026-11-11_new-talk`" in report
    assert annotations == ["::warning title=Formatting failed::1 item(s); see the step summary or PR description"]


def test_fatal_and_missing_summaries():
    s = quiet_night()
    s["update-youtube-videos"] = summary("update-youtube-videos", fatal="YOUTUBE_API_KEY not found")
    del s["format-transcriptions"]
    report, annotations = build(s)
    assert "| YouTube metadata | ❌ failed: YOUTUBE_API_KEY not found |" in report
    assert "| Formatting | ⚠️ no summary (crashed?) |" in report
    assert "**YouTube metadata failed**" in report
    assert annotations[0].startswith("::error title=YouTube metadata failed::")
    assert annotations[1].startswith("::error title=Formatting produced no summary::")


def test_skipped_steps_not_expected():
    s = quiet_night()
    del s["transcribe"], s["format-transcriptions"]
    report, annotations = build(s, expected=["update-youtube-videos", "sync-videos"])
    assert "Transcription" not in report and annotations == []


def test_long_lists_are_truncated():
    s = quiet_night()
    s["update-youtube-videos"] = summary(
        "update-youtube-videos",
        items=[
            {"status": "new", "url": f"https://www.youtube.com/watch?v={i:011d}", "slug": f"s{i}", "title": f"T{i}"}
            for i in range(100)
        ],
    )
    report, _ = build(s)
    assert "…and 60 more" in report
    assert len(report) < 65_536


def test_main_reads_directory(tmp_path, capsys):
    for script, data in typical_night().items():
        (tmp_path / f"{script}.json").write_text(json.dumps(data))
    (tmp_path / "junk.json").write_text("{not json")
    out = tmp_path / "body.md"
    assert r.main([str(tmp_path), "--output", str(out), "--annotations", "--run-url", RUN_URL]) == 0
    assert "### New videos (1)" in out.read_text()
    captured = capsys.readouterr()
    assert captured.out == ""  # no annotations on a typical night
    assert "could not read" in captured.err


def test_main_missing_directory(tmp_path, capsys):
    assert r.main([str(tmp_path / "nope"), "--annotations"]) == 0
    out = capsys.readouterr().out
    assert "⚠️ no summary (crashed?)" in out
    assert "::error title=YouTube metadata produced no summary::" in out


def test_default_run_url(monkeypatch):
    monkeypatch.setenv("GITHUB_SERVER_URL", "https://github.com")
    monkeypatch.setenv("GITHUB_REPOSITORY", "posit-dev/open-source-website")
    monkeypatch.setenv("GITHUB_RUN_ID", "1")
    assert r.default_run_url() == RUN_URL
    monkeypatch.delenv("GITHUB_RUN_ID")
    assert r.default_run_url() is None


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-p", "no:cacheprovider", *sys.argv[1:]]))
