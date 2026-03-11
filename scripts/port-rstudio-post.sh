#!/bin/bash
# Port a single rstudio.com blog post
# Usage: ./scripts/port-rstudio-post.sh <path>
# Examples:
#   ./scripts/port-rstudio-post.sh 2011-02-27-about-the-rstudio-project
#   ./scripts/port-rstudio-post.sh 2012-11-08-introducing-shiny.md

set -e

PATH_ARG="$1"

if [ -z "$PATH_ARG" ]; then
  echo "Usage: $0 <path>"
  echo "Examples:"
  echo "  $0 2011-02-27-about-the-rstudio-project"
  echo "  $0 2012-11-08-introducing-shiny.md"
  exit 1
fi

SOURCE_BASE="_external-sources/rstudio.com/content/blog"

# Determine if source is a folder or flat file
if [ -d "$SOURCE_BASE/$PATH_ARG" ]; then
  # Folder-based post
  SOURCE="$SOURCE_BASE/$PATH_ARG"
  DEST="content/blog/rstudio/$PATH_ARG"
  IS_FLAT=false
elif [ -f "$SOURCE_BASE/$PATH_ARG" ]; then
  # Flat .md file - convert to folder
  BASENAME=$(basename "$PATH_ARG" .md)
  SOURCE="$SOURCE_BASE/$PATH_ARG"
  DEST="content/blog/rstudio/$BASENAME"
  IS_FLAT=true
else
  echo "Error: Source not found: $SOURCE_BASE/$PATH_ARG"
  exit 1
fi

if [ -d "$DEST" ]; then
  echo "Error: Destination already exists: $DEST"
  exit 1
fi

echo "Porting: $PATH_ARG"

# 1. Copy/create the folder
mkdir -p "$DEST"
if [ "$IS_FLAT" = true ]; then
  cp "$SOURCE" "$DEST/index.md"
  echo "  Converted flat file to $DEST/index.md"
else
  cp -r "$SOURCE/"* "$DEST/"
  echo "  Copied folder to $DEST"
fi

# 2. Find thumbnail image if present
IMAGE=""
if [ -f "$DEST/thumbnail.png" ]; then
  IMAGE="thumbnail.png"
elif [ -f "$DEST/thumbnail.jpg" ]; then
  IMAGE="thumbnail.jpg"
fi

# Function to transform frontmatter
# Args: $1 = file, $2 = image filename (optional)
transform_frontmatter() {
  local FILE="$1"
  local IMAGE="$2"
  local TMP_FILE=$(mktemp)

  awk -v image="$IMAGE" '
    BEGIN {
      in_fm = 0
      in_authors = 0
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
          print "ported_from: rstudio"
          print "port_status: raw"
          added = 1
        }
        in_fm = 0
        print
        next
      }
    }

    in_fm {
      # Transform authors: to people:
      if (/^authors:/) {
        print "people:"
        in_authors = 1
        next
      }

      # Handle authors array items
      if (in_authors && /^- /) {
        print "  " $0
        next
      }

      # End of authors block
      if (in_authors && /^[a-zA-Z_]/) {
        in_authors = 0
      }

      # Skip authormeta (internal linking slug)
      if (/^authormeta:/) {
        # Skip this line and any following array items
        in_authormeta = 1
        next
      }
      if (in_authormeta && /^- /) {
        next
      }
      if (in_authormeta && /^[a-zA-Z_]/) {
        in_authormeta = 0
      }

      print
      next
    }

    { print }
  ' "$FILE" > "$TMP_FILE"

  mv "$TMP_FILE" "$FILE"
}

# 3. Transform index.md
MD_FILE="$DEST/index.md"
if [ -f "$MD_FILE" ]; then
  transform_frontmatter "$MD_FILE" "$IMAGE"
  echo "  Updated $MD_FILE"
fi

echo "Done: $PATH_ARG -> $DEST"
