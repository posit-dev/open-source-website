---
title: testthat 1.0.0
people:
  - Hadley Wickham
date: '2016-04-29'
categories:
- Packages
slug: testthat-1-0-0
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
events: blog
ported_from: rstudio
port_status: in-progress
---


testthat 1.0.0 is now available on CRAN. Testthat makes it easy to turn your existing informal tests into formal automated tests that you can rerun quickly and easily. Learn more at <http://r-pkgs.had.co.nz/tests.html>. Install the latest version with:

```r
install.packages("testthat")
```

This version of testthat saw a major behind the scenes overhaul. This is the reason for the 1.0.0 release, and it will make it easier to add new expectations and reporters in the future. As well as the internal changes, there are improvements in four main areas:

  * New expectations.

  * Support for the pipe.

  * More consistent tests for side-effects.

  * Support for testing C++ code.

These are described in detail below. For a complete set of changes, please see the [release notes](https://github.com/hadley/testthat/releases/tag/v1.0.0).

## Improved expectations

There are five new expectations:

  * `expect_type()` checks the base type of an object (with `typeof()`), `expect_s3_class()` tests that an object is S3 with given class, and `expect_s4_class()` tests that an object is S4 with given class. I recommend using these more specific expectations instead of the generic `expect_is()`, because they more clearly convey intent.

  * `expect_length()` checks that an object has expected length.

  * `expect_output_file()` compares output of a function with a text file, optionally update the file. This is useful for regression tests for `print()` methods.

A number of older expectations have been deprecated:

  * `expect_more_than()` and `expect_less_than()` have been deprecated. Please use `expect_gt()` and `expect_lt()` instead.

  * `takes_less_than()` has been deprecated.

  * `not()` has been deprecated. Please use the explicit individual forms `expect_error(..., NA)` , `expect_warning(.., NA)`, etc.

We also did a thorough review of the documentation, ensuring that related expectations are documented together.

## Piping

Most expectations now invisibly return the input `object`. This makes it possible to chain together expectations with magrittr:

```r
factor("a") %>%
  expect_type("integer") %>%
  expect_s3_class("factor") %>%
  expect_length(1)
```

To make this style even easier, testthat now imports and re-exports the pipe so you don't need to explicitly attach magrittr.

## Side-effects

Expectations that test for side-effects (i.e. `expect_message()`, `expect_warning()`, `expect_error()`, and `expect_output()`) are now more consistent:

  * `expect_message(f(), NA)` will fail if a message is produced (i.e. it's not missing), and similarly for `expect_output()`, `expect_warning()`, and `expect_error()`.

```r
quiet <- function() {}
noisy <- function() message("Hi!")

expect_message(quiet(), NA)
expect_message(noisy(), NA)
#> Error: noisy() showed 1 message.
#> * Hi!
```

  * `expect_message(f(), NULL)` will fail if a message isn't produced, and similarly for `expect_output()`, `expect_warning()`, and `expect_error()`.

```r
expect_message(quiet(), NULL)
#> Error: quiet() showed 0 messages
expect_message(noisy(), NULL)
```

There were three other changes made in the interest of consistency:

  * Previously testing for one side-effect (e.g. messages) tended to muffle other side effects (e.g. warnings). This is no longer the case.

  * Warnings that are not captured explicitly by `expect_warning()` are tracked and reported. These do not currently cause a test suite to fail, but may do in the future.

  * If you want to test a print method, `expect_output()` now requires you to explicitly print the object: `expect_output("a", "a")` will fail, `expect_output(print("a"), "a")` will succeed. This makes it more consistent with the other side-effect functions.

## C++

Thanks to the work of [Kevin Ushey](http://github.com/kevinushey), testthat now includes a simple interface to unit test C++ code using the [Catch](https://github.com/philsquared/Catch) library. Using Catch in your packages is easy – just call `testthat::use_catch()` and the necessary infrastructure, alongside a few sample test files, will be generated for your package. By convention, you can place your unit tests in `src/test-<name>.cpp`. Here's a simple example of a test file you might write when using testthat + Catch:

    #include <testthat.h>
    context("Addition") {
      test_that("two plus two equals four") {
        int result = 2 + 2;
        expect_true(result == 4);
      }
    }

These unit tests will be compiled and run during calls to `devtools::test()`, as well as `R CMD check`. See `?use_catch` for a full list of functions supported by testthat, and for more details.

For now, Catch unit tests will only be compiled when using the gcc and clang compilers – this implies that the unit tests you write will not be compiled + run on Solaris, which should make it easier to submit packages that use testthat for C++ unit tests to CRAN.

