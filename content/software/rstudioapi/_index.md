---
description: Safely access RStudio's API (when available)
github: rstudio/rstudioapi
image: logo.png
languages:
- R
latest_release: '2024-10-16T22:39:47+00:00'
people:
- JJ Allaire
- Hadley Wickham
- Jenny Bryan
title: rstudioapi
website: http://rstudio.github.io/rstudioapi

external:
  description: Safely access RStudio's API (when available)
  first_commit: '2014-01-10T11:37:40+00:00'
  forks: 36
  languages:
  - R
  last_updated: '2026-02-17T11:16:17.768903+00:00'
  latest_release: '2024-10-16T22:39:47+00:00'
  license: NOASSERTION
  people:
  - JJ Allaire
  - Hadley Wickham
  - Jenny Bryan
  readme_image: man/figures/logo.png
  repo: rstudio/rstudioapi
  stars: 173
  title: rstudioapi
  website: http://rstudio.github.io/rstudioapi
---

The rstudioapi package provides safe, conditional access to the RStudio IDE API for CRAN packages. It allows R package developers to integrate with RStudio features without causing R CMD check failures.

The package includes wrapper functions to check RStudio availability and version, call IDE functions conditionally, and provide graceful fallbacks when RStudio is not running. This solves the problem of writing packages that can leverage RStudio features (like the viewer pane or document manipulation) while remaining compatible with other R environments. Functions use explicit namespace calls (rstudioapi::) rather than attaching to the search path, making dependencies clear and avoiding naming conflicts.
