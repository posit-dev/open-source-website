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
update-github-repos:
    ./scripts/update-github-repos.py

# Update software metadata from repos.toml
update-software-meta:
    ./scripts/update-software-meta.py

quarto-preview:
    uv run quarto preview

hugo-serve:
    @echo "Starting Hugo development server..."
    hugo server --buildDrafts --disableFastRender
