
<!-- README.md is generated from README.Rmd. Please edit that file -->

# rray <a href='https:/rray.r-lib.org'><img src='man/figures/logo.png' align="right" height="139" /></a>

<!-- badges: start -->

[![Lifecycle:
experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)
[![Travis build
status](https://travis-ci.org/r-lib/rray.svg?branch=master)](https://travis-ci.org/r-lib/rray)
[![Codecov test
coverage](https://codecov.io/gh/r-lib/rray/branch/master/graph/badge.svg)](https://codecov.io/gh/r-lib/rray?branch=master)
<!-- badges: end -->

rray (said: “r-ray”) is an array manipulation library for R. It has
three main goals:

  - To provide an rray class that tries to be stricter and more
    consistent than base R arrays, similar in spirit to tibble.
  - To support broadcasting throughout the package, which allows for
    novel yet intuitive array operations that have been missing from the
    R ecosystem.
  - To provide a consistent, powerful toolkit for array based
    manipulation, usable by both the new rray objects and base R
    matrices/arrays.

A set of slides, presented by David Vaughan at useR\! 2019, introducing
the package and showing it’s utility can be found on
[speakerdeck](https://speakerdeck.com/davisvaughan/user-2019-rray).

View the vignettes for each goal on [the
website](https://rray.r-lib.org) to learn more about how to use rray.

  - `vignette("the-rray")`
  - `vignette("broadcasting")`
  - `vignette("toolkit")`

<!-- end list -->

``` r
library(rray)
```

## What can it do?

In short, rray tries to make array manipulation in R more intuitive by
combining the idea of broadcasting with knowing when to *not* drop
dimensions. This results in operations such as:

``` r
x <- rray(1:6, dim = c(3, 2))

# Compute proportions along the 1st dimension
x / rray_sum(x, axes = 1)
#> <rray<dbl>[,2][3]>
#>           [,1]      [,2]
#> [1,] 0.1666667 0.2666667
#> [2,] 0.3333333 0.3333333
#> [3,] 0.5000000 0.4000000

# Equivalent base R syntax
sweep(x, 2, apply(x, 2, sum), "/")
#> <rray<dbl>[,2][3]>
#>           [,1]      [,2]
#> [1,] 0.1666667 0.2666667
#> [2,] 0.3333333 0.3333333
#> [3,] 0.5000000 0.4000000
```

These concepts are baked into every part of rray, and show up in other
functions such as `rray_bind()`. Using broadcasting, `rray_bind()` can
bind arrays together in ways that base R cannot with the native
`cbind()` and `rbind()` functions.

``` r
a <- array(c(1, 2), dim = c(2, 1))
b <- array(c(3, 4), dim = c(1, 2))

a
#>      [,1]
#> [1,]    1
#> [2,]    2

b
#>      [,1] [,2]
#> [1,]    3    4

# Error
cbind(a, b)
#> Error in cbind(a, b): number of rows of matrices must match (see arg 2)

# `a` is first broadcast to have dimensions: (2, 2)
rray_bind(a, b, .axis = 1)
#>      [,1] [,2]
#> [1,]    1    1
#> [2,]    2    2
#> [3,]    3    4

# Error
rbind(a, b)
#> Error in rbind(a, b): number of columns of matrices must match (see arg 2)

# `b` is first broadcast to have dimensions: (2, 2)
rray_bind(a, b, .axis = 2)
#>      [,1] [,2] [,3]
#> [1,]    1    3    4
#> [2,]    2    3    4
```

## Installation

You can install from CRAN with:

``` r
install.packages("rray")
```

You can install the development version from Github with:

``` r
remotes::install_github("r-lib/rray")
```

## Acknowledgements

rray would not be possible without the underlying C++ library,
[`xtensor`](https://github.com/QuantStack/xtensor). Additionally, rray
uses a large amount of the infrastructure in
[`vctrs`](https://github.com/r-lib/vctrs) to be as consistent and type
stable as possible.

## Alternatives

The Matrix package implements a small subset of column-wise broadcasting
operations. rray fully supports broadcasting in all operations.

The original motivation for this package, and even for xtensor, is the
excellent Python library, NumPy. As far as I know, it has the original
implementation of broadcasting, and is a core library that a huge number
of others are built on top of.

In the past, the workhorse for flexibly binding arrays together has been
the abind package. This package has been a great source of inspiration
and has served as a nice benchmark for rray.

## Notes

Currently, rray does not handle missing values in arithmetic operations
and the reducing functions. This is coming, as the underlying library
xtensor natively supports missing values, however a few upstream bugs
are currently preventing rray from using those features.

rray will perform best on R 3.6.0 and above. It is able to take
advantage of a few of the ALTREP features there, which result in less
copies being made per function call.
