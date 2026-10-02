#!/usr/bin/env bash
# Fail if Pagefind indexed suspiciously few pages.
#
# Pagefind only exits non-zero when it finds nothing at all. A partial index --
# Hugo emitting a fraction of the site, or a layout change dropping the
# data-pagefind-body markers -- exits 0 and silently ships broken search, so the
# page count is the signal worth checking.
set -euo pipefail

entry="public/pagefind/pagefind-entry.json"
min="${MIN_INDEXED_PAGES:-500}"

if [ ! -f "$entry" ]; then
    echo "::error::Pagefind index missing: $entry"
    exit 1
fi

pages="$(jq '[.languages[].page_count] | add // 0' "$entry")"

if [ "$pages" -lt "$min" ]; then
    echo "::error::Pagefind indexed $pages pages, expected at least $min."
    exit 1
fi

echo "Pagefind indexed $pages pages."
