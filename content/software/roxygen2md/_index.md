---
image: logo.svg
color: "#447099"
description: Convert elements of roxygen documentation to markdown
github: r-lib/roxygen2md
languages:
- R
latest_release: '2024-02-18T17:50:05+00:00'
title: roxygen2md
website: https://roxygen2md.r-lib.org/

external:  # updated automatically, do not edit
  description: Convert elements of roxygen documentation to markdown
  first_commit: '2016-11-24T14:25:44+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-03-05T16:26:49.511127+00:00'
  latest_release: '2024-02-18T17:50:05+00:00'
  repo: r-lib/roxygen2md
  stars: 68
  title: roxygen2md
  website: https://roxygen2md.r-lib.org/
---

roxygen2md converts Rd (R documentation) syntax to Markdown in your package's roxygen2 documentation blocks. It automatically replaces Rd formatting commands like `\emph{}`, `\bold{}`, `\code{}`, `\link{}`, and `\url{}` with their Markdown equivalents.

The package enables modern Markdown documentation syntax in R packages while reducing manual conversion effort. It provides a staged conversion workflow for large packages, allowing you to isolate automated changes from those requiring review. The tool includes an RStudio addin interface and validation helpers to identify remaining Rd artifacts after conversion, making it practical for migrating existing package documentation.
