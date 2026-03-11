---
title: devtools 1.5
people:
  - Hadley Wickham
date: '2014-04-08'
categories:
- Packages
slug: devtools-1-5
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
events: blog
ported_from: rstudio
port_status: raw
---


devtools 1.5 is now available on CRAN. It includes four new functions to make it easier to add useful infrastructure to packages:

  * `add_test_infrastructure()` will create testthat infrastructure when needed.

  * `add_rstudio_project()` adds an Rstudio project file to your package.

  * `add_travis()` adds a basic template for [travis-ci](https://travis-ci.org/).

  * `add_build_ignore()` makes it easy to add files to `.Rbuildignore`,
escaping special characters as needed.

We've also bumped two dependencies: devtools now requires R 3.0.2 and roxygen2 3.0.0. We've also included many minor improvements and bug fixes, particularly for package installation. For example `install_github()` now prefers the safer github personal access token, and does a better job of installing the dependencies that you actually need. We also provide versions of `help()`, `?` and `system.file()` that work with all packages, regardless of how they're loaded. See a complete list of changes in the [full release notes](https://github.com/hadley/devtools/releases/tag/v1.5).

