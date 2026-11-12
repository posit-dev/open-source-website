#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "anthropic>=0.40.0",
#   "python-dotenv>=1.0.0",
#   "pytest>=8.0",
# ]
# ///

"""Tests for format-transcriptions.py. The Anthropic API is faked."""

import json
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import videolib  # noqa: E402
from videotesting import (  # noqa: E402
    SAMPLE_VTT,
    FakeAnthropic,
    RateLimitError,
    StatusError,
    load_script,
    make_repo,
    no_sleep,
    vtt_to_html,
    write_video_dir,
)

f = load_script("format-transcriptions.py")

CUES = videolib.parse_vtt(SAMPLE_VTT)
GOOD_HTML = vtt_to_html(SAMPLE_VTT)


# --- Pure helpers ---


@pytest.mark.parametrize(
    "raw, clean",
    [
        ("```html\n<p>x</p>\n```", "<p>x</p>"),
        ("```\n<p>x</p>```", "<p>x</p>"),
        ("  <p>x</p>  ", "<p>x</p>"),
    ],
)
def test_strip_markdown_fence(raw, clean):
    assert f.strip_markdown_fence(raw) == clean


def test_build_user_message():
    fm = {"title": "T", "people": ["A"], "software": ["quarto"], "description": "d" * 700}
    msg = f.build_user_message("WEBVTT", fm)
    header, vtt = msg.split("\n\n---\n\n")
    assert vtt == "WEBVTT"
    assert header.splitlines() == [
        "Video title: T",
        "People featured: A",
        "Technologies mentioned: quarto",
        "Description: " + "d" * 600,
    ]
    assert f.build_user_message("WEBVTT", {}) == "WEBVTT"


def test_split_vtt_into_chunks():
    cues = [(float(t), float(t) + 4, f"cue {t}") for t in range(0, 100, 10)]
    chunks = f.split_vtt_into_chunks(videolib.render_vtt(cues), 30)
    assert [start for _, start in chunks] == [0, 30, 60, 90]
    assert [len(videolib.parse_vtt(vtt)) for vtt, _ in chunks] == [3, 3, 3, 1]


def test_chunk_system_prompt():
    system = f.build_chunk_system(1, 4)
    assert system.startswith(f.PROMPT.rstrip())
    assert "This is segment 2 of 4." in system


class TestCoverage:
    def test_full(self):
        assert f.coverage(CUES, GOOD_HTML) == 1.0

    def test_blockquotes_and_headings_dont_count(self):
        quote = "<blockquote><a data-t=\"0\">Hello everyone, today we talk about Quarto.</a></blockquote>"
        html = "<h3>It was built by the team that also made Shiny</h3>" + quote
        assert f.coverage(CUES, html) == 0.0

    def test_entities_and_case(self):
        cues = [(0.0, 1.0, "R & Python, it's GREAT")]
        assert f.coverage(cues, '<p><a data-t="0">r &amp; python, it&#x27;s great</a></p>') == 1.0

    def test_multiplicity(self):
        cues = [(0.0, 1.0, "the the the the")]
        assert f.coverage(cues, '<p><a data-t="0">the the</a></p>') == 0.5


class TestValidateHtml:
    def test_valid(self):
        metrics = f.validate_html(GOOD_HTML, CUES, 26)
        assert metrics == {"coverage": 1.0, "anchors": 3, "warnings": None}

    def test_allowed_structure(self):
        html = (
            GOOD_HTML
            + "\n<!-- segment separator -->\n<h3>More</h3><blockquote><a data-t=\"20\">Hadley Wickham joins us later.</a></blockquote>"
        )
        assert f.validate_html(html, CUES, 26)["anchors"] == 4

    @pytest.mark.parametrize(
        "html, reason",
        [
            ("Here is your HTML: <p></p>", "not_html"),
            ("<div>" + GOOD_HTML + "</div>", "disallowed_tag"),
            (GOOD_HTML + "<h2>x</h2>", "disallowed_tag"),
            (GOOD_HTML.replace("<p>", "<span>").replace("</p>", "</span>"), "disallowed_tag"),
            (GOOD_HTML.replace("<p>", '<p class="x">'), "disallowed_attribute"),
            (GOOD_HTML.replace('<a data-t="0">', '<a a data-t="0">'), "disallowed_attribute"),
            (GOOD_HTML.replace('<a data-t="0">', '<a data-t="="0">'), "disallowed_attribute"),
            (GOOD_HTML.replace('<a data-t="0">', '<a href="/x" data-t="0">'), "disallowed_attribute"),
            (GOOD_HTML.replace('data-t="20"', 'data-t="120"'), "bad_timestamp"),
            ('<a data-t="0">Hello everyone, today we talk about Quarto.</a>', "no_paragraphs"),
            ('<p><a data-t="0">Hello everyone.</a></p>', "low_coverage"),
        ],
    )
    def test_invalid(self, html, reason):
        with pytest.raises(f.FormatError) as e:
            f.validate_html(html, CUES, 26)
        assert e.value.reason == reason

    def test_small_overshoot_is_a_warning(self):
        html = GOOD_HTML.replace('data-t="20"', 'data-t="70"')  # 44 s beyond 26 s, under 60 s
        metrics = f.validate_html(html, CUES, 26)
        assert metrics["warnings"] == ['timestamp_overshoot: data-t="70" is 44s beyond the end of the video']

    def test_overshoot_tolerance_scales_with_duration(self):
        cues = [(0.0, 3600.0, "word " * 10)]
        html = '<p><a data-t="3900">' + "word " * 10 + "</a></p>"  # 300 s over, under 10 %
        assert f.validate_html(html, cues, 3600)["warnings"]
        html = '<p><a data-t="4000">' + "word " * 10 + "</a></p>"  # 400 s over
        with pytest.raises(f.FormatError):
            f.validate_html(html, cues, 3600)

    def test_coverage_threshold(self):
        cues = [(0.0, 1.0, " ".join(f"w{i}" for i in range(100)))]

        def html(n):
            return '<p><a data-t="0">' + " ".join(f"w{i}" for i in range(n)) + "</a></p>"

        assert f.validate_html(html(95), cues, 1)["coverage"] == 0.95
        assert f.validate_html(html(90), cues, 1)["coverage"] == 0.90
        with pytest.raises(f.FormatError, match="80.0%"):
            f.validate_html(html(80), cues, 1)


# --- Timestamp repair ---


def cues_from(*texts, step=10):
    return [(float(i * step) + 0.7, float(i * step) + 9, t) for i, t in enumerate(texts)]


class TestRepairTimestamps:
    cues = cues_from(
        "Hello everyone and welcome.",
        "Today we talk about Quarto,",
        "the publishing system.",
        "And then about Shiny.",
        "Thanks for watching.",
    )

    def test_wrong_values_are_fixed(self):
        html = (
            '<p><a data-t="0">Hello everyone and welcome.</a> <a data-t="25">Today we talk about Quarto,</a> '
            '<a data-t="15">the publishing system.</a></p>\n\n<p><a data-t="99">And then about Shiny.</a></p>'
        )
        out, stats = f.repair_timestamps(html, self.cues)
        assert re.findall(r'data-t="(\d+)"', out) == ["0", "10", "20", "30"]
        assert stats == {"anchors": 4, "matched": 4, "changed": 3, "unmatched": 0}
        assert re.sub(r'data-t="\d+"', "", out) == re.sub(r'data-t="\d+"', "", html)  # only data-t changed

    def test_merged_cues_get_the_first_start(self):
        html = '<p><a data-t="7">Today we talk about Quarto, the publishing system.</a></p>'
        out, _ = f.repair_timestamps(html, self.cues)
        assert 'data-t="10"' in out

    def test_anchor_starting_mid_cue(self):
        html = '<p><a data-t="0">Hello everyone</a> <a data-t="0">and welcome.</a></p>'
        out, _ = f.repair_timestamps(html, self.cues)
        assert re.findall(r'data-t="(\d+)"', out) == ["0", "0"]

    def test_corrected_leading_word(self):
        # Whisper heard "Korto"; the model corrected it to "Quarto".
        cues = cues_from("Hello everyone and welcome.", "Korto is great for documents.")
        html = '<p><a data-t="0">Hello everyone and welcome.</a> <a data-t="3">Quarto is great for documents.</a></p>'
        out, stats = f.repair_timestamps(html, cues)
        assert 'data-t="10"' in out and stats["unmatched"] == 0

    def test_repeated_phrase_searches_forward(self):
        cues = cues_from("Thank you.", "Something in between.", "Thank you.")
        html = '<p><a data-t="0">Thank you.</a> <a data-t="0">Something in between.</a> <a data-t="0">Thank you.</a></p>'
        out, _ = f.repair_timestamps(html, cues)
        assert re.findall(r'data-t="(\d+)"', out) == ["0", "10", "20"]

    def test_blockquote_reuses_prose_value(self):
        html = (
            '<p><a data-t="0">Hello everyone and welcome.</a> <a data-t="12">And then about Shiny.</a></p>\n\n'
            '<blockquote><a data-t="12">And then about Shiny.</a></blockquote>\n\n'
            '<p><a data-t="40">Thanks for watching.</a></p>'
        )
        out, stats = f.repair_timestamps(html, self.cues)
        assert re.findall(r'data-t="(\d+)"', out) == ["0", "30", "30", "40"]
        assert stats["anchors"] == 3  # pull quotes aren't counted twice

    def test_pieces_split_by_inject_links_stay_together(self):
        linked = f.inject_links(
            '<p><a data-t="13">Today we talk about Quarto,</a> <a data-t="14">the publishing system.</a></p>',
            {},
            {"Quarto": "/software/quarto/"},
        )
        assert '<a href="/software/quarto/">Quarto</a>' in linked
        out, _ = f.repair_timestamps(linked, self.cues)
        # "Today we talk about ", "," (the pieces around the link), "the publishing system."
        assert re.findall(r'data-t="(\d+)"', out) == ["10", "10", "20"]
        assert '<a href="/software/quarto/">Quarto</a>' in out

    def test_unmatched_keeps_value_but_capped_at_last_cue(self):
        html = '<p><a data-t="5">Words that were never said.</a> <a data-t="9999">Neither were these.</a></p>'
        out, stats = f.repair_timestamps(html, self.cues)
        assert re.findall(r'data-t="(\d+)"', out) == ["5", "40"]
        assert stats["unmatched"] == 2

    def test_no_cues(self):
        html = '<p><a data-t="5">x</a></p>'
        assert f.repair_timestamps(html, [])[0] == html


def test_estimate_cost():
    assert f.estimate_cost("claude-sonnet-4-6", 1_000_000, 100_000) == 4.5
    assert f.estimate_cost("claude-haiku-4-5", 1_000_000, 0) == 1.0
    assert f.estimate_cost("some-other-model", 1, 1) is None


# --- Entity linking ---


class TestInjectLinks:
    people = {"Hadley Wickham": "/people/hadley-wickham/"}
    software = {"Quarto": "/software/quarto/", "Shiny": "/software/shiny/", "Shiny for Python": "/software/shiny-python/"}

    def test_splits_anchor_and_links_first_occurrence_only(self):
        html = '<p><a data-t="0">I love quarto a lot.</a> <a data-t="5">Quarto again.</a></p>'
        assert f.inject_links(html, {}, self.software) == (
            '<p><a data-t="0">I love </a><a href="/software/quarto/">quarto</a><a data-t="0"> a lot.</a> '
            '<a data-t="5">Quarto again.</a></p>'
        )

    def test_match_at_anchor_start_and_end(self):
        html = '<p><a data-t="3">Shiny</a></p>'
        assert f.inject_links(html, {}, self.software) == '<p><a href="/software/shiny/">Shiny</a></p>'

    def test_longest_name_first(self):
        html = '<p><a data-t="0">We use Shiny for Python here.</a></p>'
        out = f.inject_links(html, {}, self.software)
        assert '<a href="/software/shiny-python/">Shiny for Python</a>' in out
        assert '"/software/shiny/"' not in out

    def test_people_are_case_sensitive(self):
        html = '<p><a data-t="0">hadley wickham and Hadley Wickham</a></p>'
        out = f.inject_links(html, self.people, {})
        assert out == (
            '<p><a data-t="0">hadley wickham and </a><a href="/people/hadley-wickham/">Hadley Wickham</a></p>'
        )

    def test_never_nested(self):
        out = f.inject_links(GOOD_HTML, self.people, self.software)
        assert out.count("<a href") == 3  # Quarto, Shiny, Hadley Wickham
        # No <a> opens inside another <a>.
        depth = 0
        for tag in re.findall(r"</?a\b", out):
            depth += 1 if tag == "<a" else -1
            assert depth in (0, 1)
        assert depth == 0

    def test_entity_dicts_respect_ignore_list(self, tmp_path):
        repo = make_repo(tmp_path)
        people, software = f.build_entity_dicts(repo)
        assert people["Hadley Wickham"] == "/people/hadley-wickham/"
        assert set(software) == {"Quarto", "Shiny"}  # "commons" is ignored


# --- main ---


@pytest.fixture
def repo(tmp_path):
    return make_repo(tmp_path)


URL = "https://www.youtube.com/watch?v=aaaaaaaaaaa"


def run(repo, *args, client=None):
    summary = repo / "summary.json"
    code = f.main(
        ["--project-root", str(repo), "--summary-json", str(summary), *args],
        client=client if client is not None else FakeAnthropic(),
        sleep=no_sleep,
        min_request_interval=0,
    )
    return code, json.loads(summary.read_text())


def items(data, status):
    return [i for i in data["items"] if i["status"] == status]


class TestMain:
    def test_formats_and_links(self, repo):
        d = write_video_dir(repo, "2026-01-01_a", url=URL, duration=26, vtt=SAMPLE_VTT, title="Quarto talk")
        client = FakeAnthropic()
        code, data = run(repo, client=client)
        assert code == 0
        out = (d / "transcription.txt").read_text()
        assert '<a href="/software/quarto/">Quarto</a>' in out
        assert '<a href="/people/hadley-wickham/">Hadley Wickham</a>' in out
        (call,) = client.calls
        assert call["model"] == "claude-sonnet-4-6"
        assert call["system"] == f.PROMPT
        assert call["messages"][0]["content"].startswith("Video title: Quarto talk\n")
        (done,) = items(data, "formatted")
        assert done["coverage"] == 1.0
        assert done["input_tokens"] == 1000 and done["output_tokens"] == 500
        assert done["request_ids"] == ["req_fake"]
        assert done["estimated_cost_usd"] == pytest.approx(0.0105)
        assert data["extra"]["model"] == "claude-sonnet-4-6"

    def test_selection(self, repo):
        write_video_dir(repo, "2026-01-04_done", url=URL, vtt=SAMPLE_VTT, html="<p>x</p>")
        write_video_dir(repo, "2026-01-03_excluded", url=URL, vtt=SAMPLE_VTT, extra="transcribe: false\n")
        write_video_dir(repo, "2026-01-02_novtt", url=URL)
        write_video_dir(repo, "2026-01-01_todo", url=URL, duration=26, vtt=SAMPLE_VTT)
        code, data = run(repo)
        assert [i["slug"] for i in items(data, "formatted")] == ["2026-01-01_todo"]
        assert data["counts"] == {"already_formatted": 1, "excluded": 1, "formatted": 1, "no_vtt": 1}

    def test_limit_newest_first(self, repo):
        for i in range(1, 4):
            write_video_dir(repo, f"2026-01-0{i}_v", url=URL, duration=26, vtt=SAMPLE_VTT)
        code, data = run(repo, "--limit", "2")
        assert [i["slug"] for i in items(data, "formatted")] == ["2026-01-03_v", "2026-01-02_v"]
        assert data["counts"]["deferred"] == 1

    def test_force(self, repo):
        d = write_video_dir(repo, "2026-01-01_a", url=URL, duration=26, vtt=SAMPLE_VTT, html="<p>old</p>")
        run(repo, "--force")
        assert "old" not in (d / "transcription.txt").read_text()

    def test_truncated_response_rejected(self, repo):
        d = write_video_dir(repo, "2026-01-01_a", url=URL, duration=26, vtt=SAMPLE_VTT)
        code, data = run(repo, client=FakeAnthropic([(GOOD_HTML, "max_tokens")]))
        assert code == 2
        (error,) = items(data, "error")
        assert error["reason"] == "truncated"
        assert "max_tokens=16384" in error["detail"]
        assert not (d / "transcription.txt").exists()

    def test_invalid_html_not_written(self, repo):
        d = write_video_dir(repo, "2026-01-01_a", url=URL, duration=26, vtt=SAMPLE_VTT)
        code, data = run(repo, client=FakeAnthropic(["<div>nope</div>"]))
        assert code == 2
        assert items(data, "error")[0]["reason"] == "disallowed_tag"
        assert not (d / "transcription.txt").exists()

    def test_rejected_output_saved(self, repo, tmp_path):
        write_video_dir(repo, "2026-01-01_a", url=URL, duration=26, vtt=SAMPLE_VTT)
        rejected = tmp_path / "rejected"
        code, data = run(repo, "--rejected-dir", str(rejected), client=FakeAnthropic(['<p><a data-t="0">Hello.</a></p>']))
        assert code == 2
        assert (rejected / "2026-01-01_a.html").read_text() == '<p><a data-t="0">Hello.</a></p>'
        assert items(data, "error")[0]["rejected_output"] == str(rejected / "2026-01-01_a.html")

    def test_markdown_fence_stripped(self, repo):
        d = write_video_dir(repo, "2026-01-01_a", url=URL, duration=26, vtt=SAMPLE_VTT)
        code, _ = run(repo, client=FakeAnthropic([f"```html\n{GOOD_HTML}\n```"]))
        assert code == 0 and (d / "transcription.txt").read_text().startswith("<p>")

    def test_overloaded_api_retried(self, repo):
        write_video_dir(repo, "2026-01-01_a", url=URL, duration=26, vtt=SAMPLE_VTT)
        client = FakeAnthropic([StatusError(529, "overloaded"), RateLimitError(), GOOD_HTML])
        code, _ = run(repo, client=client)
        assert code == 0 and len(client.calls) == 3

    def test_auth_error_not_retried(self, repo):
        write_video_dir(repo, "2026-01-01_a", url=URL, duration=26, vtt=SAMPLE_VTT)
        client = FakeAnthropic([StatusError(401, "invalid x-api-key")])
        code, data = run(repo, client=client)
        assert code == 2 and len(client.calls) == 1
        assert items(data, "error")[0]["detail"] == "StatusError status=401 request_id=req_401: invalid x-api-key"

    def test_long_video_is_chunked(self, repo):
        cues = [(float(t), float(t) + 5, f"sentence number {t}.") for t in range(0, 3000, 10)]
        d = write_video_dir(repo, "2026-01-01_long", url=URL, duration=3000, vtt=videolib.render_vtt(cues))
        client = FakeAnthropic()
        code, data = run(repo, client=client)
        assert code == 0
        assert len(client.calls) == 4  # 50 minutes in 15-minute chunks
        assert "This is segment 1 of 4." in client.calls[0]["system"]
        assert "This is segment 4 of 4." in client.calls[3]["system"]
        out = (d / "transcription.txt").read_text()
        assert out.count("<!-- segment separator -->") == 3
        (done,) = items(data, "formatted")
        assert done["chunks"] == 4 and done["input_tokens"] == 4000
        assert done["chunk_coverage"] == [1.0, 1.0, 1.0, 1.0]

    def test_short_video_not_chunked(self, repo):
        cues = [(float(t), float(t) + 5, f"sentence number {t}.") for t in range(0, 1100, 10)]
        write_video_dir(repo, "2026-01-01_a", url=URL, duration=1100, vtt=videolib.render_vtt(cues))
        client = FakeAnthropic()
        run(repo, client=client)
        assert len(client.calls) == 1

    def test_model_from_env(self, repo, monkeypatch):
        monkeypatch.setenv("TRANSCRIPT_MODEL", "claude-haiku-4-5")
        write_video_dir(repo, "2026-01-01_a", url=URL, duration=26, vtt=SAMPLE_VTT)
        client = FakeAnthropic()
        code, data = run(repo, client=client)
        assert client.calls[0]["model"] == "claude-haiku-4-5"
        code, data = run(repo, "--force", "--model", "claude-sonnet-4-6", client=client)
        assert client.calls[1]["model"] == "claude-sonnet-4-6"

    def test_check_existing_and_reformat_invalid(self, repo):
        linked = f.inject_links(GOOD_HTML, {"Hadley Wickham": "/people/hadley-wickham/"}, {})
        write_video_dir(repo, "2026-01-02_ok", url=URL, duration=26, vtt=SAMPLE_VTT, html=linked)
        bad = write_video_dir(
            repo, "2026-01-01_bad", url=URL, duration=26, vtt=SAMPLE_VTT, html='<p><a data-t="0">Hello.</a></p>'
        )
        client = FakeAnthropic()
        code, data = run(repo, "--check-existing", client=client)
        assert code == 0 and client.calls == []
        (invalid,) = items(data, "invalid")
        assert invalid["slug"] == "2026-01-01_bad" and invalid["reason"] == "low_coverage"
        assert data["counts"]["valid"] == 1

        code, data = run(repo, "--reformat-invalid", client=client)
        assert [i["slug"] for i in items(data, "formatted")] == ["2026-01-01_bad"]
        assert len(client.calls) == 1
        assert f.check_existing(bad)[0]

    def test_timestamps_repaired_before_writing(self, repo):
        d = write_video_dir(repo, "2026-01-01_a", url=URL, duration=26, vtt=SAMPLE_VTT)
        shifted = GOOD_HTML.replace('data-t="4"', 'data-t="9"').replace('data-t="20"', 'data-t="24"')
        code, data = run(repo, client=FakeAnthropic([shifted]))
        assert code == 0
        values = re.findall(r'data-t="(\d+)"', (d / "transcription.txt").read_text())
        assert set(values) == {"0", "4", "20"}  # pieces split by inject_links repeat a value
        (done,) = items(data, "formatted")
        assert done["timestamps_repaired"] == 2 and done["timestamps_unmatched"] == 0

    def test_repair_timestamps_mode(self, repo):
        shifted = GOOD_HTML.replace('data-t="20"', 'data-t="23"')
        d = write_video_dir(repo, "2026-01-02_a", url=URL, duration=26, vtt=SAMPLE_VTT, html=shifted)
        write_video_dir(repo, "2026-01-01_ok", url=URL, duration=26, vtt=SAMPLE_VTT, html=GOOD_HTML)
        client = FakeAnthropic()
        code, data = run(repo, "--repair-timestamps", "--dry-run", client=client)
        assert (d / "transcription.txt").read_text() == shifted
        code, data = run(repo, "--repair-timestamps", client=client)
        assert code == 0 and client.calls == []
        assert 'data-t="20"' in (d / "transcription.txt").read_text()
        (fixed,) = items(data, "timestamps_repaired")
        assert fixed["slug"] == "2026-01-02_a" and fixed["changed"] == 1
        assert data["counts"]["timestamps_ok"] == 1

    def test_dry_run(self, repo):
        write_video_dir(repo, "2026-01-01_a", url=URL, duration=26, vtt=SAMPLE_VTT)
        client = FakeAnthropic()
        code, data = run(repo, "--dry-run", client=client)
        assert code == 0 and client.calls == []
        assert items(data, "would_format")[0]["slug"] == "2026-01-01_a"

    def test_missing_api_key_is_fatal(self, repo, monkeypatch):
        monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
        write_video_dir(repo, "2026-01-01_a", url=URL, duration=26, vtt=SAMPLE_VTT)
        summary = repo / "s.json"
        code = f.main(["--project-root", str(repo), "--summary-json", str(summary)])
        assert code == 1
        assert "ANTHROPIC_API_KEY" in json.loads(summary.read_text())["fatal"]

    def test_logging(self, repo, capsys, monkeypatch):
        monkeypatch.setenv("CI", "true")
        write_video_dir(repo, "2026-01-01_a", url=URL, duration=26, vtt=SAMPLE_VTT)
        run(repo)
        err = capsys.readouterr().err
        assert "2026-01-01_a (aaaaaaaaaaa): claude-sonnet-4-6 responded in" in err
        assert "1000 in / 500 out tokens, stop_reason=end_turn, request_id=req_fake" in err
        assert "wrote transcription.txt (3 anchors, 100.0% coverage, ~$0.011)" in err


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-p", "no:cacheprovider", *sys.argv[1:]]))
