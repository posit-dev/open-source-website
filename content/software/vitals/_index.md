---
color: '#F3B95D'
description: Large language model evaluation for R
github: tidyverse/vitals
image: logo.png
tags:
- AI
languages:
- JavaScript
latest_release: '2025-12-01T15:34:29+00:00'
people:
- Simon Couch
- Hadley Wickham
- Jeroen Janssens
- Mine Çetinkaya-Rundel
- Tomasz Kalinowski
title: vitals
website: https://vitals.tidyverse.org

external:  # updated automatically, do not edit
  description: Large language model evaluation for R
  first_commit: '2025-02-10T16:40:08+00:00'
  forks: 11
  languages:
  - JavaScript
  last_updated: '2026-03-05T16:21:53.717047+00:00'
  latest_release: '2025-12-01T15:34:29+00:00'
  license: NOASSERTION
  people:
  - Simon Couch
  - Hadley Wickham
  - Jeroen Janssens
  - Mine Çetinkaya-Rundel
  - Tomasz Kalinowski
  readme_image: man/figures/logo.png
  repo: tidyverse/vitals
  stars: 52
  title: vitals
  website: https://vitals.tidyverse.org
---

The vitals package provides a framework for evaluating large language model (LLM) applications built with ellmer in R. It helps developers measure and compare the performance, cost, and latency of LLM products like custom chat apps.

The package allows you to assess whether prompt changes or new tools improve your LLM application, compare different models' effects on performance metrics, and identify problematic behaviors. It's an R port of the Python Inspect framework and writes evaluation logs compatible with the Inspect log viewer, making it straightforward to transition between the two tools if needed. Evaluations are built from three components: datasets with input/target pairs, solvers that generate responses to inputs, and scorers that measure how well solver outputs match targets.
