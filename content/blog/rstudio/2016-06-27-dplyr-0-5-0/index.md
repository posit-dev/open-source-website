---
title: dplyr 0.5.0
people:
  - Hadley Wickham
date: '2016-06-27'
categories:
  - Data Wrangling
slug: dplyr-0-5-0
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - tidyverse
ported_from: rstudio
port_status: in-progress
software: ["tidyverse"]
languages: ["R"]
ported_categories:
  - Packages
  - tidyverse
---


I'm very pleased to announce that dplyr 0.5.0 is now available from CRAN. Get the latest version with:

```r
install.packages("dplyr")
```

dplyr 0.5.0 is a big release with a heap of new features, a whole bunch of minor improvements, and many bug fixes, both from me and from the broader dplyr community. In this blog post, I'll highlight the most important changes:

  * Some breaking changes to single table verbs.

  * New tibble and dtplyr packages.

  * New vector functions.

  * Replacements for `summarise_each()` and `mutate_each()`.

  * Improvements to SQL translation.

To see the complete list, please read the [release notes](https://github.com/hadley/dplyr/releases/tag/v0.5.0).

## Breaking changes

`arrange()` once again ignores grouping, reverting back to the behaviour of dplyr 0.3 and earlier. This makes `arrange()` inconsistent with other dplyr verbs, but I think this behaviour is generally more useful. Regardless, it's not going to change again, as more changes will just cause more confusion.

```r
mtcars %>%
  group_by(cyl) %>%
  arrange(desc(mpg))
#> Source: local data frame [32 x 11]
#> Groups: cyl [3]
#>
#> # A tibble: 32 x 11
#>     mpg   cyl  disp    hp  drat    wt  qsec    vs    am  gear  carb
#>   <dbl> <dbl> <dbl> <dbl> <dbl> <dbl> <dbl> <dbl> <dbl> <dbl> <dbl>
#> 1  33.9     4  71.1    65  4.22 1.835 19.90     1     1     4     1
#> 2  32.4     4  78.7    66  4.08 2.200 19.47     1     1     4     1
#> 3  30.4     4  75.7    52  4.93 1.615 18.52     1     1     4     2
#> 4  30.4     4  95.1   113  3.77 1.513 16.90     1     1     5     2
#> 5  27.3     4  79.0    66  4.08 1.935 18.90     1     1     4     1
#> ... with 27 more rows
```

If you give `distinct()` a list of variables, it now only keeps those variables (instead of, as previously, keeping the first value from the other variables). To preserve the previous behaviour, use `.keep_all = TRUE`:

```r
df <- data_frame(x = c(1, 1, 1, 2, 2), y = 1:5)

# Now only keeps x variable
df %>% distinct(x)
#> # A tibble: 2 x 1
#>       x
#>   <dbl>
#> 1     1
#> 2     2

# Previous behaviour preserved all variables
df %>% distinct(x, .keep_all = TRUE)
#> # A tibble: 2 x 2
#>       x     y
#>   <dbl> <int>
#> 1     1     1
#> 2     2     4
```

The `select()` helper functions `starts_with()`, `ends_with()`, etc are now real exported functions. This means that they have better documentation, and there's an extension mechnaism if you want to write your own helpers.

## Tibble and dtplyr packages

Functions related to the creation and coercion of `tbl_df`s ("tibble"s for short), now live in their own package: [tibble](https://blog.rstudio.com/2016/03/24/tibble-1-0-0/). See `vignette("tibble")` for more details.

Similarly, all code related to the data table dplyr backend code has been separated out in to a new [dtplyr](https://github.com/hadley/dtplyr) package. This decouples the development of the data.table interface from the development of the dplyr package, and I hope will spur improvements to the backend. If both data.table and dplyr are loaded, you'll get a message reminding you to load dtplyr.

## Vector functions

This version of dplyr gains a number of vector functions inspired by SQL. Two functions make it a little easier to eliminate or generate missing values:

  * Given a set of vectors, `coalesce()` finds the first non-missing value in each position:

```r
x <- c(1,  2, NA, 4, NA, 6)
y <- c(NA, 2,  3, 4,  5, NA)

# Use this to piece together a complete vector:
coalesce(x, y)
#> [1] 1 2 3 4 5 6

# Or just replace missing value with a constant:
coalesce(x, 0)
#> [1] 1 2 0 4 0 6
```

  * The complement of `coalesce()` is `na_if()`: it replaces a specified value with an `NA`.

```r
x <- c(1, 5, 2, -99, -99, 10)
na_if(x, -99)
#> [1]  1  5  2 NA NA 10
```

Three functions provide convenient ways of replacing values. In order from simplest to most complicated, they are:

  * `if_else()`, a vectorised if statement, takes a logical vector (usually created with a comparison operator like `==`, `<`, or `%in%`) and replaces `TRUE`s with one vector and `FALSE`s with another.

```r
x1 <- sample(5)
if_else(x1 < 5, "small", "big")
#> [1] "small" "small" "big"   "small" "small"
```

`if_else()` is similar to `base::ifelse()`, but has two useful improvements.
First, it has a fourth argument that will replace missing values:

```r
x2 <- c(NA, x1)
if_else(x2 < 5, "small", "big", "unknown")
#> [1] "unknown" "small"   "small"   "big"     "small"   "small"
```

Secondly, it also have stricter semantics that `ifelse()`: the `true` and `false` arguments must be the same type. This gives a less surprising return type, and preserves S3 vectors like dates and factors:

```r
x <- factor(sample(letters[1:5], 10, replace = TRUE))
ifelse(x %in% c("a", "b", "c"), x, factor(NA))
#>  [1] NA NA  1 NA  3  2  3 NA  3  2
if_else(x %in% c("a", "b", "c"), x, factor(NA))
#>  [1] <NA> <NA> a    <NA> c    b    c    <NA> c    b
#> Levels: a b c d e
```

Currently, `if_else()` is very strict, so you'll need to careful match the types of `true` and `false`. This is most likely to bite you when you're using missing values, and you'll need to use a specific `NA`: `NA_integer_`, `NA_real_`, or `NA_character_`:

```r
if_else(TRUE, 1, NA)
#> Error: `false` has type 'logical' not 'double'
if_else(TRUE, 1, NA_real_)
#> [1] 1
```

  * `recode()`, a vectorised `switch()`, takes a numeric vector, character vector, or factor, and replaces elements based on their values.

```r
x <- sample(c("a", "b", "c", NA), 10, replace = TRUE)

# The default is to leave non-replaced values as is
recode(x, a = "Apple")
#>  [1] "c"     "Apple" NA      NA      "c"     NA      "b"     NA
#>  [9] "c"     "Apple"
# But you can choose to override the default:
recode(x, a = "Apple", .default = NA_character_)
#>  [1] NA      "Apple" NA      NA      NA      NA      NA      NA
#>  [9] NA      "Apple"
# You can also choose what value is used for missing values
recode(x, a = "Apple", .default = NA_character_, .missing = "Unknown")
#>  [1] NA        "Apple"   "Unknown" "Unknown" NA        "Unknown" NA
#>  [8] "Unknown" NA        "Apple"
```

  * `case_when()`, is a vectorised set of `if` and `else if`s. You provide it a set of test-result pairs as formulas: The left side of the formula should return a logical vector, and the right hand side should return either a single value, or a vector the same length as the left hand side. All results must be the same type of vector.

```r
x <- 1:40
case_when(
  x %% 35 == 0 ~ "fizz buzz",
  x %% 5 == 0 ~ "fizz",
  x %% 7 == 0 ~ "buzz",
  TRUE ~ as.character(x)
)
#>  [1] "1"         "2"         "3"         "4"         "fizz"
#>  [6] "6"         "buzz"      "8"         "9"         "fizz"
#> [11] "11"        "12"        "13"        "buzz"      "fizz"
#> [16] "16"        "17"        "18"        "19"        "fizz"
#> [21] "buzz"      "22"        "23"        "24"        "fizz"
#> [26] "26"        "27"        "buzz"      "29"        "fizz"
#> [31] "31"        "32"        "33"        "34"        "fizz buzz"
#> [36] "36"        "37"        "38"        "39"        "fizz"
```

`case_when()` is still somewhat experiment and does not currently work inside `mutate()`. That will be fixed in a future version.

I also added one small helper for dealing with floating point comparisons: `near()` tests for equality with numeric tolerance (`abs(x - y) < tolerance`).

```r
x <- sqrt(2) ^ 2

x == 2
#> [1] FALSE
near(x, 2)
#> [1] TRUE
```

## Predicate functions

Thanks to ideas and code from [Lionel Henry](http://github.com/lionel-), a new family of functions improve upon `summarise_each()` and `mutate_each()`:

  * `summarise_all()` and `mutate_all()` apply a function to all (non-grouped) columns:

```r
mtcars %>% group_by(cyl) %>% summarise_all(mean)
#> # A tibble: 3 x 11
#>     cyl      mpg     disp        hp     drat       wt     qsec        vs
#>   <dbl>    <dbl>    <dbl>     <dbl>    <dbl>    <dbl>    <dbl>     <dbl>
#> 1     4 26.66364 105.1364  82.63636 4.070909 2.285727 19.13727 0.9090909
#> 2     6 19.74286 183.3143 122.28571 3.585714 3.117143 17.97714 0.5714286
#> 3     8 15.10000 353.1000 209.21429 3.229286 3.999214 16.77214 0.0000000
#> ... with 3 more variables: am <dbl>, gear <dbl>, carb <dbl>
```

  * `summarise_at()` and `mutate_at()` operate on a subset of columns. You can select columns with:

    * a character vector of column names,

    * a numeric vector of column positions, or

    * a column specification with `select()` semantics generated with the new `vars()` helper.

    mtcars %>% group_by(cyl) %>% summarise_at(c("mpg", "wt"), mean)
    #> # A tibble: 3 x 3
    #>     cyl      mpg       wt
    #>   <dbl>    <dbl>    <dbl>
    #> 1     4 26.66364 2.285727
    #> 2     6 19.74286 3.117143
    #> 3     8 15.10000 3.999214
    mtcars %>% group_by(cyl) %>% summarise_at(vars(mpg, wt), mean)
    #> # A tibble: 3 x 3
    #>     cyl      mpg       wt
    #>   <dbl>    <dbl>    <dbl>
    #> 1     4 26.66364 2.285727
    #> 2     6 19.74286 3.117143
    #> 3     8 15.10000 3.999214

  * `summarise_if()` and `mutate_if()` take a predicate function (a function that returns `TRUE` or `FALSE` when given a column). This makes it easy to apply a function only to numeric columns:

```r
iris %>% summarise_if(is.numeric, mean)
#>   Sepal.Length Sepal.Width Petal.Length Petal.Width
#> 1     5.843333    3.057333        3.758    1.199333
```

All of these functions pass `...` on to the individual `funs`:

```r
iris %>% summarise_if(is.numeric, mean, trim = 0.25)
#>   Sepal.Length Sepal.Width Petal.Length Petal.Width
#> 1     5.802632    3.032895     3.934211    1.230263
```

A new `select_if()` allows you to pick columns with a predicate function:

```r
df <- data_frame(x = 1:3, y = c("a", "b", "c"))
df %>% select_if(is.numeric)
#> # A tibble: 3 x 1
#>       x
#>   <int>
#> 1     1
#> 2     2
#> 3     3
df %>% select_if(is.character)
#> # A tibble: 3 x 1
#>       y
#>   <chr>
#> 1     a
#> 2     b
#> 3     c
```

`summarise_each()` and `mutate_each()` will be deprecated in a future release.

## SQL translation

I have completely overhauled the translation of dplyr verbs into SQL statements. Previously, dplyr used a rather ad-hoc approach which tried to guess when a new subquery was needed. Unfortunately this approach was fraught with bugs, so I have now implemented a richer internal data model. In the short-term, this is likely to lead to some minor performance decreases (as the generated SQL is more complex), but the dplyr is much more likely to generate correct SQL. In the long-term, these abstractions will make it possible to write a query optimiser/compiler in dplyr, which would make it possible to generate much more succinct queries. If you know anything about writing query optimisers or compilers and are interested in working on this problem, please let me know!

