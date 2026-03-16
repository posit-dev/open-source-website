#!/bin/bash
# Fix index.html files that weren't processed by the porting script
# Converts author -> people, adds image/ported_from/port_status
# Usage: ./scripts/fix-html-files.sh

set -e

for FILE in $(find content/blog -name "index.html"); do
  # Skip if already has people field
  if grep -q "^people:" "$FILE"; then
    continue
  fi

  # Skip if no author field
  if ! grep -q "^author:" "$FILE"; then
    echo "Skipping (no author): $FILE"
    continue
  fi

  TMP_FILE=$(mktemp)

  awk '
    BEGIN { in_fm = 0; added = 0 }

    /^---$/ {
      if (in_fm == 0) {
        in_fm = 1
        print
        next
      } else {
        # Add porting metadata before closing ---
        if (!added) {
          print "image: thumbnail-wd.jpg"
          print "ported_from: tidyverse"
          print "port_status: raw"
          added = 1
        }
        in_fm = 0
        print
        next
      }
    }

    in_fm && /^author:/ {
      # Extract author name
      author = $0
      sub(/^author:[ \t]*/, "", author)
      gsub(/["'"'"']/, "", author)

      # Check for multiple authors (and/comma)
      if (author ~ /,| and /) {
        gsub(/, and /, ",", author)
        gsub(/ and /, ",", author)
        n = split(author, names, /,/)
        print "people:"
        for (i = 1; i <= n; i++) {
          gsub(/^[ \t]+|[ \t]+$/, "", names[i])
          if (names[i] != "") {
            print "  - " names[i]
          }
        }
      } else {
        print "people:"
        print "  - " author
      }
      next
    }

    { print }
  ' "$FILE" > "$TMP_FILE"

  mv "$TMP_FILE" "$FILE"
  echo "Fixed: $FILE"
done
