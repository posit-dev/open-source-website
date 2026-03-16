#!/bin/bash
# Fix people field that has multiple names joined by "and"
# Usage: ./scripts/fix-people.sh <path-to-index.md>
# Example: ./scripts/fix-people.sh content/blog/2025/air-0-7-0/index.md

set -e

FILE="$1"

if [ -z "$FILE" ]; then
  echo "Usage: $0 <path-to-index.md>"
  exit 1
fi

if [ ! -f "$FILE" ]; then
  echo "Error: File not found: $FILE"
  exit 1
fi

TMP_FILE=$(mktemp)

awk '
  BEGIN { in_fm = 0; in_people = 0 }

  /^---$/ {
    if (in_fm == 0) {
      in_fm = 1
    } else {
      in_fm = 0
      in_people = 0
    }
    print
    next
  }

  in_fm && /^people:$/ {
    in_people = 1
    print
    next
  }

  in_fm && in_people && /^  - / {
    # Extract the name(s) after "  - "
    line = $0
    sub(/^  - /, "", line)

    # Check if it contains " and " or ", "
    if (line ~ /,| and /) {
      # Replace ", and " with "," and " and " with ","
      gsub(/, and /, ",", line)
      gsub(/ and /, ",", line)

      # Split by ","
      n = split(line, names, /,/)
      for (i = 1; i <= n; i++) {
        # Trim whitespace
        gsub(/^[ \t]+|[ \t]+$/, "", names[i])
        if (names[i] != "") {
          print "  - " names[i]
        }
      }
      next
    }
    print
    next
  }

  in_fm && in_people && /^[^ ]/ {
    # New top-level key, exit people block
    in_people = 0
  }

  { print }
' "$FILE" > "$TMP_FILE"

mv "$TMP_FILE" "$FILE"
echo "Fixed: $FILE"
