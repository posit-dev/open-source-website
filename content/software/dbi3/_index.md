---
description: DBI revisited
github: r-dbi/dbi3
languages:
- R
title: dbi3
website: https://r-dbi.github.io/dbi3

external:
  description: DBI revisited
  first_commit: '2021-10-31T23:18:46+00:00'
  forks: 2
  languages:
  - R
  last_updated: '2026-02-17T11:37:58.929628+00:00'
  repo: r-dbi/dbi3
  stars: 41
  title: dbi3
  website: https://r-dbi.github.io/dbi3
---

dbi3 is a redesign of R's database interface from the ground up, building on lessons learned from the DBI package and related R Consortium projects. It provides bidirectional compatibility with DBI while offering an async-first architecture better suited for web applications like Shiny and Plumber.

The package aims to make backend implementation easier by providing a richer feature set and more idiomatic R patterns using pure functions with callbacks. It's designed to be query-language agnostic and leverages the ADBC (Arrow Database Connectivity) standard to solve many performance, data format, and usability issues that were difficult to address in the original DBI. The project is currently in the design phase, collecting issues and planning solutions that will eventually result in a working package.
