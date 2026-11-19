"""
Shared helpers for the video pipeline scripts:

    update-youtube-videos.py  ->  sync-videos.py  ->  transcribe.py  ->  format-transcriptions.py

The scripts are PEP 723 uv scripts that import this module from their own
directory. Only pyyaml and rich are required here (imported lazily where
possible), so every script must declare both in its inline dependencies.

Conventions shared by the scripts:

- Exit codes: 0 = everything succeeded, 1 = fatal error (nothing useful was
  written), 2 = partial success (some videos failed, the rest was written).
- ``--summary-json PATH`` writes a machine-readable run summary (see
  ``RunSummary``), which ``video-sync-report.py`` turns into the PR body.
- Logging goes to stderr. In a terminal it is colored by Rich; elsewhere (CI)
  it is plain, timestamped text in UTC so that logs can be correlated.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import platform
import random
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Awaitable, Callable, TypeVar

T = TypeVar("T")

EXIT_OK = 0
EXIT_FATAL = 1
EXIT_PARTIAL = 2

DEFAULT_PROJECT_ROOT = Path(__file__).resolve().parent.parent

log = logging.getLogger("videolib")


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

_console = None


def is_interactive() -> bool:
    """True when stderr is a terminal and we're not running in CI."""
    return sys.stderr.isatty() and not os.getenv("CI")


def get_console():
    """The Rich console shared by the log handler and progress bars."""
    global _console
    if _console is None:
        from rich.console import Console

        _console = Console(stderr=True)
    return _console


class _UTCFormatter(logging.Formatter):
    converter = time.gmtime

    def formatTime(self, record, datefmt=None):  # noqa: N802 (logging API)
        t = time.gmtime(record.created)
        return time.strftime("%Y-%m-%dT%H:%M:%S", t) + f".{int(record.msecs):03d}Z"


NOISY_LOGGERS = [
    "httpx",
    "httpx2",
    "httpcore",
    "openai",
    "anthropic",
    "googleapiclient.discovery",
    "googleapiclient.discovery_cache",
    "urllib3",
]


def setup_logging(name: str, verbose: bool = False) -> logging.Logger:
    """Configure the root logger and return the logger for ``name``.

    The level is DEBUG with ``verbose``, otherwise ``$LOG_LEVEL`` or INFO.
    """
    level_name = "DEBUG" if verbose else os.getenv("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)

    root = logging.getLogger()
    for handler in list(root.handlers):
        root.removeHandler(handler)

    if is_interactive():
        from rich.logging import RichHandler

        handler: logging.Handler = RichHandler(
            console=get_console(),
            show_path=False,
            markup=False,
            rich_tracebacks=True,
            log_time_format="[%X]",
        )
    else:
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(
            _UTCFormatter("%(asctime)s %(levelname)-7s %(name)s: %(message)s")
        )
    root.addHandler(handler)
    root.setLevel(level)

    # Third-party HTTP clients are chatty at INFO/DEBUG; only show their
    # warnings unless we're debugging.
    for noisy in NOISY_LOGGERS:
        logging.getLogger(noisy).setLevel(level if verbose else logging.WARNING)

    return logging.getLogger(name)


def make_progress(*columns_extra):
    """A Rich progress bar that is disabled outside interactive terminals."""
    from rich.progress import (
        BarColumn,
        MofNCompleteColumn,
        Progress,
        SpinnerColumn,
        TextColumn,
        TimeElapsedColumn,
    )

    return Progress(
        SpinnerColumn(),
        TextColumn("{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        TimeElapsedColumn(),
        *columns_extra,
        console=get_console(),
        disable=not is_interactive(),
        transient=True,
    )


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--summary-json",
        type=Path,
        metavar="PATH",
        help="write a machine-readable run summary to PATH",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="enable debug logging"
    )
    # Hidden: lets the tests run a script against a temporary fixture repo.
    parser.add_argument(
        "--project-root",
        type=Path,
        default=DEFAULT_PROJECT_ROOT,
        help=argparse.SUPPRESS,
    )


def log_environment(
    logger: logging.Logger,
    packages: list[str] | None = None,
    tools: list[str] | None = None,
) -> dict[str, Any]:
    """Log interpreter, package, and external tool versions; return them."""
    from importlib import metadata

    env: dict[str, Any] = {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "ci": bool(os.getenv("CI")),
        "packages": {},
        "tools": {},
    }
    for package in packages or []:
        try:
            env["packages"][package] = metadata.version(package)
        except metadata.PackageNotFoundError:
            env["packages"][package] = None
    for tool in tools or []:
        env["tools"][tool] = tool_version(tool)

    logger.info(
        "Environment: python %s on %s%s",
        env["python"],
        env["platform"],
        " (CI)" if env["ci"] else "",
    )
    for package, version in env["packages"].items():
        logger.info("  package %s: %s", package, version or "not installed")
    for tool, version in env["tools"].items():
        logger.info("  tool %s: %s", tool, version or "NOT FOUND")
    return env


def tool_version(tool: str) -> str | None:
    """First line of ``tool --version`` (``-version`` for ffmpeg), or None."""
    path = shutil.which(tool)
    if not path:
        return None
    flag = "-version" if tool in ("ffmpeg", "ffprobe") else "--version"
    try:
        result = subprocess.run(
            [path, flag], capture_output=True, text=True, timeout=15
        )
    except (OSError, subprocess.SubprocessError) as e:
        return f"error: {e}"
    out = (result.stdout or result.stderr).strip().splitlines()
    return out[0] if out else "unknown"


# ---------------------------------------------------------------------------
# Run summary
# ---------------------------------------------------------------------------


def utcnow_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class RunSummary:
    """Collects per-video results of one script run.

    ``items`` hold the interesting results (new, changed, failed, ...), each
    a dict with at least ``status``. ``tallies`` count bulk outcomes that
    aren't worth listing one by one (e.g. 1,700 "already transcribed").
    An item with status ``error`` makes the run partial (exit code 2);
    ``fatal`` makes it fatal (exit code 1).
    """

    script: str
    started_at: str = field(default_factory=utcnow_iso)
    finished_at: str | None = None
    items: list[dict[str, Any]] = field(default_factory=list)
    tallies: dict[str, int] = field(default_factory=dict)
    fatal: str | None = None
    extra: dict[str, Any] = field(default_factory=dict)
    environment: dict[str, Any] = field(default_factory=dict)

    def add(self, status: str, **fields: Any) -> dict[str, Any]:
        item = {"status": status, **{k: v for k, v in fields.items() if v is not None}}
        self.items.append(item)
        return item

    def tally(self, status: str, n: int = 1) -> None:
        self.tallies[status] = self.tallies.get(status, 0) + n

    def counts(self) -> dict[str, int]:
        counts = dict(self.tallies)
        for item in self.items:
            counts[item["status"]] = counts.get(item["status"], 0) + 1
        return dict(sorted(counts.items()))

    def by_status(self, *statuses: str) -> list[dict[str, Any]]:
        return [i for i in self.items if i["status"] in statuses]

    @property
    def errors(self) -> list[dict[str, Any]]:
        return self.by_status("error")

    @property
    def exit_code(self) -> int:
        if self.fatal:
            return EXIT_FATAL
        if self.errors:
            return EXIT_PARTIAL
        return EXIT_OK

    def to_dict(self) -> dict[str, Any]:
        return {
            "script": self.script,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "exit_code": self.exit_code,
            "fatal": self.fatal,
            "counts": self.counts(),
            "extra": self.extra,
            "environment": self.environment,
            "items": self.items,
        }

    def write(self, path: Path | None) -> None:
        self.finished_at = self.finished_at or utcnow_iso()
        if path is None:
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        atomic_write_text(path, json.dumps(self.to_dict(), indent=2, default=str) + "\n")

    def log_counts(self, logger: logging.Logger) -> None:
        counts = self.counts()
        if counts:
            logger.info(
                "Summary: %s",
                ", ".join(f"{status}={n}" for status, n in counts.items()),
            )
        else:
            logger.info("Summary: nothing to do")
        if self.fatal:
            logger.error("Fatal: %s", self.fatal)
        elif self.errors:
            logger.warning("%d error(s); exit code %d", len(self.errors), self.exit_code)


def run_main(
    summary: RunSummary,
    logger: logging.Logger,
    summary_path: Path | None,
    body: Callable[[], None],
) -> int:
    """Run ``body``, turning uncaught exceptions into a fatal summary.

    The summary is always written, so the report can explain a crash.
    """
    try:
        body()
    except KeyboardInterrupt:
        summary.fatal = "interrupted"
        raise
    except Exception as e:  # noqa: BLE001 - we want every failure in the summary
        logger.exception("Unhandled error")
        summary.fatal = f"{type(e).__name__}: {e}"
    finally:
        summary.write(summary_path)
        summary.log_counts(logger)
    return summary.exit_code


# ---------------------------------------------------------------------------
# Files
# ---------------------------------------------------------------------------


def atomic_write_bytes(path: Path, data: bytes) -> None:
    """Write ``data`` to a temp file next to ``path``, then rename it."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        os.replace(tmp, path)
    except BaseException:
        tmp.unlink(missing_ok=True)
        raise


def atomic_write_text(path: Path, text: str) -> None:
    atomic_write_bytes(path, text.encode("utf-8"))


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------


def split_frontmatter(content: str) -> tuple[dict[str, Any], str, str]:
    """Return ``(frontmatter, yaml_section, remaining_content)``.

    Without (valid) frontmatter, returns ``({}, "", content)``.
    """
    import yaml

    lines = content.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, "", content
    end_idx = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end_idx is None:
        return {}, "", content
    yaml_section = "\n".join(lines[1:end_idx])
    try:
        frontmatter = yaml.safe_load(yaml_section) or {}
    except yaml.YAMLError as e:
        log.warning("Failed to parse YAML frontmatter: %s", e)
        return {}, "", content
    if not isinstance(frontmatter, dict):
        return {}, "", content
    return frontmatter, yaml_section, "\n".join(lines[end_idx + 1 :])


def parse_frontmatter(content: str) -> dict[str, Any]:
    return split_frontmatter(content)[0]


def read_frontmatter(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return parse_frontmatter(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Video directories
# ---------------------------------------------------------------------------


def video_dirs(videos_dir: Path) -> list[Path]:
    """Video directories, newest first (names start with the YYYY-MM-DD date)."""
    return sorted((d for d in videos_dir.iterdir() if d.is_dir()), reverse=True)


def resolve_video_dir(name_or_path: str, videos_dir: Path) -> Path:
    """Find a video directory by path, exact name, or unique name prefix."""
    p = Path(name_or_path)
    if p.is_absolute() and p.is_dir():
        return p
    candidate = videos_dir / name_or_path
    if candidate.is_dir():
        return candidate
    matches = [
        d for d in videos_dir.iterdir() if d.is_dir() and d.name.startswith(name_or_path)
    ]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        listed = "\n  ".join(m.name for m in sorted(matches))
        raise ValueError(f"Ambiguous video name, matches:\n  {listed}")
    raise ValueError(f"Video directory not found: {name_or_path}")


def youtube_id(url: str | None) -> str | None:
    if not url:
        return None
    m = re.search(r"(?:v=|youtu\.be/|/shorts/)([\w-]{11})", url)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# WebVTT
# ---------------------------------------------------------------------------

Cue = tuple[float, float, str]


def parse_vtt_timestamp(ts: str) -> float:
    parts = ts.strip().split(":")
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])
    return int(parts[0]) * 60 + float(parts[1])


def format_vtt_timestamp(seconds: float) -> str:
    # Work in whole milliseconds so 59.9999 doesn't render as "00:00:60.000".
    ms = round(seconds * 1000)
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


def parse_vtt(content: str) -> list[Cue]:
    cues: list[Cue] = []
    for block in re.split(r"\n{2,}", content.replace("\r\n", "\n").strip()):
        lines = block.strip().splitlines()
        arrow = next((i for i, line in enumerate(lines) if "-->" in line), None)
        if arrow is None:
            continue
        m = re.match(r"([\d:.]+)\s+-->\s+([\d:.]+)", lines[arrow].strip())
        if not m:
            continue
        start = parse_vtt_timestamp(m.group(1))
        end = parse_vtt_timestamp(m.group(2))
        text = "\n".join(lines[arrow + 1 :]).strip()
        if text:
            cues.append((start, end, text))
    return cues


def render_vtt(cues: list[Cue]) -> str:
    lines = ["WEBVTT", ""]
    for start, end, text in cues:
        lines.append(f"{format_vtt_timestamp(start)} --> {format_vtt_timestamp(end)}")
        lines.append(text)
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# API calls: rate limiting and retries
# ---------------------------------------------------------------------------


class RateLimiter:
    """Ensures at least ``min_interval`` seconds between API requests."""

    def __init__(self, min_interval: float = 1.0) -> None:
        self._lock = asyncio.Lock()
        self._last: float = 0.0
        self._interval = min_interval

    async def wait(self) -> None:
        async with self._lock:
            loop = asyncio.get_running_loop()
            elapsed = loop.time() - self._last
            if elapsed < self._interval:
                await asyncio.sleep(self._interval - elapsed)
            self._last = asyncio.get_running_loop().time()


RETRYABLE_ERROR_NAMES = {"APIConnectionError", "APITimeoutError", "RateLimitError"}


def is_retryable_api_error(e: BaseException) -> bool:
    """Rate limits, timeouts, connection errors, and 5xx responses.

    Works for both the OpenAI and Anthropic SDKs without importing either.
    """
    if any(cls.__name__ in RETRYABLE_ERROR_NAMES for cls in type(e).__mro__):
        return True
    status = getattr(e, "status_code", None)
    if isinstance(status, int):
        return status in (408, 409, 429) or status >= 500
    return isinstance(e, (TimeoutError, ConnectionError))


def describe_api_error(e: BaseException) -> str:
    """``RateLimitError status=429 request_id=req_123: message``"""
    parts = [type(e).__name__]
    status = getattr(e, "status_code", None)
    if status is not None:
        parts.append(f"status={status}")
    request_id = getattr(e, "request_id", None)
    if request_id:
        parts.append(f"request_id={request_id}")
    message = str(e).strip().splitlines()[0][:300] if str(e).strip() else ""
    return " ".join(parts) + (f": {message}" if message else "")


async def retry_async(
    fn: Callable[[], Awaitable[T]],
    *,
    label: str,
    logger: logging.Logger,
    attempts: int = 6,
    base_delay: float = 2.0,
    max_delay: float = 60.0,
    is_retryable: Callable[[BaseException], bool] = is_retryable_api_error,
    describe: Callable[[BaseException], str] = describe_api_error,
    sleep: Callable[[float], Awaitable[Any]] = asyncio.sleep,
) -> T:
    """Call ``fn`` with exponential backoff (plus jitter) on retryable errors.

    Every failed attempt is logged with the error description, so a flaky
    API is visible in the logs even when the call eventually succeeds. The
    defaults wait about a minute in total, enough to ride out a short
    network outage (with 1 s steps, a ten-second outage failed 15 videos).
    """
    for attempt in range(1, attempts + 1):
        try:
            return await fn()
        except Exception as e:
            if not is_retryable(e):
                logger.error("%s: %s (not retryable)", label, describe(e))
                raise
            if attempt == attempts:
                logger.error("%s: %s (giving up after %d attempts)", label, describe(e), attempts)
                raise
            delay = min(max_delay, base_delay * (2 ** (attempt - 1))) + random.uniform(0, base_delay)
            logger.warning(
                "%s: attempt %d/%d failed: %s; retrying in %.1fs",
                label,
                attempt,
                attempts,
                describe(e),
                delay,
            )
            await sleep(delay)
    raise AssertionError("unreachable")
