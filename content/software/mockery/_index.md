---
color: '#419599'
description: A mocking library for R.
github: r-lib/mockery
image: logo.svg
languages:
- R
latest_release: '2025-09-03T20:06:59+00:00'
people:
- Hadley Wickham
title: mockery
website: ''

external:  # updated automatically, do not edit
  description: A mocking library for R.
  first_commit: '2016-07-18T18:54:06+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-03-05T16:26:19.009172+00:00'
  latest_release: '2025-09-03T20:06:59+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  repo: r-lib/mockery
  stars: 104
  title: mockery
  website: ''
---

The mockery package provides mocking and stubbing capabilities for R unit tests, allowing you to replace functions with test doubles during testing. It is primarily used to isolate code under test by controlling dependencies and verifying function interactions.

The package offers several advantages over alternatives like testthat's with_mock: it supports mocking primitive functions, safely handles functions from base R packages without JIT compiler conflicts, and provides fine-grained control through depth parameters for nested function calls. Mock objects track how they were called, enabling assertions about call counts and arguments. However, the package is now superseded in favor of testthat::local_mocked_bindings() for new test code.
