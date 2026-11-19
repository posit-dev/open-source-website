set positional-arguments

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

# Create software directories for repos in github-repos.toml that don't exist yet
create-new-software *args:
    ./scripts/create-new-software.py {{args}}

# Download images from GitHub READMEs for software without an image
download-software-images *args:
    ./scripts/download-software-images.py {{args}}

# Download README files from GitHub for all software entries
download-software-readmes *args:
    ./scripts/download-software-readmes.py {{args}}

# Summarize software README files using Claude CLI
summarize-software-readmes *args:
    ./scripts/summarize-software-readmes.py {{args}}

# Extract dominant colors from software logos into frontmatter
extract-software-colors:
    ./scripts/extract-software-colors.py

# Create hex-placeholder logos for software projects missing an image
create-hex-logos:
    ./scripts/create-hex-logos.py

# Fetch video metadata from YouTube into data/videos.toml (pass --refresh-stats to update view counts)
update-youtube-videos *args:
    ./scripts/update-youtube-videos.py "$@"

# Sync video entries from data/videos.toml into content
sync-videos *args:
    ./scripts/sync-videos.py "$@"

# Sync courses and learning paths from Posit Academy (needs SKILLJAR_API_KEY)
sync-courses *args:
    ./scripts/sync-courses.py {{args}}

# Download audio and transcribe new videos with Whisper (needs OPENAI_API_KEY)
transcribe *args:
    ./scripts/transcribe.py "$@"

# Format VTT transcriptions into HTML using the Anthropic API
format-transcriptions *args:
    ./scripts/format-transcriptions.py "$@"

# Run the whole video pipeline locally (fallback for the nightly workflow), e.g. `just update-videos 5 chrome`
update-videos limit="15" browser="":
    #!/usr/bin/env bash
    set -euo pipefail
    # Exit code 2 means some videos failed; keep going and fix them later.
    step() {
        "$@" && return 0
        status=$?
        if [ "$status" -eq 2 ]; then
            echo "⚠ $1 finished with errors (exit code 2); continuing" >&2
            return 0
        fi
        echo "✗ $1 failed (exit code $status); stopping" >&2
        exit "$status"
    }
    cookies=()
    if [ -n "{{ browser }}" ]; then cookies=(--cookies-from-browser "{{ browser }}"); fi
    step ./scripts/update-youtube-videos.py
    step ./scripts/sync-videos.py
    step ./scripts/transcribe.py --limit "{{ limit }}" ${cookies[@]+"${cookies[@]}"}
    step ./scripts/format-transcriptions.py --limit "{{ limit }}"

# Run the tests of the Python scripts (extra arguments go to pytest)
test *args:
    ./scripts/run-tests.sh "$@"

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

# Create or update a person profile in content/people/
people-profile *args:
    ./scripts/people-profile.py "$@"
