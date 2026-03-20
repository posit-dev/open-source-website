---
color: '#79A7D7'
description: The layout packages that powers ggplot2
github: r-lib/gtable
image: logo.png
languages:
- R
latest_release: '2024-10-25T12:41:50+00:00'
people:
- Hadley Wickham
- Winston Chang
- Thomas Lin Pedersen
- Teun Van den Brand
title: gtable
website: https://gtable.r-lib.org

external:  # updated automatically, do not edit
  description: The layout packages that powers ggplot2
  first_commit: '2011-12-30T16:08:43+00:00'
  forks: 18
  languages:
  - R
  last_updated: '2026-03-20T10:27:51.550168+00:00'
  latest_release: '2024-10-25T12:41:50+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Winston Chang
  - Thomas Lin Pedersen
  - Teun Van den Brand
  readme_image: man/figures/logo.png
  repo: r-lib/gtable
  stars: 94
  title: gtable
  website: https://gtable.r-lib.org
---

gtable is a layout engine built on top of R's grid package that abstracts the creation of potentially nested grids of viewports for placing graphic objects. It serves as the layout engine powering ggplot2 and is used extensively by many R plotting functions.

The package makes it easy to ensure alignment of graphic elements and enables piecemeal composition of complex graphics. It provides a systematic way to manage grid layouts through a collection of graphic elements along with their placement in the grid and the grid's dimensions. Graphic elements can span multiple rows and columns and can themselves be gtables, allowing for complex automatically arranging layouts.
