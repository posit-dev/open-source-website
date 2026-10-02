---
image: logo.svg
color: "#419599"
description: Cache CRAN-like metadata and package files
github: r-lib/pkgcache
languages:
- R
latest_release: '2026-04-08T20:38:37+00:00'
people:
- Gábor Csárdi
- Jeroen Janssens
- Jeroen Ooms
title: pkgcache
website: https://r-lib.github.io/pkgcache/

external:  # updated automatically, do not edit
  description: Cache CRAN-like metadata and package files
  first_commit: '2018-09-12T17:49:03+00:00'
  forks: 19
  languages:
  - R
  last_updated: '2026-09-18T14:28:58.640142+00:00'
  latest_release: '2026-04-08T20:38:37+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  - Jeroen Ooms
  repo: r-lib/pkgcache
  stars: 30
  title: pkgcache
  website: https://r-lib.github.io/pkgcache/
---

pkgcache is an R package that caches package metadata and downloaded package files from CRAN-like repositories, including Bioconductor. It is a utility package designed to be used by other package management tools that want to avoid redundant downloads.

The metadata cache stores information about all available packages (including dependencies and reverse dependencies) and automatically refreshes after seven days. The package cache stores downloaded package files locally so they don't need to be re-downloaded on subsequent installs. pkgcache also includes a fast DCF parser for reading `PACKAGES` and `DESCRIPTION` files, and it provides both a high-level functional API (`meta_cache_*`, `pkg_cache_*`) and lower-level R6 classes for finer control.
