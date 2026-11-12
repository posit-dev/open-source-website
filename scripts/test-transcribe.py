#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "openai>=2.0.0",
#   "python-dotenv>=1.0.0",
#   "yt-dlp>=2025.0",
#   "pytest>=8.0",
# ]
# ///

"""Tests for transcribe.py. yt-dlp and Whisper are faked; ffmpeg is real when installed."""

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import videolib  # noqa: E402
from videotesting import (  # noqa: E402
    SAMPLE_VTT,
    FakeOpenAI,
    FakeYtDlp,
    RateLimitError,
    StatusError,
    load_script,
    make_repo,
    no_sleep,
    write_video_dir,
)

t = load_script("transcribe.py")

needs_ffmpeg = pytest.mark.skipif(not shutil.which("ffmpeg"), reason="ffmpeg not installed")

# Real yt-dlp error output (shortened where it's long).
BOT_CHECK = (
    "ERROR: [youtube] dQw4w9WgXcQ: Sign in to confirm you’re not a bot. Use --cookies-from-browser "
    "or --cookies for the authentication. See  https://github.com/yt-dlp/yt-dlp/wiki/FAQ"
)
PO_TOKEN = (
    "WARNING: [youtube] dQw4w9WgXcQ: mweb client https formats require a GVS PO Token which was not "
    "provided. They will be skipped as they may yield HTTP Error 403.\n"
    "ERROR: [youtube] dQw4w9WgXcQ: Requested format is not available. Use --list-formats for a list of available formats"
)
NETWORK = (
    "ERROR: [youtube] dQw4w9WgXcQ: Unable to download API page: <urlopen error [Errno -3] "
    "Temporary failure in name resolution> (caused by TransportError)"
)
HTTP_403 = "ERROR: unable to download video data: HTTP Error 403: Forbidden"

URL_A = "https://www.youtube.com/watch?v=aaaaaaaaaaa"
URL_B = "https://www.youtube.com/watch?v=bbbbbbbbbbb"
URL_C = "https://www.youtube.com/watch?v=ccccccccccc"
URL_D = "https://www.youtube.com/watch?v=ddddddddddd"


@pytest.mark.parametrize(
    "output, reason",
    [
        (BOT_CHECK, "bot_check"),
        ("ERROR: [youtube] x: Sign in to confirm you're not a bot. This helps protect our community.", "bot_check"),
        (PO_TOKEN, "po_token"),
        (
            "ERROR: [youtube] x: Sign in to confirm your age. This video may be inappropriate for some users.",
            "age_restricted",
        ),
        (
            "ERROR: [youtube] x: Private video. Sign in if you've been granted access to this video",
            "private",
        ),
        (
            "ERROR: [youtube] x: Join this channel to get access to members-only content like this video",
            "members_only",
        ),
        ("ERROR: [youtube] x: This live event will begin in 3 hours.", "live_or_upcoming"),
        ("ERROR: [youtube] x: Premieres in 2 hours", "live_or_upcoming"),
        ("ERROR: [youtube] x: Video unavailable. This video has been removed by the uploader", "unavailable"),
        (HTTP_403, "http_403"),
        ("ERROR: unable to download video data: HTTP Error 429: Too Many Requests", "http_429"),
        (NETWORK, "network"),
        ("ERROR: [youtube] x: Read timed out.", "network"),
        (
            "WARNING: [youtube] No supported JavaScript runtime could be found.\n"
            "ERROR: [youtube] x: Requested format is not available.",
            "js_runtime",
        ),
        ("ERROR: [youtube] x: Requested format is not available.", "format_unavailable"),
        # An unrelated warning must not override a clear error.
        ("WARNING: GVS PO Token which was not provided\nERROR: [youtube] x: Video unavailable", "unavailable"),
        ("something else entirely", "unknown"),
        ("", "unknown"),
    ],
)
def test_classify_ytdlp_error(output, reason):
    assert t.classify_ytdlp_error(output) == reason


def test_last_error_line():
    assert t.last_error_line(PO_TOKEN).startswith("ERROR: [youtube] dQw4w9WgXcQ: Requested format")
    assert t.last_error_line("just a line\n\n") == "just a line"
    assert t.last_error_line("") == "(no output)"


class TestCircuitBreaker:
    def test_trips_after_consecutive_blocks(self):
        b = t.CircuitBreaker(threshold=3)
        for reason in ["bot_check", "po_token"]:
            b.record(reason)
        assert not b.tripped
        b.record("http_429")
        assert b.tripped

    def test_other_outcomes_reset(self):
        b = t.CircuitBreaker(threshold=3)
        for reason in ["bot_check", "bot_check", None, "bot_check", "private", "bot_check"]:
            b.record(reason)
        assert not b.tripped and b.consecutive == 1


def test_build_ytdlp_cmd(tmp_path):
    cmd = t.build_ytdlp_cmd(URL_A, tmp_path, "chrome", Path("c.txt"))
    assert cmd[1:3] == ["-m", "yt_dlp"]
    assert "--remote-components" in cmd and "ejs:github" in cmd
    assert cmd[cmd.index("--output") + 1] == str(tmp_path / "audio.%(ext)s")
    assert cmd[cmd.index("--cookies-from-browser") + 1] == "chrome"
    assert cmd[cmd.index("--cookies") + 1] == "c.txt"
    assert "--no-warnings" not in cmd  # warnings explain failures
    assert cmd[-1] == URL_A


class TestChunking:
    def test_single_chunk(self):
        assert t.compute_chunk_boundaries(100, 10, [50], max_bytes=100) == [(0.0, 100)]

    def test_cuts_at_last_silence_before_limit(self):
        # 100 s at 1 byte/s, 40 bytes per chunk -> at most 40 s per chunk.
        assert t.compute_chunk_boundaries(100, 100, [10, 35, 38, 70, 79], max_bytes=40) == [
            (0.0, 38),
            (38, 70),
            (70, 100),
        ]

    def test_hard_cut_without_silence(self):
        assert t.compute_chunk_boundaries(100, 100, [], max_bytes=40) == [(0.0, 40.0), (40.0, 80.0), (80.0, 100)]

    def test_merge_vtt_offsets(self):
        part = "WEBVTT\n\n00:00:01.000 --> 00:00:02.000\nhi\n"
        merged = t.merge_vtt([(part, 0.0), (part, 600.5)])
        assert videolib.parse_vtt(merged) == [(1.0, 2.0, "hi"), (601.5, 602.5, "hi")]


class TestCheckTranscript:
    def test_empty(self):
        with pytest.raises(t.TranscriptError) as e:
            t.check_transcript("WEBVTT\n\n", 100)
        assert e.value.reason == "empty_transcript"

    def test_ok(self):
        cues, warnings = t.check_transcript(SAMPLE_VTT, 26)
        assert len(cues) == 3 and warnings == []

    def test_truncated(self):
        _, warnings = t.check_transcript(SAMPLE_VTT, 600)
        assert warnings == ["suspect_truncated: last cue ends at 00:00:25.000 of 00:10:00.000"]


def test_build_prompt():
    assert t.build_prompt({"title": "Quarto talk", "software": ["quarto", "shiny"]}) == "Quarto talk, quarto, shiny"
    assert t.build_prompt({}) == ""


# --- Selection ---


@pytest.fixture
def repo(tmp_path):
    return make_repo(tmp_path)


def videos_dir(repo):
    return repo / "content/resources/videos"


class TestSelect:
    def test_rules_and_order(self, repo):
        write_video_dir(repo, "2026-01-01_old", url=URL_A)
        write_video_dir(repo, "2026-03-01_new", url=URL_B)
        write_video_dir(repo, "2026-02-01_done", url=URL_C, vtt=SAMPLE_VTT)
        write_video_dir(repo, "2026-02-02_excluded", url=URL_D, extra="transcribe: false\n")
        write_video_dir(repo, "2026-02-03_live", url=URL_D, duration=0)
        (videos_dir(repo) / "2026-02-04_empty").mkdir()
        summary = videolib.RunSummary("transcribe")
        selected = t.select_videos(videolib.video_dirs(videos_dir(repo)), summary)
        assert [c.slug for c in selected] == ["2026-03-01_new", "2026-01-01_old"]
        assert summary.counts() == {"already_transcribed": 1, "excluded": 1, "skipped": 2}
        reasons = {i["slug"]: i["reason"] for i in summary.items}
        assert reasons == {"2026-02-04_empty": "no_index", "2026-02-03_live": "no_duration"}

    def test_limit(self, repo):
        for i in range(5):
            write_video_dir(repo, f"2026-01-0{i + 1}_v", url=URL_A)
        summary = videolib.RunSummary("transcribe")
        selected = t.select_videos(videolib.video_dirs(videos_dir(repo)), summary, limit=2)
        assert [c.slug for c in selected] == ["2026-01-05_v", "2026-01-04_v"]
        assert summary.tallies["deferred"] == 3
        assert summary.extra["deferred"] == ["2026-01-03_v", "2026-01-02_v", "2026-01-01_v"]

    def test_audio_budget(self, repo):
        write_video_dir(repo, "2026-01-03_a", url=URL_A, duration=3600)
        write_video_dir(repo, "2026-01-02_b", url=URL_B, duration=1800)
        write_video_dir(repo, "2026-01-01_c", url=URL_C, duration=600)
        summary = videolib.RunSummary("transcribe")
        selected = t.select_videos(videolib.video_dirs(videos_dir(repo)), summary, max_audio_minutes=75)
        # 60 min fits, 30 more doesn't, but 10 more does.
        assert [c.slug for c in selected] == ["2026-01-03_a", "2026-01-01_c"]
        assert summary.extra["selected_audio_minutes"] == 70.0

    def test_first_video_over_budget_still_taken(self, repo):
        write_video_dir(repo, "2026-01-03_long", url=URL_A, duration=4 * 3600)
        summary = videolib.RunSummary("transcribe")
        selected = t.select_videos(videolib.video_dirs(videos_dir(repo)), summary, max_audio_minutes=60)
        assert [c.slug for c in selected] == ["2026-01-03_long"]


# --- main ---


def run(repo, *args, client=None, ytdlp=None, max_bytes=t.MAX_BYTES):
    summary = repo / "summary.json"
    code = t.main(
        ["--project-root", str(repo), "--summary-json", str(summary), *args],
        client=client if client is not None else FakeOpenAI(),
        run=ytdlp or FakeYtDlp(),
        sleep=no_sleep,
        max_bytes=max_bytes,
        min_request_interval=0,
    )
    return code, json.loads(summary.read_text())


def items(data, status):
    return [i for i in data["items"] if i["status"] == status]


class TestMain:
    def test_transcribes_and_cleans_up(self, repo, monkeypatch, tmp_path):
        temp_root = tmp_path / "tmp"
        temp_root.mkdir()
        monkeypatch.setattr(t.tempfile, "tempdir", str(temp_root))
        a = write_video_dir(repo, "2026-01-02_a", url=URL_A, duration=26, title="Quarto talk")
        b = write_video_dir(repo, "2026-01-01_b", url=URL_B, duration=26)
        client = FakeOpenAI()
        ytdlp = FakeYtDlp()
        code, data = run(repo, client=client, ytdlp=ytdlp)
        assert code == 0
        assert (a / "transcription.vtt").read_text() == SAMPLE_VTT
        assert (b / "transcription.vtt").exists()
        assert not list(a.glob("audio.*"))
        assert list(temp_root.iterdir()) == []  # temporary download dirs removed
        assert [c[-1] for c in ytdlp.calls] == [URL_A, URL_B]
        assert client.calls[0]["model"] == "whisper-1"
        assert client.calls[0]["response_format"] == "vtt"
        assert client.calls[0]["prompt"] == "Quarto talk, quarto"
        done = items(data, "transcribed")
        assert [i["slug"] for i in done] == ["2026-01-02_a", "2026-01-01_b"]
        assert done[0]["cues"] == 3
        assert done[0]["chunks"] == 1
        assert done[0]["estimated_cost_usd"] == pytest.approx(26 / 60 * 0.006, abs=1e-4)
        assert "download_s" in done[0]["timings"]
        assert data["extra"]["breaker_tripped"] is False

    def test_second_run_does_nothing(self, repo):
        write_video_dir(repo, "2026-01-02_a", url=URL_A, duration=26)
        run(repo)
        ytdlp = FakeYtDlp()
        code, data = run(repo, ytdlp=ytdlp)
        assert code == 0 and ytdlp.calls == []
        assert data["counts"] == {"already_transcribed": 1}

    def test_circuit_breaker(self, repo):
        for i, url in enumerate([URL_A, URL_B, URL_C, URL_D]):
            write_video_dir(repo, f"2026-01-0{4 - i}_v{i}", url=url, duration=26)
        ytdlp = FakeYtDlp({URL_A: [BOT_CHECK], URL_B: [PO_TOKEN], URL_C: [BOT_CHECK]})
        code, data = run(repo, "--jobs", "1", ytdlp=ytdlp)
        assert code == 2
        assert [i["reason"] for i in items(data, "error")] == ["bot_check", "po_token", "bot_check"]
        (skipped,) = items(data, "skipped")
        assert skipped["reason"] == "download_blocked" and skipped["video_id"] == "ddddddddddd"
        assert len(ytdlp.calls) == 3
        assert data["extra"]["breaker_tripped"] is True

    def test_download_error_details_in_summary_and_log(self, repo, capsys, monkeypatch):
        monkeypatch.setenv("CI", "true")
        write_video_dir(repo, "2026-01-01_a", url=URL_A, duration=26)
        code, data = run(repo, ytdlp=FakeYtDlp({URL_A: [PO_TOKEN]}))
        assert code == 2
        (error,) = items(data, "error")
        assert error["stage"] == "download"
        assert error["reason"] == "po_token"
        assert error["detail"].startswith("ERROR: [youtube] dQw4w9WgXcQ: Requested format")
        assert "GVS PO Token" in error["stderr"]
        err = capsys.readouterr().err
        assert "2026-01-01_a (aaaaaaaaaaa): download failed: po_token" in err
        assert "yt-dlp: WARNING: [youtube] dQw4w9WgXcQ: mweb client" in err

    def test_network_error_retried(self, repo):
        write_video_dir(repo, "2026-01-01_a", url=URL_A, duration=26)
        ytdlp = FakeYtDlp({URL_A: [NETWORK, "ok"]})
        code, data = run(repo, ytdlp=ytdlp)
        assert code == 0 and len(ytdlp.calls) == 2

    def test_403_retried_once_then_error(self, repo):
        write_video_dir(repo, "2026-01-01_a", url=URL_A, duration=26)
        ytdlp = FakeYtDlp({URL_A: [HTTP_403, HTTP_403]})
        code, data = run(repo, ytdlp=ytdlp)
        (error,) = items(data, "error")
        assert error["reason"] == "http_403" and error["attempts"] == 2
        assert len(ytdlp.calls) == 2

    def test_whisper_rate_limit_retried(self, repo):
        a = write_video_dir(repo, "2026-01-01_a", url=URL_A, duration=26)
        client = FakeOpenAI([RateLimitError(), StatusError(503)])
        code, _ = run(repo, client=client)
        assert code == 0 and len(client.calls) == 3
        assert (a / "transcription.vtt").exists()

    def test_whisper_client_error_not_retried(self, repo):
        a = write_video_dir(repo, "2026-01-01_a", url=URL_A, duration=26)
        client = FakeOpenAI([StatusError(400, "Invalid file format")])
        code, data = run(repo, client=client)
        assert code == 2 and len(client.calls) == 1
        (error,) = items(data, "error")
        assert error["reason"] == "transcription_failed"
        assert error["detail"] == "StatusError status=400 request_id=req_400: Invalid file format"
        assert not (a / "transcription.vtt").exists()

    def test_empty_transcript_not_written(self, repo):
        a = write_video_dir(repo, "2026-01-01_a", url=URL_A, duration=26)
        code, data = run(repo, client=FakeOpenAI(["WEBVTT\n\n"]))
        assert code == 2
        assert items(data, "error")[0]["reason"] == "empty_transcript"
        assert not (a / "transcription.vtt").exists()

    def test_truncated_is_a_warning(self, repo):
        a = write_video_dir(repo, "2026-01-01_a", url=URL_A, duration=600)
        code, data = run(repo)
        assert code == 0 and (a / "transcription.vtt").exists()
        assert items(data, "transcribed")[0]["warnings"][0].startswith("suspect_truncated")

    def test_existing_audio_used_and_deleted(self, repo):
        a = write_video_dir(repo, "2026-01-01_a", url=URL_A, duration=26)
        (a / "audio.m4a").write_bytes(b"\0" * 100)
        ytdlp = FakeYtDlp()
        code, _ = run(repo, ytdlp=ytdlp)
        assert code == 0 and ytdlp.calls == []
        assert not (a / "audio.m4a").exists()

    def test_existing_audio_kept_on_failure(self, repo):
        a = write_video_dir(repo, "2026-01-01_a", url=URL_A, duration=26)
        (a / "audio.m4a").write_bytes(b"\0" * 100)
        run(repo, client=FakeOpenAI([StatusError(400)]))
        assert (a / "audio.m4a").exists()

    def test_video_option(self, repo):
        write_video_dir(repo, "2026-01-02_a", url=URL_A, duration=26)
        b = write_video_dir(repo, "2026-01-01_b", url=URL_B, duration=26)
        code, data = run(repo, "--video", "2026-01-01")
        assert [i["slug"] for i in items(data, "transcribed")] == ["2026-01-01_b"]
        assert (b / "transcription.vtt").exists()

    def test_dry_run(self, repo):
        a = write_video_dir(repo, "2026-01-01_a", url=URL_A, duration=26)
        ytdlp, client = FakeYtDlp(), FakeOpenAI()
        code, data = run(repo, "--dry-run", ytdlp=ytdlp, client=client)
        assert code == 0 and ytdlp.calls == [] and client.calls == []
        assert items(data, "would_transcribe")[0]["slug"] == "2026-01-01_a"
        assert not (a / "transcription.vtt").exists()

    def test_missing_api_key_is_fatal(self, repo, monkeypatch):
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        write_video_dir(repo, "2026-01-01_a", url=URL_A, duration=26)
        summary = repo / "s.json"
        code = t.main(["--project-root", str(repo), "--summary-json", str(summary)], run=FakeYtDlp())
        assert code == 1
        assert "OPENAI_API_KEY" in json.loads(summary.read_text())["fatal"]

    def test_nothing_to_do_needs_no_api_key(self, repo, monkeypatch):
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        code = t.main(["--project-root", str(repo)], run=FakeYtDlp())
        assert code == 0

    def test_missing_ffmpeg_is_fatal(self, repo, monkeypatch):
        real_which = shutil.which
        monkeypatch.setattr(t.shutil, "which", lambda name: None if name == "ffprobe" else real_which(name))
        code, data = run(repo)
        assert code == 1 and data["fatal"] == "Required tools not found: ffprobe"


# --- ffmpeg (real) ---


def make_tone_silence_tone(path: Path) -> None:
    subprocess.run(
        [
            "ffmpeg", "-y", "-v", "error",
            "-f", "lavfi", "-i", "sine=frequency=440:duration=1",
            "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono:d=1",
            "-f", "lavfi", "-i", "sine=frequency=440:duration=1",
            "-filter_complex", "[0][1][2]concat=n=3:v=0:a=1",
            "-ac", "1", "-ar", "44100", str(path),
        ],
        check=True,
    )  # fmt: skip


@needs_ffmpeg
def test_detect_silence(tmp_path):
    audio = tmp_path / "audio.wav"
    make_tone_silence_tone(audio)
    (point,) = t.detect_silence(audio)
    assert 1.2 < point < 1.8
    assert t.get_audio_duration(audio) == pytest.approx(3.0, abs=0.05)


@needs_ffmpeg
def test_large_audio_split_and_merged(repo):
    a = write_video_dir(repo, "2026-01-01_a", url=URL_A, duration=3)
    audio = a / "audio.wav"
    make_tone_silence_tone(audio)
    one_cue = "WEBVTT\n\n00:00:00.200 --> 00:00:00.900\npart\n"
    client = FakeOpenAI(default=one_cue)
    # Force a split: chunks may be at most ~60% of the file.
    code, data = run(repo, client=client, max_bytes=int(audio.stat().st_size * 0.6))
    assert code == 0
    (done,) = items(data, "transcribed")
    assert done["chunks"] == 2
    cues = videolib.parse_vtt((a / "transcription.vtt").read_text())
    assert len(cues) == 2
    assert cues[0][0] == pytest.approx(0.2)
    assert 1.2 < cues[1][0] - 0.2 < 1.8  # second chunk starts at the silence


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-p", "no:cacheprovider", *sys.argv[1:]]))
