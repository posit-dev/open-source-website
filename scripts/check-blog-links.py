#!/usr/bin/env python3
"""Check for broken internal blog links in a Hugo build.

Parses all HTML files under BUILD_DIR/blog/, extracts <a href="..."> values,
resolves them to filesystem paths, and reports any that don't exist in the
build output.

Usage: python3 scripts/check-blog-links.py BUILD_DIR
"""

import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

ASSET_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico",
    ".css", ".js", ".json", ".xml",
    ".csv", ".tsv", ".xlsx", ".rds", ".rda",
    ".pdf", ".zip", ".tar", ".gz",
    ".woff", ".woff2", ".ttf", ".eot",
    ".mp4", ".webm", ".ogg", ".mp3",
    ".R", ".r", ".py", ".qmd", ".Rmd", ".ipynb",
    ".bib", ".lua", ".scala", ".yml", ".yaml", ".toml",
    ".txt", ".lock", ".map",
}


class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href" and value:
                    self.links.append(value)


def extract_links(html_file: Path) -> list[str]:
    parser = LinkExtractor()
    parser.feed(html_file.read_text(errors="replace"))
    return parser.links


def is_internal_page_link(href: str) -> bool:
    if href.startswith(("http://", "https://", "mailto:", "javascript:", "data:", "#")):
        return False
    # Skip custom URI schemes (e.g. positron://...)
    if "://" in href.split("?")[0].split("#")[0]:
        return False
    # Skip bare hostnames (e.g. "repo.r-wasm.org") — missing scheme in source
    bare = href.split("#")[0].split("?")[0].split("/")[0]
    if "." in bare and not bare.startswith("."):
        parts = bare.rsplit(".", 1)
        if len(parts) == 2 and parts[1] in ("org", "com", "net", "io", "dev", "co", "ai"):
            return False
    # Strip fragment and check extension
    path = href.split("#")[0].split("?")[0].rstrip("/")
    ext = Path(path).suffix
    if ext and ext in ASSET_EXTENSIONS:
        return False
    return bool(path)


def resolve_href(href: str, source_file: Path, build_dir: Path) -> Path:
    path = unquote(href.split("#")[0].split("?")[0])
    if not path:
        return source_file.parent

    if path.startswith("/"):
        return (build_dir / path.lstrip("/")).resolve()
    else:
        return (source_file.parent / path).resolve()


def path_exists(path: Path) -> bool:
    if path.is_file():
        return True
    if path.is_dir() and (path / "index.html").is_file():
        return True
    if path.with_suffix(".html").is_file():
        return True
    return False


def href_to_url(href: str, source_file: Path, build_dir: Path) -> str:
    """Convert a resolved href back to a URL path for display."""
    resolved = resolve_href(href, source_file, build_dir)
    try:
        return "/" + str(resolved.relative_to(build_dir))
    except ValueError:
        return str(resolved)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/check-blog-links.py BUILD_DIR", file=sys.stderr)
        sys.exit(1)

    build_dir = Path(sys.argv[1]).resolve()
    blog_dir = build_dir / "blog"

    if not blog_dir.is_dir():
        print(f"Error: {blog_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    # source_page -> [(raw_href, resolved_url)]
    broken: dict[str, list[tuple[str, str]]] = defaultdict(list)

    for html_file in sorted(blog_dir.rglob("*.html")):
        for href in extract_links(html_file):
            if not is_internal_page_link(href):
                continue
            resolved = resolve_href(href, html_file, build_dir)
            if not path_exists(resolved):
                source = str(html_file.relative_to(build_dir))
                url = href_to_url(href, html_file, build_dir)
                broken[source].append((href, url))

    total = 0
    for source in sorted(broken):
        print(source)
        for raw_href, resolved_url in broken[source]:
            if raw_href == resolved_url:
                print(f"  {raw_href}")
            else:
                print(f"  {raw_href}  ->  {resolved_url}")
            total += 1
        print()

    print(f"{total} broken link(s) in {len(broken)} file(s).")
    sys.exit(1 if total > 0 else 0)


if __name__ == "__main__":
    main()
