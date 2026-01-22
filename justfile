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

quarto-preview:
    uv run quarto preview

hugo-serve:
    @echo "Starting Hugo development server..."
    hugo server --buildDrafts --disableFastRender
