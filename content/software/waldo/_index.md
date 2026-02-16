---
description: Find differences between R objects
github: r-lib/waldo
image: unnamed-chunk-2.svg
languages:
- R
latest_release: '2025-07-11T13:26:57+00:00'
people:
- Hadley Wickham
- Davis Vaughan
- Tomasz Kalinowski
title: waldo
website: http://waldo.r-lib.org/

external:
  contributors:
  - hadley
  - krlmlr
  - DavisVaughan
  - torockel
  - olivroy
  - MichaelChirico
  - averissimo
  - brodieG
  - batpigandme
  - mnazarov
  - mgirlich
  - michaelquinn32
  - sorhawell
  - t-kalinowski
  - dmurdoch
  description: Find differences between R objects
  first_commit: '2020-03-29T16:00:40+00:00'
  forks: 21
  languages:
  - R
  last_updated: '2026-02-13T14:17:20.225354+00:00'
  latest_release: '2025-07-11T13:26:57+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Davis Vaughan
  - Tomasz Kalinowski
  readme_image: man/figures/README/unnamed-chunk-2.svg
  repo: r-lib/waldo
  stars: 300
  title: waldo
  website: http://waldo.r-lib.org/
---

When your R unit tests fail, tracking down exactly what went wrong can be frustrating. waldo makes this detective work effortless by finding and clearly describing the differences between two R objects. Inspired by `all.equal()` but designed with developer experience in mind, waldo provides intelligent, color-coded diffs that highlight what actually changed, ordered from most to least important. Whether you're comparing atomic vectors, nested lists, or complex data frames, waldo generates actionable insights by showing differences with executable R code paths, comparing elements by name rather than position, and displaying just enough context to understand the issue without overwhelming you with output.

waldo's smart comparison engine adapts to your console width and data structure complexity. For vectors, it produces git-style diffs showing additions, deletions, and changes with surrounding context. For nested objects like lists and data frames, it creates precise code paths that pinpoint exactly where differences occur, even in deeply recursive structures. This makes waldo an indispensable tool for package developers and data scientists who need to quickly understand test failures and validate data transformations.
