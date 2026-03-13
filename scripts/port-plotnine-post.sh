#!/bin/bash
# Port a single plotnine blog post
# Usage: ./scripts/port-plotnine-post.sh <year/month/folder-name>
# Example:
#   ./scripts/port-plotnine-post.sh 2024/11/version-0.14.0

set -e

FULL_PATH="$1"
FOLDER=$(basename "$FULL_PATH")

if [ -z "$FULL_PATH" ]; then
  echo "Usage: $0 <year/month/folder-name>"
  echo "Example:"
  echo "  $0 2024/11/version-0.14.0"
  exit 1
fi

SOURCE="_external-sources/plotnine.org/source/blog/$FULL_PATH"
DEST="content/blog/plotnine/$FOLDER"

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
          print "ported_from: plotnine"
          print "port_status: raw"
          added_porting = 1
        }
        in_fm = 0
        print
        next
      }
    }

    in_fm {
      # Skip format block (Quarto-specific)
      if (/^format:/) { skip_block = 1; next }
      # Skip aliases (handled differently in Hugo)
      if (/^aliases:/) { skip_block = 1; next }
      # Skip freeze, jupyter
      if (/^freeze:/) { next }
      if (/^jupyter:/) { next }

      # End skip_block when we hit a new top-level key
      if (skip_block && /^[a-zA-Z_-]/ && !/^  / && !/^-/) { skip_block = 0 }

      # Skip indented lines in a block being skipped
      if (skip_block) { next }

      # Transform author to people (if present)
      if (/^author:/) {
        author = $0
        sub(/^author:[ \t]*/, "", author)
        gsub(/["'"'"']/, "", author)

        print "people:"
        n = split(author, authors, " and ")
        for (i = 1; i <= n; i++) {
          gsub(/^[ \t]+|[ \t]+$/, "", authors[i])
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

# 3. Render with Quarto from content/blog/plotnine/ (using uv environment)
echo "  Rendering with Quarto..."
(cd content/blog/plotnine && uv run quarto render "$FOLDER/index.qmd" --to hugo-md 2>/dev/null) || {
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
