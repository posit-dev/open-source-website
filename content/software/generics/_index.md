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
  description: Common generic methods
  first_commit: '2018-06-12T15:55:26+00:00'
  forks: 13
  languages:
  - R
  last_updated: '2026-02-17T11:35:00.806207+00:00'
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

The generics package provides a collection of S3 generic methods that package developers can import and re-export instead of depending on heavier packages like broom. This reduces the number of dependencies needed to implement common methods like `tidy()`, `fit()`, or `explain()` for custom objects.

The package solves the dependency problem where developers previously had to import entire packages just to access a single generic method. It's lightweight and contains only generic function definitions, allowing packages to implement methods without pulling in unnecessary dependencies. For example, the recipes package uses generics to define `tidy()` methods without depending on broom.
