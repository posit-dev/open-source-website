---
description: 'dplyr: A grammar of data manipulation'
github: tidyverse/dplyr
image: dplyr.png
color: "#D84B3A"
languages:
- R
latest_release: '2026-02-04T11:30:38+00:00'
people:
- Hadley Wickham
- Lionel Henry
- Davis Vaughan
- Mine Çetinkaya-Rundel
- Jenny Bryan
- Christophe Dervieux
- Gábor Csárdi
- Simon Couch
- Neal Richardson
- Tomasz Kalinowski
- Charlotte Wickham
- Carson Sievert
- Barret Schloerke
- Jeroen Janssens
- Joe Cheng
title: dplyr
website: https://dplyr.tidyverse.org/

external:  # updated automatically, do not edit
  description: 'dplyr: A grammar of data manipulation'
  first_commit: '2012-10-28T13:39:17+00:00'
  forks: 2131
  languages:
  - R
  last_updated: '2026-03-05T16:20:15.502502+00:00'
  latest_release: '2026-02-04T11:30:38+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  - Davis Vaughan
  - Mine Çetinkaya-Rundel
  - Jenny Bryan
  - Christophe Dervieux
  - Gábor Csárdi
  - Simon Couch
  - Neal Richardson
  - Tomasz Kalinowski
  - Charlotte Wickham
  - Carson Sievert
  - Barret Schloerke
  - Jeroen Janssens
  - Joe Cheng
  readme_image: man/figures/logo.png
  repo: tidyverse/dplyr
  stars: 5008
  title: dplyr
  website: https://dplyr.tidyverse.org/
---

dplyr is an R package that provides a grammar of data manipulation with a consistent set of verbs for common data tasks: filtering rows, selecting columns, creating new variables, sorting data, and computing summaries. These operations work naturally with grouping to perform calculations by category.

The package handles multiple computational backends beyond standard data frames, translating your code to work efficiently with databases (via SQL), large in-memory datasets (via data.table or DuckDB), cloud storage (via Apache Arrow), and distributed systems (via Apache Spark). This backend flexibility lets you use the same dplyr syntax whether your data fits in memory or requires specialized storage systems. The package integrates with other tidyverse tools for end-to-end data analysis workflows.
