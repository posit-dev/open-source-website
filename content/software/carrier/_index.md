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

external:
  contributors:
  - lionel-
  - shikokuchuo
  - batpigandme
  description: Create standalone functions for remote execution
  first_commit: '2018-08-22T16:01:23+00:00'
  forks: 3
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.829872+00:00'
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

Carrier makes it easy to package R functions for execution in remote sessions or different processes. When working with distributed computing frameworks, parallel processing, or cloud environments, functions often fail because they rely on hidden dependencies that don't exist in the remote context. Carrier solves this problem by providing tools to create self-contained "crates" that bundle functions with their required dependencies and data, ensuring they work reliably wherever they're sent.

The package's `crate()` function helps you explicitly declare what your function needs to run, from namespace requirements to data objects. Carrier enforces best practices by requiring namespace prefixes for non-base functions, preventing subtle bugs that only appear in production. It also displays the total size of packaged functions, giving you visibility into data transmission costs before deploying to remote workers. Whether you're running parallel computations across cores or distributing workloads to cloud instances, carrier ensures your functions arrive complete and ready to execute.
