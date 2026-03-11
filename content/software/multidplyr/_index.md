---
image: logo.svg
color: "#9A4665"
description: A dplyr backend that partitions a data frame over multiple processes
github: tidyverse/multidplyr
languages:
- R
latest_release: '2025-11-13T13:40:03+00:00'
people:
- Hadley Wickham
- Jenny Bryan
- Davis Vaughan
- Carlos Scheidegger
title: multidplyr
website: https://multidplyr.tidyverse.org

external:  # updated automatically, do not edit
  description: A dplyr backend that partitions a data frame over multiple processes
  first_commit: '2015-11-05T22:55:06+00:00'
  forks: 76
  languages:
  - R
  last_updated: '2026-03-05T16:20:51.039679+00:00'
  latest_release: '2025-11-13T13:40:03+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jenny Bryan
  - Davis Vaughan
  - Carlos Scheidegger
  repo: tidyverse/multidplyr
  stars: 649
  title: multidplyr
  website: https://multidplyr.tidyverse.org
---

multidplyr is a dplyr backend that partitions data frames across multiple R processes to enable parallel computation on multi-core systems. You split your data with `partition()`, perform dplyr operations in parallel, and retrieve results with `collect()`.

This package is most valuable for parallelizing complex, slow functions on datasets with 10+ million rows, where the computation cost outweighs the overhead of distributing data across cores. It works best when you can partition data by meaningful groups or read different files directly on each worker. For simpler operations on smaller datasets, the communication overhead makes alternatives like dtplyr more efficient.
