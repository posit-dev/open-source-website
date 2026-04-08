---
title: tidyr 0.6.0
description: "tidyr 0.6.0 adds drop_na() to remove rows containing missing values in selected or all columns."
auto-description: true
people:
  - Hadley Wickham
date: '2016-08-15'
categories:
  - Data Wrangling
slug: tidyr-0-6-0
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


I'm pleased to announce tidyr 0.6.0. tidyr makes it easy to "tidy" your data, storing it in a consistent form so that it's easy to manipulate, visualise and model. Tidy data has a simple convention: put variables in the columns and observations in the rows. You can learn more about it in the [tidy data](http://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html) vignette. Install it with:

```r
install.packages("tidyr")
```

I mostly released this version to bundle up a number of small tweaks needed for [R for Data Science](http://r4ds.had.co.nz/tidy-data.html). But there's one nice new feature, contributed by [Jan Schulz](https://github.com/janschulz): `drop_na()`. `drop_na()`drops rows containing missing values:

```r
df <- tibble(x = c(1, 2, NA), y = c("a", NA, "b"))
df
#> # A tibble: 3 × 2
#>       x     y
#>   <dbl> <chr>
#> 1     1     a
#> 2     2  <NA>
#> 3    NA     b

# Called without arguments, it drops rows containing
# missing values in any variable:
df %>% drop_na()
#> # A tibble: 1 × 2
#>       x     y
#>   <dbl> <chr>
#> 1     1     a

# Or you can restrict the variables it looks at,
# using select() style syntax:
df %>% drop_na(x)
#> # A tibble: 2 × 2
#>       x     y
#>   <dbl> <chr>
#> 1     1     a
#> 2     2  <NA>
```

Please see the [release notes](https://github.com/hadley/tidyr/releases/tag/v0.6.0) for a complete list of changes.

