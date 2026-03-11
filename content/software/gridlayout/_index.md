---
description: Package for setting up CSS grid layouts in Shiny apps or RMarkdown documents
github: rstudio/gridlayout
image: geyser_demo.png
color: "#26405F"
languages:
- HTML
people:
- Nick Strayer
title: gridlayout
website: https://rstudio.github.io/gridlayout

external:  # updated automatically, do not edit
  description: Package for setting up CSS grid layouts in Shiny apps or RMarkdown
    documents
  first_commit: '2021-02-17T21:57:27+00:00'
  forks: 4
  languages:
  - HTML
  last_updated: '2026-03-05T16:16:55.085459+00:00'
  license: NOASSERTION
  people:
  - Nick Strayer
  readme_image: man/figures/geyser_demo.png
  repo: rstudio/gridlayout
  stars: 44
  title: gridlayout
  website: https://rstudio.github.io/gridlayout
---

The gridlayout package enables dashboard-style layouts for Shiny apps and RMarkdown documents using CSS Grid. It uses a visual character vector syntax where you arrange layout elements in a grid pattern that matches the final layout.

The package solves the problem of building complex, responsive layouts without writing CSS. It provides functions for full-page layouts (`grid_page()`), embedded grids (`grid_container()`), and nested grids (`grid_nested()`). The visual syntax makes layouts easy to understand and modify at a glance, and it automatically handles responsive behavior for different screen sizes.
