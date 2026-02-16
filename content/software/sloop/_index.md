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
  contributors:
  - hadley
  - jimhester
  - krlmlr
  - mgirlich
  description: S language OOP ⛵️
  first_commit: '2017-02-08T18:50:26+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.320817+00:00'
  latest_release: '2019-02-17T15:12:20+00:00'
  people:
  - Hadley Wickham
  readme_image: man/figures/logo.png
  repo: r-lib/sloop
  stars: 103
  title: sloop
  website: https://sloop.r-lib.org
---

Understanding object-oriented programming in R can be challenging, especially when working with S3, R's most commonly used OO system. sloop provides a suite of interactive tools designed to help you explore and understand how S3 method dispatch works in practice. Whether you're trying to figure out which method gets called for a specific function, identify the type of object or function you're working with, or discover all methods associated with a generic or class, sloop gives you the visibility you need to navigate R's OO systems with confidence.

At the heart of sloop is `s3_dispatch()`, which shows you exactly which methods are considered, found, and called for any function invocation. The package handles the full complexity of S3 dispatch including group generics, internal generics, implicit classes, and `NextMethod()` chains. Additional utilities like `ftype()` and `otype()` help you quickly identify whether you're dealing with S3, S4, R6, or base objects and functions, while `s3_methods_class()` and `s3_methods_generic()` let you explore the complete method landscape for any class or generic. These tools make sloop an essential companion for anyone learning R's OO systems or debugging method dispatch issues in their code.
