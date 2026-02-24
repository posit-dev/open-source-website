---
description: A version of eval for R that returns more information about what happened
github: r-lib/evaluate
languages:
- R
latest_release: '2025-08-27T16:20:44+00:00'
people:
- Hadley Wickham
- Christophe Dervieux
- Jeroen Ooms
- Lionel Henry
- Carson Sievert
- Barret Schloerke
title: evaluate
website: http://evaluate.r-lib.org/

external:  # updated automatically, do not edit
  description: A version of eval for R that returns more information about what happened
  first_commit: '2008-05-18T13:40:10+00:00'
  forks: 36
  languages:
  - R
  last_updated: '2026-02-24T09:26:33.908691+00:00'
  latest_release: '2025-08-27T16:20:44+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Christophe Dervieux
  - Jeroen Ooms
  - Lionel Henry
  - Carson Sievert
  - Barret Schloerke
  repo: r-lib/evaluate
  stars: 139
  title: evaluate
  website: http://evaluate.r-lib.org/
---

The evaluate package captures and recreates the full execution of R code, including parsing, evaluation, and all output in the correct order. It provides detailed tracking of expressions, results, messages, warnings, and errors as they occur during code execution.

The package solves the problem of accurately reproducing what happens when R code runs at the command line, which is essential for tools like knitr and R Markdown. It preserves source code formatting and comments through enhanced parsing, tracks all output in proper sequence, and provides a flexible replay system that can be adapted for different output formats like HTML or LaTeX. This makes it a fundamental building block for literate programming and reproducible research tools in R.
