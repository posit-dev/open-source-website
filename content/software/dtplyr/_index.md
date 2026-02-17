---
description: Data table backend for dplyr
github: tidyverse/dtplyr
image: logo.png
languages:
- R
latest_release: '2026-02-10T17:24:35+00:00'
people:
- Hadley Wickham
- Lionel Henry
- Davis Vaughan
- Jeroen Janssens
title: dtplyr
website: https://dtplyr.tidyverse.org

external:
  description: Data table backend for dplyr
  first_commit: '2016-03-07T23:28:16+00:00'
  forks: 60
  languages:
  - R
  last_updated: '2026-02-17T11:28:11.989399+00:00'
  latest_release: '2026-02-10T17:24:35+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  - Davis Vaughan
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidyverse/dtplyr
  stars: 673
  title: dtplyr
  website: https://dtplyr.tidyverse.org
---

dtplyr provides a data.table backend for dplyr, automatically translating dplyr code into equivalent data.table code. This allows you to write in dplyr syntax while getting the performance benefits of data.table.

The package is valuable for working with large datasets where data.table's speed matters but you prefer dplyr's syntax. It creates "lazy" data tables that track operations and generate optimized data.table code when you access results. While there's some overhead from translation and copying to match dplyr semantics, this is negligible for large datasets where data.table's performance advantages are most important.
