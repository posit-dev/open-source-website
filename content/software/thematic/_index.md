---
description: Theme ggplot2, lattice, and base graphics based on a few simple settings.
github: rstudio/thematic
image: logo.png
languages:
- R
latest_release: '2025-06-16T15:29:51+00:00'
people:
- Carson Sievert
- Teun Van den Brand
- Barret Schloerke
- Garrick Aden-Buie
- Winston Chang
title: thematic
website: https://rstudio.github.io/thematic/

external:
  contributors:
  - cpsievert
  - teunbrand
  - schloerke
  - gadenbuie
  - wch
  - antivirak
  description: Theme ggplot2, lattice, and base graphics based on a few simple settings.
  first_commit: '2020-03-06T23:01:11+00:00'
  forks: 11
  languages:
  - R
  last_updated: '2026-02-13T14:17:04.560702+00:00'
  latest_release: '2025-06-16T15:29:51+00:00'
  license: NOASSERTION
  people:
  - Carson Sievert
  - Teun Van den Brand
  - Barret Schloerke
  - Garrick Aden-Buie
  - Winston Chang
  readme_image: man/figures/logo.png
  repo: rstudio/thematic
  stars: 252
  title: thematic
  website: https://rstudio.github.io/thematic/
---

Styling R graphics across different plotting systems—ggplot2, lattice, and base R—typically requires learning and maintaining separate theming approaches for each framework. thematic eliminates this complexity by providing a unified theming interface that works seamlessly across all major R graphics systems. With just a few simple settings for colors and fonts, thematic automatically applies consistent styling to your entire visualization ecosystem, whether you're working in Shiny apps, R Markdown documents, or the RStudio IDE.

What makes thematic particularly powerful is its ability to automatically detect and adapt to your working environment. In Shiny applications, it intelligently syncs plot aesthetics with your app's CSS theme, ensuring visual harmony between your interface and embedded graphics. In RStudio, it reads your IDE theme preferences to style plots accordingly, and in R Markdown it integrates with bslib for seamless theme coordination. This "automatic theming" capability means you can maintain design consistency without writing repetitive styling code, while still retaining full control to override global defaults with plot-specific customizations whenever needed.
