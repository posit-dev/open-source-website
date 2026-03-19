---
title: testthat 0.9
people:
  - Hadley Wickham
date: '2014-09-23'
categories:
  - Best Practices
slug: testthat-0-9
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - RStudio
ported_from: rstudio
port_status: in-progress
software: ["testthat"]
languages: ["R"]
ported_categories:
  - Packages
---


testthat 0.9 is now available on CRAN. Testthat makes it easy to turn the informal testing that you're already doing into formal automated tests. Learn more at <http://r-pkgs.had.co.nz/tests.html>

This version of testthat has four important new features that bring testthat up to speed with unit testing frameworks in other languages:

  * You can `skip()` tests with an informative message, if their prerequisites are not available. This is particularly use for CRAN packages, since tests only have a limited amount of time to run. Use `skip_on_cran()` skip selected tests when run on CRAN.

```r
test_that("a complicated simulation takes a long time", {
  skip_on_cran()

  ...
})
```

  * Experiment with behaviour driven development with the new `describe()` function contributed by [Dirk Schumacher](https://github.com/dirkschumacher):

```r
describe("matrix()", {
  it("can be multiplied by a scalar", {
    m1 <- matrix(1:4, 2, 2)
    m2 <- m1 * 2
    expect_equivalent(matrix(1:4 * 2, 2, 2), m2)
  })
})
```

  * Use `with_mock()` to "mock" functions, replacing slow, resource intensive or inconsistent functions with your own quick approximations. This is particularly useful when you want to test functions that call web APIs without being connected to the internet. Contributed by [Kirill Müller](https://github.com/krlmlr).

  * Sometimes it's difficult to figure out exactly what a function should return and instead you just want to make sure that it returned the same thing as the last time you ran it. A new expectation, `expect_equal_to_reference()`, makes this easy to do. Contributed by [Jon Clayden](https://github.com/jonclayden).

Other changes of note: `auto_test_package()` is working again (and uses `devtools::load_all()` to load the code), random praise has been re-enabled (after being accidentally disabled), and `expect_identical()` works better with R-devel. See the [release notes](https://github.com/hadley/testthat/releases/tag/v0.9) for complete list of changes.

