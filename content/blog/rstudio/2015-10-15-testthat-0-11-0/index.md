---
title: testthat 0.11.0
people:
  - Hadley Wickham
date: '2015-10-15'
categories:
- Packages
slug: testthat-0-11-0
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
software: ["testthat"]
languages: ["R"]
---


testthat 0.11.0 is now available on CRAN. Testthat makes it easy to turn your existing informal tests into formal automated tests that you can rerun quickly and easily. Learn more at <http://r-pkgs.had.co.nz/tests.html>. Install the latest version with:

```r
install.packages("testthat")
```

In this version:

  * New `expect_silent()` ensures that code produces no output, messages, or warnings. `expect_output()`, `expect_message()`, `expect_warning()`, and `expect_error()` now accept `NA` as the second argument to indicate that there shouldn't be any output, messages, warnings, or errors (i.e. they should be missing)

```r
f <- function() {
  print(1)
  message(2)
  warning(3)
}
expect_silent(f())
#> Error: f() produced output, warnings, messages

expect_warning(log(-1), NA)
#> Error: log(-1) expected no warnings:
#> *  NaNs produced
```

  * Praise gets more diverse thanks to Gabor Csardi's [praise](https://github.com/gaborcsardi/praise) package, and you now also get random encouragment if your tests don't pass.

  * testthat no longer muffles warning messages. This was a bug in the previous version, as warning messages are usually important and should be dealt with explicitly, either by resolving the problem or explicitly capturing them with `expect_warning()`.

  * Two new skip functions make it easier to skip tests that don't work in certain environments: `skip_on_os()` skips tests on the specified operating system, and `skip_on_appveyor()` skips tests on [Appveyor](http://www.appveyor.com).

There were a number of other minor improvements and bug fixes. See the [release notes](https://github.com/hadley/testthat/releases/tag/v0.11.0) for a complete list.

A big thanks goes out to all the contributors who made this release happen. There's no way I could be as productive without the fantastic commmunity of R developers who come up with thoughtful new features, and who discover and fix my bugs!

