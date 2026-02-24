---
description: Format columns with colour
github: r-lib/pillar
languages:
- R
latest_release: '2025-09-17T03:59:06+00:00'
people:
- Hadley Wickham
- Lionel Henry
- Teun Van den Brand
title: pillar
website: https://pillar.r-lib.org/

external:  # updated automatically, do not edit
  description: Format columns with colour
  first_commit: '2017-05-15T19:04:32+00:00'
  forks: 41
  languages:
  - R
  last_updated: '2026-02-24T09:26:35.255678+00:00'
  latest_release: '2025-09-17T03:59:06+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  - Teun Van den Brand
  repo: r-lib/pillar
  stars: 182
  title: pillar
  website: https://pillar.r-lib.org/
---

pillar provides tools for styling and formatting columns of data in R, using color and unicode characters to improve readability. It powers the print and format methods for tibbles and other table-like objects.

This package is designed for developers who create custom vector classes or custom table classes, not for end-users directly. It provides generics and helpers that allow package authors to customize how their data types are displayed in tibbles through methods like `pillar_shaft()` for column formatting and `tbl_sum()` for table summaries. The package handles complex formatting decisions like number alignment, decimal placement, and visual styling automatically.
