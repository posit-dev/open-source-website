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
  description: Private configuration for R packages
  first_commit: '2014-09-07T18:37:00+00:00'
  forks: 2
  languages:
  - R
  last_updated: '2026-02-17T11:32:20.481417+00:00'
  latest_release: '2019-09-22T08:42:05+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  repo: r-lib/pkgconfig
  stars: 42
  title: pkgconfig
  website: ''
---

The pkgconfig package provides private, package-specific configuration settings for R packages. It solves the problem of global options that affect all packages when only one package should be affected.

The package allows different packages to set the same configuration parameter to different values without conflicts. When a function queries a configuration value, it receives the value set by the package closest to it in the call stack, preventing packages from interfering with each other's behavior. This is particularly useful for managing backward compatibility options or feature flags that would otherwise require global settings.
