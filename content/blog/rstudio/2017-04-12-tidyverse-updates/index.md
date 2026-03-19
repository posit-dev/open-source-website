---
title: tidyverse updates
people:
  - Hadley Wickham
date: '2017-04-12'
categories:
- Packages
slug: tidyverse-updates
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
software: ["tidyverse"]
languages: ["R"]
---


Over the couple of months there have been a bunch of smaller releases to packages in the [tidyverse](http://tidyverse.org). This includes:

  * [forcats](http://forcats.tidyverse.org) 0.2.0, for working with factors.

  * [readr](http://readr.tidyverse.org) 1.1.0, for reading flat-files from disk.

  * [stringr](http://stringr.tidyverse.org) 1.2.0, for manipulating strings.

  * [tibble](http://tibble.tidyverse.org) 1.3.0, a modern re-imagining of the data frame.

This blog post summarises the most important new features, and points to the full release notes where you can learn more.

(If you've never heard of the tidyverse before, it's an set of packages that are designed to work together to help you do data science. The best place to learn all about it is [R for Data Science](http://r4ds.had.co.nz).)

## forcats 0.2.0

forcats has three new functions:

  * `as_factor()` is a generic version of `as.factor()`, which creates factors from character vectors ordered by appearance, rather than alphabetically. This ensures means that `as_factor(x)` will always return the same result, regardless of the current locale.

  * `fct_other()` makes it easier to convert selected levels to "other":

```r
x <- factor(rep(LETTERS[1:6], times = c(10, 5, 1, 1, 1, 1)))

x %>%
  fct_other(keep = c("A", "B")) %>%
  fct_count()
#> # A tibble: 3 × 2
#>        f     n
#>
#> 1      A    10
#> 2      B     5
#> 3  Other     4

x %>%
  fct_other(drop = c("A", "B")) %>%
  fct_count()
#> # A tibble: 5 × 2
#>        f     n
#>
#> 1      C     1
#> 2      D     1
#> 3      E     1
#> 4      F     1
#> 5  Other    15
```

  * `fct_relabel()` allows programmatic relabeling of levels:

```r
x <- factor(letters[1:3])
x
#> [1] a b c
#> Levels: a b c

x %>% fct_relabel(function(x) paste0("-", x, "-"))
#> [1] -a- -b- -c-
#> Levels: -a- -b- -c-
```

See the full list of other changes in the [release notes](https://github.com/tidyverse/forcats/releases/tag/v0.2.0).

## stringr 1.2.0

This release includes a change to the API: `str_match_all()` now returns NA if an optional group doesn't match (previously it returned ""). This is more consistent with `str_match()` and other match failures.

```r
x <- c("a=1,b=2", "c=3", "d=")

x %>% str_match("(.)=(\\d)?")
#>      [,1]  [,2] [,3]
#> [1,] "a=1" "a"  "1"
#> [2,] "c=3" "c"  "3"
#> [3,] "d="  "d"  NA
x %>% str_match_all("(.)=(\\d)?,?")
#> [[1]]
#>      [,1]   [,2] [,3]
#> [1,] "a=1," "a"  "1"
#> [2,] "b=2"  "b"  "2"
#>
#> [[2]]
#>      [,1]  [,2] [,3]
#> [1,] "c=3" "c"  "3"
#>
#> [[3]]
#>      [,1] [,2] [,3]
#> [1,] "d=" "d"  NA
```

There are three new features:

  * In `str_replace()`, `replacement` can now be a function. The function is once for each match and its return value will be used as the replacement.

```r
redact <- function(x) {
  str_dup("-", str_length(x))
}

x <- c("It cost $500", "We spent $1,200 on stickers")
x %>% str_replace_all("\\$[0-9,]+", redact)
#> [1] "It cost ----"                "We spent ------ on stickers"
```

  * New `str_which()` mimics `grep()`:

```r
fruit <- c("apple", "banana", "pear", "pinapple")

# Matching positions
str_which(fruit, "p")
#> [1] 1 3 4

# Matching values
str_subset(fruit, "p")
#> [1] "apple"    "pear"     "pinapple"
```

  * A new vignette ([`vignette("regular-expressions")`](http://stringr.tidyverse.org/articles/regular-expressions.html)) describes the details of the regular expressions supported by stringr. The main vignette ([`vignette("stringr")`](http://stringr.tidyverse.org/articles/stringr.html)) has been updated to give a high-level overview of the package.

See the full list of other changes in the [release notes](https://github.com/tidyverse/stringr/releases/tag/v1.2.0).

## readr 1.1.0

readr gains two new features:

  * All `write_*()` functions now support connections. This means that that you can write directly to compressed formats such as `.gz`, `bz2` or `.xz` (and readr will automatically do so if you use one of those suffixes).

```r
write_csv(iris, "iris.csv.bz2")
```

  * `parse_factor(levels = NULL)` and `col_factor(levels = NULL)` will produce a factor column based on the levels in the data, mimicing factor parsing in base R (with the exception that levels are created in the order seen).

```r
iris2 <- read_csv("iris.csv.bz2", col_types = cols(
  Species = col_factor(levels = NULL)
))
```

See the full list of other changes in the [release notes](https://github.com/tidyverse/readr/releases/tag/v1.1.0).

## tibble 1.3.0

tibble has one handy new function: `deframe()` is the opposite of `enframe()`: it turns a two-column data frame into a named vector.

```r
df <- tibble(x = c("a", "b", "c"), y = 1:3)
deframe(df)
#> a b c
#> 1 2 3
```

See the full list of other changes in the [release notes](https://github.com/tidyverse/tibble/releases/tag/v1.3.0).

