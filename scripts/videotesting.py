"""
Test helpers for the video pipeline tests (scripts/test-*.py).

Provides a loader for the hyphenated scripts, a tiny fixture repository, and
fakes for every external service the pipeline talks to: the YouTube Data
API, thumbnail downloads, yt-dlp, OpenAI Whisper, and the Anthropic API.
Nothing in here touches the network.
"""

from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace
from typing import Any

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

import videolib  # noqa: E402


def load_script(filename: str):
    """Import a hyphenated script (e.g. ``sync-videos.py``) as a module."""
    name = filename.removesuffix(".py").replace("-", "_")
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, SCRIPTS_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# Fixture repository
# ---------------------------------------------------------------------------


def write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def make_repo(root: Path) -> Path:
    """A minimal project tree with people, software, and YouTube config."""
    write(root / "content/people/hadley-wickham/_index.md", "---\ntitle: Hadley Wickham\n---\n")
    write(root / "content/people/mine-cetinkaya-rundel/_index.md", "---\ntitle: Mine Çetinkaya-Rundel\n---\n")
    write(root / "content/software/quarto/_index.md", "---\ntitle: Quarto\n---\n")
    write(root / "content/software/shiny/_index.md", "---\ntitle: Shiny\n---\n")
    write(root / "content/software/commons/_index.md", "---\ntitle: commons\n---\n")
    write(root / "data/software-match-ignore.toml", 'names = ["commons"]\n')
    write(
        root / "data/youtube.toml",
        'channels = ["PositPBC"]\nplaylists = ["PLtest"]\nvideos = ["indiv000001"]\n',
    )
    (root / "content/resources/videos").mkdir(parents=True, exist_ok=True)
    return root


def write_video_dir(
    root: Path,
    slug: str,
    *,
    url: str = "https://www.youtube.com/watch?v=abcdefghijk",
    title: str = "A talk",
    duration: int = 600,
    extra: str = "",
    vtt: str | None = None,
    html: str | None = None,
) -> Path:
    """Write a video directory as sync-videos.py would have produced it."""
    d = root / "content/resources/videos" / slug
    write(
        d / "_index.md",
        f"---\ntitle: {title}\nresource_type: video\nsoftware:\n- quarto\n{extra}"
        f"external:\n  url: {url}\n  duration: {duration}\n---\n",
    )
    if vtt is not None:
        write(d / "transcription.vtt", vtt)
    if html is not None:
        write(d / "transcription.txt", html)
    return d


SAMPLE_VTT = """WEBVTT

00:00:00.000 --> 00:00:04.000
Hello everyone, today we talk about Quarto.

00:00:04.000 --> 00:00:09.500
It was built by the team that also made Shiny.

00:00:20.000 --> 00:00:25.000
Hadley Wickham joins us later.
"""


def vtt_to_html(vtt: str) -> str:
    """What a well-behaved model returns: one <p> with one <a> per cue."""
    cues = videolib.parse_vtt(vtt)
    anchors = " ".join(f'<a data-t="{int(start)}">{text}</a>' for start, _, text in cues)
    return f"<p>{anchors}</p>"


# ---------------------------------------------------------------------------
# YouTube Data API fake
# ---------------------------------------------------------------------------


def yt_item(
    video_id: str,
    title: str = "A talk",
    *,
    published: str = "2026-10-01T12:00:00Z",
    description: str = "",
    duration: str = "PT10M",
    views: int = 100,
    likes: int = 10,
    comments: int = 1,
    tags: list[str] | None = None,
    channel_title: str = "Posit PBC",
) -> dict[str, Any]:
    return {
        "id": video_id,
        "snippet": {
            "title": title,
            "publishedAt": published,
            "description": description,
            "channelTitle": channel_title,
            "tags": tags or [],
            "thumbnails": {"high": {"url": f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"}},
            "defaultAudioLanguage": "en",
        },
        "contentDetails": {"duration": duration, "caption": "false", "definition": "hd"},
        "statistics": {"viewCount": str(views), "likeCount": str(likes), "commentCount": str(comments)},
    }


class HttpError(Exception):
    """Stand-in for googleapiclient.errors.HttpError."""

    def __init__(self, status: int, message: str = "error"):
        super().__init__(f"<HttpError {status}: {message}>")
        self.status_code = status


class _Request:
    def __init__(self, fn, kwargs):
        self._fn = fn
        self.kwargs = kwargs

    def execute(self, num_retries: int = 0):
        return self._fn(**self.kwargs)


class FakeYouTube:
    """Mimics the parts of ``googleapiclient`` the metadata script uses.

    ``channels``: handle -> (uploads playlist id, channel title)
    ``playlists``: playlist id -> list of video ids
    ``videos``: video id -> API item (missing ids are "private/deleted")
    ``page_size``: items per playlistItems page, to exercise pagination
    ``fail_playlists`` / ``fail_videos``: raise HttpError for these
    """

    def __init__(self, channels=None, playlists=None, videos=None, page_size=50):
        self.channels_data = channels or {}
        self.playlists_data = playlists or {}
        self.videos_data = videos or {}
        self.page_size = page_size
        self.fail_playlists: set[str] = set()
        self.fail_videos = False
        self.calls: list[str] = []

    # channels().list(...)
    def channels(self):
        def list_(part, forUsername=None, forHandle=None):  # noqa: N803 - API names
            def run():
                self.calls.append("channels.list")
                key = forUsername or (forHandle or "").lstrip("@")
                if forUsername and key not in self.channels_data:
                    return {}
                if key in self.channels_data:
                    uploads, title = self.channels_data[key]
                    return {
                        "items": [
                            {
                                "contentDetails": {"relatedPlaylists": {"uploads": uploads}},
                                "snippet": {"title": title},
                            }
                        ]
                    }
                return {}

            return _Request(lambda: run(), {})

        return SimpleNamespace(list=list_)

    # playlistItems().list(...) / list_next(...)
    def playlistItems(self):  # noqa: N802 - API name
        def page(playlistId, start):  # noqa: N803
            self.calls.append("playlistItems.list")
            if playlistId in self.fail_playlists or playlistId not in self.playlists_data:
                raise HttpError(404, f"playlist {playlistId} not found")
            ids = self.playlists_data[playlistId]
            chunk = ids[start : start + self.page_size]
            response = {"items": [{"contentDetails": {"videoId": v}} for v in chunk]}
            if start + self.page_size < len(ids):
                response["nextPageToken"] = str(start + self.page_size)
            return response

        def list_(part, playlistId, maxResults=50, pageToken=None):  # noqa: N803
            start = int(pageToken or 0)
            req = _Request(lambda: page(playlistId, start), {})
            req.playlist_id = playlistId
            return req

        def list_next(request, response):
            token = response.get("nextPageToken")
            if not token:
                return None
            return list_("contentDetails", request.playlist_id, pageToken=token)

        return SimpleNamespace(list=list_, list_next=list_next)

    # videos().list(...)
    def videos(self):
        def list_(part, id):  # noqa: A002 - API name
            def run():
                self.calls.append("videos.list")
                if self.fail_videos:
                    raise HttpError(403, "quotaExceeded")
                ids = id.split(",")
                return {"items": [self.videos_data[v] for v in ids if v in self.videos_data]}

            return _Request(lambda: run(), {})

        return SimpleNamespace(list=list_)


# ---------------------------------------------------------------------------
# HTTP (thumbnails)
# ---------------------------------------------------------------------------


class FakeHttp:
    """``get(url, timeout)`` returning a response with ``content``."""

    def __init__(self, fail_urls: set[str] | None = None):
        self.fail_urls = fail_urls or set()
        self.requested: list[str] = []

    def __call__(self, url: str, timeout: float = 15):
        self.requested.append(url)
        if url in self.fail_urls:
            raise OSError(f"connection refused: {url}")
        return SimpleNamespace(content=b"JPEG:" + url.encode(), raise_for_status=lambda: None)


# ---------------------------------------------------------------------------
# yt-dlp fake
# ---------------------------------------------------------------------------


class FakeYtDlp:
    """Stands in for ``subprocess.run`` when transcribe.py calls yt-dlp.

    ``outcomes`` maps a video URL to a list of results, consumed in order;
    each result is either ``"ok"`` (an audio file is written) or an stderr
    string (exit code 1). URLs without outcomes always succeed.
    """

    def __init__(self, outcomes: dict[str, list[str]] | None = None, size: int = 1024):
        self.outcomes = {k: list(v) for k, v in (outcomes or {}).items()}
        self.size = size
        self.calls: list[list[str]] = []

    def __call__(self, cmd, capture_output=True, text=True, **kwargs):
        self.calls.append(cmd)
        url = cmd[-1]
        queue = self.outcomes.get(url)
        result = queue.pop(0) if queue else "ok"
        if result != "ok":
            return subprocess.CompletedProcess(cmd, 1, stdout="", stderr=result)
        template = cmd[cmd.index("--output") + 1]
        out = Path(template.replace("%(ext)s", "webm"))
        out.write_bytes(b"\0" * self.size)
        return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")


# ---------------------------------------------------------------------------
# OpenAI / Anthropic fakes
# ---------------------------------------------------------------------------


class StatusError(Exception):
    """Mimics an SDK ``APIStatusError`` (has ``status_code`` and ``request_id``)."""

    def __init__(self, status: int, message: str = "boom"):
        super().__init__(message)
        self.status_code = status
        self.request_id = f"req_{status}"


class RateLimitError(StatusError):
    def __init__(self):
        super().__init__(429, "rate limited")


class FakeOpenAI:
    """``client.audio.transcriptions.create(file=..., **kwargs)`` returning VTT.

    ``responses`` is a list consumed in order; an Exception instance is
    raised instead of returned. When exhausted, ``default`` is returned.
    """

    def __init__(self, responses: list | None = None, default: str = SAMPLE_VTT):
        self.responses = list(responses or [])
        self.default = default
        self.calls: list[dict[str, Any]] = []
        self.audio = SimpleNamespace(transcriptions=SimpleNamespace(create=self._create))

    async def _create(self, file, **kwargs):
        self.calls.append({"file": getattr(file, "name", None), **kwargs})
        result = self.responses.pop(0) if self.responses else self.default
        if isinstance(result, BaseException):
            raise result
        return result


class FakeAnthropic:
    """``client.messages.create(...)`` returning a message-like object.

    ``responses`` entries may be a string (the text), a ``(text,
    stop_reason)`` tuple, or an Exception to raise. When exhausted, the
    response is generated from the VTT in the user message.
    """

    def __init__(self, responses: list | None = None):
        self.responses = list(responses or [])
        self.calls: list[dict[str, Any]] = []
        self.messages = SimpleNamespace(create=self._create)

    async def _create(self, **kwargs):
        self.calls.append(kwargs)
        if self.responses:
            result = self.responses.pop(0)
        else:
            user = kwargs["messages"][0]["content"]
            vtt = user.split("\n\n---\n\n", 1)[-1]
            result = vtt_to_html(vtt)
        if isinstance(result, BaseException):
            raise result
        text, stop_reason = result if isinstance(result, tuple) else (result, "end_turn")
        return SimpleNamespace(
            content=[SimpleNamespace(type="text", text=text)],
            stop_reason=stop_reason,
            usage=SimpleNamespace(input_tokens=1000, output_tokens=500),
            _request_id="req_fake",
        )


async def no_sleep(_seconds: float) -> None:
    return None


def strip_ansi(text: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", text)
