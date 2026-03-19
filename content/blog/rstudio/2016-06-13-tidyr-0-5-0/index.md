---
title: tidyr 0.5.0
people:
  - Hadley Wickham
date: '2016-06-13'
categories:
  - Data Wrangling
slug: tidyr-0-5-0
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


I'm pleased to announce tidyr 0.5.0. tidyr makes it easy to "tidy" your data, storing it in a consistent form so that it's easy to manipulate, visualise and model. Tidy data has a simple convention: put variables in the columns and observations in the rows. You can learn more about it in the [tidy data](http://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html) vignette. Install it with:

```r
install.packages("tidyr")
```

This release has three useful new features:

  1. `separate_rows()` separates values that contain multiple values separated by a delimited into multiple rows. Thanks to [Aaron Wolen](https://github.com/aaronwolen) for the contribution!

```r
df <- data_frame(x = 1:2, y = c("a,b", "d,e,f"))
df %>%
  separate_rows(y, sep = ",")
#> Source: local data frame [5 x 2]
#>
#>       x     y
#>   <int> <chr>
#> 1     1     a
#> 2     1     b
#> 3     2     d
#> 4     2     e
#> 5     2     f
```

Compare with `separate()` which separates into (named) columns:

```r
df %>%
  separate(y, c("y1", "y2", "y3"), sep = ",", fill = "right")
#> Source: local data frame [2 x 4]
#>
#>       x    y1    y2    y3
#> * <int> <chr> <chr> <chr>
#> 1     1     a     b  <NA>
#> 2     2     d     e     f
```

  2. `spread()` gains a `sep` argument. Setting this will name columns as "key|sep|value". This is useful when you're spreading based on a numeric column:

```r
df <- data_frame(
  x = c(1, 2, 1),
  key = c(1, 1, 2),
  val = c("a", "b", "c")
)
df %>% spread(key, val)
#> Source: local data frame [2 x 3]
#>
#>       x     1     2
#> * <dbl> <chr> <chr>
#> 1     1     a     c
#> 2     2     b  <NA>
df %>% spread(key, val, sep = "_")
#> Source: local data frame [2 x 3]
#>
#>       x key_1 key_2
#> * <dbl> <chr> <chr>
#> 1     1     a     c
#> 2     2     b  <NA>
```

  3. `unnest()` gains a `.sep` argument. This is useful if you have multiple columns of data frames that have the same variable names:

```r
df <- data_frame(
  x = 1:2,
  y1 = list(
    data_frame(y = 1),
    data_frame(y = 2)
  ),
  y2 = list(
    data_frame(y = "a"),
    data_frame(y = "b")
  )
)
df %>% unnest()
#> Source: local data frame [2 x 3]
#>
#>       x     y     y
#>   <int> <dbl> <chr>
#> 1     1     1     a
#> 2     2     2     b
df %>% unnest(.sep = "_")
#> Source: local data frame [2 x 3]
#>
#>       x  y1_y  y2_y
#>   <int> <dbl> <chr>
#> 1     1     1     a
#> 2     2     2     b
```

It also gains a `.id` column that makes the names of the list explicit:

```r
df <- data_frame(
  x = 1:2,
  y = list(
    a = 1:3,
    b = 3:1
  )
)
df %>% unnest()
#> Source: local data frame [6 x 2]
#>
#>       x     y
#>   <int> <int>
#> 1     1     1
#> 2     1     2
#> 3     1     3
#> 4     2     3
#> 5     2     2
#> 6     2     1
df %>% unnest(.id = "id")
#> Source: local data frame [6 x 3]
#>
#>       x     y    id
#>   <int> <int> <chr>
#> 1     1     1     a
#> 2     1     2     a
#> 3     1     3     a
#> 4     2     3     b
#> 5     2     2     b
#> 6     2     1     b
```

tidyr 0.5.0 also includes a bumper crop of bug fixes, including fixes for `spread()` and `gather()` in the presence of list-columns. Please see the [release notes](https://github.com/hadley/tidyr/releases/tag/v0.5.0) for a complete list of changes.

