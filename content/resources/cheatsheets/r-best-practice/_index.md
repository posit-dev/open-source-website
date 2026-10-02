---
title: Best Practice for R
image: page-1.png
resource_type: cheatsheet
by: community
date: '2023-11-01'
description: Recommended tools, project structure, function design, and coding style for writing maintainable R code.
download_url: R-best-practice.pdf
people:
- Jacob Scott
thumbnails:
- page-1.png
software:
- usethis
- reprex
- renv
languages:
- R
source_files:
- file: R-best-practice.key
  format: Keynote
---

This cheat sheet summarizes best practices for R development, covering IDE and tooling choices, project structure with renv, recommended package ecosystems for common tasks, guidelines for writing clean functions, and code style conventions from the Tidyverse style guide. It includes a workflow for writing minimal reproducible examples with `reprex::reprex()`.

## What's covered
- Software – RStudio, Quarto, git, and GitHub for version control and collaboration
- Packages – tidyverse, tidymodels, shiny, renv, and when to trust a package (GitHub stars heuristic)
- Project creation and structure – directory layout, `.gitignore`, `renv.lock`, `run-all.R`
- Databases – `{DBI}` and `{odbc}` connection helper functions
- Getting help – `reprex::reprex()`, etiquette for Teams and Stack Overflow
- Functions – writing workflow, verb-like naming conventions
- Styling – `lower_snake_case`, whitespace around operators, 80-character line limit, indentation rules
