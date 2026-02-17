---
description: Render bits of R code for sharing, e.g., on GitHub or StackOverflow.
github: tidyverse/reprex
image: logo.png
languages:
- R
latest_release: '2024-07-06T00:20:34+00:00'
people:
- Jenny Bryan
- Hadley Wickham
- Christophe Dervieux
- Gábor Csárdi
- Charlotte Wickham
- Jeroen Janssens
- Julia Silge
- Lionel Henry
title: reprex
website: https://reprex.tidyverse.org

external:
  description: Render bits of R code for sharing, e.g., on GitHub or StackOverflow.
  first_commit: '2015-08-25T17:06:45+00:00'
  forks: 84
  languages:
  - R
  last_updated: '2026-02-17T11:28:03.641966+00:00'
  latest_release: '2024-07-06T00:20:34+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  - Hadley Wickham
  - Christophe Dervieux
  - Gábor Csárdi
  - Charlotte Wickham
  - Jeroen Janssens
  - Julia Silge
  - Lionel Henry
  readme_image: man/figures/logo.png
  repo: tidyverse/reprex
  stars: 749
  title: reprex
  website: https://reprex.tidyverse.org
---

The reprex package helps R users create minimal, reproducible examples of their code along with its output, formatted for sharing on platforms like GitHub, Stack Overflow, Slack, or in presentations. It takes R code from various sources (clipboard, files, or direct input), runs it, and returns the code with its output in a format optimized for your chosen platform.

reprex solves the common problem of sharing code that others can immediately run and understand when asking for help or reporting bugs. It automatically handles rendering through rmarkdown, supports multiple output formats (Markdown, HTML, R script, or RTF), uploads plots to imgur, and can strip prompts from pasted console output. The package also includes utilities to extract clean code from existing reprexes found online.
