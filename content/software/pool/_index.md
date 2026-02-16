---
description: Object Pooling in R
github: rstudio/pool
languages:
- R
latest_release: '2024-10-07T14:57:52+00:00'
people:
- Hadley Wickham
- Joe Cheng
- Winston Chang
- Barret Schloerke
title: pool
website: http://rstudio.github.io/pool/

external:
  contributors:
  - bborgesr
  - hadley
  - jcheng5
  - wch
  - yupimaki
  - schloerke
  - krlmlr
  - renkun-ken
  - marcosci
  - nwstephens
  - philippleppert
  - smach
  - caewok
  - pnacht
  description: Object Pooling in R
  first_commit: '2016-05-18T17:33:18+00:00'
  forks: 32
  languages:
  - R
  last_updated: '2026-02-13T14:17:02.341689+00:00'
  latest_release: '2024-10-07T14:57:52+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Joe Cheng
  - Winston Chang
  - Barret Schloerke
  repo: rstudio/pool
  stars: 255
  title: pool
  website: http://rstudio.github.io/pool/
---

The pool package simplifies database connection management in R by automatically handling the creation, maintenance, and closure of connections. Instead of manually managing individual database connections, pool creates an intelligent connection pool that expands, contracts, or maintains its size based on demand. This automated approach eliminates the complexity of connection lifecycle management while improving resource efficiency, making it particularly valuable for Shiny applications and other interactive contexts where multiple concurrent database requests are common.

Pool integrates seamlessly with existing R workflows, working with both DBI and dplyr packages. Implementation is straightforward—simply replace `DBI::dbConnect()` calls with `dbPool()` and add `poolClose()` when finished. The package handles all operational details transparently, allowing you to focus on your data analysis rather than connection management. While optimized for database connections, pool's general-purpose architecture can be used to pool any type of object, providing flexible resource management across a variety of use cases.
