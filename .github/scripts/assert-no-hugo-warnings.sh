#!/usr/bin/env bash
# Fail if a Hugo build log contains WARN/ERROR lines that aren't allowlisted.
#
# Usage: assert-no-hugo-warnings.sh <hugo-build.log>
set -euo pipefail

log="${1:?usage: $0 <hugo-build.log>}"
allowlist="$(dirname "$0")/../hugo-warning-allowlist.txt"

if [ ! -f "$log" ]; then
    echo "::error::Build log not found: $log"
    exit 1
fi

# Hugo prefixes diagnostics with "WARN" / "ERROR". Strip the log level and any
# leading whitespace so allowlist entries can be written as the bare message.
warnings="$(grep -E '^(WARN|ERROR)' "$log" || true)"

if [ -z "$warnings" ]; then
    echo "No Hugo warnings or errors."
    exit 0
fi

# Drop comments and blank lines from the allowlist. A blank line would be a
# fixed-string pattern matching every line, silently suppressing everything.
patterns="$(mktemp)"
trap 'rm -f "$patterns"' EXIT
if [ -f "$allowlist" ]; then
    grep -vE '^[[:space:]]*(#|$)' "$allowlist" > "$patterns" || true
fi

unexpected="$(printf '%s\n' "$warnings" | grep -vFf "$patterns" || true)"

if [ -n "$unexpected" ]; then
    count="$(printf '%s\n' "$unexpected" | wc -l | tr -d ' ')"
    printf '%s\n' "$unexpected"
    echo "::error::Hugo emitted $count unexpected warning/error line(s); see above."
    echo "Fix them, or add the message to $(basename "$allowlist") with a comment explaining why."
    exit 1
fi

echo "All Hugo warnings are allowlisted."
