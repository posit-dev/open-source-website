#!/bin/bash
# Port a single shiny.posit.co blog post
# Usage: ./scripts/port-shiny-post.sh <folder-name>
# Example:
#   ./scripts/port-shiny-post.sh shiny-on-hugging-face

set -e

FOLDER="$1"

if [ -z "$FOLDER" ]; then
  echo "Usage: $0 <folder-name>"
  echo "Example:"
  echo "  $0 shiny-on-hugging-face"
  exit 1
fi

SOURCE="_external-sources/shiny-dev-center/blog/posts/$FOLDER"
DEST="content/blog/shiny/$FOLDER"

if [ ! -d "$SOURCE" ]; then
  echo "Error: Source not found: $SOURCE"
  exit 1
fi

if [ -d "$DEST" ]; then
  echo "Error: Destination already exists: $DEST"
  exit 1
fi

echo "Porting: $FOLDER"

# 1. Copy the folder
cp -r "$SOURCE" "$DEST"
echo "  Copied to $DEST"

# 2. Transform frontmatter in index.qmd FIRST (so rendering preserves it)
QMD_FILE="$DEST/index.qmd"
if [ -f "$QMD_FILE" ]; then
  TMP_FILE=$(mktemp)

  awk '
    BEGIN {
      in_fm = 0
      skip_block = 0
      added_porting = 0
    }

    /^---$/ {
      if (in_fm == 0) {
        in_fm = 1
        print
        next
      } else {
        # Add porting fields before closing ---
        if (!added_porting) {
          print "ported_from: shiny"
          print "port_status: raw"
          added_porting = 1
        }
        in_fm = 0
        print
        next
      }
    }

    in_fm {
      # Skip twitter-card block
      if (/^twitter-card:/) { skip_block = 1; next }
      # Skip open-graph block
      if (/^open-graph:/) { skip_block = 1; next }
      # Skip format (we pass --to hugo-md on command line)
      if (/^format:/) { skip_block = 1; next }

      # End skip_block when we hit a new top-level key
      if (skip_block && /^[a-zA-Z_-]/ && !/^  /) { skip_block = 0 }

      # Skip indented lines in a block being skipped
      if (skip_block) { next }

      # Transform author to people (handles quoted and unquoted)
      if (/^author:/) {
        author = $0
        sub(/^author:[ \t]*/, "", author)
        gsub(/["'"'"']/, "", author)
        print "people:"
        print "  - " author
        next
      }

      # Transform imagealt to image-alt
      if (/^imagealt:/) {
        sub(/^imagealt:/, "image-alt:")
        print
        next
      }

      print
      next
    }

    { print }
  ' "$QMD_FILE" > "$TMP_FILE"

  mv "$TMP_FILE" "$QMD_FILE"
  echo "  Transformed frontmatter in index.qmd"
fi

# 3. Render with Quarto from content/blog/shiny/ (to use renv/uv environments)
# This will create index.md with the transformed frontmatter
echo "  Rendering with Quarto..."
(cd content/blog/shiny && quarto render "$FOLDER/index.qmd" --to hugo-md 2>/dev/null)
echo "  Rendered index.md"

# 4. Check for internal links that need fixing
MD_FILE="$DEST/index.md"
BROKEN_LINKS=$(grep -oE '\]\(/[^)]+\)' "$MD_FILE" 2>/dev/null | head -5 || true)
if [ -n "$BROKEN_LINKS" ]; then
  echo ""
  echo "  WARNING: Found site-relative links that may need fixing:"
  echo "$BROKEN_LINKS" | sed 's/^/    /'
  echo "  These should be converted to absolute URLs (e.g., https://shiny.posit.co/...)"
  echo "  Update index.qmd, then re-render"
fi

# Also check for converted relative links like ../../../../
RELATIVE_LINKS=$(grep -oE '\]\(\.\./[^)]+\)' "$MD_FILE" 2>/dev/null | head -5 || true)
if [ -n "$RELATIVE_LINKS" ]; then
  echo ""
  echo "  WARNING: Found relative links that need fixing:"
  echo "$RELATIVE_LINKS" | sed 's/^/    /'
  echo "  These should be converted to absolute URLs"
  echo "  Update index.qmd, then re-render"
fi

echo ""
echo "Done: $FOLDER"
