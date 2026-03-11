---
color: '#447099'
description: cpp11 helps you to interact with R objects using C++ code.
github: r-lib/cpp11
image: logo.svg
languages:
- C++
latest_release: '2026-01-20T19:57:34+00:00'
people:
- Davis Vaughan
- Jeroen Ooms
- Jenny Bryan
- Hadley Wickham
- Emil Hvitfeldt
- Thomas Lin Pedersen
- Neal Richardson
title: cpp11
website: https://cpp11.r-lib.org/

external:  # updated automatically, do not edit
  description: cpp11 helps you to interact with R objects using C++ code.
  first_commit: '2020-06-10T18:40:48+00:00'
  forks: 54
  languages:
  - C++
  last_updated: '2026-03-05T16:29:26.495396+00:00'
  latest_release: '2026-01-20T19:57:34+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Jeroen Ooms
  - Jenny Bryan
  - Hadley Wickham
  - Emil Hvitfeldt
  - Thomas Lin Pedersen
  - Neal Richardson
  repo: r-lib/cpp11
  stars: 222
  title: cpp11
  website: https://cpp11.r-lib.org/
---

cpp11 is a header-only C++ library that enables R package developers to write C++ code that interacts with R objects. It provides a modern alternative to Rcpp with similar syntax for interfacing C++ with R.

The package offers several technical improvements including enforced copy-on-write semantics, safer R API usage, ALTREP support, and UTF-8 string handling throughout. It compiles faster with lower memory requirements than alternatives and avoids ABI compatibility issues by being completely header-only. The library can be vendored into packages to lock header versions and uses efficient data structures for memory protection and vector growth operations.
