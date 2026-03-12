---
title: dplyr 0.4.0
people:
  - Hadley Wickham
date: '2015-01-09'
slug: dplyr-0-4-0
events: blog
ported_from: rstudio
port_status: in-progress
---


I'm very pleased to announce that dplyr 0.4.0 is now available from CRAN. Get the latest version by running:

```r
install.packages("dplyr")
```

dplyr 0.4.0 includes over 80 minor improvements and bug fixes, which are described in detail in the [release notes](https://github.com/hadley/dplyr/releases/tag/v0.4.0). Here I wanted to draw your attention to two areas that have particularly improved since dplyr 0.3, two-table verbs and data frame support.

## Two table verbs

dplyr now has full support for all two-table verbs provided by SQL:

  * Mutating joins, which add new variables to one table from matching rows in another: `inner_join()`, `left_join()`, `right_join()`, `full_join()`. (Support for non-equi joins is planned for dplyr 0.5.0.)

  * Filtering joins, which filter observations from one table based on whether or not they match an observation in the other table: `semi_join()`, `anti_join()`.

  * Set operations, which combine the observations in two data sets as if they were set elements: `intersect()`, `union()`, `setdiff()`.

Together, these verbs should allow you to solve 95% of data manipulation problems that involve multiple tables. If any of the concepts are unfamiliar to you, I highly recommend reading the [two-table vignette](http://cran.r-project.org/web/packages/dplyr/vignettes/two-table.html) (and if you still don't understand, please let me know so I can make it better.)

## Data frames

dplyr wraps data frames in a `tbl_df` class. These objects are structured in exactly the same way as regular data frames, but their behaviour has been tweaked a little to make them easier to work with. The new [data_frames vignette](http://cran.r-project.org/web/packages/dplyr/vignettes/data_frames.html) describes how dplyr works with data frames in general, and below I highlight some of the features new in 0.4.0.

### Printing

The biggest difference is printing: `print.tbl_df()` doesn't try and print 10,000 rows! Printing got a lot of love in dplyr 0.4 and now:

  * All `print()` method methods invisibly return their input so you can interleave `print()` statements into a pipeline to see interim results.

  * If you've managed to produce a 0-row data frame, dplyr won't try to print the data, but will tell you the column names and types:

```r
data_frame(x = numeric(), y = character())
#> Source: local data frame [0 x 2]
#>
#> Variables not shown: x (dbl), y (chr)
```

  * dplyr never prints row names since no dplyr method is guaranteed to preserve them:

```r
df <- data.frame(x = c(a = 1, b = 2, c = 3))
df
#>   x
#> a 1
#> b 2
#> c 3
df %>% tbl_df()
#> Source: local data frame [3 x 1]
#>
#>   x
#> 1 1
#> 2 2
#> 3 3
```

I don't think using row names is a good idea because it violates one of the principles of [tidy data](http://vita.had.co.nz/papers/tidy-data.html): every variable should be stored in the same way.

To make life a bit easier if you do have row names, you can use the new `add_rownames()` to turn your row names into a proper variable:

```r
df %>%
  add_rownames()
#>   rowname x
#> 1       a 1
#> 2       b 2
#> 3       c 3
```

(But you're better off never creating them in the first place.)

  * `options(dplyr.print_max)` is now 20, so dplyr will never print more than 20 rows of data (previously it was 100). The best way to see more rows of data is to use `View()`.

### Coercing lists to data frames

When you have a list of vectors of equal length that you want to turn into a data frame, dplyr provides `as_data_frame()` as a simple alternative to `as.data.frame()`. `as_data_frame()` is considerably faster than `as.data.frame()` because it does much less:

```r
l <- replicate(26, sample(100), simplify = FALSE)
names(l) <- letters
microbenchmark::microbenchmark(
  as_data_frame(l),
  as.data.frame(l)
)
#> Unit: microseconds
#>              expr      min        lq   median        uq      max neval
#>  as_data_frame(l)  101.856  112.0615  124.855  143.0965  254.193   100
#>  as.data.frame(l) 1402.075 1466.6365 1511.644 1635.1205 3007.299   100
```

It's difficult to precisely describe what `as.data.frame(x)` does, but it's similar to `do.call(cbind, lapply(x, data.frame))` - it coerces each component to a data frame and then `cbind()`s them all together.

The speed of `as.data.frame()` is not usually a bottleneck in interactive use, but can be a problem when combining thousands of lists into one tidy data frame (this is common when working with data stored in json or xml).

### Binding rows and columns

dplyr now provides `bind_rows()` and `bind_cols()` for binding data frames together. Compared to `rbind()` and `cbind()`, the functions:

  * Accept either individual data frames, or a list of data frames:

```r
a <- data_frame(x = 1:5)
b <- data_frame(x = 6:10)

bind_rows(a, b)
#> Source: local data frame [10 x 1]
#>
#>    x
#> 1  1
#> 2  2
#> 3  3
#> 4  4
#> 5  5
#> .. .
bind_rows(list(a, b))
#> Source: local data frame [10 x 1]
#>
#>    x
#> 1  1
#> 2  2
#> 3  3
#> 4  4
#> 5  5
#> .. .
```

If `x` is a list of data frames, `bind_rows(x)` is equivalent to `do.call(rbind, x)`.

  * Are much faster:

```r
dfs <- replicate(100, data_frame(x = runif(100)), simplify = FALSE)
microbenchmark::microbenchmark(
  do.call("rbind", dfs),
  bind_rows(dfs)
)
#> Unit: microseconds
#>                   expr      min        lq   median        uq       max
#>  do.call("rbind", dfs) 5344.660 6605.3805 6964.236 7693.8465 43457.061
#>         bind_rows(dfs)  240.342  262.0845  317.582  346.6465  2345.832
#>  neval
#>    100
#>    100
```

(Generally you should avoid `bind_cols()` in favour of a join; otherwise check carefully that the rows are in a compatible order).

### List-variables

Data frames are usually made up of a list of atomic vectors that all have the same length. However, it's also possible to have a variable that's a list, which I call a list-variable. Because of `data.frame()`s complex coercion rules, the easiest way to create a data frame containing a list-column is with `data_frame()`:

```r
data_frame(x = 1, y = list(1), z = list(list(1:5, "a", "b")))
#> Source: local data frame [1 x 3]
#>
#>   x        y         z
#> 1 1 <dbl[1]> <list[3]>
```

Note how list-variables are printed: a list-variable could contain a lot of data, so dplyr only shows a brief summary of the contents. List-variables are useful for:

  * Working with summary functions that return more than one value:

```r
qs <- mtcars %>%
  group_by(cyl) %>%
  summarise(y = list(quantile(mpg)))

# Unnest input to collpase into rows
qs %>% tidyr::unnest(y)
#> Source: local data frame [15 x 2]
#>
#>    cyl    y
#> 1    4 21.4
#> 2    4 22.8
#> 3    4 26.0
#> 4    4 30.4
#> 5    4 33.9
#> .. ...  ...

# To extract individual elements into columns, wrap the result in rowwise()
# then use summarise()
qs %>%
  rowwise() %>%
  summarise(q25 = y[2], q75 = y[4])
#> Source: local data frame [3 x 2]
#>
#>     q25   q75
#> 1 22.80 30.40
#> 2 18.65 21.00
#> 3 14.40 16.25
```

  * Keeping associated data frames and models together:

```r
by_cyl <- split(mtcars, mtcars$cyl)
models <- lapply(by_cyl, lm, formula = mpg ~ wt)

data_frame(cyl = c(4, 6, 8), data = by_cyl, model = models)
#> Source: local data frame [3 x 3]
#>
#>   cyl            data   model
#> 1   4 <S3:data.frame> <S3:lm>
#> 2   6 <S3:data.frame> <S3:lm>
#> 3   8 <S3:data.frame> <S3:lm>
```

dplyr's support for list-variables continues to mature. In 0.4.0, you can join and row bind list-variables and you can create them in summarise and mutate.

My vision of list-variables is still partial and incomplete, but I'm convinced that they will make pipeable APIs for modelling much eaiser. See the draft [lowliner](https://github.com/hadley/lowliner) package for more explorations in this direction.

## Bonus

My colleague, Garrett, helped me make a cheat sheet that summarizes the data wrangling features of dplyr 0.4.0. You can download it from RStudio's new [gallery of R cheat sheets](https://www.rstudio.com/resources/cheatsheets/).

[![Data wrangling cheatsheet](https://rstudioblog.files.wordpress.com/2015/01/dplyr-0-4-cheatsheet.png)](https://www.rstudio.com/resources/cheatsheets/)

