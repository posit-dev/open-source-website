---
description: Common generic methods
github: r-lib/generics
languages:
- R
latest_release: '2025-05-09T18:17:34+00:00'
people:
- Max Kuhn
- Davis Vaughan
- Hadley Wickham
- Hannah Frick
title: generics
website: https://generics.r-lib.org/

external:
  contributors:
  - topepo
  - DavisVaughan
  - hadley
  - mitchelloharawild
  - hfrick
  - batpigandme
  - alexpghayes
  - dpprdan
  - config-i1
  - jimhester
  description: Common generic methods
  first_commit: '2018-06-12T15:55:26+00:00'
  forks: 13
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.763803+00:00'
  latest_release: '2025-05-09T18:17:34+00:00'
  license: NOASSERTION
  people:
  - Max Kuhn
  - Davis Vaughan
  - Hadley Wickham
  - Hannah Frick
  repo: r-lib/generics
  stars: 61
  title: generics
  website: https://generics.r-lib.org/
---

The generics package solves a critical dependency management challenge for R package developers. When creating packages that use S3 methods, developers often need to import entire packages just to access a single generic function. For example, using `tidy()` traditionally required importing the full broom package, even if you only needed the generic definition. The generics package provides a lightweight, focused solution by offering a curated collection of commonly used generic methods that can be imported without the overhead of large dependencies.

By providing generic functions like `fit()`, `tidy()`, `glance()`, `augment()`, and `explain()` in one minimal package, generics enables cleaner package architecture and faster installation times. Package authors can import just the generics they need, define their S3 methods, and re-export them to users—all while maintaining a lean dependency footprint. This approach has been adopted by popular packages like recipes, which transitioned from depending on broom to using generics instead, demonstrating the practical benefits of this streamlined workflow for both package developers and end users.
