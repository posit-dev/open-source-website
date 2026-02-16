---
description: A DBI-compliant interface to PostgreSQL
github: r-dbi/RPostgres
languages:
- R
latest_release: '2026-02-05T20:15:25+00:00'
people:
- Hadley Wickham
- Jeroen Ooms
title: RPostgres
website: https://rpostgres.r-dbi.org

external:
  contributors:
  - krlmlr
  - hadley
  - jeroen
  - Antonov548
  - dpprdan
  - thrasibule
  - github-actions[bot]
  - zozlak
  - JackStat
  - aviator-app[bot]
  - lentinj
  - TSchiefer
  - IndrajeetPatil
  - JSchoenbachler
  - etiennebr
  - pachadotdev
  - jakob-r
  - galachad
  - mmuurr
  - maelle
  - jaredk-porch
  - web-flow
  - ateucher
  - baderstine
  - Copilot
  - jimhester
  - robertzk
  - gatscha-trafficon
  - troels
  - harvey131
  - karawoo
  - oz-r
  - toppyy
  - hrbrmstr
  - rstammer
  - pedrobtz
  - junduck
  - daattali
  - ClaytonJY
  - Altons
  description: A DBI-compliant interface to PostgreSQL
  first_commit: '2015-01-05T17:43:02+00:00'
  forks: 79
  languages:
  - R
  last_updated: '2026-02-13T14:17:21.921846+00:00'
  latest_release: '2026-02-05T20:15:25+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jeroen Ooms
  repo: r-dbi/RPostgres
  stars: 337
  title: RPostgres
  website: https://rpostgres.r-dbi.org
---

RPostgres is a modern database interface that enables R users to connect with PostgreSQL databases. Built from scratch using C++ and cpp11, it implements the DBI (Database Interface) standard and provides a streamlined way for data scientists and developers to perform database operations in R, including querying, reading, and writing data to PostgreSQL instances—whether local or cloud-hosted. RPostgres modernizes PostgreSQL connectivity for R users with cleaner code patterns, better resource handling, and improved performance compared to its predecessor RPostgreSQL.

Key features include support for secure parameterized queries through `dbSendQuery()` and `dbBind()` functions to help prevent SQL injection vulnerabilities, automatic cleanup of open connections and result sets to reduce concerns about memory leaks, and modest speed improvements of approximately 5ms faster per query. The package integrates seamlessly with R's broader database ecosystem and follows established DBI conventions, making it intuitive for users already familiar with R's data access patterns and particularly valuable for analysts working with large datasets or building production applications requiring reliable database interactions.
