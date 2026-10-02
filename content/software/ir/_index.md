---
image: logo.svg
color: "#D44000"
description: ''
github: r-lib/ir
languages:
- Rust
latest_release: '2026-08-12T14:16:16+00:00'
people:
- Tomasz Kalinowski
- Charlie Gao
- Christophe Dervieux
- Jeroen Janssens
title: ir
website: https://r-lib.github.io/ir/

external:  # updated automatically, do not edit
  description: ''
  first_commit: '2026-06-02T17:39:53+00:00'
  forks: 2
  languages:
  - Rust
  last_updated: '2026-09-18T14:31:55.245348+00:00'
  latest_release: '2026-08-12T14:16:16+00:00'
  license: MIT
  people:
  - Tomasz Kalinowski
  - Charlie Gao
  - Christophe Dervieux
  - Jeroen Janssens
  repo: r-lib/ir
  stars: 65
  title: ir
  website: https://r-lib.github.io/ir/
---

`ir` is a command-line tool that runs self-describing R scripts and renders Quarto documents. You embed package requirements and R version constraints directly in the script's frontmatter, and `ir` resolves dependencies, prepares a cached library, and executes the file — no separate environment setup needed.

`ir` caches resolved environments aggressively, so repeated runs with the same requirements skip dependency resolution entirely. It supports reproducibility features like pinning package versions, selecting R versions via `rig`, and freezing CRAN/Bioconductor snapshots to a specific date with `exclude-newer`. It also provides `rx` for running package-bundled executables and a tool store for persistent launchers, making it practical for single-file workflows that don't warrant a full project directory.
