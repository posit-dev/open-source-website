---
color: '#096EF9'
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

external:  # updated automatically, do not edit
  description: Fast reading of delimited files
  first_commit: '2018-12-11T22:00:39+00:00'
  forks: 65
  languages:
  - C++
  last_updated: '2026-03-05T16:21:38.089681+00:00'
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
  stars: 643
  title: vroom
  website: https://vroom.tidyverse.org
---

vroom is a delimited file reader for R that achieves speeds up to 1.23 GB/sec by indexing file locations rather than immediately reading all data. It uses R's Altrep framework to lazily load data only when accessed, eliminating the performance cost of reading unused columns or rows.

The package supports nearly all readr parsing features while adding multi-file reading, multi-byte Unicode delimiters, and column selection. It uses multiple threads for indexing and parsing to further improve performance, delivering speeds 50x faster than base R and 10x faster than data.table on large datasets. vroom handles all standard delimited file complexities including quoted fields, custom delimiters, type guessing, and embedded newlines.
