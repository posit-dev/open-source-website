---
description: A re-styled version of the R manuals
github: rstudio/r-manuals
languages:
- R
people:
- Christophe Dervieux
title: r-manuals
website: https://rstudio.github.io/r-manuals

external:
  description: A re-styled version of the R manuals
  first_commit: '2021-12-28T15:17:10+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-02-17T11:25:00.724486+00:00'
  license: NOASSERTION
  people:
  - Christophe Dervieux
  repo: rstudio/r-manuals
  stars: 97
  title: r-manuals
  website: https://rstudio.github.io/r-manuals
---

This project converts the official R manuals from their original texinfo format into modern Quarto books. It restructures the documentation to be more web-friendly by splitting manuals into separate chapter pages and deploying them as a searchable website.

The conversion pipeline provides several readability improvements over the standard R documentation: syntax highlighting for code examples, sidebar footnotes for easier reference, enhanced search functionality, and a cleaner overall design. The tool automates the entire process from downloading source files from the R SVN repository to generating the final Quarto website, using a combination of makeinfo, pandoc with custom Lua filters, and R scripts for post-processing.
