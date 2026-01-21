# List all available recipes
default:
    @just --list

# Start Hugo development server with live reload
hugo-serve:
    @echo "Starting Hugo development server..."
    hugo server --buildDrafts --disableFastRender
