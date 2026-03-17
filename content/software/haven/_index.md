---
color: '#14497F'
description: Read SPSS, Stata and SAS files from R
github: tidyverse/haven
image: logo.png
languages:
- C
latest_release: '2025-05-30T13:08:26+00:00'
people:
- Hadley Wickham
- Lionel Henry
- Jeroen Ooms
- Jeroen Janssens
- JJ Allaire
tags:
- tidyverse
title: haven
website: https://haven.tidyverse.org

external:  # updated automatically, do not edit
  description: Read SPSS, Stata and SAS files from R
  first_commit: '2015-02-04T16:28:17+00:00'
  forks: 116
  languages:
  - C
  last_updated: '2026-03-05T16:20:40.076783+00:00'
  latest_release: '2025-05-30T13:08:26+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  - Jeroen Ooms
  - Jeroen Janssens
  - JJ Allaire
  readme_image: man/figures/logo.png
  repo: tidyverse/haven
  stars: 447
  title: haven
  website: https://haven.tidyverse.org
---

haven is an R package that reads and writes data files from SAS, SPSS, and Stata statistical software. It wraps the ReadStat C library to handle these proprietary formats and returns data as tibbles.

The package preserves important metadata like value labels through a `labelled()` class, handles special missing values correctly, and converts dates and times to R's native classes. It supports modern file format versions (SAS .sas7bdat and transport files, SPSS .sav and .por files, and Stata .dta files up to version 15) and provides both read and write functions for most formats.
