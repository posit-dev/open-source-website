---
description: R Markdown Format for reveal.js Presentations
github: rstudio/revealjs
languages:
- JavaScript
people:
- Christophe Dervieux
- JJ Allaire
title: revealjs
website: ''

external:  # updated automatically, do not edit
  description: R Markdown Format for reveal.js Presentations
  first_commit: '2014-09-15T13:20:50+00:00'
  forks: 85
  languages:
  - JavaScript
  last_updated: '2026-02-24T09:26:14.833642+00:00'
  license: NOASSERTION
  people:
  - Christophe Dervieux
  - JJ Allaire
  repo: rstudio/revealjs
  stars: 330
  title: revealjs
  website: ''
---

The revealjs R package provides an R Markdown output format for creating reveal.js HTML presentations. It bundles reveal.js version 4.2.1 and integrates it with R Markdown's rendering system so you can build slide decks using markdown syntax with `#` and `##` headers to define slides.

The package supports reveal.js's full feature set including slide transitions, custom themes, background effects, 2D navigation layouts, and plugins for speaker notes, search, and annotation. It handles R-specific needs like rendering plots with configurable dimensions, displaying MathJax equations, and managing dependencies either as standalone files or self-contained presentations. The format works through RStudio's Knit button, `rmarkdown::render()`, or command-line rendering.
