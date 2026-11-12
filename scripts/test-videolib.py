#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "pytest>=8.0",
# ]
# ///

"""Tests for videolib.py, the shared helpers of the video pipeline."""

import asyncio
import json
import logging
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import videolib  # noqa: E402
from videotesting import RateLimitError, StatusError, no_sleep  # noqa: E402

# --- VTT ---


class TestVttTimestamps:
    @pytest.mark.parametrize(
        "ts, seconds",
        [
            ("00:00:00.000", 0.0),
            ("00:01:30.500", 90.5),
            ("01:02:03.100", 3723.1),
            ("02:05.250", 125.25),  # no hours
        ],
    )
    def test_parse(self, ts, seconds):
        assert videolib.parse_vtt_timestamp(ts) == pytest.approx(seconds)

    @pytest.mark.parametrize(
        "seconds, ts",
        [
            (0, "00:00:00.000"),
            (90.5, "00:01:30.500"),
            (3723.1, "01:02:03.100"),
            (59.9996, "00:01:00.000"),  # rounds up instead of "00:00:60.000"
        ],
    )
    def test_format(self, seconds, ts):
        assert videolib.format_vtt_timestamp(seconds) == ts


class TestParseVtt:
    def test_basic(self):
        vtt = "WEBVTT\n\n00:00:01.000 --> 00:00:02.500\nHello\n\n00:00:03.000 --> 00:00:04.000\nWorld\n"
        assert videolib.parse_vtt(vtt) == [(1.0, 2.5, "Hello"), (3.0, 4.0, "World")]

    def test_multiline_cue_and_identifier(self):
        vtt = "WEBVTT\n\ncue-1\n00:00:01.000 --> 00:00:02.000\nline one\nline two\n"
        assert videolib.parse_vtt(vtt) == [(1.0, 2.0, "line one\nline two")]

    def test_empty_cues_dropped(self):
        vtt = "WEBVTT\n\n00:00:01.000 --> 00:00:02.000\n\n\n00:00:03.000 --> 00:00:04.000\nkept\n"
        assert videolib.parse_vtt(vtt) == [(3.0, 4.0, "kept")]

    def test_crlf(self):
        vtt = "WEBVTT\r\n\r\n00:00:01.000 --> 00:00:02.000\r\nHi\r\n"
        assert videolib.parse_vtt(vtt) == [(1.0, 2.0, "Hi")]

    def test_not_vtt(self):
        assert videolib.parse_vtt("") == []
        assert videolib.parse_vtt("just some text") == []

    def test_round_trip(self):
        cues = [(0.0, 4.0, "a"), (4.0, 9.5, "b c"), (3600.25, 3605.0, "d")]
        assert videolib.parse_vtt(videolib.render_vtt(cues)) == cues


# --- Frontmatter ---


class TestFrontmatter:
    def test_split(self):
        fm, section, rest = videolib.split_frontmatter("---\ntitle: X\n---\nbody\n")
        assert fm == {"title": "X"}
        assert section == "title: X"
        assert rest == "body\n"

    @pytest.mark.parametrize(
        "content",
        [
            "no frontmatter",
            "---\ntitle: X\nnever closed\n",
            "---\ntitle: [unclosed\n---\n",
            "---\n- a list\n---\n",
        ],
    )
    def test_invalid(self, content):
        fm, section, rest = videolib.split_frontmatter(content)
        assert fm == {} and section == "" and rest == content

    def test_read_missing_file(self, tmp_path):
        assert videolib.read_frontmatter(tmp_path / "nope.md") == {}


# --- Files ---


class TestAtomicWrite:
    def test_writes(self, tmp_path):
        p = tmp_path / "sub" / "f.txt"
        videolib.atomic_write_text(p, "héllo")
        assert p.read_text(encoding="utf-8") == "héllo"

    def test_failure_leaves_original_and_no_temp_files(self, tmp_path, monkeypatch):
        p = tmp_path / "f.txt"
        p.write_text("original")

        def boom(*_):
            raise OSError("disk full")

        monkeypatch.setattr(videolib.os, "replace", boom)
        with pytest.raises(OSError):
            videolib.atomic_write_text(p, "new")
        assert p.read_text() == "original"
        assert list(tmp_path.iterdir()) == [p]


# --- Video directories ---


class TestVideoDirs:
    def test_newest_first(self, tmp_path):
        for name in ["2024-01-01_a", "2026-05-01_b", "2025-03-03_c"]:
            (tmp_path / name).mkdir()
        (tmp_path / "file.txt").write_text("x")
        assert [d.name for d in videolib.video_dirs(tmp_path)] == [
            "2026-05-01_b",
            "2025-03-03_c",
            "2024-01-01_a",
        ]

    def test_resolve(self, tmp_path):
        (tmp_path / "2026-01-01_talk-one").mkdir()
        (tmp_path / "2026-01-01_talk-two").mkdir()
        (tmp_path / "2025-01-01_other").mkdir()
        assert videolib.resolve_video_dir("2025", tmp_path).name == "2025-01-01_other"
        assert videolib.resolve_video_dir("2026-01-01_talk-one", tmp_path).name == "2026-01-01_talk-one"
        with pytest.raises(ValueError, match="Ambiguous"):
            videolib.resolve_video_dir("2026-01-01_talk", tmp_path)
        with pytest.raises(ValueError, match="not found"):
            videolib.resolve_video_dir("1999", tmp_path)

    @pytest.mark.parametrize(
        "url, vid",
        [
            ("https://www.youtube.com/watch?v=ohUZNk5WCGQ", "ohUZNk5WCGQ"),
            ("https://youtu.be/ohUZNk5WCGQ", "ohUZNk5WCGQ"),
            ("https://www.youtube.com/shorts/ohUZNk5WCGQ", "ohUZNk5WCGQ"),
            ("https://example.com", None),
            (None, None),
        ],
    )
    def test_youtube_id(self, url, vid):
        assert videolib.youtube_id(url) == vid


# --- Run summary ---


class TestRunSummary:
    def test_exit_codes(self):
        s = videolib.RunSummary("x")
        s.add("created", slug="a")
        assert s.exit_code == videolib.EXIT_OK
        s.add("error", slug="b", reason="boom")
        assert s.exit_code == videolib.EXIT_PARTIAL
        s.fatal = "no API key"
        assert s.exit_code == videolib.EXIT_FATAL

    def test_counts_merge_items_and_tallies(self):
        s = videolib.RunSummary("x")
        s.add("created", slug="a")
        s.add("created", slug="b")
        s.tally("unchanged", 1700)
        s.tally("created")
        assert s.counts() == {"created": 3, "unchanged": 1700}

    def test_none_fields_dropped(self):
        s = videolib.RunSummary("x")
        item = s.add("error", slug="a", reason=None, detail="d")
        assert item == {"status": "error", "slug": "a", "detail": "d"}

    def test_json_schema(self, tmp_path):
        s = videolib.RunSummary("sync-videos")
        s.add("error", slug="a", reason="boom")
        s.extra["dry_run"] = False
        path = tmp_path / "out" / "summary.json"
        s.write(path)
        data = json.loads(path.read_text())
        assert set(data) == {
            "script",
            "started_at",
            "finished_at",
            "exit_code",
            "fatal",
            "counts",
            "extra",
            "environment",
            "items",
        }
        assert data["script"] == "sync-videos"
        assert data["exit_code"] == 2
        assert data["counts"] == {"error": 1}
        assert data["finished_at"] is not None

    def test_run_main_turns_exceptions_into_fatal(self, tmp_path, caplog):
        s = videolib.RunSummary("x")
        path = tmp_path / "s.json"

        def body():
            raise RuntimeError("kaput")

        with caplog.at_level(logging.ERROR):
            code = videolib.run_main(s, logging.getLogger("t"), path, body)
        assert code == 1
        assert json.loads(path.read_text())["fatal"] == "RuntimeError: kaput"
        assert "Unhandled error" in caplog.text

    def test_run_main_ok(self, tmp_path):
        s = videolib.RunSummary("x")
        assert videolib.run_main(s, logging.getLogger("t"), None, lambda: None) == 0


# --- Retries ---


class TestRetryableErrors:
    @pytest.mark.parametrize(
        "error, retryable",
        [
            (RateLimitError(), True),
            (StatusError(500), True),
            (StatusError(529), True),  # Anthropic "overloaded"
            (StatusError(408), True),
            (StatusError(400), False),
            (StatusError(401), False),
            (TimeoutError(), True),
            (ValueError("bad"), False),
        ],
    )
    def test_is_retryable(self, error, retryable):
        assert videolib.is_retryable_api_error(error) is retryable

    def test_connection_error_by_class_name(self):
        class APIConnectionError(Exception):
            pass

        class APITimeoutError(APIConnectionError):
            pass

        assert videolib.is_retryable_api_error(APITimeoutError())

    def test_describe(self):
        assert videolib.describe_api_error(StatusError(429, "slow down")) == (
            "StatusError status=429 request_id=req_429: slow down"
        )
        assert videolib.describe_api_error(ValueError()) == "ValueError"


class TestRetryAsync:
    def run(self, fn, **kwargs):
        sleeps = []

        async def fake_sleep(s):
            sleeps.append(s)

        result = asyncio.run(
            videolib.retry_async(
                fn, label="video-x", logger=logging.getLogger("t"), sleep=fake_sleep, **kwargs
            )
        )
        return result, sleeps

    def test_retries_then_succeeds(self, caplog):
        outcomes = [RateLimitError(), StatusError(503), "ok"]

        async def fn():
            r = outcomes.pop(0)
            if isinstance(r, Exception):
                raise r
            return r

        with caplog.at_level(logging.WARNING):
            result, sleeps = self.run(fn, base_delay=1.0)
        assert result == "ok"
        assert len(sleeps) == 2
        assert 1.0 <= sleeps[0] < 2.0 and 2.0 <= sleeps[1] < 3.0  # exponential + jitter
        assert "video-x: attempt 1/5 failed: RateLimitError status=429" in caplog.text
        assert "attempt 2/5 failed: StatusError status=503" in caplog.text

    def test_non_retryable_raises_immediately(self, caplog):
        calls = []

        async def fn():
            calls.append(1)
            raise StatusError(400, "bad request")

        with caplog.at_level(logging.ERROR), pytest.raises(StatusError):
            self.run(fn)
        assert calls == [1]
        assert "not retryable" in caplog.text

    def test_gives_up(self, caplog):
        calls = []

        async def fn():
            calls.append(1)
            raise StatusError(500)

        with caplog.at_level(logging.ERROR), pytest.raises(StatusError):
            self.run(fn, attempts=3)
        assert len(calls) == 3
        assert "giving up after 3 attempts" in caplog.text


class TestRateLimiter:
    def test_spacing(self):
        async def go():
            limiter = videolib.RateLimiter(min_interval=0.05)
            loop = asyncio.get_running_loop()
            times = []
            for _ in range(3):
                await limiter.wait()
                times.append(loop.time())
            return times

        times = asyncio.run(go())
        assert times[1] - times[0] >= 0.045
        assert times[2] - times[1] >= 0.045


# --- Logging ---


class TestLogging:
    def test_plain_format_in_ci(self, monkeypatch, capsys):
        monkeypatch.setenv("CI", "true")
        logger = videolib.setup_logging("test-logger")
        logger.info("hello %s", "world")
        err = capsys.readouterr().err
        assert "INFO    test-logger: hello world" in err
        assert err[:4].isdigit() and "Z " in err  # UTC timestamp first

    def test_verbose_and_env_level(self, monkeypatch):
        monkeypatch.setenv("CI", "true")
        assert videolib.setup_logging("a", verbose=True).getEffectiveLevel() == logging.DEBUG
        monkeypatch.setenv("LOG_LEVEL", "warning")
        assert videolib.setup_logging("a").getEffectiveLevel() == logging.WARNING

    def test_noisy_loggers_quieted(self, monkeypatch):
        monkeypatch.setenv("CI", "true")
        videolib.setup_logging("a")
        assert logging.getLogger("httpx").level == logging.WARNING

    def test_log_environment(self, caplog):
        with caplog.at_level(logging.INFO):
            env = videolib.log_environment(
                logging.getLogger("t"), packages=["pyyaml", "no-such-package-xyz"], tools=["no-such-tool-xyz"]
            )
        assert env["packages"]["pyyaml"]
        assert env["packages"]["no-such-package-xyz"] is None
        assert env["tools"]["no-such-tool-xyz"] is None
        assert "tool no-such-tool-xyz: NOT FOUND" in caplog.text


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-p", "no:cacheprovider", *sys.argv[1:]]))
