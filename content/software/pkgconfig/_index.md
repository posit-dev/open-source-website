---
description: Private configuration for R packages
github: r-lib/pkgconfig
languages:
- R
latest_release: '2019-09-22T08:42:05+00:00'
people:
- Gábor Csárdi
title: pkgconfig
website: ''

external:
  contributors:
  - gaborcsardi
  - richfitz
  - salim-b
  description: Private configuration for R packages
  first_commit: '2014-09-07T18:37:00+00:00'
  forks: 2
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.622886+00:00'
  latest_release: '2019-09-22T08:42:05+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  repo: r-lib/pkgconfig
  stars: 42
  title: pkgconfig
  website: ''
---

pkgconfig provides an elegant solution to a common problem in R package development: managing configuration parameters that need to work differently across multiple packages. When you use global options in R, changing a setting in one package can inadvertently affect the behavior of other packages that rely on the same option. pkgconfig eliminates this conflict by creating package-specific configuration values that remain completely independent from one another.

The package offers a simple API with two core functions: `set_config()` for establishing configuration parameters and `get_config()` for retrieving values with sensible fallback defaults. This makes it particularly valuable when building packages that depend on other packages with configurable behavior, allowing each package to maintain its own settings without interference. For developers working on complex projects with multiple package dependencies, pkgconfig ensures that your configuration choices stay local to your package while respecting the preferences of packages higher in the call stack.
