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
  contributors:
  - jennybc
  - hadley
  - batpigandme
  - jimhester
  - cderv
  - yutannihilation
  - krlmlr
  - lorenzwalthert
  - gaborcsardi
  - olivroy
  - mrchypark
  - cwickham
  - alistaire47
  - paternogbc
  - Bisaloo
  - assignUser
  - jeroenjanssens
  - juliasilge
  - lionel-
  - marionlouveaux
  - markdly
  - mdlincoln
  - njtierney
  - uribo
  - remlapmot
  - atusy
  - tappek
  description: Render bits of R code for sharing, e.g., on GitHub or StackOverflow.
  first_commit: '2015-08-25T17:06:45+00:00'
  forks: 84
  languages:
  - R
  last_updated: '2026-02-13T14:17:08.591911+00:00'
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

Creating a reproducible example is essential when seeking help with code issues or collaborating with colleagues, but formatting code for sharing can be tedious and error-prone. Reprex streamlines this process by automatically preparing R code for posting to GitHub issues, StackOverflow, Slack messages, or even presentation slides. Simply provide your code from the clipboard, RStudio selection, or a file, and reprex executes it, captures the output, and formats everything into ready-to-share Markdown or other formats.

The package offers multiple output formats including GitHub-flavored Markdown, Slack-optimized Markdown, and runnable R scripts with commented output. Key features include automatic syntax highlighting, figure uploads to imgur.com, session information inclusion, and utility functions for cleaning and inverting examples. By ensuring that your shared code is immediately runnable by others without modification, reprex significantly improves the quality of technical support requests and accelerates collaborative debugging across data science teams.
