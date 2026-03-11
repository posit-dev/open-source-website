---
image: logo.svg
color: "#419599"
description: Manage the life cycle of your exported functions and arguments
github: r-lib/lifecycle
languages:
- R
latest_release: '2026-01-09T14:10:39+00:00'
people:
- Lionel Henry
- Hadley Wickham
- Davis Vaughan
- Hannah Frick
- Jenny Bryan
- Jeroen Janssens
title: lifecycle
website: https://lifecycle.r-lib.org

external:  # updated automatically, do not edit
  description: Manage the life cycle of your exported functions and arguments
  first_commit: '2018-12-27T16:31:45+00:00'
  forks: 25
  languages:
  - R
  last_updated: '2026-03-05T16:28:38.358223+00:00'
  latest_release: '2026-01-09T14:10:39+00:00'
  license: NOASSERTION
  people:
  - Lionel Henry
  - Hadley Wickham
  - Davis Vaughan
  - Hannah Frick
  - Jenny Bryan
  - Jeroen Janssens
  repo: r-lib/lifecycle
  stars: 92
  title: lifecycle
  website: https://lifecycle.r-lib.org
---

lifecycle provides a set of tools and conventions to manage the life cycle of your exported R functions. It helps package developers communicate the status and stability of their functions to users.

The package defines clear stages for functions (experimental, stable, deprecated, superseded) and provides tools to both signal these states to users and handle lifecycle changes in dependencies. It establishes consistent conventions for evolving APIs over time, making it easier for developers to maintain packages and for users to understand which functions are safe to rely on. The package emerged from practices developed while maintaining the tidyverse.
