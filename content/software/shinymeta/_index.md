---
color: '#72994E'
description: Record and expose Shiny app logic using metaprogramming
github: rstudio/shinymeta
image: logo.svg
languages:
- R
latest_release: '2026-03-02T21:45:37+00:00'
people:
- Carson Sievert
- Joe Cheng
- Barret Schloerke
- Lionel Henry
title: shinymeta
website: https://rstudio.github.io/shinymeta

external:  # updated automatically, do not edit
  description: Record and expose Shiny app logic using metaprogramming
  first_commit: '2019-05-09T06:00:50+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-03-05T16:14:53.561704+00:00'
  latest_release: '2026-03-02T21:45:37+00:00'
  license: NOASSERTION
  people:
  - Carson Sievert
  - Joe Cheng
  - Barret Schloerke
  - Lionel Henry
  readme_image: https://i.imgur.com/5gNquPE.gif
  repo: rstudio/shinymeta
  stars: 226
  title: shinymeta
  website: https://rstudio.github.io/shinymeta
---

shinymeta captures the logic in a Shiny app and exposes it as standalone R code that can be run outside of Shiny. It provides meta-counterparts to Shiny's reactive building blocks (like metaReactive(), metaObserve(), and metaRender()) that track the logic needed to recreate their current state.

This package enables users to automate workflows by taking app logic into R scripts or scheduled reports, makes analysis more transparent and reproducible, and allows users to modify and extend the analysis beyond what the app interface provides. It solves the problem of Shiny apps being ephemeral black boxes by generating code that reveals and preserves the underlying analysis. The package is particularly useful for apps that work with changing data or perform exploratory analysis where users benefit from seeing and running the code themselves.
