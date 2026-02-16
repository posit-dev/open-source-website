---
description: DBI revisited
github: r-dbi/dbi3
languages:
- R
title: dbi3
website: https://r-dbi.github.io/dbi3

external:
  contributors:
  - krlmlr
  - maelle
  description: DBI revisited
  first_commit: '2021-10-31T23:18:46+00:00'
  forks: 2
  languages:
  - R
  last_updated: '2026-02-13T14:17:22.102311+00:00'
  repo: r-dbi/dbi3
  stars: 41
  title: dbi3
  website: https://r-dbi.github.io/dbi3
---

dbi3 is an experimental next-generation database interface for R that reimagines how R connects to and communicates with databases. Built from the ground up with modern R development in mind, it addresses key limitations of the original DBI package while maintaining backward compatibility. The package features an async-first architecture that enables efficient performance in interactive web applications like Shiny and Plumber, along with a more natural functional programming approach using pure functions and callbacks that align with R idioms.

What makes dbi3 particularly valuable for data scientists and developers is its query-language agnostic design that works seamlessly across different database systems, combined with enhanced support for modern database features like query cancellation, Arrow/Flight SQL, and improved type management. The bidirectional compatibility approach means new backends automatically support legacy DBI code, while existing DBI backends can leverage the new interface. Whether you're building database-backed applications or implementing database drivers, dbi3 provides a more robust foundation that makes backend development easier and unlocks performance improvements that weren't possible with the original interface.
