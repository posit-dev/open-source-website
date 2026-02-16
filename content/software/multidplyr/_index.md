---
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

external:
  contributors:
  - hadley
  - romainfrancois
  - Maschette
  - FvD
  - jennybc
  - smsaladi
  - paulponcet
  - eipi10
  - anobel
  - wibeasley
  - traversc
  - michaelgrund
  - fugufisch
  - batpigandme
  - DavisVaughan
  - cscheid
  - bbrewington
  description: A dplyr backend that partitions a data frame over multiple processes
  first_commit: '2015-11-05T22:55:06+00:00'
  forks: 76
  languages:
  - R
  last_updated: '2026-02-13T14:17:08.623613+00:00'
  latest_release: '2025-11-13T13:40:03+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jenny Bryan
  - Davis Vaughan
  - Carlos Scheidegger
  repo: tidyverse/multidplyr
  stars: 647
  title: multidplyr
  website: https://multidplyr.tidyverse.org
---

multidplyr is a parallel processing backend for dplyr that enables data scientists to harness the full power of multi-core processors when working with large datasets. By partitioning data frames across multiple CPU cores and keeping them distributed during computation, multidplyr allows you to apply familiar dplyr operations at scale without rewriting your code. The package seamlessly integrates with your existing dplyr workflows—simply wrap your data with `partition()`, perform your transformations using standard dplyr verbs, and collect results back to your main R session.

Designed for computationally intensive operations on datasets with millions of observations, multidplyr excels when parallelizing complex functions where the computational gains outweigh communication overhead. The package offers flexible data distribution strategies, allowing you to either read different files on each worker or partition already-loaded data using `group_by()` to ensure related observations stay together. Inspired by partools and distributedR, multidplyr prioritizes minimizing inter-node data transfer while maximizing parallel performance, making it an essential tool for data scientists tackling large-scale data processing challenges in R.
