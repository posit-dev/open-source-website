#!/bin/bash
# Port a post from the AI blog (blogs.rstudio.com/ai) to this site
# Usage: ./scripts/port-ai-post.sh <folder-name>
# Example: ./scripts/port-ai-post.sh 2017-09-06-keras-for-r

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <folder-name>"
    echo "Example: $0 2017-09-06-keras-for-r"
    exit 1
fi

FOLDER_NAME="$1"
SOURCE_DIR="_external-sources/ai-blog/_posts/$FOLDER_NAME"
DEST_DIR="content/blog/ai/$FOLDER_NAME"

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory not found: $SOURCE_DIR"
    exit 1
fi

# Find HTML and Rmd files
HTML_FILE=$(find "$SOURCE_DIR" -maxdepth 1 -name "*.html" | head -1)
RMD_FILE=$(find "$SOURCE_DIR" -maxdepth 1 -name "*.Rmd" | head -1)

if [ -z "$HTML_FILE" ]; then
    echo "Error: No HTML file found in $SOURCE_DIR"
    echo "This post may need rendering first."
    exit 1
fi

if [ -z "$RMD_FILE" ]; then
    echo "Warning: No Rmd file found, will extract metadata from HTML"
fi

echo "Porting: $FOLDER_NAME"
echo "  HTML: $(basename "$HTML_FILE")"
[ -n "$RMD_FILE" ] && echo "  Rmd: $(basename "$RMD_FILE")"

# Create destination directory
mkdir -p "$DEST_DIR"

# Extract frontmatter from Rmd (or HTML if no Rmd)
if [ -n "$RMD_FILE" ]; then
    # Extract YAML frontmatter from Rmd
    FRONTMATTER=$(sed -n '/^---$/,/^---$/p' "$RMD_FILE" | sed '1d;$d')
else
    echo "Warning: Extracting metadata from HTML (limited)"
    FRONTMATTER=""
fi

# Parse frontmatter fields using grep/sed
get_field() {
    echo "$FRONTMATTER" | grep -E "^$1:" | sed "s/^$1: *//" | sed 's/^"//' | sed 's/"$//' | head -1
}

get_multiline_field() {
    # For fields like description that use | for multiline
    echo "$FRONTMATTER" | sed -n "/^$1:/,/^[a-z_]*:/p" | sed '1d;$d' | sed 's/^  //'
}

TITLE=$(get_field "title")
DESCRIPTION=$(echo "$FRONTMATTER" | sed -n '/^description:/,/^[a-z_]*:/p' | sed '1d;$d' | tr '\n' ' ' | sed 's/  */ /g' | sed 's/^ *//' | sed 's/ *$//')

# Handle date format MM-DD-YYYY -> YYYY-MM-DD
RAW_DATE=$(get_field "date")
if [[ "$RAW_DATE" =~ ^([0-9]{2})-([0-9]{2})-([0-9]{4})$ ]]; then
    DATE="${BASH_REMATCH[3]}-${BASH_REMATCH[1]}-${BASH_REMATCH[2]}"
else
    DATE="$RAW_DATE"
fi

# Extract categories (multiline YAML list)
CATEGORIES=$(echo "$FRONTMATTER" | sed -n '/^categories:/,/^[a-z_]*:/p' | grep '^ *- ' | sed 's/^ *- /  - /')

# Extract author info
# Author can be complex: name, url, affiliation, affiliation_url
AUTHOR_BLOCK=$(echo "$FRONTMATTER" | sed -n '/^author:/,/^[a-z_]*:/p' | sed '$d')
AUTHOR_NAME=$(echo "$AUTHOR_BLOCK" | grep '^ *- *name:' | sed 's/.*name: *//' | sed 's/^"//' | sed 's/"$//')
AUTHOR_URL=$(echo "$AUTHOR_BLOCK" | grep '^ *url:' | sed 's/.*url: *//')
AUTHOR_AFFILIATION=$(echo "$AUTHOR_BLOCK" | grep '^ *affiliation:' | grep -v 'affiliation_url' | sed 's/.*affiliation: *//')
AUTHOR_AFFILIATION_URL=$(echo "$AUTHOR_BLOCK" | grep '^ *affiliation_url:' | sed 's/.*affiliation_url: *//')

# Check if author has extra fields beyond just name
HAS_AUTHOR_METADATA=false
if [ -n "$AUTHOR_URL" ] || [ -n "$AUTHOR_AFFILIATION" ]; then
    HAS_AUTHOR_METADATA=true
fi

# Get preview path from frontmatter
PREVIEW_PATH=$(get_field "preview")

# Extract article content from HTML and convert to markdown
BASENAME=$(basename "$HTML_FILE" .html)
# First filter out the empty highlighting div from HTML before pandoc
CONTENT=$(sed -n '/<div class="d-article">/,/<\/d-article>/p' "$HTML_FILE" | \
    sed '/<pre class="sourceCode r distill-force-highlighting-css">/,/<\/pre>/d' | \
    pandoc -f html -t markdown --wrap=none 2>/dev/null | \
    grep -v '^:::' | \
    grep -v '^:::::' | \
    sed 's/\[\\\@\([^]]*\)\]{\.citation[^}]*}/@\1/g' | \
    sed -E 's/\[.*\]\{\.citation cites="([^"]*)"\}/[@\1]/g' | \
    sed 's/\[\]{#fig:[^}]*}//g' | \
    sed '/^``` {\.sourceCode/d' | \
    sed 's/^``` r$/```r/' | \
    sed '/^```$/{ N; /^```\n$/d; }' | \
    sed '/^\[\^[0-9]*\]:$/d')  # Remove orphaned footnote markers

# Build the frontmatter
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
        echo "author:"
        echo "  - name: $AUTHOR_NAME"
        [ -n "$AUTHOR_URL" ] && echo "    url: $AUTHOR_URL"
        [ -n "$AUTHOR_AFFILIATION" ] && echo "    affiliation: $AUTHOR_AFFILIATION"
        [ -n "$AUTHOR_AFFILIATION_URL" ] && echo "    affiliation_url: $AUTHOR_AFFILIATION_URL"
    fi
    echo "people:"
    echo "  - $AUTHOR_NAME"
    echo "image: thumbnail.png"
    echo "image-alt: \"$TITLE\""
    echo "ported_from: ai"
    echo "port_status: raw"
    echo "---"
    echo ""
    echo "$CONTENT"
} > "$DEST_DIR/index.md"

# Copy preview image as thumbnail
# First try the path from frontmatter, then fall back to common locations
PREVIEW_FILE=""
if [ -n "$PREVIEW_PATH" ] && [ -f "$SOURCE_DIR/$PREVIEW_PATH" ]; then
    PREVIEW_FILE="$SOURCE_DIR/$PREVIEW_PATH"
else
    for loc in "$SOURCE_DIR/preview.png" "$SOURCE_DIR/preview.jpg" "$SOURCE_DIR/images/preview.png" "$SOURCE_DIR/images/preview.jpg"; do
        if [ -f "$loc" ]; then
            PREVIEW_FILE="$loc"
            break
        fi
    done
fi

if [ -n "$PREVIEW_FILE" ]; then
    EXT="${PREVIEW_FILE##*.}"
    cp "$PREVIEW_FILE" "$DEST_DIR/thumbnail.$EXT"
    if [ "$EXT" = "jpg" ]; then
        sed -i '' 's/image: thumbnail.png/image: thumbnail.jpg/' "$DEST_DIR/index.md"
    fi
    echo "  Copied: $(basename "$PREVIEW_FILE") -> thumbnail.$EXT"
else
    echo "  Warning: No preview image found"
fi

# Copy source Rmd for reference
if [ -n "$RMD_FILE" ]; then
    cp "$RMD_FILE" "$DEST_DIR/"
    echo "  Copied: $(basename "$RMD_FILE")"
fi

# Copy images folder if it exists (many posts have images/ subfolder)
if [ -d "$SOURCE_DIR/images" ]; then
    cp -r "$SOURCE_DIR/images" "$DEST_DIR/"
    echo "  Copied: images/"
fi

# Copy figure files if they exist
FIGURES_DIR="$SOURCE_DIR/${BASENAME}_files/figure-html5"
if [ -d "$FIGURES_DIR" ]; then
    mkdir -p "$DEST_DIR/figures"
    cp "$FIGURES_DIR"/*.png "$DEST_DIR/figures/" 2>/dev/null || true
    echo "  Copied: figure files to figures/"
    # TODO: Update image references in content
fi

echo "Done: $DEST_DIR/index.md"
echo ""
echo "Next steps:"
echo "  1. Review the post at /blog/ai/$FOLDER_NAME/"
echo "  2. Twitter embeds: convert blockquotes to {{< tweet user=\"...\" id=\"...\" >}}"
echo "  3. Code output: add language hint to distinguish from input (e.g. \`\`\` vs \`\`\`r)"
echo "  4. References: may need reordering (footnotes sometimes appear before heading)"
echo "  5. Update image-alt with a proper description"
echo "  6. Check author name matches /people/ page"
