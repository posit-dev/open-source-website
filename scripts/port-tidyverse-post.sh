#!/bin/bash
# Port a single tidyverse.org blog post
# Usage: ./scripts/port-tidyverse-post.sh <slug>

set -e

SLUG="$1"

if [ -z "$SLUG" ]; then
  echo "Usage: $0 <slug>"
  echo "Example: $0 dplyr-performance"
  exit 1
fi

SOURCE="_external-sources/tidyverse.org/content/blog/$SLUG"
DEST="content/blog/$SLUG"

if [ ! -d "$SOURCE" ]; then
  echo "Error: Source not found: $SOURCE"
  exit 1
fi

if [ -d "$DEST" ]; then
  echo "Error: Destination already exists: $DEST"
  exit 1
fi

echo "Porting: $SLUG"

# 1. Copy the folder
cp -r "$SOURCE" "$DEST"
echo "  Copied to $DEST"

# Function to transform frontmatter
# Args: $1 = file, $2 = "md" or "rmd" (md removes more fields)
transform_frontmatter() {
  local FILE="$1"
  local TYPE="$2"
  local TMP_FILE=$(mktemp)

  awk -v type="$TYPE" '
    BEGIN {
      in_fm = 0
      skip_block = 0
      added = 0
    }

    /^---$/ {
      if (in_fm == 0) {
        in_fm = 1
        print
        next
      } else {
        # Add new fields before closing ---
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

    in_fm {
      # Skip output line (md only)
      if (type == "md" && /^output:/) { next }

      # Skip rmd_hash (md only)
      if (type == "md" && /^rmd_hash:/) { next }

      # Skip editor blocks (md only)
      if (type == "md" && /^editor:/) { skip_block = 1; next }
      if (type == "md" && /^editor_options:/) { skip_block = 1; next }

      # End skip_block when we hit a new top-level key
      if (skip_block && /^[a-zA-Z_]/ && !/^  /) { skip_block = 0 }

      # Skip indented lines in a block being skipped
      if (skip_block) { next }

      # Transform author to people
      if (/^author:/) {
        # Extract everything after "author:" and clean up
        author = $0
        sub(/^author:[ \t]*/, "", author)
        gsub(/["'"'"']/, "", author)
        print "people:"
        print "  - " author
        next
      }

      print
      next
    }

    { print }
  ' "$FILE" > "$TMP_FILE"

  mv "$TMP_FILE" "$FILE"
}

# 2. Transform index.md
MD_FILE="$DEST/index.md"
if [ -f "$MD_FILE" ]; then
  transform_frontmatter "$MD_FILE" "md"
  echo "  Updated $MD_FILE"
fi

# 3. Transform index.Rmd (keeps editor/editor_options)
RMD_FILE="$DEST/index.Rmd"
if [ -f "$RMD_FILE" ]; then
  transform_frontmatter "$RMD_FILE" "rmd"
  echo "  Updated $RMD_FILE"
fi

echo "Done: $SLUG"
