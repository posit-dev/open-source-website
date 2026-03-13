#!/bin/bash
# Port a blog post from quarto-web to this site
# Usage: ./scripts/port-quarto-post.sh <post-folder>
# Example: ./scripts/port-quarto-post.sh 2022-02-17-advanced-layout

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <post-folder>"
    echo "Example: $0 2022-02-17-advanced-layout"
    exit 1
fi

POST="$1"
SOURCE_DIR="_external-sources/quarto-web/docs/blog/posts/$POST"
FREEZE_DIR="_external-sources/quarto-web/_freeze/docs/blog/posts/$POST/index"
DEST_DIR="content/blog/quarto/$POST"

# Check source exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory not found: $SOURCE_DIR"
    exit 1
fi

# Create destination
mkdir -p "$DEST_DIR"

# Copy all files from source (qmd, images, etc.)
echo "Copying source files..."
cp -r "$SOURCE_DIR"/* "$DEST_DIR/"

# Check if freeze exists
if [ -f "$FREEZE_DIR/execute-results/html.json" ]; then
    echo "Found freeze file, extracting markdown..."

    # Extract markdown from freeze using Python
    python3 - "$FREEZE_DIR/execute-results/html.json" "$DEST_DIR" <<'PYTHON'
import json
import sys
import shutil
from pathlib import Path

freeze_file = Path(sys.argv[1])
dest_dir = Path(sys.argv[2])

with open(freeze_file) as f:
    data = json.load(f)

markdown = data["result"]["markdown"]
supporting = data["result"].get("supporting", [])

# Write extracted markdown
md_file = dest_dir / "index.md"
with open(md_file, "w") as f:
    f.write(markdown)
print(f"  Extracted markdown: {len(markdown):,} chars -> {md_file}")

# Copy supporting files (figure-html, etc.)
freeze_parent = freeze_file.parent.parent  # Go up from execute-results/html.json
for subdir in ["figure-html", "libs"]:
    src = freeze_parent / subdir
    if src.exists():
        dest = dest_dir / "index_files" / subdir
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(src, dest)
        print(f"  Copied: {subdir} -> index_files/{subdir}")
PYTHON

    # Convert to hugo-md format
    echo "Converting to hugo-md..."
    (cd "$DEST_DIR" && quarto render index.md --to hugo-md 2>/dev/null)

    # Clean up intermediate files
    rm -f "$DEST_DIR/index.md"
    if [ -f "$DEST_DIR/index-commonmark.md" ]; then
        mv "$DEST_DIR/index-commonmark.md" "$DEST_DIR/index.md"
    fi
else
    echo "No freeze file - will render from .qmd"

    # Transform .qmd frontmatter BEFORE rendering
    if [ -f "$DEST_DIR/index.qmd" ]; then
        echo "Transforming .qmd frontmatter..."
        python3 - "$DEST_DIR/index.qmd" <<'PYTHON'
import sys
import re
import yaml
from pathlib import Path

qmd_file = Path(sys.argv[1])
content = qmd_file.read_text()

match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
if not match:
    print("  Warning: Could not parse frontmatter")
    sys.exit(0)

fm_text, body = match.groups()

# Parse YAML
try:
    fm = yaml.safe_load(fm_text)
except:
    print("  Warning: Could not parse YAML")
    sys.exit(0)

if fm is None:
    fm = {}

# Transform author -> people
if 'author' in fm:
    author = fm.pop('author')
    people = []
    if isinstance(author, str):
        people = [author]
    elif isinstance(author, list):
        for a in author:
            if isinstance(a, str):
                people.append(a)
            elif isinstance(a, dict) and 'name' in a:
                people.append(a['name'])
    if people:
        fm['people'] = people

# Fix date format (M/D/YYYY -> YYYY-MM-DD)
if 'date' in fm:
    date_str = str(fm['date'])
    parts = date_str.split('/')
    if len(parts) == 3:
        month, day, year = parts
        fm['date'] = f"{year}-{int(month):02d}-{int(day):02d}"

# Add porting metadata
fm['ported_from'] = 'quarto'
fm['port_status'] = 'raw'

# Write back with proper YAML formatting
new_fm = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
qmd_file.write_text(f'---\n{new_fm}---\n{body}')
print("  .qmd frontmatter transformed")
PYTHON
    fi

    # Render to hugo-md
    echo "Rendering to hugo-md..."
    (cd "$DEST_DIR" && quarto render index.qmd --to hugo-md)

    # Rename output
    if [ -f "$DEST_DIR/index-commonmark.md" ]; then
        mv "$DEST_DIR/index-commonmark.md" "$DEST_DIR/index.md"
    fi
fi

# Transform frontmatter in index.md (if exists, for freeze path)
if [ -f "$DEST_DIR/index.md" ]; then
    echo "Transforming frontmatter..."
    python3 - "$DEST_DIR/index.md" <<'PYTHON'
import sys
import re
from pathlib import Path

md_file = Path(sys.argv[1])
content = md_file.read_text()

# Split frontmatter and body
match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
if not match:
    print("  Warning: Could not parse frontmatter")
    sys.exit(0)

frontmatter, body = match.groups()

# Transform author -> people
def transform_author(fm):
    # Handle "author: Name" -> "people:\n  - Name"
    fm = re.sub(r'^author:\s*([^\n\[]+)$', r'people:\n  - \1', fm, flags=re.MULTILINE)
    # Handle author list
    fm = re.sub(r'^author:\s*\n', r'people:\n', fm, flags=re.MULTILINE)
    return fm

frontmatter = transform_author(frontmatter)

# Fix date format (M/D/YYYY -> YYYY-MM-DD)
def fix_date(m):
    date_str = m.group(1).strip('"\'')
    parts = date_str.split('/')
    if len(parts) == 3:
        month, day, year = parts
        return f'date: "{year}-{int(month):02d}-{int(day):02d}"'
    return m.group(0)

frontmatter = re.sub(r'^date:\s*(.+)$', fix_date, frontmatter, flags=re.MULTILINE)

# Add porting metadata if not present
if 'ported_from:' not in frontmatter:
    frontmatter += '\nported_from: quarto'
if 'port_status:' not in frontmatter:
    frontmatter += '\nport_status: raw'

# Remove quarto-specific fields that don't apply
for field in ['reference-location', 'citation-location', 'freeze', 'format']:
    frontmatter = re.sub(rf'^{field}:.*\n?', '', frontmatter, flags=re.MULTILINE)

# Write back
md_file.write_text(f'---\n{frontmatter}\n---\n{body}')
print("  Frontmatter transformed")
PYTHON
fi

# Also transform frontmatter in .qmd
if [ -f "$DEST_DIR/index.qmd" ]; then
    echo "Transforming .qmd frontmatter..."
    python3 - "$DEST_DIR/index.qmd" <<'PYTHON'
import sys
import re
from pathlib import Path

qmd_file = Path(sys.argv[1])
content = qmd_file.read_text()

# Split frontmatter and body
match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
if not match:
    print("  Warning: Could not parse frontmatter")
    sys.exit(0)

frontmatter, body = match.groups()

# Transform author -> people
def transform_author(fm):
    fm = re.sub(r'^author:\s*([^\n\[]+)$', r'people:\n  - \1', fm, flags=re.MULTILINE)
    fm = re.sub(r'^author:\s*\n', r'people:\n', fm, flags=re.MULTILINE)
    return fm

frontmatter = transform_author(frontmatter)

# Fix date format
def fix_date(m):
    date_str = m.group(1).strip('"\'')
    parts = date_str.split('/')
    if len(parts) == 3:
        month, day, year = parts
        return f'date: "{year}-{int(month):02d}-{int(day):02d}"'
    return m.group(0)

frontmatter = re.sub(r'^date:\s*(.+)$', fix_date, frontmatter, flags=re.MULTILINE)

# Add porting metadata
if 'ported_from:' not in frontmatter:
    frontmatter += '\nported_from: quarto'
if 'port_status:' not in frontmatter:
    frontmatter += '\nport_status: raw'

qmd_file.write_text(f'---\n{frontmatter}\n---\n{body}')
print("  .qmd frontmatter transformed")
PYTHON
fi

echo ""
echo "Done! Post ported to: $DEST_DIR"
echo ""
echo "Next steps:"
echo "  1. Check the post: hugo server, then visit /blog/quarto/$POST/"
echo "  2. Fix any broken links (especially /docs/... links to quarto.org)"
echo "  3. Update port_status when ready"
