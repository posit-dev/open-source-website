---
title: testthat 0.8 (and 0.8.1)
people:
  - Hadley Wickham
date: '2014-02-25'
categories:
- Packages
slug: testthat-0-8
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
events: blog
ported_from: rstudio
port_status: raw
---


We're pleased to announce a new major version of testthat. Version 0.8 comes with a new recommended structure for storing your tests. To better meet CRAN recommended practices, we now recommend that tests live in `tests/testthat`, instead of `inst/tests`. This makes it possible for users to choose whether or not to install tests. With this new structure, you'll need to use `test_check()` instead of `test_packages()` in the test file (usually `tests/testthat.R`) that runs all testthat unit tests.

Another big improvement comes from [Karl Forner](https://github.com/kforner). He contributed code which provides line numbers in test errors so you can see exactly where the problems are. There are also four new expectations (`expect_null()`, `expected_named()`, `expect_more_than()`, `expect_less_than()`) and many other minor improvements and bug fixes. For a complete list of changes, please see the [github release](https://github.com/hadley/testthat/releases/tag/v0.8). After release of 0.8 to CRAN, we discovered two small bugs. These were fixed in [0.8.1](https://github.com/hadley/testthat/releases/tag/v0.8.1).

As always, you can install the latest version with `install.packages("testthat")`.

