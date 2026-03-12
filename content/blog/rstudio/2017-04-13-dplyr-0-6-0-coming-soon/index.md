---
title: dplyr 0.6.0 coming soon!
people:
  - Hadley Wickham
date: '2017-04-13'
categories:
- Packages
slug: dplyr-0-6-0-coming-soon
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
events: blog
ported_from: rstudio
port_status: in-progress
---


I'm planning to submit dplyr 0.6.0 to CRAN on May 11 (in four weeks time). In preparation, I'd like to announce that the release candidate, dplyr 0.5.0.9002 is now available. I would really appreciate it if you'd try it out and report any problems. This will ensure that the official release has as few bugs as possible.

## Installation

Install the pre-release version with:

```r
# install.packages("devtools")
devtools::install_github("tidyverse/dplyr")
```

If you discover any problems, please file a minimal [reprex](http://github.com/jennybc/reprex#readme) on [GitHub](https://github.com/tidyverse/dplyr/issues). You can roll back to the released version with:

```r
install.packages("dplyr")
```

## Features

dplyr 0.6.0 is a major release including over 100 bug fixes and improvements. There are three big changes that I want to touch on here:

  * Databases

  * Improved encoding support (particularly for CJK on windows)

  * Tidyeval, a new framework for programming with dplyr

You can see a complete list of changes in the draft [release notes](https://github.com/tidyverse/dplyr/releases/tag/v0.6.0-rc).

### Databases

Almost all database related code has been moved out of dplyr and into a new package, [dbplyr](http://github.com/hadley/dbplyr/). This makes dplyr simpler, and will make it easier to release fixes for bugs that only affect databases.

To install the development version of dbplyr so you can try it out, run:

```r
devtools::install_github("hadley/dbplyr")
```

There's one major change, as well as a whole heap of bug fixes and minor improvements. It is now no longer necessary to create a remote "src". Instead you can work directly with the database connection returned by DBI, reflecting the robustness of the DBI ecosystem. Thanks largely to the work of [Kirill Muller](https://github.com/krlmlr) (funded by the [R Consortium](https://www.r-consortium.org)) DBI backends are now much more consistent, comprehensive, and easier to use. That means that there's no longer a need for a layer between you and DBI.

You can continue to use `src_mysql()`, `src_postgres()`, and `src_sqlite()` (which still live in dplyr), but I recommend a new style that makes the connection to DBI more clear:

```r
con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")
DBI::dbWriteTable(con, "iris", iris)
#> [1] TRUE

iris2 <- tbl(con, "iris")
iris2
#> Source:     table<iris> [?? x 5]
#> Database:   sqlite 3.11.1 [:memory:]
#>
#>    Sepal.Length Sepal.Width Petal.Length Petal.Width Species
#>           <dbl>       <dbl>        <dbl>       <dbl>   <chr>
#> 1           5.1         3.5          1.4         0.2  setosa
#> 2           4.9         3.0          1.4         0.2  setosa
#> 3           4.7         3.2          1.3         0.2  setosa
#> 4           4.6         3.1          1.5         0.2  setosa
#> 5           5.0         3.6          1.4         0.2  setosa
#> 6           5.4         3.9          1.7         0.4  setosa
#> 7           4.6         3.4          1.4         0.3  setosa
#> 8           5.0         3.4          1.5         0.2  setosa
#> 9           4.4         2.9          1.4         0.2  setosa
#> 10          4.9         3.1          1.5         0.1  setosa
#> # ... with more rows
```

This is particularly useful if you want to perform non-SELECT queries as you can do whatever you want with `DBI::dbGetQuery()` and `DBI::dbExecute()`.

If you've implemented a database backend for dplyr, please read the [backend news](https://github.com/hadley/dbplyr/blob/master/NEWS.md#backends) to see what's changed from your perspective (not much). If you want to ensure your package works with both the current and previous version of dplyr, see `wrap_dbplyr_obj()` for helpers.

### Character encoding

We have done a lot of work to ensure that dplyr works with encodings other that Latin1 on Windows. This is most likely to affect you if you work with data that contains Chinese, Japanese, or Korean (CJK) characters. dplyr should now just work with such data.

### Tidyeval

dplyr has a new approach to non-standard evaluation (NSE) called tidyeval. Tidyeval is described in detail in a new [vignette about programming with dplyr](http://dplyr.tidyverse.org/articles/programming.html) but, in brief, it gives you the ability to interpolate values in contexts where dplyr usually works with expressions:

```r
my_var <- quo(homeworld)

starwars %>%
  group_by(!!my_var) %>%
  summarise_at(vars(height:mass), mean, na.rm = TRUE)
#> # A tibble: 49 × 3
#>         homeworld   height  mass
#>             <chr>    <dbl> <dbl>
#> 1        Alderaan 176.3333  64.0
#> 2     Aleen Minor  79.0000  15.0
#> 3          Bespin 175.0000  79.0
#> 4      Bestine IV 180.0000 110.0
#> 5  Cato Neimoidia 191.0000  90.0
#> 6           Cerea 198.0000  82.0
#> 7        Champala 196.0000   NaN
#> 8       Chandrila 150.0000   NaN
#> 9    Concord Dawn 183.0000  79.0
#> 10       Corellia 175.0000  78.5
#> # ... with 39 more rows
```

This will make it much easier to eliminate copy-and-pasted dplyr code by extracting repeated code into a function.

This also means that the underscored version of each main verb (`filter_()`, `select_()` etc). is no longer needed, and so these functions have been deprecated (but remain around for backward compatibility).

