---
description: Visualize R profiling data
github: r-lib/profvis
languages:
- JavaScript
latest_release: '2024-09-19T19:25:49+00:00'
people:
- Winston Chang
- Lionel Henry
- Hadley Wickham
- Joe Cheng
- Barret Schloerke
- JJ Allaire
- Jenny Bryan
- Jeroen Janssens
title: profvis
website: https://profvis.r-lib.org/

external:  # updated automatically, do not edit
  description: Visualize R profiling data
  first_commit: '2015-09-18T18:01:49+00:00'
  forks: 38
  languages:
  - JavaScript
  last_updated: '2026-02-24T09:26:34.542790+00:00'
  latest_release: '2024-09-19T19:25:49+00:00'
  license: NOASSERTION
  people:
  - Winston Chang
  - Lionel Henry
  - Hadley Wickham
  - Joe Cheng
  - Barret Schloerke
  - JJ Allaire
  - Jenny Bryan
  - Jeroen Janssens
  repo: r-lib/profvis
  stars: 311
  title: profvis
  website: https://profvis.r-lib.org/
---

profvis is a tool for visualizing code profiling data from R. It creates an interactive web-based interface for exploring performance data collected during code execution.

The package wraps R expressions with `profvis()` to collect profiling data and automatically generates an interactive visualization in a web browser. It returns an htmlwidget object that can be saved and viewed later, making it easy to analyze where code spends time and identify performance bottlenecks. The graphical interface provides a more intuitive way to explore profiling data compared to raw text-based output.
