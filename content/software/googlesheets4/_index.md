---
color: '#AADFF8'
description: Google Spreadsheets R API (reboot of the googlesheets package)
github: tidyverse/googlesheets4
image: logo.png
languages:
- R
tags:
- tidyverse
latest_release: '2025-09-03T23:00:17+00:00'
people:
- Jenny Bryan
- Joe Cheng
- Mine Çetinkaya-Rundel
title: googlesheets4
website: https://googlesheets4.tidyverse.org

external:  # updated automatically, do not edit
  description: Google Spreadsheets R API (reboot of the googlesheets package)
  first_commit: '2017-04-28T02:03:33+00:00'
  forks: 53
  languages:
  - R
  last_updated: '2026-03-05T16:21:22.990885+00:00'
  latest_release: '2025-09-03T23:00:17+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  - Joe Cheng
  - Mine Çetinkaya-Rundel
  readme_image: man/figures/logo.png
  repo: tidyverse/googlesheets4
  stars: 371
  title: googlesheets4
  website: https://googlesheets4.tidyverse.org
---

googlesheets4 provides an R interface to Google Sheets through the Sheets API v4. It allows you to read from and write to Google Sheets directly from R, treating them like local data frames.

The package handles authentication automatically for reading private sheets and writing data. It supports multiple ways to identify sheets (URL, ID, or file name lookup) and integrates with the tidyverse ecosystem, using similar syntax to readr and readxl for reading data and supporting pipe-friendly workflows. It replaces the older googlesheets package which used the deprecated API v3.
