---
description: An alternative conflict resolution strategy for R
github: r-lib/conflicted
languages:
- R
latest_release: '2023-01-31T19:50:16+00:00'
people:
- Hadley Wickham
- Lionel Henry
title: conflicted
website: https://conflicted.r-lib.org/

external:
  contributors:
  - hadley
  - krlmlr
  - batpigandme
  - klmr
  - lionel-
  - MichaelChirico
  - nerskin
  - romainfrancois
  description: An alternative conflict resolution strategy for R
  first_commit: '2018-05-20T23:37:42+00:00'
  forks: 14
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.747336+00:00'
  latest_release: '2023-01-31T19:50:16+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  repo: r-lib/conflicted
  stars: 254
  title: conflicted
  website: https://conflicted.r-lib.org/
---

conflicted provides an alternative conflict resolution strategy for R that makes function name conflicts explicit rather than silent. When multiple packages export functions with the same name, R normally uses the most recently loaded version without warning, which can lead to hard-to-debug errors, especially when package updates introduce new naming overlaps. conflicted takes a different approach by turning every conflict into an error, forcing you to explicitly choose which function to use either by declaring session-wide preferences with `conflicts_prefer()` or by using namespaced calls like `dplyr::filter()`.

This pragmatic middle-ground approach helps data scientists and R developers avoid the subtle bugs that arise from function masking, without requiring the upfront overhead of explicitly importing every function. By catching ambiguous function calls at runtime with clear error messages, conflicted makes your R code more predictable and maintainable while preserving the convenience of R's package system.
