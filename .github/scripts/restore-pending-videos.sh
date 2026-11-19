#!/usr/bin/env bash
# Carry over the work of an unmerged sync PR into this run.
#
# The nightly sync starts from main. If last night's PR hasn't been merged
# yet, its new video directories and transcripts would otherwise be created
# (and paid for) again, and the nondeterministic formatting would rewrite
# the PR every night. So: take every file the PR branch *added* under
# content/resources/videos/ (relative to its merge base with main) and put
# it in the working tree, unless main has a file at that path by now.
# Files the PR modified are not restored; the scripts regenerate them.
#
# Usage: restore-pending-videos.sh [BRANCH] [BASE]
#   BRANCH defaults to automation/sync-videos, BASE to main.
# Needs a checkout with full history (actions/checkout fetch-depth: 0).

set -euo pipefail

branch="${1:-automation/sync-videos}"
base="${2:-main}"
prefix="content/resources/videos/"

if ! git ls-remote --exit-code --heads origin "$branch" >/dev/null 2>&1; then
  echo "No pending branch $branch; nothing to restore."
  exit 0
fi

git fetch --quiet --no-tags origin "$branch" "$base"
remote_branch="origin/$branch"
remote_base="origin/$base"

added=()
while IFS= read -r -d '' path; do
  added+=("$path")
done < <(git diff -z --name-only --diff-filter=A "$remote_base...$remote_branch" -- "$prefix")

restored=()
skipped=0
for path in ${added[@]+"${added[@]}"}; do
  if [[ -e "$path" ]]; then
    echo "  keep main's version: $path"
    skipped=$((skipped + 1))
    continue
  fi
  restored+=("$path")
done

if ((${#restored[@]})); then
  # --worktree only: leave the index alone, create-pull-request picks the
  # files up as changes.
  git restore --source="$remote_branch" --worktree -- "${restored[@]}"
  printf '  restored: %s\n' "${restored[@]}"
fi

echo "Restored ${#restored[@]} file(s) from $branch (${#added[@]} added there, $skipped already on $base)."
