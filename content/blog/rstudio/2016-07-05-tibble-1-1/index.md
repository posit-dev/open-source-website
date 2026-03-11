---
title: tibble 1.1
people:
  - Hadley Wickham
date: '2016-07-05'
categories:
- Packages
- tidyverse
slug: tibble-1-1
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
- tidyverse
events: blog
ported_from: rstudio
port_status: raw
---


We're proud to announce version 1.1 of the `tibble` package. Tibbles are a modern reimagining of the data frame, keeping what time has shown to be effective, and throwing out what is not. Grab the latest version with:

```r
install.packages("tibble")
```

There are three major new features:

  * A more consistent naming scheme

  * Changes to how columns are extracted

  * Tweaks to the output

There are many other small improvements and bug fixes: please see the [release notes](https://github.com/hadley/tibble/releases/tag/v1.1) for a complete list.

## A better naming scheme

It's caused some confusion that you use `data_frame()` and `as_data_frame()` to create and coerce tibbles. It's also more important to make the distinction between tibbles and data frames more clear as we evolve a little further away from the semantics of data frames.

Now, we're consistently using "tibble" as the key word in creation, coercion, and testing functions:

```r
tibble(x = 1:5, y = letters[1:5])
#> # A tibble: 5 x 2
#>       x     y
#>   <int> <chr>
#> 1     1     a
#> 2     2     b
#> 3     3     c
#> 4     4     d
#> 5     5     e
as_tibble(data.frame(x = runif(5)))
#> # A tibble: 5 x 1
#>           x
#>       <dbl>
#> 1 0.4603887
#> 2 0.4824339
#> 3 0.4546795
#> 4 0.5042028
#> 5 0.4558387
is_tibble(data.frame())
#> [1] FALSE
```

Previously `tibble()` was an alias for `frame_data()`. If you were using `tibble()` to create tibbles by rows, you'll need to switch to `frame_data()`. This is a breaking change, but we believe that the new naming scheme will be less confusing in the long run.

## Extracting columns

The previous version of tibble was a little too strict when you attempted to retrieve a column that did not exist: we had forgotten that many people check for the presence of column with `is.null(df$x)`. This is bad idea because of partial matching, but it is common:

```r
df1 <- data.frame(xyz = 1)
df1$x
#> [1] 1
```

Now, instead of throwing an error, tibble will return `NULL`. If you use `$`, common in interactive scripts, tibble will generate a warning:

```r
df2 <- tibble(xyz = 1)
df2$x
#> Warning: Unknown column 'x'
#> NULL
df2[["x"]]
#> NULL
```

We also provide a convenient helper for detecting the presence/absence of a column:

```r
has_name(df1, "x")
#> [1] FALSE
has_name(df2, "x")
#> [1] FALSE
```

## Output tweaks

We've tweaked the output to have a shorter header, more information in the footer. We're using `#` consistently to denote metadata, and we print missing character values as `<NA>` (instead of `NA`).

The example below shows the new rendering of the `flights` table.

```r
nycflights13::flights
#> # A tibble: 336,776 x 19
#>     year month   day dep_time sched_dep_time dep_delay arr_time
#>    <int> <int> <int>    <int>          <int>     <dbl>    <int>
#> 1   2013     1     1      517            515         2      830
#> 2   2013     1     1      533            529         4      850
#> 3   2013     1     1      542            540         2      923
#> 4   2013     1     1      544            545        -1     1004
#> 5   2013     1     1      554            600        -6      812
#> 6   2013     1     1      554            558        -4      740
#> 7   2013     1     1      555            600        -5      913
#> 8   2013     1     1      557            600        -3      709
#> 9   2013     1     1      557            600        -3      838
#> 10  2013     1     1      558            600        -2      753
#> # ... with 336,766 more rows, and 12 more variables: sched_arr_time <int>,
#> #   arr_delay <dbl>, carrier <chr>, flight <int>, tailnum <chr>,
#> #   origin <chr>, dest <chr>, air_time <dbl>, distance <dbl>, hour <dbl>,
#> #   minute <dbl>, time_hour <time>
```

Thanks to [Lionel Henry](http://github.com/lionel-) for contributing an option for determining the number of printed extra columns: `getOption("tibble.max_extra_cols")`. This is particularly important for the ultra-wide tables often released by statistical offices and other institutions.

Expect the printed output to continue to evolve. In the next version, we hope to do better with very wide columns (e.g. from long strings), and to make better use of now unused horizontal space (e.g. from long column names).

