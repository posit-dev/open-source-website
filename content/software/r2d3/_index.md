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
  contributors:
  - javierluraschi
  - jjallaire
  - edgararuiz-zz
  - schloerke
  - rgerecke
  - alexvpickering
  - jimhester
  - mnazarov
  - condour
  - mspan
  - nstrayer
  - shrektan
  description: R Interface to D3 Visualizations
  first_commit: '2018-03-20T21:31:01+00:00'
  forks: 104
  languages:
  - R
  last_updated: '2026-02-13T14:17:03.303761+00:00'
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

r2d3 is an R package that bridges the power of R's data analysis capabilities with D3.js, the industry-standard JavaScript library for creating sophisticated data visualizations. It seamlessly binds data from R to D3 visualizations, enabling you to create highly custom, interactive graphics that go beyond what traditional plotting libraries offer. The package handles the technical infrastructure automatically, translating R objects into D3-compatible data structures and providing essential variables like data, svg, width, and height directly to your D3 scripts, so you can focus on visualization design rather than boilerplate code.

What makes r2d3 particularly valuable is its deep integration with the R ecosystem. Your D3 visualizations render directly in RStudio Viewer, R Notebooks, and R Markdown documents, and work seamlessly with Shiny applications for interactive dashboards. The package includes built-in support for dynamic resizing, making your visualizations responsive across different display contexts. Whether you're a data scientist needing precise control over complex visual encodings or a developer building custom interactive tools, r2d3 lets you leverage D3's full expressive power while staying within your R workflow.