#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-api-python-client>=2.100.0",
#   "tomli-w>=1.0.0",
#   "python-dotenv>=1.0.0",
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "requests>=2.28.0",
#   "openai>=2.0.0",
#   "anthropic>=0.40.0",
#   "yt-dlp>=2025.0",
#   "pytest>=8.0",
# ]
# ///

"""
End-to-end test of the video pipeline: the four scripts and the report, run
in order against a fixture repository, with every external service faked.

The key property: a second run without changes on YouTube changes nothing,
which is what keeps the nightly pull requests small.
"""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from videotesting import (  # noqa: E402
    FakeAnthropic,
    FakeHttp,
    FakeOpenAI,
    FakeYouTube,
    FakeYtDlp,
    load_script,
    make_repo,
    no_sleep,
    yt_item,
)

update = load_script("update-youtube-videos.py")
sync = load_script("sync-videos.py")
transcribe = load_script("transcribe.py")
fmt = load_script("format-transcriptions.py")
report = load_script("video-sync-report.py")


def youtube(**titles):
    titles = {"video000001": "Quarto with Hadley Wickham", "video000002": "Shiny tips", **titles}
    return FakeYouTube(
        channels={"PositPBC": ("UUposit", "Posit PBC")},
        playlists={"UUposit": list(titles), "PLtest": []},
        videos={
            vid: yt_item(vid, title, published=f"2026-11-0{i + 1}T10:00:00Z", duration="PT26S", views=10)
            for i, (vid, title) in enumerate(titles.items())
        },
    )


class Pipeline:
    def __init__(self, root: Path):
        self.root = root
        self.ytdlp = FakeYtDlp()
        self.openai = FakeOpenAI()
        self.anthropic = FakeAnthropic()
        self.http = FakeHttp()

    def run(self, yt: FakeYouTube, *update_args: str) -> dict[str, int]:
        summaries = self.root.parent / "summaries"
        common = ["--project-root", str(self.root)]
        codes = {
            "update": update.main(
                [*common, *update_args, "--summary-json", str(summaries / "1.json")], youtube=yt
            ),
            "sync": sync.main([*common, "--summary-json", str(summaries / "2.json")], http_get=self.http),
            "transcribe": transcribe.main(
                [*common, "--summary-json", str(summaries / "3.json")],
                client=self.openai,
                run=self.ytdlp,
                sleep=no_sleep,
                min_request_interval=0,
            ),
            "format": fmt.main(
                [*common, "--summary-json", str(summaries / "4.json")],
                client=self.anthropic,
                sleep=no_sleep,
                min_request_interval=0,
            ),
        }
        self.report, self.annotations = report.build_report(
            report.load_summaries(summaries), expected=list(report.STEPS)
        )
        return codes

    def snapshot(self) -> dict[str, tuple[bytes, int]]:
        return {
            str(p.relative_to(self.root)): (p.read_bytes(), p.stat().st_mtime_ns)
            for p in sorted(self.root.rglob("*"))
            if p.is_file()
        }


@pytest.fixture
def pipeline(tmp_path):
    return Pipeline(make_repo(tmp_path / "repo"))


def changed(before, after):
    return sorted(
        path
        for path in set(before) | set(after)
        if before.get(path, (None,))[0] != after.get(path, (None,))[0]
    )


def test_first_run_creates_everything(pipeline):
    codes = pipeline.run(youtube())
    assert codes == {"update": 0, "sync": 0, "transcribe": 0, "format": 0}
    d = pipeline.root / "content/resources/videos/2026-11-01_quarto-with-hadley-wickham"
    assert sorted(p.name for p in d.iterdir()) == ["_index.md", "thumbnail.jpg", "transcription.txt", "transcription.vtt"]
    html = (d / "transcription.txt").read_text()
    assert '<a href="/people/hadley-wickham/">Hadley Wickham</a>' in html
    fm = sync.parse_frontmatter((d / "_index.md").read_text())[0]
    assert fm["people"] == ["Hadley Wickham"] and fm["software"] == ["quarto"]
    # The transcription prompt used the synced frontmatter.
    assert pipeline.openai.calls[-1]["prompt"].startswith("Quarto with Hadley Wickham")
    assert "### New videos (2)" in pipeline.report
    assert "| Transcription | 2 transcribed" in pipeline.report
    assert "| Formatting | 2 formatted" in pipeline.report
    assert pipeline.annotations == []


def test_second_run_changes_nothing(pipeline):
    pipeline.run(youtube())
    before = pipeline.snapshot()
    calls = (len(pipeline.ytdlp.calls), len(pipeline.openai.calls), len(pipeline.anthropic.calls))
    codes = pipeline.run(youtube())
    after = pipeline.snapshot()
    assert codes == {"update": 0, "sync": 0, "transcribe": 0, "format": 0}
    assert before == after  # contents and modification times
    assert (len(pipeline.ytdlp.calls), len(pipeline.openai.calls), len(pipeline.anthropic.calls)) == calls
    assert "| YouTube metadata | 2 unchanged |" in pipeline.report


def test_title_change_renames_without_new_transcripts(pipeline):
    pipeline.run(youtube())
    before = pipeline.snapshot()
    calls = (len(pipeline.ytdlp.calls), len(pipeline.openai.calls), len(pipeline.anthropic.calls))
    pipeline.run(youtube(video000002="Shiny tips and tricks"))
    after = pipeline.snapshot()
    old, new = "content/resources/videos/2026-11-02_shiny-tips", "content/resources/videos/2026-11-02_shiny-tips-and-tricks"
    assert changed(before, after) == sorted([
        f"{old}/_index.md",
        f"{old}/thumbnail.jpg",
        f"{old}/transcription.txt",
        f"{old}/transcription.vtt",
        f"{new}/_index.md",
        f"{new}/thumbnail.jpg",
        f"{new}/transcription.txt",
        f"{new}/transcription.vtt",
        "data/videos.toml",
    ])
    # The transcripts moved along; nothing was transcribed or formatted again.
    assert after[f"{new}/transcription.vtt"][0] == before[f"{old}/transcription.vtt"][0]
    assert (len(pipeline.ytdlp.calls), len(pipeline.openai.calls), len(pipeline.anthropic.calls)) == calls
    assert "`2026-11-02_shiny-tips` → `2026-11-02_shiny-tips-and-tricks`" in pipeline.report


def test_stats_refresh_only_touches_metadata(pipeline):
    pipeline.run(youtube())
    before = pipeline.snapshot()
    yt = youtube()
    for item in yt.videos_data.values():
        item["statistics"]["viewCount"] = "5000"
    pipeline.run(yt)
    assert changed(before, pipeline.snapshot()) == []  # not a stats day
    pipeline.run(yt, "--refresh-stats")
    assert changed(before, pipeline.snapshot()) == [
        "content/resources/videos/2026-11-01_quarto-with-hadley-wickham/_index.md",
        "content/resources/videos/2026-11-02_shiny-tips/_index.md",
        "data/videos.toml",
    ]
    assert "stats refreshed" in pipeline.report


def test_blocked_downloads_are_retried_next_run(pipeline):
    blocked = "ERROR: [youtube] video000001: Sign in to confirm you’re not a bot."
    pipeline.ytdlp = FakeYtDlp({"https://www.youtube.com/watch?v=video000001": [blocked]})
    codes = pipeline.run(youtube())
    assert codes["transcribe"] == 2 and codes["format"] == 0
    assert "**Audio downloads failed**" in pipeline.report
    assert "::warning title=Audio downloads failed::" in pipeline.annotations[0]
    d = pipeline.root / "content/resources/videos/2026-11-01_quarto-with-hadley-wickham"
    assert not (d / "transcription.vtt").exists()
    # Next night the download works and the video catches up.
    codes = pipeline.run(youtube())
    assert codes == {"update": 0, "sync": 0, "transcribe": 0, "format": 0}
    assert (d / "transcription.txt").exists()


def test_summaries_are_valid_json(pipeline):
    pipeline.run(youtube())
    for path in sorted((pipeline.root.parent / "summaries").glob("*.json")):
        data = json.loads(path.read_text())
        assert data["exit_code"] == 0 and data["finished_at"]


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-p", "no:cacheprovider", *sys.argv[1:]]))
