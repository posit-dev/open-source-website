---
color: '#252B4D'
description: Generic programming with typed R vectors
github: r-lib/vctrs
image: logo.png
languages:
- C
latest_release: '2026-04-17T13:51:34+00:00'
people:
- Lionel Henry
- Davis Vaughan
- Hadley Wickham
- Jenny Bryan
- George Stagg
title: vctrs
topics:
- Best Practices
- Data Wrangling
website: https://vctrs.r-lib.org

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Generic programming with typed R vectors
  first_commit: '2016-09-06T21:32:53+00:00'
  forks: 72
  languages:
  - C
  last_updated: '2026-05-20T08:05:55.468987+00:00'
  latest_release: '2026-04-17T13:51:34+00:00'
  license: NOASSERTION
  people:
  - Lionel Henry
  - Davis Vaughan
  - Hadley Wickham
  - Jenny Bryan
  - George Stagg
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/vctrs
  stars: 301
  title: vctrs
  website: https://vctrs.r-lib.org
---

The vctrs package provides a framework for working with vectors in R through three core concepts: standardized definitions of size and type (via `vec_size()` and `vec_ptype()`), size-recycling and type-coercion rules, and a base class for creating new S3 vector types. It's designed as a developer-focused tool for building robust vector classes that work consistently across R packages.

This package solves the problem of inconsistent vector behavior in base R by establishing principles of size-stability and type-stability for functions. It simplifies the creation of new S3 vector types by providing a `vctr` base class with methods for many base generics, reducing implementation complexity. The framework enables package developers to create new vector classes that work seamlessly throughout the tidyverse ecosystem while maintaining minimal dependencies.
