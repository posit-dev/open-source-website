#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""
Turn the run summaries of the video pipeline into a Markdown report.

Reads the --summary-json files written by update-youtube-videos.py,
sync-videos.py, transcribe.py, and format-transcriptions.py, and writes the
pull request description of the nightly sync (also used for the GitHub
Actions step summary). With --annotations, also prints ::warning:: and
::error:: workflow commands so problems show up on the run page.

Usage:
    ./scripts/video-sync-report.py SUMMARY_DIR [--output FILE] [--annotations]
        [--expect update-youtube-videos,sync-videos,...] [--run-url URL]
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

STEPS = {
    "update-youtube-videos": "YouTube metadata",
    "sync-videos": "Video pages",
    "transcribe": "Transcription",
    "format-transcriptions": "Formatting",
}

# Download failures that won't go away by trying again.
PERMANENT_REASONS = {"private", "members_only", "unavailable", "age_restricted"}
# Download failures that mean YouTube is blocking the runner (see transcribe.py).
BLOCKING_REASONS = {"bot_check", "po_token", "http_429"}

MAX_LIST = 40  # items per list, to stay well under GitHub's 65,536-character limit


def load_summaries(directory: Path) -> dict[str, dict[str, Any]]:
    summaries = {}
    for path in sorted(directory.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            print(f"warning: could not read {path}: {e}", file=sys.stderr)
            continue
        if isinstance(data, dict) and data.get("script") in STEPS:
            summaries[data["script"]] = data
    return summaries


def items(summary: dict[str, Any] | None, *statuses: str) -> list[dict[str, Any]]:
    if not summary:
        return []
    return [i for i in summary.get("items", []) if i.get("status") in statuses]


def count(summary: dict[str, Any] | None, status: str) -> int:
    return (summary or {}).get("counts", {}).get(status, 0)


def plural(n: int, word: str, plural_word: str | None = None) -> str:
    return f"{n:,} {word if n == 1 else (plural_word or word + 's')}"


def bullet_list(lines: list[str]) -> list[str]:
    out = [f"- {line}" for line in lines[:MAX_LIST]]
    if len(lines) > MAX_LIST:
        out.append(f"- …and {len(lines) - MAX_LIST:,} more (see the run summaries)")
    return out


def details(summary_text: str, lines: list[str]) -> list[str]:
    return ["<details><summary>" + summary_text + "</summary>", "", *bullet_list(lines), "", "</details>", ""]


def money(value: float | None) -> str:
    return f" (~${value:.2f})" if value else ""


def code(text: str | None) -> str:
    return f"`{text}`" if text else "(unknown)"


def one_line(text: str | None, limit: int = 200) -> str:
    text = " ".join((text or "").split())
    text = text.replace("|", "\\|")
    return text if len(text) <= limit else text[: limit - 1] + "…"


# ---------------------------------------------------------------------------
# Report sections
# ---------------------------------------------------------------------------


def results_table(summaries: dict[str, dict[str, Any]], expected: list[str]) -> list[str]:
    update = summaries.get("update-youtube-videos")
    sync = summaries.get("sync-videos")
    transcribe = summaries.get("transcribe")
    fmt = summaries.get("format-transcriptions")

    rows: list[tuple[str, str]] = []

    def describe(script: str, parts: list[str]) -> str:
        s = summaries.get(script)
        if s is None:
            return "⚠️ no summary (crashed?)" if script in expected else "skipped"
        if s.get("fatal"):
            return f"❌ failed: {one_line(s['fatal'], 120)}"
        text = ", ".join(p for p in parts if p) or "nothing to do"
        return ("⚠️ " if s.get("exit_code") == 2 else "") + text

    if "update-youtube-videos" in expected or update:
        stats = (update or {}).get("extra", {}).get("refresh_stats")
        rows.append(
            (
                STEPS["update-youtube-videos"],
                describe(
                    "update-youtube-videos",
                    [
                        f"{count(update, 'new'):,} new" if count(update, "new") else "",
                        f"{count(update, 'changed'):,} changed" if count(update, "changed") else "",
                        f"{count(update, 'unchanged') + count(update, 'stats_refreshed'):,} unchanged",
                        "stats refreshed" if stats else "",
                    ],
                ),
            )
        )
    if "sync-videos" in expected or sync:
        rows.append(
            (
                STEPS["sync-videos"],
                describe(
                    "sync-videos",
                    [
                        f"{count(sync, 'created'):,} created" if count(sync, "created") else "",
                        f"{count(sync, 'updated'):,} updated" if count(sync, "updated") else "",
                        f"{count(sync, 'renamed'):,} renamed" if count(sync, "renamed") else "",
                        f"{count(sync, 'error'):,} failed" if count(sync, "error") else "",
                        f"{count(sync, 'unchanged'):,} unchanged" if count(sync, "unchanged") else "",
                    ],
                ),
            )
        )
    if "transcribe" in expected or transcribe:
        extra = (transcribe or {}).get("extra", {})
        rows.append(
            (
                STEPS["transcribe"],
                describe(
                    "transcribe",
                    [
                        f"{count(transcribe, 'transcribed'):,} transcribed{money(extra.get('estimated_cost_usd'))}"
                        if count(transcribe, "transcribed")
                        else "",
                        f"{count(transcribe, 'error'):,} failed" if count(transcribe, "error") else "",
                        "downloads blocked" if extra.get("breaker_tripped") else "",
                        f"{count(transcribe, 'deferred'):,} deferred" if count(transcribe, "deferred") else "",
                    ],
                ),
            )
        )
    if "format-transcriptions" in expected or fmt:
        extra = (fmt or {}).get("extra", {})
        rows.append(
            (
                STEPS["format-transcriptions"],
                describe(
                    "format-transcriptions",
                    [
                        f"{count(fmt, 'formatted'):,} formatted{money(extra.get('estimated_cost_usd'))}"
                        if count(fmt, "formatted")
                        else "",
                        f"{count(fmt, 'error'):,} failed" if count(fmt, "error") else "",
                        f"{count(fmt, 'deferred'):,} deferred" if count(fmt, "deferred") else "",
                    ],
                ),
            )
        )
    if not rows:
        return []
    return ["| Step | Result |", "| --- | --- |", *(f"| {step} | {result} |" for step, result in rows), ""]


def changes_sections(summaries: dict[str, dict[str, Any]]) -> list[str]:
    update = summaries.get("update-youtube-videos")
    sync = summaries.get("sync-videos")
    transcribe = summaries.get("transcribe")
    fmt = summaries.get("format-transcriptions")
    out: list[str] = []

    new = items(update, "new")
    if new:
        out += [f"### New videos ({len(new)})", ""]
        out += bullet_list([f"[{one_line(i.get('title'), 120)}]({i['url']}) {code(i.get('slug'))}" for i in new])
        out.append("")

    renamed = items(sync, "renamed")
    if renamed:
        out += [f"### Renamed ({len(renamed)})", "", "The URLs of these pages change; links in the repo were updated.", ""]
        lines = []
        for i in renamed:
            line = f"{code(i.get('old_slug'))} → {code(i.get('slug'))}"
            if i.get("action") == "merged":
                line += " (merged into an existing directory)"
            refs = i.get("updated_references") or []
            if refs:
                line += f"; references updated in {', '.join(code(r) for r in refs)}"
            lines.append(line)
        out += bullet_list(lines) + [""]

    changed = items(update, "changed")
    if changed:
        out += ["### Changed metadata", ""]
        out += details(
            plural(len(changed), "video"),
            [f"{code(i.get('slug'))}: {', '.join(i.get('changed_fields', []))}" for i in changed],
        )

    transcribed = items(transcribe, "transcribed")
    formatted = items(fmt, "formatted")
    if transcribed or formatted:
        out += ["### Transcripts", ""]
        lines = []
        formatted_slugs = {i["slug"] for i in formatted}
        for i in transcribed:
            note = " and formatted" if i["slug"] in formatted_slugs else " (not formatted yet)"
            warn = f" ⚠️ {'; '.join(i['warnings'])}" if i.get("warnings") else ""
            lines.append(f"{code(i['slug'])}: transcribed{note}{warn}")
        transcribed_slugs = {i["slug"] for i in transcribed}
        for i in formatted:
            if i["slug"] not in transcribed_slugs:
                lines.append(f"{code(i['slug'])}: formatted")
        for i in formatted:
            if i.get("warnings"):
                lines.append(f"{code(i['slug'])}: ⚠️ {'; '.join(i['warnings'])}")
        out += details(plural(len(lines), "video"), lines)
    return out


def problems_section(summaries: dict[str, dict[str, Any]], expected: list[str]) -> tuple[list[str], list[str]]:
    """Return (markdown lines, annotations)."""
    update = summaries.get("update-youtube-videos")
    sync = summaries.get("sync-videos")
    transcribe = summaries.get("transcribe")
    fmt = summaries.get("format-transcriptions")
    out: list[str] = []
    annotations: list[str] = []

    def block(title: str, lines: list[str], hint: str | None = None, level: str = "warning") -> None:
        if not lines:
            return
        nonlocal out
        out += [f"**{title}**", ""]
        if hint:
            out += [hint, ""]
        out += bullet_list(lines) + [""]
        annotations.append(f"::{level} title={title}::{len(lines)} item(s); see the step summary or PR description")

    for script in STEPS:
        s = summaries.get(script)
        if s and s.get("fatal"):
            block(f"{STEPS[script]} failed", [one_line(s["fatal"], 500)], level="error")
        elif s is None and script in expected:
            block(f"{STEPS[script]} produced no summary", ["The step crashed before writing it; check the job log."], level="error")

    block(
        "Could not fetch some YouTube sources",
        [f"{code(i.get('source'))}: {one_line(i.get('detail'))}" for i in items(update, "error")],
    )

    extra = (transcribe or {}).get("extra", {})
    download_errors = [i for i in items(transcribe, "error") if i.get("stage") == "download"]
    blocked = items(transcribe, "skipped")
    blocked = [i for i in blocked if i.get("reason") == "download_blocked"]
    if extra.get("breaker_tripped"):
        block(
            "YouTube blocked the downloads",
            [
                f"{plural(len(blocked), 'more video')} skipped after repeated "
                f"{', '.join(sorted({i['reason'] for i in download_errors} & BLOCKING_REASONS)) or 'blocking'} errors"
            ],
            hint="Transcribe them locally with `just update-videos 15 chrome` on this branch and push, "
            "or wait for the next run.",
        )
    if download_errors:
        lines = []
        for i in download_errors:
            fix = f"`just transcribe --video {i['slug']} --cookies-from-browser chrome`"
            if i.get("reason") in PERMANENT_REASONS:
                fix += " or set `transcribe: false` in its `_index.md`"
            lines.append(f"{code(i['slug'])}: **{i.get('reason')}**: {one_line(i.get('detail'))}. Fix: {fix}")
        block("Audio downloads failed", lines)

    block(
        "Transcription failed",
        [
            f"{code(i['slug'])}: **{i.get('reason')}**: {one_line(i.get('detail'))}. "
            f"Fix: `just transcribe --video {i['slug']}`"
            for i in items(transcribe, "error")
            if i.get("stage") != "download"
        ],
    )
    block(
        "Formatting failed",
        [
            f"{code(i['slug'])}: **{i.get('reason')}**: {one_line(i.get('detail'))}. "
            f"It's retried in the next run, or run `just format-transcriptions --video {i['slug']}`"
            for i in items(fmt, "error")
        ],
    )
    block(
        "Video pages failed",
        [f"{code(i.get('slug'))}: **{i.get('reason')}**: {one_line(i.get('detail'))}" for i in items(sync, "error")],
    )

    # Informational: not errors, but worth a look.
    info: list[str] = []
    missing = items(update, "missing")
    if missing:
        info += details(
            f"{plural(len(missing), 'video')} in <code>data/videos.toml</code> no longer on the channel or playlists "
            "(set <code>publish = false</code> to unpublish)",
            [f"{code(i.get('slug'))} ({i.get('url')})" for i in missing],
        )
    unavailable = items(update, "unavailable")
    if unavailable:
        info += details(
            f"{plural(len(unavailable), 'video')} listed but not returned by the API (private or deleted?)",
            [f"{code(i.get('slug') or i.get('video_id'))} ({i.get('url')})" for i in unavailable],
        )
    duplicates = items(update, "duplicate_slug")
    if duplicates:
        info += details(
            f"{plural(len(duplicates), 'video')} skipped because another video has the same slug",
            [f"{code(i.get('slug'))}: skipped {i.get('url')}, kept {i.get('kept')}" for i in duplicates],
        )
    orphans = items(sync, "orphan")
    if orphans:
        info += details(
            f"{plural(len(orphans), 'directory', 'directories')} without an entry in <code>data/videos.toml</code>",
            [code(i.get("slug")) for i in orphans],
        )
    skipped = [i for i in items(transcribe, "skipped") if i.get("reason") != "download_blocked"]
    if skipped:
        info += details(
            f"{plural(len(skipped), 'video')} not transcribed",
            [f"{code(i.get('slug'))}: {i.get('reason')}" for i in skipped],
        )

    if out:
        out = ["### ⚠️ Problems", ""] + out
    if info:
        out += ["### Notes", ""] + info
    return out, annotations


def build_report(
    summaries: dict[str, dict[str, Any]],
    *,
    expected: list[str],
    run_url: str | None = None,
) -> tuple[str, list[str]]:
    out = [
        "Nightly sync of [Posit's YouTube videos](https://www.youtube.com/@PositPBC) into "
        "`content/resources/videos/`"
        + (f" ([workflow run]({run_url}))" if run_url else "")
        + ".",
        "",
        "Review the changes below, then approve and merge to publish them.",
        "",
    ]
    out += results_table(summaries, expected)
    out += changes_sections(summaries)
    problems, annotations = problems_section(summaries, expected)
    out += problems

    out += [
        "---",
        "",
        "Adjust a video with `include`, `exclude`, or `override` blocks in its `_index.md`, "
        "hide it with `publish = false` in `data/videos.toml`, or skip its transcript with "
        "`transcribe: false`."
        + (f" Logs and run summaries are attached to the [workflow run]({run_url})." if run_url else ""),
    ]
    return "\n".join(out).rstrip() + "\n", annotations


def default_run_url() -> str | None:
    server = os.getenv("GITHUB_SERVER_URL")
    repo = os.getenv("GITHUB_REPOSITORY")
    run_id = os.getenv("GITHUB_RUN_ID")
    if server and repo and run_id:
        return f"{server}/{repo}/actions/runs/{run_id}"
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n\n")[0])
    parser.add_argument("summary_dir", type=Path, help="directory with the *.json run summaries")
    parser.add_argument("--output", "-o", type=Path, help="write the report here instead of stdout")
    parser.add_argument("--annotations", action="store_true", help="print GitHub Actions annotations to stdout")
    parser.add_argument(
        "--expect",
        default=",".join(STEPS),
        help="comma-separated steps that should have a summary (default: all four)",
    )
    parser.add_argument("--run-url", default=default_run_url(), help="link to the workflow run")
    args = parser.parse_args(argv)

    expected = [s for s in args.expect.split(",") if s]
    summaries = load_summaries(args.summary_dir) if args.summary_dir.exists() else {}
    report, annotations = build_report(summaries, expected=expected, run_url=args.run_url)

    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        sys.stdout.write(report)
    if args.annotations:
        for line in annotations:
            print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
