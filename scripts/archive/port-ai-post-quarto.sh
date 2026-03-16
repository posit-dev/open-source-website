#!/bin/bash
# Port a post from the AI blog using Quarto rendering
# Usage: ./scripts/port-ai-post-quarto.sh <folder-name>
# Example: ./scripts/port-ai-post-quarto.sh 2020-09-29-introducing-torch-for-r

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <folder-name>"
    echo "Example: $0 2020-09-29-introducing-torch-for-r"
    exit 1
fi

FOLDER_NAME="$1"
SOURCE_DIR="_external-sources/ai-blog/_posts/$FOLDER_NAME"
DEST_DIR="content/blog/ai/$FOLDER_NAME"

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory not found: $SOURCE_DIR"
    exit 1
fi

# Find Rmd file
RMD_FILE=$(find "$SOURCE_DIR" -maxdepth 1 -name "*.Rmd" | head -1)

if [ -z "$RMD_FILE" ]; then
    echo "Error: No Rmd file found in $SOURCE_DIR"
    exit 1
fi

RMD_BASENAME=$(basename "$RMD_FILE")
MD_BASENAME="${RMD_BASENAME%.Rmd}.md"

echo "Porting: $FOLDER_NAME"
echo "  Source: $RMD_BASENAME"

# Step 1: Copy source files to destination (excluding Distill artifacts)
echo "  Copying files..."
mkdir -p "$DEST_DIR"
for item in "$SOURCE_DIR"/*; do
    name=$(basename "$item")
    # Skip Distill artifacts: *_files/, content/, *.html
    [[ "$name" == *_files ]] && continue
    [[ "$name" == "content" ]] && continue
    [[ "$name" == *.html ]] && continue
    cp -r "$item" "$DEST_DIR/"
done

# Step 2: Render with Quarto (from ai directory to activate renv)
echo "  Rendering with Quarto..."
cd "content/blog/ai"
if ! quarto render "$FOLDER_NAME/$RMD_BASENAME" --to hugo-md 2>&1 | grep -q "Output created"; then
    echo "Error: Quarto render failed"
    cd - > /dev/null
    exit 1
fi
cd - > /dev/null

# Check if rendering succeeded
MD_FILE="$DEST_DIR/$MD_BASENAME"
if [ ! -f "$MD_FILE" ]; then
    echo "Error: Rendered file not found: $MD_FILE"
    exit 1
fi

# Step 3: Transform frontmatter in place
echo "  Transforming frontmatter..."

# Extract frontmatter and body using awk (more reliable than sed for multiline)
FRONTMATTER=$(awk 'BEGIN{p=0} /^---$/{p++;next} p==1{print}' "$MD_FILE")
BODY=$(awk 'BEGIN{p=0} /^---$/{p++;next} p>=2{print}' "$MD_FILE")

# Helper to get field value
get_field() {
    echo "$FRONTMATTER" | grep -E "^$1:" | sed "s/^$1: *//" | sed "s/^['\"]//;s/['\"]$//" | head -1
}

TITLE=$(get_field "title")

# Handle date format MM-DD-YYYY -> YYYY-MM-DD
RAW_DATE=$(get_field "date")
if [[ "$RAW_DATE" =~ ^([0-9]{2})-([0-9]{2})-([0-9]{4})$ ]]; then
    DATE="${BASH_REMATCH[3]}-${BASH_REMATCH[1]}-${BASH_REMATCH[2]}"
else
    DATE="$RAW_DATE"
fi

# Extract author block (preserve full YAML structure for multiple authors)
AUTHOR_BLOCK=$(echo "$FRONTMATTER" | sed -n '/^author:/,/^[a-z_]*:/p' | sed '$d')

# Extract author names for people array
AUTHOR_NAMES=$(echo "$AUTHOR_BLOCK" | grep '^ *- *name:' | sed 's/.*name: *//' | sed "s/^['\"]//;s/['\"]$//")

# Check if any author has metadata beyond just name
HAS_AUTHOR_METADATA=false
if echo "$AUTHOR_BLOCK" | grep -q '^ *url:\|^ *affiliation:'; then
    HAS_AUTHOR_METADATA=true
fi

# Extract categories
CATEGORIES=$(echo "$FRONTMATTER" | sed -n '/^categories:/,/^[a-z_]*:/p' | grep '^ *- ' | sed 's/^ *- /  - /')

# Extract description (may be multiline with >)
DESCRIPTION=$(echo "$FRONTMATTER" | sed -n '/^description:/,/^[a-z_]*:/p' | sed '1d;$d' | tr '\n' ' ' | sed 's/  */ /g;s/^ *//;s/ *$//')

# Get preview path for thumbnail
PREVIEW_PATH=$(get_field "preview")

# Build new frontmatter and write file
{
    echo "---"
    echo "title: \"$TITLE\""
    if [ -n "$DESCRIPTION" ]; then
        echo "description: |"
        echo "  $DESCRIPTION"
    fi
    echo "date: $DATE"
    if [ -n "$CATEGORIES" ]; then
        echo "categories:"
        echo "$CATEGORIES"
    fi
    if [ "$HAS_AUTHOR_METADATA" = true ]; then
        echo "$AUTHOR_BLOCK"
    fi
    echo "people:"
    echo "$AUTHOR_NAMES" | while read -r name; do
        [ -n "$name" ] && echo "  - $name"
    done
    echo "image: thumbnail.png"
    echo "image-alt: \"$TITLE\""
    echo "ported_from: ai"
    echo "port_status: raw"
    echo "---"
    echo ""
    echo "$BODY"
} > "$MD_FILE"

# Step 4: Copy preview image as thumbnail
THUMB_EXT="png"
if [ -n "$PREVIEW_PATH" ] && [ -f "$DEST_DIR/$PREVIEW_PATH" ]; then
    EXT="${PREVIEW_PATH##*.}"
    cp "$DEST_DIR/$PREVIEW_PATH" "$DEST_DIR/thumbnail.$EXT"
    if [ "$EXT" = "jpg" ] || [ "$EXT" = "jpeg" ]; then
        sed -i '' 's/image: thumbnail.png/image: thumbnail.jpg/' "$MD_FILE"
        THUMB_EXT="jpg"
    fi
    echo "  Created: thumbnail.$EXT"
fi

# Step 5: Rename to index.Rmd and index.md for Hugo page bundles
mv "$DEST_DIR/$RMD_BASENAME" "$DEST_DIR/index.Rmd"
mv "$MD_FILE" "$DEST_DIR/index.md"
MD_FILE="$DEST_DIR/index.md"
echo "  Renamed to index.Rmd and index.md"

# Step 6: Clean up intermediate files
rm -f "$DEST_DIR"/*.html
rm -rf "$DEST_DIR"/*_files
echo "  Cleaned up intermediate files"

echo ""
echo "Done: $MD_FILE"
echo ""
echo "Files:"
ls "$DEST_DIR"
echo ""
echo "Next steps:"
echo "  1. Review the post at /blog/ai/$FOLDER_NAME/"
echo "  2. Update image-alt with a proper description"
echo "  3. Check author name matches /people/ page"
