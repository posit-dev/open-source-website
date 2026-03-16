#!/bin/bash
# Port a single education.rstudio.com blog post
# Usage: ./scripts/port-education-post.sh <folder-name>
# Example:
#   ./scripts/port-education-post.sh 2019-09-24-welcome

set -e

PATH_ARG="$1"

if [ -z "$PATH_ARG" ]; then
  echo "Usage: $0 <folder-name>"
  echo "Example:"
  echo "  $0 2019-09-24-welcome"
  exit 1
fi

SOURCE="_external-sources/education.rstudio.com/content/blog/$PATH_ARG"

# Keep original folder name structure under education/
DEST="content/blog/education/$PATH_ARG"

if [ ! -d "$SOURCE" ]; then
  echo "Error: Source not found: $SOURCE"
  exit 1
fi

if [ -d "$DEST" ]; then
  echo "Error: Destination already exists: $DEST"
  exit 1
fi

echo "Porting: $PATH_ARG"
echo "  -> $DEST"

# 1. Copy the folder (create parent dirs if needed)
mkdir -p "$(dirname "$DEST")"
cp -r "$SOURCE" "$DEST"
echo "  Copied to $DEST"

# 2. Find hero image (prefer -wd suffix, then thumbnail)
IMAGE=""
WD_IMAGE=$(ls "$DEST"/*-wd.jpg "$DEST"/*-wd.png 2>/dev/null | head -1)
if [ -n "$WD_IMAGE" ]; then
  IMAGE=$(basename "$WD_IMAGE")
  echo "  Found hero image: $IMAGE"
fi

# Function to transform frontmatter
# Args: $1 = file, $2 = "md" or "rmd", $3 = image filename (optional)
transform_frontmatter() {
  local FILE="$1"
  local TYPE="$2"
  local IMAGE="$3"
  local TMP_FILE=$(mktemp)

  awk -v type="$TYPE" -v image="$IMAGE" '
    BEGIN {
      in_fm = 0
      in_author = 0
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
          if (image != "") {
            print "image: " image
          }
          print "ported_from: education"
          print "port_status: raw"
          added = 1
        }
        in_fm = 0
        print
        next
      }
    }

    in_fm {
      # Transform author: to people:
      if (/^author:/) {
        print "people:"
        in_author = 1
        next
      }

      # Handle author array items
      if (in_author && /^  - /) {
        print
        next
      }

      # End of author block
      if (in_author && /^[a-zA-Z_]/) {
        in_author = 0
      }

      print
      next
    }

    { print }
  ' "$FILE" > "$TMP_FILE"

  mv "$TMP_FILE" "$FILE"
}

# 3. Transform index.markdown
MD_FILE="$DEST/index.markdown"
if [ -f "$MD_FILE" ]; then
  transform_frontmatter "$MD_FILE" "md" "$IMAGE"
  echo "  Updated $MD_FILE"
fi

# 4. Transform index.Rmarkdown
RMD_FILE="$DEST/index.Rmarkdown"
if [ -f "$RMD_FILE" ]; then
  transform_frontmatter "$RMD_FILE" "rmd" "$IMAGE"
  echo "  Updated $RMD_FILE"
fi

# 5. Also handle index.md if present (some posts may have this)
MD_FILE2="$DEST/index.md"
if [ -f "$MD_FILE2" ]; then
  transform_frontmatter "$MD_FILE2" "md" "$IMAGE"
  echo "  Updated $MD_FILE2"
fi

echo "Done: $PATH_ARG -> $DEST"
echo ""
echo "NOTE: Check author names - education posts often use first names only."
echo "      You may need to expand to full names (e.g., 'Alison' -> 'Alison Hill')"
