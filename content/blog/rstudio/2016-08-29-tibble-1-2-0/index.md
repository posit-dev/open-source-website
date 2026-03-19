---
title: tibble 1.2.0
people:
  - Hadley Wickham
date: '2016-08-29'
categories:
  - Data Wrangling
slug: tibble-1-2-0
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


We're proud to announce version 1.2.0 of the tibble package. Tibbles are a modern reimagining of the data frame, keeping what time has shown to be effective, and throwing out what is not. Grab the latest version with:

```r
install.packages("tibble")
```

This is mostly a maintenance release, with the following major changes:

  * More options for adding individual rows and (new!) columns

  * Improved function names

  * Minor tweaks to the output

There are many other small improvements and bug fixes: please see the [release notes](https://github.com/hadley/tibble/releases/tag/v1.2) for a complete list.

Thanks to [Jenny Bryan](https://github.com/jennybc) for `add_row()` and `add_column()` improvements and ideas, to [William Dunlap](https://github.com/BillDunlap) for pointing out a bug with tibble's implementation of `all.equal()`, to [Kevin Wright](https://github.com/kwstat) for pointing out a rare bug with `glimpse()`, and to all the other contributors. Use the [issue tracker](https://github.com/hadley/tibble/issues) to submit bugs or suggest ideas, your contributions are always welcome.

## Adding rows and columns

There are now more options for adding individual rows, and columns can be added in a similar way, illustrated with this small tibble:

```r
df <- tibble(x = 1:3, y = 3:1)
df
#> # A tibble: 3 × 2
#>       x     y
#>   <int> <int>
#> 1     1     3
#> 2     2     2
#> 3     3     1
```

The `add_row()` function allows control over where the new rows are added. In the following example, the row (4, 0) is added before the second row:

```r
df %>%
  add_row(x = 4, y = 0, .before = 2)
#> # A tibble: 4 × 2
#>       x     y
#>   <dbl> <dbl>
#> 1     1     3
#> 2     4     0
#> 3     2     2
#> 4     3     1
```

Adding more than one row is now fully supported, although not recommended in general because it can be a bit hard to read.

```r
df %>%
  add_row(x = 4:5, y = 0:-1)
#> # A tibble: 5 × 2
#>       x     y
#>   <int> <int>
#> 1     1     3
#> 2     2     2
#> 3     3     1
#> 4     4     0
#> 5     5    -1
```

Columns can now be added in much the same way with the new `add_column()` function:

```r
df %>%
  add_column(z = -1:1, w = 0)
#> # A tibble: 3 × 4
#>       x     y     z     w
#>   <int> <int> <int> <dbl>
#> 1     1     3    -1     0
#> 2     2     2     0     0
#> 3     3     1     1     0
```

It also supports `.before` and `.after` arguments:

```r
df %>%
  add_column(z = -1:1, .after = 1)
#> # A tibble: 3 × 3
#>       x     z     y
#>   <int> <int> <int>
#> 1     1    -1     3
#> 2     2     0     2
#> 3     3     1     1

df %>%
  add_column(w = 0:2, .before = "x")
#> # A tibble: 3 × 3
#>       w     x     y
#>   <int> <int> <int>
#> 1     0     1     3
#> 2     1     2     2
#> 3     2     3     1
```

The `add_column()` function will never alter your existing data: you can't overwrite existing columns, and you can't add new observations.

## Function names

`frame_data()` is now `tribble()`, which stands for "transposed tibble". The old name still works, but will be deprecated eventually.

```r
tribble(
  ~x, ~y,
   1, "a",
   2, "z"
)
#> # A tibble: 2 × 2
#>       x     y
#>   <dbl> <chr>
#> 1     1     a
#> 2     2     z
```

## Output tweaks

We've tweaked the output again to use the multiply character `×` instead of `x` when printing dimensions (this still renders nicely on Windows.) We surround non-semantic column with backticks, and `dttm` is now used instead of `time` to distinguish `POSIXt` and `hms` (or `difftime`) values.

The example below shows the new rendering:

```r
tibble(`date and time` = Sys.time(), time = hms::hms(minutes = 3))
#> # A tibble: 1 × 2
#>       `date and time`     time
#>                <dttm>   <time>
#> 1 2016-08-29 16:48:57 00:03:00
```

Expect the printed output to continue to evolve in next release. Stay tuned for a new function that reconstructs `tribble()` calls from existing data frames.

