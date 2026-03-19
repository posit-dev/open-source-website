---
title: memoise 1.0.0
people:
  - Jim Hester
date: '2016-02-02'
categories:
- Packages
slug: memoise-1-0-0
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
software: ["memoise"]
languages: ["R"]
---


We are pleased to announce version 1.0.0 of the memoise package is now available on [CRAN](https://cran.r-project.org/web/packages/memoise/). [Memoization](https://en.wikipedia.org/wiki/Memoization) stores the value of function call and returns the cached result when the function is called again with the same arguments.

The following function computes [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) and illustrates the usefulness of memoization. Because the function definition is recursive, the intermediate results can be looked up rather than recalculated at each level of recursion, which reduces the runtime drastically. The last time the memoised function is called the final result can simply be returned, so no measurable execution time is recorded.

```r
fib <- function(n) {
  if (n < 2) {
    return(n)
  } else {
    return(fib(n-1) + fib(n-2))
  }
}
system.time(x <- fib(30))
#>    user  system elapsed
#>   4.454   0.010   4.472
fib <- memoise(fib)
system.time(y <- fib(30))
#>    user  system elapsed
#>   0.004   0.000   0.004
system.time(z <- fib(30))
#>    user  system elapsed
#>       0       0       0
all.equal(x, y)
#> [1] TRUE
all.equal(x, z)
#> [1] TRUE
```

Memoization is also very useful for storing queries to external resources, such as network APIs and databases.

Improvements in this release make memoised functions much nicer to use interactively. Memoised functions now have a print method which outputs the original function definition rather than the memoization code.

```r
mem_sum <- memoise(sum)
mem_sum
#> Memoised Function:
#> function (..., na.rm = FALSE)  .Primitive("sum")
```

Memoised functions now forward their arguments from the original function rather than simply passing them with `...`. This allows autocompletion to work transparently for memoised functions and also fixes a bug related to non-constant default arguments. [[1](https://github.com/hadley/memoise/issues/6)]

```r
mem_scan <- memoise(scan)
args(mem_scan)
#> function (file = "", what = double(), nmax = -1L, n = -1L, sep = "",
#>     quote = if (identical(sep, "\n")) "" else "'\"", dec = ".",
#>     skip = 0L, nlines = 0L, na.strings = "NA", flush = FALSE,
#>     fill = FALSE, strip.white = FALSE, quiet = FALSE, blank.lines.skip = TRUE,
#>     multi.line = TRUE, comment.char = "", allowEscapes = FALSE,
#>     fileEncoding = "", encoding = "unknown", text, skipNul = FALSE)
#> NULL
```

Memoisation can now depend on external variables aside from the function arguments. This feature can be used in a variety of ways, such as invalidating the memoisation when a new package is attached.

```r
mem_f <- memoise(runif, ~search())
mem_f(2)
#> [1] 0.009113091 0.988083122
mem_f(2)
#> [1] 0.009113091 0.988083122
library(ggplot2)
mem_f(2)
#> [1] 0.89150566 0.01128355
```

Or invalidating the memoisation after a given amount of time has elapsed. A `timeout()` helper function is provided to make this feature easier to use.

```r
mem_f <- memoise(runif, ~timeout(10))
mem_f(2)
#> [1] 0.6935329 0.3584699
mem_f(2)
#> [1] 0.6935329 0.3584699
Sys.sleep(10)
mem_f(2)
#> [1] 0.2008418 0.4538413
```

A great amount of thanks for this release goes to [Kirill Müller](http://krlmlr.github.io/), who wrote the argument forwarding implementation and added comprehensive tests to the package. [[2](https://github.com/hadley/memoise/pull/13), [3](https://github.com/hadley/memoise/pull/14)]

See the [release notes](https://github.com/hadley/memoise/releases/tag/v1.0.0) for a complete list of changes.

