---
color: '#EA4A41'
description: Database (DBI) backend for dplyr
github: tidyverse/dbplyr
image: logo.png
languages:
- R
latest_release: '2026-02-13T13:26:38+00:00'
people:
- Hadley Wickham
- Lionel Henry
- Edgar Ruiz
- Simon Couch
- Christophe Dervieux
- Davis Vaughan
- Mine Çetinkaya-Rundel
- Carson Sievert
- Joe Cheng
- Garrick Aden-Buie
tags:
- tidyverse
title: dbplyr
topics:
- Data Wrangling
website: https://dbplyr.tidyverse.org

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Database (DBI) backend for dplyr
  first_commit: '2017-03-28T20:29:16+00:00'
  forks: 188
  languages:
  - R
  last_updated: '2026-05-20T08:05:44.408899+00:00'
  latest_release: '2026-02-13T13:26:38+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  - Edgar Ruiz
  - Simon Couch
  - Christophe Dervieux
  - Davis Vaughan
  - Jeroen Janssens
  - Mine Çetinkaya-Rundel
  - Carson Sievert
  - Joe Cheng
  - Garrick Aden-Buie
  readme_image: man/figures/logo.png
  repo: tidyverse/dbplyr
  stars: 507
  title: dbplyr
  website: https://dbplyr.tidyverse.org
---

dbplyr is the database backend for dplyr that lets you work with remote database tables using dplyr syntax. It automatically translates your R code into SQL, eliminating the need to write SQL queries directly.

The package provides lazy evaluation, meaning queries are only executed when you explicitly request results, which improves performance when working with large databases. It integrates seamlessly with the DBI package ecosystem and supports standard dplyr operations like filtering, grouping, and summarizing on database tables. You can preview generated SQL queries before execution and work with databases as if they were local data frames.
