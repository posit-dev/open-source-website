---
description: Build CLI applications in R
github: r-lib/Rapp
image: logo.png
languages:
- R
latest_release: '2025-12-14T18:49:06+00:00'
people:
- Tomasz Kalinowski
title: Rapp
website: ''

external:  # updated automatically, do not edit
  description: Build CLI applications in R
  first_commit: '2022-10-12T15:49:38+00:00'
  forks: 1
  languages:
  - R
  last_updated: '2026-02-24T09:26:36.701568+00:00'
  latest_release: '2025-12-14T18:49:06+00:00'
  license: NOASSERTION
  people:
  - Tomasz Kalinowski
  readme_image: man/figures/logo.png
  repo: r-lib/Rapp
  stars: 77
  title: Rapp
  website: ''
---

Rapp is a drop-in replacement for Rscript that automatically parses command-line arguments into R values, making it straightforward to build polished CLI applications from simple R scripts. It converts standard R patterns like scalar assignments, NULL assignments, and switch statements into command-line options, positional arguments, and commands without requiring explicit argument parsing libraries.

The package enables seamless transition from interactive REPL development to command-line execution by recognizing R expression patterns at the top level of scripts. It handles option parsing, type coercion, automatic help generation, nested commands with their own options, and repeatable arguments through familiar R syntax. Rapp works cross-platform including Windows, supports distribution via R packages through the exec/ directory, and allows interactive development with Rapp::run() for debugging.
