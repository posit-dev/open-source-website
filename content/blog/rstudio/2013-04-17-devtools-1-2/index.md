---
title: Version 1.2 of devtools released
description: "devtools 1.2 speeds up installation, supports R 3.0 vignettes, and adds sha verification for source_url()."
auto-description: true
people:
  - Hadley Wickham
date: '2013-04-17'
categories:
  - Best Practices
slug: devtools-1-2
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - RStudio
ported_from: rstudio
port_status: in-progress
software: ["devtools"]
languages: ["R"]
ported_categories:
  - Packages
---


We're very pleased to announce the release of devtools 1.2. This version continues to make working with packages easier by increasing installation speed (skipping the build step unless `local = FALSE`), enhancing vignette handling (to support the non-Sweave vignettes available in R 3.0.0), and providing better default compiler flags for C and C++ code.

Also new in this release is the `sha` argument to `source_url` and `source_gist`. If provided, this checks that the file you download is what your expected, and is an important safety feature when running scripts over the web.

Devtools 1.2 contains many other bug fixes and minor improvements; to see them all, please read the [NEWS](https://github.com/hadley/devtools/blob/master/NEWS) file on github.

