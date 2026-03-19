---
title: testthat 0.10.0
people:
  - Hadley Wickham
date: '2015-05-29'
slug: testthat-0-10-0
ported_from: rstudio
port_status: in-progress
software: ["testthat"]
languages: ["R"]
---


testthat 0.10.0 is now available on CRAN. Testthat makes it easy to turn the informal testing that you're already doing into formal automated tests. Learn more at <http://r-pkgs.had.co.nz/tests.html>. Install the latest version with:

```r
install.packages("testthat")
```

There are four big changes in this release:

  * `test_check()` uses a new reporter specifically designed for R CMD check. It displays a summary at the end of the tests, designed to be <13 lines long so test failures in R CMD check display are as useful as possible.

  * New `skip_if_not_installed()` skips tests if a package isn't installed: this is useful if you want tests to skip if a suggested package isn't installed.

  * The `expect_that(a, equals(b))` style of testing has been soft-deprecated in favour of `expect_equals(a, b)`. It will keep working, but it's no longer demonstrated in the documentation, and new expectations will only be available in `expect_equal(a, b)` style.

  * `compare()` is now documented and exported: compare is used to display test failures for `expect_equal()`, and is designed to help you spot exactly where the failure occured. It currently has methods for character and numeric vectors.

There were a number of other minor improvements and bug fixes. See the [release notes](https://github.com/hadley/testthat/releases/tag/v0.10.0) for a complete list.

