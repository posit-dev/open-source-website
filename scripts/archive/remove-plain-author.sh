#!/bin/bash
# Remove author field from posts where it doesn't contain markdown links

FILE="$1"

if [ -z "$FILE" ]; then
  echo "Usage: $0 <file>"
  exit 1
fi

# Check if file has author field without markdown
if grep -q "^author:" "$FILE"; then
  if ! grep -A1 "^author:" "$FILE" | grep -q "\["; then
    # No markdown - remove the author block
    TMP=$(mktemp)
    awk '
      /^author:/ { in_author=1; next }
      in_author && /^  - / { next }
      in_author && /^[a-zA-Z_]/ { in_author=0; print; next }
      in_author { next }
      { print }
    ' "$FILE" > "$TMP"
    mv "$TMP" "$FILE"
    echo "Removed author from: $FILE"
  fi
fi
