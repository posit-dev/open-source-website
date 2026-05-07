#!/usr/bin/env python3
"""Check for broken internal image references in a Hugo build.

Parses all HTML files under BUILD_DIR/blog/, extracts <img src>, <source srcset>,
and <img srcset> values, resolves them to filesystem paths, and reports any that
don't exist in the build output.

Usage: python3 scripts/check-blog-images.py BUILD_DIR
"""

import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote


class ImageRefExtractor(HTMLParser):
    """Extract image references from <img src> and <source>/<img> srcset attributes."""

    def __init__(self):
        super().__init__()
        self.refs: list[str] = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)

        if tag == "img" and attr_dict.get("src"):
            self.refs.append(attr_dict["src"])

        # srcset on <img> or <source> — comma-separated, each entry has URL + optional descriptor
        if tag in ("img", "source") and attr_dict.get("srcset"):
            for entry in attr_dict["srcset"].split(","):
                entry = entry.strip()
                if entry:
                    # First token is the URL; rest is size descriptor (e.g. "2x", "300w")
                    self.refs.append(entry.split()[0])


def extract_image_refs(html_file: Path) -> list[str]:
    parser = ImageRefExtractor()
    parser.feed(html_file.read_text(errors="replace"))
    return parser.refs


def is_internal_ref(ref: str) -> bool:
    """Return True if ref is a local path (not external or data URI)."""
    if ref.startswith(("http://", "https://", "data:", "//")):
        return False
    return bool(ref.split("#")[0].split("?")[0])


def resolve_ref(ref: str, source_file: Path, build_dir: Path) -> Path:
    path = unquote(ref.split("#")[0].split("?")[0])
    if path.startswith("/"):
        return (build_dir / path.lstrip("/")).resolve()
    else:
        return (source_file.parent / path).resolve()


def ref_to_url(ref: str, source_file: Path, build_dir: Path) -> str:
    """Convert a resolved ref back to a URL path for display."""
    resolved = resolve_ref(ref, source_file, build_dir)
    try:
        return "/" + str(resolved.relative_to(build_dir))
    except ValueError:
        return str(resolved)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/check-blog-images.py BUILD_DIR", file=sys.stderr)
        sys.exit(1)

    build_dir = Path(sys.argv[1]).resolve()
    blog_dir = build_dir / "blog"

    if not blog_dir.is_dir():
        print(f"Error: {blog_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    # source_page -> [(raw_ref, resolved_url)]
    broken: dict[str, list[tuple[str, str]]] = defaultdict(list)

    for html_file in sorted(blog_dir.rglob("*.html")):
        for ref in extract_image_refs(html_file):
            if not is_internal_ref(ref):
                continue
            resolved = resolve_ref(ref, html_file, build_dir)
            if not resolved.is_file():
                source = str(html_file.relative_to(build_dir))
                url = ref_to_url(ref, html_file, build_dir)
                broken[source].append((ref, url))

    total = 0
    for source in sorted(broken):
        print(source)
        for raw_ref, resolved_url in broken[source]:
            if raw_ref == resolved_url:
                print(f"  {raw_ref}")
            else:
                print(f"  {raw_ref}  ->  {resolved_url}")
            total += 1
        print()

    print(f"{total} broken image(s) in {len(broken)} file(s).")
    sys.exit(1 if total > 0 else 0)


if __name__ == "__main__":
    main()
