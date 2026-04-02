---
title: purrr 0.1.0
description: "Introducing purrr: functional programming tools for R with map functions, formula shortcuts for anonymous functions, and list manipulation."
auto-description: true
people:
  - Hadley Wickham
date: '2015-09-29'
categories:
  - Data Wrangling
slug: purrr-0-1-0
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - RStudio
ported_from: rstudio
port_status: in-progress
software: ["tidyverse"]
languages: ["R"]
ported_categories:
  - Packages
  - tidyverse
---


Purrr is a new package that fills in the missing pieces in R's functional programming tools: it's designed to make your pure functions purrr. Like many of my recent packages, it works with [magrittr](https://github.com/smbache/magrittr) to allow you to express complex operations by combining simple pieces in a standard way.

Install it with:

```r
install.packages("purrr")
```

Purrr wouldn't be possible without [Lionel Henry](https://github.com/lionel-). He wrote a lot of the package and his insightful comments helped me rapidly iterate towards a stable, useful, and understandable package.

## Map functions

The core of purrr is a set of functions for manipulating vectors (atomic vectors, lists, and data frames). The goal is similar to dplyr: help you tackle the most common 90% of data manipulation challenges. But where dplyr focusses on data frames, purrr focusses on vectors. For example, the following code splits the built-in mtcars dataset up by number of cylinders (using the base `split()` function), fits a linear model to each piece, summarises each model, then extracts the the \(R^2\):

```r
mtcars %>%
  split(.$cyl) %>%
  map(~lm(mpg ~ wt, data = .)) %>%
  map(summary) %>%
  map_dbl("r.squared")
#>     4     6     8
#> 0.509 0.465 0.423
```

The first argument to all map functions is the vector to operate on. The second argument, `.f` specifies what to do with each piece. It can be:

  * A function, like `summary()`.

  * A formula, which is converted to an anonymous function, so that `~ lm(mpg ~ wt, data = .)` is shorthand for `function(x) lm(mpg ~ wt, data = x)`.

  * A string or number, which is used to extract components, i.e. `"r.squared"` is shorthand for `function(x) x[[r.squared]]` and `1` is shorthand for `function(x) x[[1]]`.

Map functions come in a few different variations based on their inputs and output:

  * `map()` takes a vector (list or atomic vector) and returns a list. `map_lgl()`, `map_int()`, `map_dbl()`, and `map_chr()` take a vector and return an atomic vector. `flatmap()` works similarly, but allows the function to return arbitrary length vectors.

  * `map_if()` only applies `.f` to those elements of the list where `.p` is true. For example, the following snippet converts factors into characters:

```r
iris %>% map_if(is.factor, as.character) %>% str()
#> 'data.frame':    150 obs. of  5 variables:
#>  $ Sepal.Length: num  5.1 4.9 4.7 4.6 5 5.4 4.6 5 4.4 4.9 ...
#>  $ Sepal.Width : num  3.5 3 3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 ...
#>  $ Petal.Length: num  1.4 1.4 1.3 1.5 1.4 1.7 1.4 1.5 1.4 1.5 ...
#>  $ Petal.Width : num  0.2 0.2 0.2 0.2 0.2 0.4 0.3 0.2 0.2 0.1 ...
#>  $ Species     : chr  "setosa" "setosa" "setosa" "setosa" ...
```

`map_at()` works similarly but instead of working with a logical vector or predicate function, it works with a integer vector of element positions.

  * `map2()` takes a pair of lists and iterates through them in parallel:

```r
map2(1:3, 2:4, c)
#> [[1]]
#> [1] 1 2
#>
#> [[2]]
#> [1] 2 3
#>
#> [[3]]
#> [1] 3 4
map2(1:3, 2:4, ~ .x * (.y - 1))
#> [[1]]
#> [1] 1
#>
#> [[2]]
#> [1] 4
#>
#> [[3]]
#> [1] 9
```

`map3()` does the same thing for three lists, and `map_n()` does it in general.

  * `invoke()`, `invoke_lgl()`, `invoke_int()`, `invoke_dbl()`, and `invoke_chr()` take a list of functions, and call each one with the supplied arguments:

```r
list(m1 = mean, m2 = median) %>%
  invoke_dbl(rcauchy(100))
#>    m1    m2
#> 9.765 0.117
```

  * `walk()` takes a vector, calls a function on piece, and returns its original input. It's useful for functions called for their side-effects; it returns the input so you can use it in a pipe.

### Purrr and dplyr

I'm becoming increasingly enamoured with the list-columns in data frames. The following example combines purrr and dplyr to generate 100 random test-training splits in order to compute an unbiased estimate of prediction quality. These tools are still experimental (and currently need quite a bit of extra scaffolding), but I think the basic approach is really appealing.

```r
library(dplyr)
random_group <- function(n, probs) {
  probs <- probs / sum(probs)
  g <- findInterval(seq(0, 1, length = n), c(0, cumsum(probs)),
    rightmost.closed = TRUE)
  names(probs)[sample(g)]
}
partition <- function(df, n, probs) {
  n %>%
    replicate(split(df, random_group(nrow(df), probs)), FALSE) %>%
    zip_n() %>%
    as_data_frame()
}

msd <- function(x, y) sqrt(mean((x - y) ^ 2))

# Genearte 100 random test-training splits,
cv <- mtcars %>%
  partition(100, c(training = 0.8, test = 0.2)) %>%
  mutate(
    # Fit the model
    model = map(training, ~ lm(mpg ~ wt, data = .)),
    # Make predictions on test data
    pred = map2(model, test, predict),
    # Calculate mean squared difference
    diff = map2(pred, test %>% map("mpg"), msd) %>% flatten()
  )
cv
#> Source: local data frame [100 x 5]
#>
#>                   test             training   model     pred  diff
#>                 (list)               (list)  (list)   (list) (dbl)
#> 1  <data.frame [7,11]> <data.frame [25,11]> <S3:lm> <dbl[7]>  3.70
#> 2  <data.frame [7,11]> <data.frame [25,11]> <S3:lm> <dbl[7]>  2.03
#> 3  <data.frame [7,11]> <data.frame [25,11]> <S3:lm> <dbl[7]>  2.29
#> 4  <data.frame [7,11]> <data.frame [25,11]> <S3:lm> <dbl[7]>  4.88
#> 5  <data.frame [7,11]> <data.frame [25,11]> <S3:lm> <dbl[7]>  3.20
#> 6  <data.frame [7,11]> <data.frame [25,11]> <S3:lm> <dbl[7]>  4.68
#> 7  <data.frame [7,11]> <data.frame [25,11]> <S3:lm> <dbl[7]>  3.39
#> 8  <data.frame [7,11]> <data.frame [25,11]> <S3:lm> <dbl[7]>  3.82
#> 9  <data.frame [7,11]> <data.frame [25,11]> <S3:lm> <dbl[7]>  2.56
#> 10 <data.frame [7,11]> <data.frame [25,11]> <S3:lm> <dbl[7]>  3.40
#> ..                 ...                  ...     ...      ...   ...
mean(cv$diff)
#> [1] 3.22
```

## Other functions

There are too many other pieces of purrr to describe in detail here. A few of the most useful functions are noted below:

  * `zip_n()` allows you to turn a list of lists "inside-out":

```r
x <- list(list(a = 1, b = 2), list(a = 2, b = 1))
x %>% str()
#> List of 2
#>  $ :List of 2
#>   ..$ a: num 1
#>   ..$ b: num 2
#>  $ :List of 2
#>   ..$ a: num 2
#>   ..$ b: num 1

x %>%
  zip_n() %>%
  str()
#> List of 2
#>  $ a:List of 2
#>   ..$ : num 1
#>   ..$ : num 2
#>  $ b:List of 2
#>   ..$ : num 2
#>   ..$ : num 1

x %>%
  zip_n(.simplify = TRUE) %>%
  str()
#> List of 2
#>  $ a: num [1:2] 1 2
#>  $ b: num [1:2] 2 1
```

  * `keep()` and `discard()` allow you to filter a vector based on a predicate function. `compact()` is a helpful wrapper that throws away empty elements of a list.

```r
1:10 %>% keep(~. %% 2 == 0)
#> [1]  2  4  6  8 10
1:10 %>% discard(~. %% 2 == 0)
#> [1] 1 3 5 7 9

list(list(x = TRUE, y = 10), list(x = FALSE, y = 20)) %>%
  keep("x") %>%
  str()
#> List of 1
#>  $ :List of 2
#>   ..$ x: logi TRUE
#>   ..$ y: num 10

list(NULL, 1:3, NULL, 7) %>%
  compact() %>%
  str()
#> List of 2
#>  $ : int [1:3] 1 2 3
#>  $ : num 7
```

  * `lift()` (and friends) allow you to convert a function that takes multiple arguments into a function that takes a list. It helps you compose functions by lifting their domain from a kind of input to another kind. The domain can be changed to and from a list (l), a vector (v) and dots (d).

  * `cross2()`, `cross3()` and `cross_n()` allow you to create the Cartesian product of the inputs (with optional filtering).

  * A number of functions let you manipulate functions: `negate()`, `compose()`, `partial()`.

  * A complete set of predicate functions provides predictable versions of the `is.*` functions: `is_logical()`, `is_list()`, `is_bare_double()`, `is_scalar_character()`, etc.

  * Other equivalents functions wrap existing base R functions into to the consistent design of purrr: `replicate()` -> `rerun()`, `Reduce()` -> `reduce()`, `Find()` -> `detect()`, `Position()` -> `detect_index()`.

## Design philosophy

The goal of purrr is not try and turn R into Haskell in R: it does not implement currying, or destructuring binds, or pattern matching. The goal is to give you similar expressiveness to a classical FP language, while allowing you to write code that looks and feels like R.

  * Anonymous functions are verbose in R, so we provide two convenient shorthands. For predicate functions, `~ .x + 1` is equivalent to `function(.x) .x + 1`. For chains of transformations functions, `. %>% f() %>% g()` is equivalent to `function(.) . %>% f() %>% g()`.

  * R is weakly typed, so we can implement general `zip_n()`, rather than having to specialise on the number of arguments. That said, we still provide `map2()` and `map3()` since it's useful to clearly separate which arguments are vectorised over. Functions are designed to be output type-stable (respecting [Postel's law](https://en.wikipedia.org/wiki/Robustness_principle)) so you can rely on the output being as you expect.

  * R has named arguments, so instead of providing different functions for minor variations (e.g. `detect()` and `detectLast()`) we use a named arguments.

  * Instead of currying, we use `...` to pass in extra arguments. Arguments of purrr functions always start with `.` to avoid matching to the arguments of `.f` passed in via `...`.

  * Instead of point free style, use the pipe, `%>%`, to write code that can be read from left to right.

