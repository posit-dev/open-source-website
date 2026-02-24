---
description: Reimplementations of Functions Introduced Since R-3.0.0
github: r-lib/backports
languages:
- R
latest_release: '2024-08-12T09:35:38+00:00'
title: backports
website: ''

external:  # updated automatically, do not edit
  description: Reimplementations of Functions Introduced Since R-3.0.0
  first_commit: '2016-02-12T08:08:46+00:00'
  forks: 14
  languages:
  - R
  last_updated: '2026-02-24T09:26:34.643202+00:00'
  latest_release: '2024-08-12T09:35:38+00:00'
  repo: r-lib/backports
  stars: 66
  title: backports
  website: ''
---

The backports package provides implementations of functions and function arguments that were introduced in newer versions of base R, allowing package developers to use modern R features while maintaining compatibility with older R installations. When a package imports backports, R automatically uses the native version if available or falls back to the backported implementation for older R versions.

This package is particularly valuable for maintaining backward compatibility without writing conditional code or sacrificing access to useful new functions. It includes backports for dozens of base R functions introduced from version 3.2.0 through 4.3.0, such as `dir.exists()`, `startsWith()`, `isFALSE()`, and `deparse1()`. Package developers can import all backports or selectively import only the specific functions they need, making it easy to support users running older R versions without duplicating implementation code.
