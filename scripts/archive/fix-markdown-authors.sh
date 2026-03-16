#!/bin/bash
# Fix markdown author links in education posts
# Transforms:
#   people:
#     - '[Name](URL)'
# To:
#   author:
#     - '[Name](URL)'
#   people:
#     - Name

set -e

FILE="$1"

if [ -z "$FILE" ]; then
  echo "Usage: $0 <file>"
  exit 1
fi

TMP_FILE=$(mktemp)

awk '
BEGIN {
  in_fm = 0
  in_people = 0
  people_count = 0
}

/^---$/ {
  if (in_fm == 0) {
    in_fm = 1
    print
    next
  } else {
    # End of frontmatter - output author block if we collected any
    if (people_count > 0) {
      print "author:"
      for (i = 1; i <= people_count; i++) {
        print "  - " people_orig[i]
      }
      print "people:"
      for (i = 1; i <= people_count; i++) {
        print "  - " people_name[i]
      }
    }
    in_fm = 0
    in_people = 0
    print
    next
  }
}

in_fm && /^people:/ {
  in_people = 1
  next
}

in_fm && in_people && /^  - / {
  people_count++
  # Store original value (remove leading "  - ")
  orig = $0
  sub(/^  - /, "", orig)
  # Remove surrounding quotes if present
  gsub(/^["'"'"']|["'"'"']$/, "", orig)
  people_orig[people_count] = "\"" orig "\""

  # Extract name from markdown link [Name](URL)
  name = orig
  # Check if it looks like a markdown link
  if (index(orig, "[") == 1 && index(orig, "](") > 0) {
    # Extract text between [ and ]
    start = 2
    end = index(orig, "](") - 1
    name = substr(orig, start, end - start + 1)
  }
  people_name[people_count] = name
  next
}

in_fm && in_people && /^[a-zA-Z_]/ {
  # New field - end of people block, output collected data
  if (people_count > 0) {
    print "author:"
    for (i = 1; i <= people_count; i++) {
      print "  - " people_orig[i]
    }
    print "people:"
    for (i = 1; i <= people_count; i++) {
      print "  - " people_name[i]
    }
    people_count = 0
  }
  in_people = 0
  print
  next
}

{ print }
' "$FILE" > "$TMP_FILE"

mv "$TMP_FILE" "$FILE"
