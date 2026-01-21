# List all available recipes
default:
    @just --list

quarto-preview:
    uv run quarto preview

hugo-serve:
    @echo "Starting Hugo development server..."
    hugo server --buildDrafts --disableFastRender
