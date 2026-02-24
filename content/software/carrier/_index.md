---
description: Create standalone functions for remote execution
github: r-lib/carrier
languages:
- R
latest_release: '2025-09-11T09:52:03+00:00'
people:
- Lionel Henry
- Charlie Gao
title: carrier
website: ''

external:  # updated automatically, do not edit
  description: Create standalone functions for remote execution
  first_commit: '2018-08-22T16:01:23+00:00'
  forks: 3
  languages:
  - R
  last_updated: '2026-02-24T09:26:35.678459+00:00'
  latest_release: '2025-09-11T09:52:03+00:00'
  license: NOASSERTION
  people:
  - Lionel Henry
  - Charlie Gao
  repo: r-lib/carrier
  stars: 67
  title: carrier
  website: ''
---

The carrier package provides tools for packaging R functions so they can be safely sent to remote R sessions or different processes. It helps you explicitly control what data and dependencies are bundled with your functions and monitor the size of the packaged result.

The package addresses the problem of implicit dependencies and hidden data references that can cause functions to fail when moved to different environments. It requires explicit namespace prefixes for non-base functions and provides two methods for packaging data: passing objects as named arguments or unquoting them inline with `!!`. The crated functions display their total size and break down the size of each component, making it easy to track what you're sending to remote processes.
