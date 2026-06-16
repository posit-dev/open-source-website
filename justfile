# List all available recipes
default:
    @just --list

clean:
    rm -rf public

# Install Node.js dependencies
install:
    yarn install

# Start local development server (Hugo + Tailwind watcher)
# Pass "all" to also include expired/future content with the production environment
dev mode="": build-tailwind
    #!/usr/bin/env bash
    port=1313
    while lsof -i :$port >/dev/null 2>&1; do
        port=$((port + 1))
    done
    hugo_flags="-D --disableFastRender -p $port"
    if [ "{{ mode }}" = "all" ]; then
        hugo_flags="-DEF --disableFastRender -p $port -e production"
    fi
    ( sleep 2 && open "http://localhost:$port" ) &
    yarn dev-tailwind & hugo server $hugo_flags

# Build Tailwind CSS
build-tailwind:
    yarn build-tailwind

# Build the site (Tailwind + Hugo)
build: build-tailwind
    hugo

# Build the search index with Pagefind
build-search:
    yarn build-search

# Update GitHub repository metadata
update-github-repos *args:
    ./scripts/update-github-repos.py {{args}}

# Update software frontmatter from github-repos.toml
update-software-frontmatter:
    ./scripts/update-software-frontmatter.py

# Update videos
update-youtube-videos:
    ./scripts/update-youtube-videos.py

# Sync video entries from data/videos.toml into content
sync-videos:
    ./scripts/sync-videos.py

download-youtube-audio *args:
    ./scripts/download-youtube-audio.py {{args}}

transcribe:
    ./scripts/transcribe.py

# Format VTT transcriptions into HTML using the Anthropic API
format-transcriptions *args:
    ./scripts/format-transcriptions.py {{args}}

quarto-preview:
    uv run quarto preview

hugo-serve:
    @echo "Starting Hugo development server..."
    hugo server --buildDrafts --disableFastRender

# Import cheatsheets from rstudio.github.io/cheatsheets
import-cheatsheets:
    ./scripts/import-cheatsheets.py

# Create thumbnails for a cheatsheet PDF
create-cheatsheet-thumbnails *args:
    ./scripts/create-cheatsheet-thumbnails.py {{args}}

# Resize oversized images in content/ to reduce Hugo memory usage
resize-images *args:
    ./scripts/resize-images.py {{args}}
