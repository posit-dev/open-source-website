---
title: dplyr 0.4.3
people:
  - Hadley Wickham
date: '2015-09-04'
categories:
- Packages
- tidyverse
slug: dplyr-0-4-3
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
- tidyverse
events: blog
ported_from: rstudio
port_status: in-progress
---


dplyr 0.4.3 includes over 30 minor improvements and bug fixes, which are described in detail in the [release notes](https://github.com/hadley/dplyr/releases/tag/v0.4.3). Here I wanted to draw your attention five small, but important, changes:

  * `mutate()` no longer randomly crashes! (Sorry it took us so long to fix this - I know it's been causing a lot of pain.)

  * dplyr now has much better support for non-ASCII column names. It's probably not perfect, but should be a lot better than previous versions.

  * When printing a `tbl_df`, you now see the types of all columns, not just those that don't fit on the screen:

```r
data_frame(x = 1:3, y = letters[x], z = factor(y))
#> Source: local data frame [3 x 3]
#>
#>       x     y      z
#>   (int) (chr) (fctr)
#> 1     1     a      a
#> 2     2     b      b
#> 3     3     c      c
```

  * `bind_rows()` gains a `.id` argument. When supplied, it creates a new column that gives the name of each data frame:

```r
a <- data_frame(x = 1, y = "a")
b <- data_frame(x = 2, y = "c")

bind_rows(a = a, b = b)
#> Source: local data frame [2 x 2]
#>
#>       x     y
#>   (dbl) (chr)
#> 1     1     a
#> 2     2     c
bind_rows(a = a, b = b, .id = "source")
#> Source: local data frame [2 x 3]
#>
#>   source     x     y
#>    (chr) (dbl) (chr)
#> 1      a     1     a
#> 2      b     2     c
# Or equivalently
bind_rows(list(a = a, b = b), .id = "source")
#> Source: local data frame [2 x 3]
#>
#>   source     x     y
#>    (chr) (dbl) (chr)
#> 1      a     1     a
#> 2      b     2     c
```

  * dplyr is now more forgiving of unknown attributes. All functions should now copy column attributes from the input to the output, instead of complaining. Additionally `arrange()`, `filter()`, `slice()`, and `summarise()` preserve attributes of the data frame itself.

