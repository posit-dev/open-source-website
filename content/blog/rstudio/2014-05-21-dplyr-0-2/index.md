---
title: dplyr 0.2
people:
  - Hadley Wickham
date: '2014-05-21'
categories:
- Packages
slug: dplyr-0-2
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
events: blog
ported_from: rstudio
port_status: in-progress
---


I'm very excited to announce dplyr 0.2. It has three big features:

  * improved piping courtesy of the [magrittr](https://github.com/smbache/magrittr) package

  * a vastly more useful implementation of `do()`

  * five new verbs: `sample_n()`, `sample_frac()`, `summarise_each()`, `mutate_each` and `glimpse()`.

These features are described in more detail below. To learn more about the 35 new minor improvements and bug fixes, please read the [full release notes](https://github.com/hadley/dplyr/releases/tag/v0.2.0).

## Improved piping

dplyr now imports `%>%` from the [magrittr](https://github.com/smbache/magrittr) package by [Stefan Milton Bache](http://www.stefanbache.dk/). I recommend that you use this instead of `%.%` because it is easier to type (since you can hold down the shift key) and is more flexible. With you `%>%`, you can control which argument on the RHS receives the LHS with the pronoun `.`. This makes `%>%` more useful with base R functions because they don't always take the data frame as the first argument. For example you could pipe `mtcars` to `xtabs()` with:

```r
mtcars %>% xtabs( ~ cyl + vs, data = .)
```

dplyr only exports `%>%` from magrittr, but magrittr contains many other useful functions. To use them, load magrittr explicitly with `library(magrittr)`. For more details, see `vignette("magrittr")`.
`%.%` will be deprecated in a future version of dplyr, but it won't happen for a while. I've deprecated `chain()` to encourage a single style of dplyr usage: please use `%>%` instead.

## Do

`do()` has been completely overhauled, and `group_by()` + `do()` is now equivalent in power to `plyr::dlply()`. There are two ways to use `do()`, either with multiple named arguments or a single unnamed arguments. If you use named arguments, each argument becomes a list-variable in the output. A list-variable can contain any arbitrary R object which makes this form of `do()` useful for storing models:

```r
library(dplyr)
models %>% group_by(cyl) %>% do(model = lm(mpg ~ wt, data = .))
models %>% summarise(rsq = summary(model)$r.squared)
```

If you use an unnamed argument, the result should be a data frame. This allows you to apply arbitrary functions to each group.

```r
mtcars %>% group_by(cyl) %>% do(head(., 1))
```

Note the use of the pronoun `.` to refer to the data in the current group.
`do()` also has an automatic progress bar. It appears if the computation takes longer than 2 seconds and estimates how long the job will take to complete.

## New verbs

`sample_n()` randomly samples a fixed number of rows from a tbl; `sample_frac()` randomly samples a fixed fraction of rows. They currently only work for local data frames and data tables.
`summarise_each()` and `mutate_each()` make it easy to apply one or more functions to multiple columns in a tbl. These works for all srcs that `summarise()` and `mutate()` work for.
`glimpse()` makes it possible to see all the columns in a tbl, displaying as much data for each variable as can be fit on a single line.

