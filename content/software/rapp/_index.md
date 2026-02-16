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

external:
  contributors:
  - t-kalinowski
  description: Build CLI applications in R
  first_commit: '2022-10-12T15:49:38+00:00'
  forks: 1
  languages:
  - R
  last_updated: '2026-02-13T14:17:20.653609+00:00'
  latest_release: '2025-12-14T18:49:06+00:00'
  license: NOASSERTION
  people:
  - Tomasz Kalinowski
  readme_image: man/figures/logo.png
  repo: r-lib/Rapp
  stars: 68
  title: Rapp
  website: ''
---

Rapp is an R package that transforms your R scripts into professional command-line applications with minimal effort. Serving as a modern alternative to Rscript, it automatically converts command-line arguments into R values through an intuitive syntax where simple R expressions define your CLI interface. Scalar assignments become options, NULL assignments create positional arguments, and boolean assignments enable toggle switches, all while maintaining the readability and simplicity that R developers expect.

What makes Rapp particularly valuable for data scientists and developers is its ability to bridge the gap between interactive R development and production-ready command-line tools. The package includes automatic help generation, support for subcommands and repeatable options, and the flexibility to annotate your interface with custom documentation using YAML comments. Whether you're packaging analytical scripts for colleagues, building data pipeline utilities, or distributing R-based tools to end users, Rapp streamlines the process of creating polished CLI applications that can be shared as standalone scripts or bundled within R packages.
