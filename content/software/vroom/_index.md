---
description: Fast reading of delimited files
github: tidyverse/vroom
image: logo.png
languages:
- C++
latest_release: '2026-01-25T17:49:54+00:00'
people:
- Jenny Bryan
- Davis Vaughan
- Lionel Henry
- Hadley Wickham
- Jeroen Ooms
- Jeroen Janssens
title: vroom
website: https://vroom.tidyverse.org

external:
  contributors:
  - jimhester
  - jennybc
  - DavisVaughan
  - sbearrows
  - meta00
  - MichaelChirico
  - R3myG
  - MikeJohnPage
  - batpigandme
  - lionel-
  - AB-Kent
  - hadley
  - olivroy
  - jrf1111
  - bart1
  - philaris
  - maurolepore
  - lwjohnst86
  - jeroen
  - jeroenjanssens
  - bairdj
  - frm1789
  - edzer
  - CriscelyLP
  - wlattner
  - Anirban166
  - andrie
  description: Fast reading of delimited files
  first_commit: '2018-12-11T22:00:39+00:00'
  forks: 65
  languages:
  - C++
  last_updated: '2026-02-13T14:17:08.943626+00:00'
  latest_release: '2026-01-25T17:49:54+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  - Davis Vaughan
  - Lionel Henry
  - Hadley Wickham
  - Jeroen Ooms
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidyverse/vroom
  stars: 641
  title: vroom
  website: https://vroom.tidyverse.org
---

Reading large delimited files in R can be painfully slow with traditional approaches. Vroom eliminates this bottleneck by rethinking how data is loaded: instead of parsing everything upfront, it creates an index of where each record is located and loads values only when you actually use them. This lazy evaluation approach, powered by R's Altrep framework, means you get dramatically faster initial load times while still enjoying the full power of R's data manipulation tools without any changes to your workflow.

Vroom provides all the features you expect from a modern CSV reader, including automatic column type detection, flexible delimiter handling, column selection with dplyr-style syntax, and multi-file reading with source tracking. Benchmarks demonstrate impressive speed gains: vroom processes files at over 1 GB/sec, significantly outperforming data.table, readr, and base R alternatives. Whether you're working with large datasets where you only need a subset of columns or processing data progressively, vroom's intelligent approach ensures you only pay for what you use.
