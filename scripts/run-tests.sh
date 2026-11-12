#!/usr/bin/env bash
# Run every scripts/test-*.py. Each test file is a PEP 723 uv script that
# declares its own dependencies, so each one runs in its own environment.
# Extra arguments are passed on to pytest, e.g. `./scripts/run-tests.sh -q -x`.

set -uo pipefail
cd "$(dirname "$0")/.."

failed=()
for test_file in scripts/test-*.py; do
  if [[ -n "${GITHUB_ACTIONS:-}" ]]; then echo "::group::$test_file"; else echo "==> $test_file"; fi
  if ! uv run --quiet --script "$test_file" "$@"; then
    failed+=("$test_file")
  fi
  if [[ -n "${GITHUB_ACTIONS:-}" ]]; then echo "::endgroup::"; fi
done

if ((${#failed[@]})); then
  echo
  echo "Failed test files:"
  printf '  %s\n' "${failed[@]}"
  exit 1
fi
echo
echo "All test files passed."
