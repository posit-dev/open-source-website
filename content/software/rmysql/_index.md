---
description: Legacy DBI interface for MySQL
github: r-dbi/RMySQL
languages:
- C
latest_release: '2022-12-05T23:01:14+00:00'
people:
- Jeroen Ooms
- Hadley Wickham
- Gábor Csárdi
title: RMySQL
website: http://cran.r-project.org/package=RMySQL

external:
  contributors:
  - jeroen
  - hadley
  - jeffreyhorner
  - gagern
  - ankane
  - ggrothendieck
  - jph98
  - rjoomen
  - kongdd
  - gaborcsardi
  - jinzhen-lin
  description: Legacy DBI interface for MySQL
  first_commit: '2012-01-12T17:27:03+00:00'
  forks: 108
  languages:
  - C
  last_updated: '2026-02-13T14:17:21.835837+00:00'
  latest_release: '2022-12-05T23:01:14+00:00'
  people:
  - Jeroen Ooms
  - Hadley Wickham
  - Gábor Csárdi
  repo: r-dbi/RMySQL
  stars: 209
  title: RMySQL
  website: http://cran.r-project.org/package=RMySQL
---

RMySQL is a database interface and MySQL driver for R that enables seamless connectivity between your R environment and MySQL databases. Implementing the DBI (Database Interface) specification, it provides a standardized, reliable approach for data scientists and developers to read, write, and query MySQL databases directly from their R workflows. Whether you're loading production data for statistical analysis, writing R datasets to persistent storage, or running complex SQL queries while leveraging R's analytical capabilities, RMySQL bridges the gap between database operations and data science.

The package offers essential features for database-driven data science, including flexible connection management with support for credential files, the ability to read and write tables efficiently, and progressive result fetching for handling large datasets that exceed memory constraints. While RMySQL is now considered a legacy package being phased out in favor of RMariaDB, it remains functional and continues to serve existing projects that rely on MySQL connectivity in R.
