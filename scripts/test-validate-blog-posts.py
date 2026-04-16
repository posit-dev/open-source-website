#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "pyyaml>=6.0",
#   "rich>=13.0.0",
#   "pytest>=8.0",
# ]
# ///

"""Tests for validate-blog-posts.py."""

import datetime
import importlib.util
import sys
from pathlib import Path

import pytest

# Import the script by file path (it uses hyphens, not a regular module)
_spec = importlib.util.spec_from_file_location(
    "validate_blog_posts",
    Path(__file__).parent / "validate-blog-posts.py",
)
v = importlib.util.module_from_spec(_spec)
sys.modules["validate_blog_posts"] = v
_spec.loader.exec_module(v)


# --- Helpers ---


def make_ctx(
    tmp_path: Path,
    topics: list[str] | None = None,
    software: list[str] | None = None,
    people: list[str] | None = None,
) -> v.ValidationContext:
    """Build a ValidationContext with test data under tmp_path."""
    ctx = v.ValidationContext(project_root=tmp_path)
    ctx.valid_topics = topics or ["Best Practices", "Visualization"]
    ctx.valid_software = set(software or ["ggplot2", "quarto"])
    ctx.valid_people_slugs = set(people or ["hadley-wickham", "julia-silge"])

    # Create blog dir so placement checks work
    (tmp_path / "content" / "blog").mkdir(parents=True, exist_ok=True)
    return ctx


def post_path(tmp_path: Path, *parts: str) -> Path:
    """Create a post directory and return the index.md path."""
    d = tmp_path / "content" / "blog" / Path(*parts)
    d.mkdir(parents=True, exist_ok=True)
    return d / "index.md"


VALID_FM: dict = {
    "title": "My Post",
    "date": datetime.date(2026, 4, 15),
    "people": ["Hadley Wickham"],
    "description": "A post about things.",
    "image": "thumbnail.png",
    "image-alt": "A screenshot of the thing",
    "topics": ["Visualization"],
    "software": ["ggplot2"],
    "languages": ["R"],
}


# --- parse_frontmatter ---


class TestParseFrontmatter:
    def test_valid(self):
        content = "---\ntitle: Hello\ndate: '2026-01-01'\n---\nBody."
        fm = v.parse_frontmatter(content)
        assert fm is not None
        assert fm["title"] == "Hello"

    def test_no_frontmatter(self):
        assert v.parse_frontmatter("Just some text") is None

    def test_unclosed_frontmatter(self):
        assert v.parse_frontmatter("---\ntitle: Hello\n") is None

    def test_invalid_yaml(self):
        assert v.parse_frontmatter("---\n: :\n---\n") is None

    def test_empty_frontmatter(self):
        fm = v.parse_frontmatter("---\n---\n")
        assert fm == {}


# --- slugify ---


class TestSlugify:
    def test_basic(self):
        assert v.slugify("Hadley Wickham") == "hadley-wickham"

    def test_accented(self):
        assert v.slugify("Isabella Velásquez") == "isabella-velásquez"

    def test_hyphens(self):
        assert v.slugify("Mary-Jane Watson") == "mary-jane-watson"


# --- severity ---


class TestSeverity:
    def test_new_post(self):
        assert v.severity({}) == "error"

    def test_ported_incomplete(self):
        assert v.severity({"ported_from": "tidyverse"}) == "warning"
        assert (
            v.severity({"ported_from": "tidyverse", "port_status": "raw"})
            == "warning"
        )

    def test_ported_complete(self):
        assert (
            v.severity(
                {"ported_from": "tidyverse", "port_status": "complete"}
            )
            == "error"
        )
        assert (
            v.severity(
                {"ported_from": "tidyverse", "port_status": "review"}
            )
            == "error"
        )


# --- check_placement ---


class TestCheckPlacement:
    def test_top_level_ok(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        assert v.check_placement(p, {}, ctx) == []

    def test_nested_without_ported_from(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "tidyverse", "my-post")
        issues = v.check_placement(p, {}, ctx)
        assert len(issues) == 1
        assert issues[0].level == "error"
        assert "nested" in issues[0].message

    def test_nested_with_ported_from(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "tidyverse", "my-post")
        assert v.check_placement(p, {"ported_from": "tidyverse"}, ctx) == []


# --- check_required_fields ---


class TestCheckRequiredFields:
    def test_all_present(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        assert v.check_required_fields(p, VALID_FM, ctx) == []

    def test_missing_fields(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        issues = v.check_required_fields(p, {"title": "Hello"}, ctx)
        messages = " ".join(i.message for i in issues)
        assert "`topics`" in messages
        assert "`image-alt`" in messages
        assert all(i.level == "error" for i in issues)

    def test_ported_gets_warnings(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "old", "post")
        fm = {"title": "Hello", "ported_from": "tidyverse"}
        issues = v.check_required_fields(p, fm, ctx)
        assert all(i.level == "warning" for i in issues)

    def test_none_value_counts_as_missing(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {**VALID_FM, "image": None}
        issues = v.check_required_fields(p, fm, ctx)
        assert any("image" in i.message for i in issues)


# --- check_forbidden_fields ---


class TestCheckForbiddenFields:
    def test_no_categories(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        assert v.check_forbidden_fields(p, VALID_FM, ctx) == []

    def test_categories_present(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {**VALID_FM, "categories": ["Open Source"]}
        issues = v.check_forbidden_fields(p, fm, ctx)
        assert len(issues) == 1
        assert issues[0].level == "error"
        assert "topics" in issues[0].message

    def test_categories_always_error_even_ported(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "old", "post")
        fm = {"ported_from": "tidyverse", "categories": ["X"]}
        issues = v.check_forbidden_fields(p, fm, ctx)
        assert issues[0].level == "error"


# --- check_date_format ---


class TestCheckDateFormat:
    def test_date_object(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"date": datetime.date(2026, 4, 15)}
        assert v.check_date_format(p, fm, ctx) == []

    def test_valid_string(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"date": "2026-04-15"}
        assert v.check_date_format(p, fm, ctx) == []

    def test_datetime_object(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"date": datetime.datetime(2026, 4, 15, tzinfo=datetime.timezone.utc)}
        issues = v.check_date_format(p, fm, ctx)
        assert len(issues) == 1
        assert "timestamp" in issues[0].message

    def test_bad_string(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"date": "April 15, 2026"}
        issues = v.check_date_format(p, fm, ctx)
        assert len(issues) == 1

    def test_missing_date_skipped(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        assert v.check_date_format(p, {}, ctx) == []

    def test_timestamp_ported_is_warning(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "old", "post")
        fm = {
            "date": datetime.datetime(2023, 1, 1, tzinfo=datetime.timezone.utc),
            "ported_from": "quarto",
        }
        issues = v.check_date_format(p, fm, ctx)
        assert issues[0].level == "warning"


# --- check_date_past ---


class TestCheckDatePast:
    def test_future_date(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        future = datetime.date.today() + datetime.timedelta(days=7)
        fm = {"date": future}
        assert v.check_date_past(p, fm, ctx) == []

    def test_today(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"date": datetime.date.today()}
        assert v.check_date_past(p, fm, ctx) == []

    def test_past_date(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        past = datetime.date.today() - datetime.timedelta(days=1)
        fm = {"date": past}
        issues = v.check_date_past(p, fm, ctx)
        assert len(issues) == 1
        assert issues[0].level == "warning"
        assert "in the past" in issues[0].message

    def test_past_string_date(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"date": "2020-01-01"}
        issues = v.check_date_past(p, fm, ctx)
        assert len(issues) == 1
        assert "publish immediately" in issues[0].message

    def test_ported_skipped(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "old", "post")
        fm = {"date": datetime.date(2020, 1, 1), "ported_from": "tidyverse"}
        assert v.check_date_past(p, fm, ctx) == []

    def test_bad_format_skipped(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"date": "not-a-date"}
        assert v.check_date_past(p, fm, ctx) == []


# --- check_topics ---


class TestCheckTopics:
    def test_valid(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"topics": ["Visualization"]}
        assert v.check_topics(p, fm, ctx) == []

    def test_invalid(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"topics": ["Data Science"]}
        issues = v.check_topics(p, fm, ctx)
        assert len(issues) == 1
        assert "Data Science" in issues[0].message

    def test_single_string_is_validated(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"topics": "Data Science"}
        issues = v.check_topics(p, fm, ctx)
        assert len(issues) == 1
        assert "Data Science" in issues[0].message

    def test_missing_skipped(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        assert v.check_topics(p, {}, ctx) == []


# --- check_software ---


class TestCheckSoftware:
    def test_valid(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"software": ["ggplot2"]}
        assert v.check_software(p, fm, ctx) == []

    def test_invalid(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"software": ["nonexistent-pkg"]}
        issues = v.check_software(p, fm, ctx)
        assert len(issues) == 1
        assert "nonexistent-pkg" in issues[0].message

    def test_single_string_is_validated(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"software": "nonexistent-pkg"}
        issues = v.check_software(p, fm, ctx)
        assert len(issues) == 1
        assert "nonexistent-pkg" in issues[0].message

    def test_missing(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        issues = v.check_software(p, {}, ctx)
        assert len(issues) == 1
        assert issues[0].level == "warning"

    def test_empty_list(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        issues = v.check_software(p, {"software": []}, ctx)
        assert len(issues) == 1
        assert issues[0].level == "warning"


# --- check_people ---


class TestCheckPeople:
    def test_valid(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"people": ["Hadley Wickham"]}
        assert v.check_people(p, fm, ctx) == []

    def test_single_string_is_validated(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"people": "Unknown Person"}
        issues = v.check_people(p, fm, ctx)
        assert any("people page" in i.message for i in issues)

    def test_team_name(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"people": ["Shiny Team"]}
        issues = v.check_people(p, fm, ctx)
        team_issues = [i for i in issues if "team name" in i.message]
        assert len(team_issues) == 1
        assert team_issues[0].level == "warning"

    def test_missing_person_page(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"people": ["Unknown Person"]}
        issues = v.check_people(p, fm, ctx)
        page_issues = [i for i in issues if "people page" in i.message.lower()]
        assert len(page_issues) == 1
        assert page_issues[0].level == "warning"


# --- check_languages ---


class TestCheckLanguages:
    def test_present(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"languages": ["R"]}
        assert v.check_languages(p, fm, ctx) == []

    def test_missing(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        issues = v.check_languages(p, {}, ctx)
        assert len(issues) == 1
        assert issues[0].level == "warning"
        assert "R" in issues[0].message
        assert "Python" in issues[0].message

    def test_empty_list(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        issues = v.check_languages(p, {"languages": []}, ctx)
        assert len(issues) == 1
        assert issues[0].level == "warning"


# --- check_source ---


class TestCheckSource:
    def test_new_post_no_source(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        assert v.check_source(p, {}, ctx) == []

    def test_new_post_with_valid_source(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"source": "tidyverse"}
        assert v.check_source(p, fm, ctx) == []

    def test_new_post_with_invalid_source(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"source": "nonexistent"}
        issues = v.check_source(p, fm, ctx)
        assert len(issues) == 1
        assert issues[0].level == "error"

    def test_ported_with_matching_source(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "old", "post")
        fm = {"ported_from": "tidyverse", "source": "tidyverse"}
        assert v.check_source(p, fm, ctx) == []

    def test_ported_missing_source(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "old", "post")
        fm = {"ported_from": "tidyverse"}
        issues = v.check_source(p, fm, ctx)
        assert len(issues) == 1
        assert "ported_from" in issues[0].message

    def test_ported_mismatched_source(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "old", "post")
        fm = {"ported_from": "tidyverse", "source": "shiny"}
        issues = v.check_source(p, fm, ctx)
        assert len(issues) == 1
        assert issues[0].level == "error"
        assert "tidyverse" in issues[0].message


# --- check_image_exists ---


class TestCheckImageExists:
    def test_local_image_exists(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        (p.parent / "thumb.png").touch()
        fm = {"image": "thumb.png"}
        assert v.check_image_exists(p, fm, ctx) == []

    def test_local_image_missing(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"image": "missing.png"}
        issues = v.check_image_exists(p, fm, ctx)
        assert len(issues) == 1
        assert issues[0].level == "error"

    def test_url_image_skipped(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        fm = {"image": "https://example.com/img.png"}
        assert v.check_image_exists(p, fm, ctx) == []

    def test_subdirectory_image(self, tmp_path):
        ctx = make_ctx(tmp_path)
        p = post_path(tmp_path, "my-post")
        (p.parent / "assets").mkdir()
        (p.parent / "assets" / "hero.png").touch()
        fm = {"image": "assets/hero.png"}
        assert v.check_image_exists(p, fm, ctx) == []
