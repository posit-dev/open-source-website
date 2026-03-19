---
title: tidyr 0.2.0 (and reshape2 1.4.1)
people:
  - Hadley Wickham
date: '2014-12-08'
categories:
  - Data Wrangling
slug: tidyr-0-2-0
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


tidyr 0.2.0 is now available on CRAN. tidyr makes it easy to "tidy" your data, storing it in a consistent form so that it's easy to manipulate, visualise and model. Tidy data has variables in columns and observations in rows, and is described in more detail in the [tidy data](http://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html) vignette. Install tidyr with:

```r
install.packages("tidyr")
```

There are three important additions to tidyr 0.2.0:

  * `expand()` is a wrapper around `expand.grid()` that allows you to generate all possible combinations of two or more variables. In conjunction with `dplyr::left_join()`, this makes it easy to fill in missing rows of data.

```r
sales <- dplyr::data_frame(
  year = rep(c(2012, 2013), c(4, 2)),
  quarter = c(1, 2, 3, 4, 2, 3),
  sales = sample(6) * 100
)

# Missing sales data for 2013 Q1 & Q4
sales
#> Source: local data frame [6 x 3]
#>
#>   year quarter sales
#> 1 2012       1   400
#> 2 2012       2   200
#> 3 2012       3   500
#> 4 2012       4   600
#> 5 2013       2   300
#> 6 2013       3   100

# Missing values are now explicit
sales %>%
  expand(year, quarter) %>%
  dplyr::left_join(sales)
#> Joining by: c("year", "quarter")
#> Source: local data frame [8 x 3]
#>
#>   year quarter sales
#> 1 2012       1   400
#> 2 2012       2   200
#> 3 2012       3   500
#> 4 2012       4   600
#> 5 2013       1    NA
#> 6 2013       2   300
#> 7 2013       3   100
#> 8 2013       4    NA
```

  * In the process of data tidying, it's sometimes useful to have a column of a data frame that is a list of vectors. `unnest()` lets you simplify that column back down to an atomic vector, duplicating the original rows as needed. (NB: If you're working with data frames containing lists, I highly recommend using dplyr's `tbl_df`, which will display list-columns in a way that makes their structure more clear. Use `dplyr::data_frame()` to create a data frame wrapped with the `tbl_df` class.)

```r
raw <- dplyr::data_frame(
  x = 1:3,
  y = c("a", "d,e,f", "g,h")
)
# y is character vector containing comma separated strings
raw
#> Source: local data frame [3 x 2]
#>
#>   x     y
#> 1 1     a
#> 2 2 d,e,f
#> 3 3   g,h

# y is a list of character vectors
as_list <- raw %>% mutate(y = strsplit(y, ","))
as_list
#> Source: local data frame [3 x 2]
#>
#>   x        y
#> 1 1 <chr[1]>
#> 2 2 <chr[3]>
#> 3 3 <chr[2]>

# y is a character vector; rows are duplicated as needed
as_list %>% unnest(y)
#> Source: local data frame [6 x 2]
#>
#>   x y
#> 1 1 a
#> 2 2 d
#> 3 2 e
#> 4 2 f
#> 5 3 g
#> 6 3 h
```

  * `separate()` has a new `extra` argument that allows you to control what happens if a column doesn't always split into the same number of pieces.

```r
raw %>% separate(y, c("trt", "B"), ",")
#> Error: Values not split into 2 pieces at 1, 2
raw %>% separate(y, c("trt", "B"), ",", extra = "drop")
#> Source: local data frame [3 x 3]
#>
#>   x trt  B
#> 1 1   a NA
#> 2 2   d  e
#> 3 3   g  h
raw %>% separate(y, c("trt", "B"), ",", extra = "merge")
#> Source: local data frame [3 x 3]
#>
#>   x trt   B
#> 1 1   a  NA
#> 2 2   d e,f
#> 3 3   g   h
```

To read about the other minor changes and bug fixes, please consult the [release notes](https://github.com/hadley/tidyr/releases/tag/v0.2.0).

## reshape2 1.4.1

There's also a new version of reshape2, 1.4.1. It includes three bug fixes for `melt.data.frame()` contributed by [Kevin Ushey](https://github.com/kevinushey). Read all about them on the [release notes](https://github.com/hadley/reshape/releases/tag/v1.4.1) and install it with:

```r
install.packages("reshape2")
```

