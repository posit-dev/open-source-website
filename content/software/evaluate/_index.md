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

external:
  contributors:
  - yihui
  - hadley
  - cderv
  - lawremi
  - krlmlr
  - takluyver
  - karoliskoncevicius
  - yutannihilation
  - jeroen
  - MichaelChirico
  - olivroy
  - trevorld
  - wahani
  - flying-sheep
  - mllg
  - lionel-
  - filipsch
  - cpsievert
  - schloerke
  - adamryczkowski
  description: A version of eval for R that returns more information about what happened
  first_commit: '2008-05-18T13:40:10+00:00'
  forks: 36
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.381478+00:00'
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

The evaluate package provides powerful tools for recreating how R code is parsed, executed, and displayed at the command line. Unlike standard evaluation functions, evaluate captures and interleaves all aspects of code execution—including output, messages, warnings, and errors—in the exact sequence they occur. This makes it invaluable for building documentation systems, literate programming tools, and any application that needs to faithfully reproduce interactive R sessions.

At its core, evaluate offers three key functions: `parse_all()` preserves source code formatting and comments during parsing, `evaluate()` executes code while systematically tracking all outputs and side effects, and `replay()` formats the captured information for display. This architecture provides the foundation for tools like knitr and R Markdown, enabling developers to easily adapt R code execution for different output formats such as HTML, LaTeX, or custom report generators. Whether you're building interactive notebooks, automated testing frameworks, or educational materials, evaluate gives you fine-grained control over code execution and presentation.
