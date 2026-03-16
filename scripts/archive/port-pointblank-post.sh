#!/bin/bash
# Port a single pointblank blog post
# Usage: ./scripts/port-pointblank-post.sh <folder-name>
# Example:
#   ./scripts/port-pointblank-post.sh design-philosophy

set -e

FOLDER="$1"

if [ -z "$FOLDER" ]; then
  echo "Usage: $0 <folder-name>"
  echo "Example:"
  echo "  $0 design-philosophy"
  exit 1
fi

SOURCE="_external-sources/pointblank/docs/blog/$FOLDER"
DEST="content/blog/pointblank/$FOLDER"

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

# 2. Transform frontmatter in index.qmd
QMD_FILE="$DEST/index.qmd"
if [ -f "$QMD_FILE" ]; then
  TMP_FILE=$(mktemp)

  awk '
    BEGIN {
      in_fm = 0
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
          print "ported_from: pointblank"
          print "port_status: raw"
          added_porting = 1
        }
        in_fm = 0
        print
        next
      }
    }

    in_fm {
      # Skip html-table-processing, freeze, jupyter (not needed for Hugo)
      if (/^html-table-processing:/) { next }
      if (/^freeze:/) { next }
      if (/^jupyter:/) { next }

      # Transform author to people
      if (/^author:/) {
        # Extract author value, handle "Name1 and Name2" format
        author = $0
        sub(/^author:[ \t]*/, "", author)
        gsub(/["'"'"']/, "", author)

        print "people:"
        # Split on " and " to handle multiple authors
        n = split(author, authors, " and ")
        for (i = 1; i <= n; i++) {
          gsub(/^[ \t]+|[ \t]+$/, "", authors[i])  # trim whitespace
          print "  - " authors[i]
        }
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

# 3. Render with Quarto from content/blog/pointblank/ (using uv environment)
echo "  Rendering with Quarto..."
(cd content/blog/pointblank && uv run quarto render "$FOLDER/index.qmd" --to hugo-md 2>/dev/null) || {
  echo "  WARNING: Quarto render failed - may need manual intervention"
}
if [ -f "$DEST/index.md" ]; then
  echo "  Rendered index.md"
fi

# 4. Check for relative links that need fixing
MD_FILE="$DEST/index.md"
if [ -f "$MD_FILE" ]; then
  RELATIVE_LINKS=$(grep -oE '\]\(\.\./[^)]+\)|\]\(\.\./\.\./[^)]+\)' "$MD_FILE" 2>/dev/null | head -5 || true)
  if [ -n "$RELATIVE_LINKS" ]; then
    echo ""
    echo "  WARNING: Found relative links that need fixing:"
    echo "$RELATIVE_LINKS" | sed 's/^/    /'
    echo "  Update index.qmd, then re-render"
  fi
fi

echo ""
echo "Done: $FOLDER"
