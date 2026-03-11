---
description: R formatter and language server
github: posit-dev/air
image: air.png
color: "#F6C777"
languages:
- Rust
- R
latest_release: '2026-02-27T20:04:56+00:00'
people:
- Davis Vaughan
- Lionel Henry
- Barret Schloerke
- Garrick Aden-Buie
- Julia Silge
title: air
website: https://posit-dev.github.io/air/

include:
  languages:
  - R

external:  # updated automatically, do not edit
  description: R formatter and language server
  first_commit: '2024-10-26T18:24:07+00:00'
  forks: 29
  languages:
  - Rust
  last_updated: '2026-03-05T16:04:53.163156+00:00'
  latest_release: '2026-02-27T20:04:56+00:00'
  license: MIT
  people:
  - Davis Vaughan
  - Lionel Henry
  - Barret Schloerke
  - Garrick Aden-Buie
  - Julia Silge
  readme_image: docs/images/air.png
  repo: posit-dev/air
  stars: 391
  title: air
  website: https://posit-dev.github.io/air/
---

Air is an R code formatter and language server implementation written in Rust. It provides both command-line formatting tools and language server protocol support for code editors.

Air offers a fast, modern alternative to existing R formatting tools by leveraging Rust's performance and the Biome project's language-agnostic tooling infrastructure. It implements the tidyverse style guide and integrates with popular code editors through LSP support. The Rust implementation provides significant speed improvements over R-based formatters while maintaining compatibility with established R code style conventions.
