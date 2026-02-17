---
description: An R interface to MariaDB
github: r-dbi/RMariaDB
languages:
- R
latest_release: '2025-02-24T18:19:14+00:00'
people:
- Hadley Wickham
- Jeroen Ooms
- Gábor Csárdi
title: RMariaDB
website: https://rmariadb.r-dbi.org

external:
  description: An R interface to MariaDB
  first_commit: '2017-07-05T15:35:16+00:00'
  forks: 39
  languages:
  - R
  last_updated: '2026-02-17T11:37:44.251636+00:00'
  latest_release: '2025-02-24T18:19:14+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jeroen Ooms
  - Gábor Csárdi
  repo: r-dbi/RMariaDB
  stars: 137
  title: RMariaDB
  website: https://rmariadb.r-dbi.org
---

RMariaDB is a database interface and MariaDB driver for R that provides full compliance with the DBI specification. It serves as a modern replacement for the older RMySQL package, enabling R users to connect to and interact with MariaDB and MySQL databases.

The package implements the complete DBI interface, allowing users to execute queries, fetch results in chunks or all at once, and manage database connections reliably. It supports MariaDB Connector/C (version 2.3.4/3.0.3 or later recommended) and Oracle's libmysqlclient for improved handling of character and blob columns. Users can configure database connections through MariaDB configuration files rather than hardcoding credentials, improving security and convenience.
