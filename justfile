# List all available recipes
default:
    @just --list

# Install Node.js dependencies
install:
    npm install

# Start local development server (Hugo + Tailwind watcher)
dev:
    npm run dev

# Build Tailwind CSS
build-tailwind:
    npm run build-tailwind

# Build the site (Tailwind + Hugo)
build: build-tailwind
    hugo

# Build the search index with Pagefind
build-search:
    npm run build-search

# Update GitHub repository metadata
update-github-repos *args:
    ./scripts/update-github-repos.py {{args}}

# Update software frontmatter from github-repos.toml
update-software-frontmatter:
    ./scripts/update-software-frontmatter.py

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
