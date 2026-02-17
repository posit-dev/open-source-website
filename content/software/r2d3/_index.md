---
description: R Interface to D3 Visualizations
github: rstudio/r2d3
image: r2d3-hex.png
languages:
- R
latest_release: '2018-12-18T18:00:22+00:00'
people:
- JJ Allaire
- Barret Schloerke
- Nick Strayer
title: r2d3
website: https://rstudio.github.io/r2d3

external:
  description: R Interface to D3 Visualizations
  first_commit: '2018-03-20T21:31:01+00:00'
  forks: 104
  languages:
  - R
  last_updated: '2026-02-17T11:20:24.968378+00:00'
  latest_release: '2018-12-18T18:00:22+00:00'
  license: NOASSERTION
  people:
  - JJ Allaire
  - Barret Schloerke
  - Nick Strayer
  readme_image: man/figures/r2d3-hex.png
  repo: rstudio/r2d3
  stars: 525
  title: r2d3
  website: https://rstudio.github.io/r2d3
---

The r2d3 package provides an interface for using D3.js visualizations within R. It handles the translation of R data structures into D3-compatible formats and renders D3 scripts in RStudio, R Markdown documents, Shiny applications, and R Notebooks.

The package solves the problem of binding R data to existing D3 visualizations from sources like the D3 gallery and bl.ocks.org without manual data conversion. It automatically provides key variables (data, SVG container, width, height) that D3 scripts typically create manually, enabling dynamic data binding and automatic resizing. r2d3 is designed for creating highly custom visualizations when existing packages don't meet specific needs, requiring more low-level SVG programming compared to higher-level htmlwidgets packages.
