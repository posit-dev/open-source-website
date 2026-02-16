---
description: Create a map of functions for an R package - WORK IN PROGRESS!
github: r-lib/pkgapi
languages:
- R
people:
- Gábor Csárdi
title: pkgapi
website: ''

external:
  contributors:
  - krlmlr
  - gaborcsardi
  description: Create a map of functions for an R package - WORK IN PROGRESS!
  first_commit: '2016-11-28T03:02:36+00:00'
  forks: 11
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.254554+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  repo: r-lib/pkgapi
  stars: 70
  title: pkgapi
  website: ''
---

pkgapi is a specialized R package that creates comprehensive maps of function calls within your R packages, revealing how functions interact with each other and with imported dependencies. It automatically analyzes your package code to generate a complete call graph, showing which functions call which other functions, and tracking usage of external packages throughout your codebase. This visibility is invaluable when you need to understand package architecture, optimize dependencies, or refactor code with confidence.

For R package developers and maintainers, pkgapi addresses a critical need: understanding the internal structure and dependency relationships of your code. Whether you're working on a legacy codebase, preparing for a major refactor, or simply documenting how your package functions interconnect, pkgapi provides clear insights into call chains and dependency patterns. By automatically mapping these relationships, it helps you make informed decisions about code organization, identify potential optimization opportunities, and maintain a cleaner, more maintainable package structure.
