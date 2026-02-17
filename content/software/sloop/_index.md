---
description: S language OOP ⛵️
github: r-lib/sloop
image: logo.png
languages:
- R
latest_release: '2019-02-17T15:12:20+00:00'
people:
- Hadley Wickham
title: sloop
website: https://sloop.r-lib.org

external:
  description: S language OOP ⛵️
  first_commit: '2017-02-08T18:50:26+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-02-17T11:34:00.669747+00:00'
  latest_release: '2019-02-17T15:12:20+00:00'
  people:
  - Hadley Wickham
  readme_image: man/figures/logo.png
  repo: r-lib/sloop
  stars: 103
  title: sloop
  website: https://sloop.r-lib.org
---

sloop is an R package that provides interactive tools for exploring and understanding object-oriented programming in R, with a focus on the S3 system. It helps developers inspect method dispatch, function types, and class relationships during development and debugging.

The package solves the problem of S3's often opaque behavior by making method dispatch visible and traceable. Key features include `s3_dispatch()` which shows exactly which methods are considered and called for any function, support for complex dispatch scenarios like group generics and NextMethod(), and utilities to identify function types (`ftype()`), object types (`otype()`), and enumerate all methods for a class or generic. This makes it particularly useful for understanding how S3 works under the hood and debugging method dispatch issues.
