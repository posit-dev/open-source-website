---
title: tidyr 0.3.0
people:
  - Hadley Wickham
date: '2015-09-13'
categories:
  - Data Wrangling
slug: tidyr-0-3-0
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


tidyr 0.3.0 is now available on CRAN. tidyr makes it easy to "tidy" your data, storing it in a consistent form so that it's easy to manipulate, visualise and model. Tidy data has variables in columns and observations in rows, and is described in more detail in the [tidy data](http://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html) vignette. Install tidyr with:

```r
install.packages("tidyr")
```

tidyr contains four new verbs: `fill()`, `replace()` and `complete()`, and `unnest()`, and lots of smaller bug fixes and improvements.

## `fill()`

The new fill function fills in missing observations from the last non-missing value. This is useful if you're getting data from Excel users who haven't read Karl Broman's excellent [data organisation guide](http://kbroman.org/dataorg/) and [leave cells blank](http://kbroman.org/dataorg/pages/no_empty_cells.html) to indicate that the previous value should be carried forward:

```r
df <- dplyr::data_frame(
  year = c(2015, NA, NA, NA),
  trt = c("A", NA, "B", NA)
)
df
#> Source: local data frame [4 x 2]
#>
#>    year   trt
#>   (dbl) (chr)
#> 1  2015     A
#> 2    NA    NA
#> 3    NA     B
#> 4    NA    NA
df %>% fill(year, trt)
#> Source: local data frame [4 x 2]
#>
#>    year   trt
#>   (dbl) (chr)
#> 1  2015     A
#> 2  2015     A
#> 3  2015     B
#> 4  2015     B
```

## `replace_na()` and `complete()`

`replace_na()` makes it easy to replace missing values on a column-by-column basis:

```r
df <- dplyr::data_frame(
  x = c(1, 2, NA),
  y = c("a", NA, "b")
)
df %>% replace_na(list(x = 0, y = "unknown"))
#> Source: local data frame [3 x 2]
#>
#>       x       y
#>   (dbl)   (chr)
#> 1     1       a
#> 2     2 unknown
#> 3     0       b
```

It is particularly useful when called from `complete()`, which makes it easy to fill in missing combinations of your data:

```r
df <- dplyr::data_frame(
  group = c(1:2, 1),
  item_id = c(1:2, 2),
  item_name = c("a", "b", "b"),
  value1 = 1:3,
  value2 = 4:6
)
df
#> Source: local data frame [3 x 5]
#>
#>   group item_id item_name value1 value2
#>   (dbl)   (dbl)     (chr)  (int)  (int)
#> 1     1       1         a      1      4
#> 2     2       2         b      2      5
#> 3     1       2         b      3      6

df %>% complete(group, c(item_id, item_name))
#> Source: local data frame [4 x 5]
#>
#>   group item_id item_name value1 value2
#>   (dbl)   (dbl)     (chr)  (int)  (int)
#> 1     1       1         a      1      4
#> 2     1       2         b      3      6
#> 3     2       1         a     NA     NA
#> 4     2       2         b      2      5

df %>% complete(
  group, c(item_id, item_name),
  fill = list(value1 = 0)
)
#> Source: local data frame [4 x 5]
#>
#>   group item_id item_name value1 value2
#>   (dbl)   (dbl)     (chr)  (dbl)  (int)
#> 1     1       1         a      1      4
#> 2     1       2         b      3      6
#> 3     2       1         a      0     NA
#> 4     2       2         b      2      5
```

Note how I've grouped `item_id` and `item_name` together with `c(item_id, item_name)`. This treats them as nested, not crossed, so we don't get every combination of `group`, `item_id` and `item_name`, as we would otherwise:

```r
df %>% complete(group, item_id, item_name)
#> Source: local data frame [8 x 5]
#>
#>    group item_id item_name value1 value2
#>    (dbl)   (dbl)     (chr)  (int)  (int)
#> 1      1       1         a      1      4
#> 2      1       1         b     NA     NA
#> 3      1       2         a     NA     NA
#> 4      1       2         b      3      6
#> 5      2       1         a     NA     NA
#> ..   ...     ...       ...    ...    ...
```

Read more about this behaviour in `?expand`.

## `unnest()`

`unnest()` is out of beta, and is now ready to help you unnest columns that are lists of vectors. This can occur when you have hierarchical data that's been collapsed into a string:

```r
df <- dplyr::data_frame(x = 1:2, y = c("1,2", "3,4,5,6,7"))
df
#> Source: local data frame [2 x 2]
#>
#>       x         y
#>   (int)     (chr)
#> 1     1       1,2
#> 2     2 3,4,5,6,7

df %>%
  dplyr::mutate(y = strsplit(y, ","))
#> Source: local data frame [2 x 2]
#>
#>       x        y
#>   (int)   (list)
#> 1     1 <chr[2]>
#> 2     2 <chr[5]>

df %>%
  dplyr::mutate(y = strsplit(y, ",")) %>%
  unnest()
#> Source: local data frame [7 x 2]
#>
#>        x     y
#>    (int) (chr)
#> 1      1     1
#> 2      1     2
#> 3      2     3
#> 4      2     4
#> 5      2     5
#> ..   ...   ...
```

`unnest()` also works on columns that are lists of data frames. This is admittedly esoteric, but I think it might be useful when you're generating pairs of test-training splits. I'm still thinking about this idea, so look for more examples and better support across my packages in the future.

## Minor improvements

There were 13 minor improvements and bug fixes. The most important are listed below. To read about the rest, please consult the [release notes](https://github.com/hadley/tidyr/releases/tag/v0.3.0).

  * `%>%` is re-exported from magrittr: this means that you no longer need to load dplyr or magrittr if you want to use the pipe.

  * `extract()` and `separate()` now return multiple NA columns for NA inputs:

```r
df <- dplyr::data_frame(x = c("a-b", NA, "c-d"))
df %>% separate(x, c("x", "y"), "-")
#> Source: local data frame [3 x 2]
#>
#>       x     y
#>   (chr) (chr)
#> 1     a     b
#> 2    NA    NA
#> 3     c     d
```

  * `separate()` gains finer control if there are too few matches:

```r
df <- dplyr::data_frame(x = c("a-b-c", "a-c"))
df %>% separate(x, c("x", "y", "z"), "-")
#> Warning: Too few values at 1 locations: 2
#> Source: local data frame [2 x 3]
#>
#>       x     y     z
#>   (chr) (chr) (chr)
#> 1     a     b     c
#> 2     a     c    NA
df %>% separate(x, c("x", "y", "z"), "-", fill = "right")
#> Source: local data frame [2 x 3]
#>
#>       x     y     z
#>   (chr) (chr) (chr)
#> 1     a     b     c
#> 2     a     c    NA
df %>% separate(x, c("x", "y", "z"), "-", fill = "left")
#> Source: local data frame [2 x 3]
#>
#>       x     y     z
#>   (chr) (chr) (chr)
#> 1     a     b     c
#> 2    NA     c     a
```

This complements the support for too many matches:

```r
df <- dplyr::data_frame(x = c("a-b-c", "a-c"))
df %>% separate(x, c("x", "y"), "-")
#> Warning: Too many values at 1 locations: 1
#> Source: local data frame [2 x 2]
#>
#>       x     y
#>   (chr) (chr)
#> 1     a     b
#> 2     a     c
df %>% separate(x, c("x", "y"), "-", extra = "merge")
#> Source: local data frame [2 x 2]
#>
#>       x     y
#>   (chr) (chr)
#> 1     a   b-c
#> 2     a     c
df %>% separate(x, c("x", "y"), "-", extra = "drop")
#> Source: local data frame [2 x 2]
#>
#>       x     y
#>   (chr) (chr)
#> 1     a     b
#> 2     a     c
```

  * tidyr no longer depends on reshape2. This should fix issues when you load reshape and tidyr at the same time. It also frees tidyr to evolve in a different direction to the more general reshape2.

