---
description: Progress bar in your R terminal
github: r-lib/progress
image: logo.png
languages:
- R
latest_release: '2023-12-05T09:32:50+00:00'
people:
- Gábor Csárdi
- Jeroen Janssens
title: progress
website: http://r-lib.github.io/progress/

external:
  contributors:
  - gaborcsardi
  - jimhester
  - mllg
  - Lenostatos
  - Fuco1
  - richfitz
  - DanChaltiel
  - chendaniely
  - ddsjoberg
  - HenrikBengtsson
  - jeroenjanssens
  - MHenderson
  - devillemereuil
  description: Progress bar in your R terminal
  first_commit: '2014-10-03T20:14:56+00:00'
  forks: 40
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.721071+00:00'
  latest_release: '2023-12-05T09:32:50+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/progress
  stars: 474
  title: progress
  website: http://r-lib.github.io/progress/
---

progress is an elegant R package that brings visual feedback to your terminal through customizable ASCII progress bars. When running long computations, processing large datasets, or downloading files, progress transforms the waiting experience by displaying real-time updates on completion status, elapsed time, estimated time to completion, and processing rates. This immediate visual feedback helps you track the advancement of your work and make informed decisions about whether to wait or optimize your code.

What makes progress particularly valuable is its flexibility and ease of integration into existing workflows. Whether you're working with simple loops, functional programming patterns using purrr, or batch operations with plyr, progress adapts to your coding style. The package offers extensive customization through tokens that display percentages, download speeds, tick counts, and custom information, while its R6 class design makes it straightforward to implement. For data scientists and developers running iterative analyses or ETL pipelines, progress provides the transparency needed to monitor operations without interrupting your flow or requiring complex setup.
