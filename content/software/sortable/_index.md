---
color: '#5E95D1'
description: R htmlwidget for Sortable.js
github: rstudio/sortable
image: logo.png
languages:
- R
people:
- Barret Schloerke
- Christophe Dervieux
title: sortable
website: https://rstudio.github.io/sortable/

external:  # updated automatically, do not edit
  description: R htmlwidget for Sortable.js
  first_commit: '2015-03-03T19:57:30+00:00'
  forks: 33
  languages:
  - R
  last_updated: '2026-03-20T10:27:31.612437+00:00'
  license: NOASSERTION
  people:
  - Barret Schloerke
  - Christophe Dervieux
  readme_image: man/figures/logo.png
  repo: rstudio/sortable
  stars: 135
  title: sortable
  website: https://rstudio.github.io/sortable/
---

The sortable package brings drag-and-drop functionality to R Shiny applications by wrapping the SortableJS JavaScript library as an htmlwidget. It works in Shiny apps, learnr tutorials, and R Markdown documents, and includes a custom learnr question type called `question_rank()` for creating ranking exercises.

The package provides three main components: `rank_list()` for creating single sortable lists with configurable behaviors like multi-drag and item swapping, `bucket_list()` for building multiple interconnected lists useful for classification tasks, and `sortable_js()` for adding drag-and-drop to any HTML element or widget. These tools make it straightforward to build interactive ranking exercises, categorization tasks, or reorderable UI components without writing JavaScript.
