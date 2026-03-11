---
image: logo.svg
color: "#447099"
description: An R package showcasing how RStudio addins can be registered and used.
github: rstudio/addinexamples
languages:
- R
people:
- JJ Allaire
- Joe Cheng
title: addinexamples
website: ''

external:  # updated automatically, do not edit
  description: An R package showcasing how RStudio addins can be registered and used.
  first_commit: '2015-12-17T00:45:21+00:00'
  forks: 65
  languages:
  - R
  last_updated: '2026-03-05T16:10:15.746963+00:00'
  license: NOASSERTION
  people:
  - JJ Allaire
  - Joe Cheng
  repo: rstudio/addinexamples
  stars: 86
  title: addinexamples
  website: ''
---

RStudio addins are R functions that can be called through RStudio's interface. This package provides example addins and demonstrates how package authors can create and expose their own addins.

Addins are standard R functions with special registration metadata that RStudio automatically discovers from installed packages. The package includes working examples like insertInAddin (inserts `%in%` at cursor position) and findAndReplaceAddin (interactive code refactoring with Shiny), showing developers how to build both simple text insertion and interactive UI-based addins. Addins can be invoked through keyboard shortcuts and other RStudio UI gestures once registered.
