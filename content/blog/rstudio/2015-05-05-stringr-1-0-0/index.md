---
title: stringr 1.0.0
people:
  - Hadley Wickham
date: '2015-05-05'
categories:
  - Data Wrangling
slug: stringr-1-0-0
blogcategories:
  - Products and Technology
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


I'm very excited to announce the 1.0.0 release of the stringr package. If you haven't heard of stringr before, it makes string manipulation easier by:

  * Using consistent function and argument names: all functions start with `str_`, and the first argument is always the input string This makes stringr easier to learn and easy to use with [the pipe](http://github.com/smbache/magrittr/).

  * Eliminating options that you don't need 95% of the time.

To get started with stringr, check out the [new vignette](http://cran.r-project.org/web/packages/stringr/vignettes/stringr.html).

## What's new?

The biggest change in this release is that stringr is now powered by the [stringi](https://github.com/Rexamine/stringi) package instead of base R. This has two big benefits: stringr is now much faster, and has much better unicode support.

If you've used stringi before, you might wonder why stringr is still necessary: stringi does everything that stringr does, and much much more. There are two reasons that I think stringr is still important:

  1. Lots of people use it already, so this update will give many people a performance boost for free.

  2. The smaller API of stringr makes it a little easier to learn.

That said, once you've learned stringr, using stringi should be easy, so it's a great place to start if you need a tool that doesn't exist in stringr.

## New features and functions

  * `str_replace_all()` gains a convenient syntax for applying multiple pairs of pattern and replacement to the same vector:

```r
x <- c("abc", "def")
str_replace_all(x, c("[ad]" = "!", "[cf]" = "?"))
#> [1] "!b?" "!e?"
```

  * `str_subset()` keeps values that match a pattern:

```r
x <- c("abc", "def", "jhi", "klm", "nop")
str_subset(x, "[aeiou]")
#> [1] "abc" "def" "jhi" "nop"
```

  * `str_order()` and `str_sort()` sort and order strings in a specified locale. `str_conv()` to converts strings from specified encoding to UTF-8.

```r
# The vowels come before the consonants in Hawaiian
str_sort(letters[1:10], locale = "haw")
#>  [1] "a" "e" "i" "b" "c" "d" "f" "g" "h" "j"
```

  * New modifier `boundary()` allows you to count, locate and split by character, word, line and sentence boundaries.

```r
words <- c("These are   some words. Some more words.")
str_count(words, boundary("word"))
#> [1] 7
str_split(words, boundary("word"))
#> [[1]]
#> [1] "These" "are"   "some"  "words" "Some"  "more"  "words"
```

There were two minor changes to make stringr a little more consistent:

  * `str_c()` now returns a zero length vector if any of its inputs are zero length vectors. This is consistent with all other functions, and standard R recycling rules. Similarly, using `str_c("x", NA)` now yields `NA`. If you want `"xNA"`, use `str_replace_na()` on the inputs.

  * `str_match()` now returns NA if an optional group doesn't match (previously it returned ""). This is more consistent with `str_extract()` and other match failures.

## Development

Stringr is over five years old and is quite stable (the last release was over two years ago). Although I've endeavoured to make the change to stringi as seemless as possible, it's likely that it has created some new bugs. If you have problems, please try the [development version](https://github.com/hadley/stringr), and if that doesn't help, [file an issue on github](https://github.com/hadley/stringr/issues).

