---
color: '#FBEB1E'
description: A drop-in replacement for dplyr, powered by DuckDB for speed.
github: tidyverse/duckplyr
image: logo.png
languages:
- R
latest_release: '2026-02-24T22:07:23+00:00'
people:
- Davis Vaughan
- Hadley Wickham
- Jeroen Janssens
- Mine Çetinkaya-Rundel
title: duckplyr
website: https://duckplyr.tidyverse.org/

external:  # updated automatically, do not edit
  description: A drop-in replacement for dplyr, powered by DuckDB for speed.
  first_commit: '2022-11-29T08:20:48+00:00'
  forks: 27
  languages:
  - R
  last_updated: '2026-03-20T10:27:41.306448+00:00'
  latest_release: '2026-02-24T22:07:23+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Hadley Wickham
  - Jeroen Janssens
  - Mine Çetinkaya-Rundel
  readme_image: man/figures/logo.png
  repo: tidyverse/duckplyr
  stars: 379
  title: duckplyr
  website: https://duckplyr.tidyverse.org/
---

duckplyr is a drop-in replacement for dplyr that uses DuckDB as its execution engine to run data manipulation operations faster. It executes existing dplyr code with identical results while automatically leveraging DuckDB's performance optimizations.

The package handles larger-than-memory datasets by working directly with files on disk or remote URLs without loading everything into memory. It automatically falls back to standard dplyr when DuckDB doesn't support a specific operation, providing transparent acceleration without requiring code changes. The package can query Parquet, CSV, and JSON files efficiently, including remote files over HTTP, making it practical for analyzing datasets that exceed available RAM.
