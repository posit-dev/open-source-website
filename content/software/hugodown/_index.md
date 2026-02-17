---
description: Make websites with hugo and RMarkdown
github: r-lib/hugodown
image: logo.png
languages:
- R
people:
- Hadley Wickham
- JJ Allaire
- Jenny Bryan
- Davis Vaughan
title: hugodown
website: https://hugodown.r-lib.org

external:
  description: Make websites with hugo and RMarkdown
  first_commit: '2020-05-18T14:26:06+00:00'
  forks: 23
  languages:
  - R
  last_updated: '2026-02-17T11:36:10.923708+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - JJ Allaire
  - Jenny Bryan
  - Davis Vaughan
  readme_image: man/figures/logo.png
  repo: r-lib/hugodown
  stars: 163
  title: hugodown
  website: https://hugodown.r-lib.org
---

hugodown is an R package that transforms RMarkdown (.Rmd) files into markdown (.md) files specifically for Hugo static websites. It handles the R-to-markdown conversion while leaving Hugo to handle markdown-to-HTML rendering.

The package solves workflow challenges by only re-running R code when explicitly requested through knitting, making it practical for long-running analyses and multi-contributor blogs. It pins local previews to specific Hugo versions to prevent version conflicts, provides out-of-the-box support for HTML widgets and syntax highlighting, and includes helper functions for starting Hugo servers and creating new posts. Unlike blogdown, it maintains a strict separation between R processing and Hugo site generation.
