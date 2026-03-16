---
title: dplyr 0.3
people:
  - Hadley Wickham
date: '2014-10-13'
categories:
- Packages
- tidyverse
slug: dplyr-0-3-2
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


I'm very pleased to announce that dplyr 0.3 is now available from CRAN. Get the latest version by running:

```r
install.packages("dplyr")
```

There are four major new features:

  * Four new high-level verbs: `distinct()`, `slice()`, `rename()`, and `transmute()`.

  * Three new helper functions `between`, `count()`, and `data_frame()`.

  * More flexible join specifications.

  * Support for row-based set operations.

There are two new features of interest to developers. They make it easier to write packages that use dplyr:

  * It's now much easier to program with dplyr (using standard evaluation).

  * Improved database backends.

I describe each of these in turn below.

## New verbs

`distinct()` returns distinct (unique) rows of a table:

```r
library(nycflights13)
# Find all origin-destination pairs
flights %>%
  select(origin, dest) %>%
  distinct()
#> Source: local data frame [224 x 2]
#>
#>    origin dest
#> 1     EWR  IAH
#> 2     LGA  IAH
#> 3     JFK  MIA
#> 4     JFK  BQN
#> 5     LGA  ATL
#> ..    ...  ...
```

`slice()` allows you to select rows by position. It includes positive integers and drops negative integers:

```r
# Get the first flight to each destination
flights %>%
  group_by(dest) %>%
  slice(1)
#> Source: local data frame [105 x 16]
#> Groups: dest
#>
#>    year month day dep_time dep_delay arr_time arr_delay carrier tailnum
#> 1  2013    10   1     1955        -6     2213       -35      B6  N554JB
#> 2  2013    10   1     1149       -10     1245       -14      B6  N346JB
#> 3  2013     1   1     1315        -2     1413       -10      EV  N13538
#> 4  2013     7   6     1629        14     1954         1      UA  N587UA
#> 5  2013     1   1      554        -6      812       -25      DL  N668DN
#> ..  ...   ... ...      ...       ...      ...       ...     ...     ...
#> Variables not shown: flight (int), origin (chr), dest (chr), air_time
#>   (dbl), distance (dbl), hour (dbl), minute (dbl)
```

`transmute()` and `rename()` are variants of `mutate()` and `select()`. Transmute drops all columns that you didn't specifically mention, `rename()` keeps all columns that you didn't specifically mention. They complete this table:

| | Drop others | Keep others |
|:---|:---|:---|
| Rename & reorder variables | `select()` | `rename()` |
| Compute new variables | `transmute()` | `mutate()` |

## New helpers

`data_frame()`, contributed by [Kevin Ushey](https://github.com/kevinushey), is a nice way to create data frames:

  * It never changes the type of its inputs (i.e. no more `stringsAsFactors = FALSE`!)

```r
data.frame(x = letters) %>% sapply(class)
#>        x
#> "factor"
data_frame(x = letters) %>% sapply(class)
#>           x
#> "character"
```

  * Or the names of variables:

```r
data.frame(`crazy name` = 1) %>% names()
#> [1] "crazy.name"
data_frame(`crazy name` = 1) %>% names()
#> [1] "crazy name"
```

  * It evaluates its arguments lazyily and in order:

```r
data_frame(x = 1:5, y = x ^ 2)
#> Source: local data frame [5 x 2]
#>
#>   x  y
#> 1 1  1
#> 2 2  4
#> 3 3  9
#> 4 4 16
#> 5 5 25
```

  * It adds `tbl_df()` class to output, never adds `row.names()`, and only recycles vectors of length 1 (recycling is a frequent source of bugs in my experience).

The `count()` function wraps up the common combination of `group_by()` and `summarise()`:

```r
# How many flights to each destination?
flights %>% count(dest)
#> Source: local data frame [105 x 2]
#>
#>    dest     n
#> 1   ABQ   254
#> 2   ACK   265
#> 3   ALB   439
#> 4   ANC     8
#> 5   ATL 17215
#> ..  ...   ...

# Which planes flew the most?
flights %>% count(tailnum, sort = TRUE)
#> Source: local data frame [4,044 x 2]
#>
#>    tailnum    n
#> 1          2512
#> 2   N725MQ  575
#> 3   N722MQ  513
#> 4   N723MQ  507
#> 5   N711MQ  486
#> ..     ...  ...

# What's the total carrying capacity of planes by year of purchase
planes %>% count(year, wt = seats)
#> Source: local data frame [47 x 2]
#>
#>    year   n
#> 1  1956 102
#> 2  1959  18
#> 3  1963  10
#> 4  1965 149
#> 5  1967   9
#> ..  ... ...
```

## Better joins

You can now join by different variables in each table:

```r
narrow <- flights %>% select(origin, dest, year:day)

# Add destination airport metadata
narrow %>% left_join(airports, c("dest" = "faa"))
#> Source: local data frame [336,776 x 11]
#>
#>    dest origin year month day                            name   lat    lon
#> 1   IAH    EWR 2013     1   1    George Bush Intercontinental 29.98 -95.34
#> 2   IAH    LGA 2013     1   1    George Bush Intercontinental 29.98 -95.34
#> 3   MIA    JFK 2013     1   1                      Miami Intl 25.79 -80.29
#> 4   BQN    JFK 2013     1   1                              NA    NA     NA
#> 5   ATL    LGA 2013     1   1 Hartsfield Jackson Atlanta Intl 33.64 -84.43
#> ..  ...    ...  ...   ... ...                             ...   ...    ...
#> Variables not shown: alt (int), tz (dbl), dst (chr)

# Add origin airport metadata
narrow %>% left_join(airports, c("origin" = "faa"))
#> Source: local data frame [336,776 x 11]
#>
#>    origin dest year month day                name   lat    lon alt tz dst
#> 1     EWR  IAH 2013     1   1 Newark Liberty Intl 40.69 -74.17  18 -5   A
#> 2     LGA  IAH 2013     1   1          La Guardia 40.78 -73.87  22 -5   A
#> 3     JFK  MIA 2013     1   1 John F Kennedy Intl 40.64 -73.78  13 -5   A
#> 4     JFK  BQN 2013     1   1 John F Kennedy Intl 40.64 -73.78  13 -5   A
#> 5     LGA  ATL 2013     1   1          La Guardia 40.78 -73.87  22 -5   A
#> ..    ...  ...  ...   ... ...                 ...   ...    ... ... .. ...
```

(`right_join()` and `outer_join()` implementations are planned for dplyr 0.4.)

## Set operations

You can use `intersect()`, `union()` and `setdiff()` with data frames, data tables and databases:

```r
jfk_planes <- flights %>%
  filter(origin == "JFK") %>%
  select(tailnum) %>%
  distinct()
lga_planes <- flights %>%
  filter(origin == "LGA") %>%
  select(tailnum) %>%
  distinct()

# Planes that fly out of either JGK or LGA
nrow(union(jfk_planes, lga_planes))
#> [1] 3592

# Planes that fly out of both JFK and LGA
nrow(intersect(jfk_planes, lga_planes))
#> [1] 1311

# Planes that fly out JGK but not LGA
nrow(setdiff(jfk_planes, lga_planes))
#> [1] 647
```

## Programming with dplyr

You can now program with dplyr - every function that uses non-standard evaluation (NSE) also has a standard evaluation (SE) twin that ends in `_`. For example, the SE version of `filter()` is called `filter_()`. The SE version of each function has similar arguments, but they must be explicitly "quoted". Usually the best way to do this is to use `~`:

```r
airport <- "ANC"
# NSE version
filter(flights, dest == airport)
#> Source: local data frame [8 x 16]
#>
#>    year month day dep_time dep_delay arr_time arr_delay carrier tailnum
#> 1  2013     7   6     1629        14     1954         1      UA  N587UA
#> 2  2013     7  13     1618         3     1955         2      UA  N572UA
#> 3  2013     7  20     1618         3     2003        10      UA  N567UA
#> 4  2013     7  27     1617         2     1906       -47      UA  N559UA
#> 5  2013     8   3     1615         0     2003        10      UA  N572UA
#> ..  ...   ... ...      ...       ...      ...       ...     ...     ...
#> Variables not shown: flight (int), origin (chr), dest (chr), air_time
#>   (dbl), distance (dbl), hour (dbl), minute (dbl)

# Equivalent SE code:
criteria <- ~dest == airport
filter_(flights, criteria)
#> Source: local data frame [8 x 16]
#>
#>    year month day dep_time dep_delay arr_time arr_delay carrier tailnum
#> 1  2013     7   6     1629        14     1954         1      UA  N587UA
#> 2  2013     7  13     1618         3     1955         2      UA  N572UA
#> 3  2013     7  20     1618         3     2003        10      UA  N567UA
#> 4  2013     7  27     1617         2     1906       -47      UA  N559UA
#> 5  2013     8   3     1615         0     2003        10      UA  N572UA
#> ..  ...   ... ...      ...       ...      ...       ...     ...     ...
#> Variables not shown: flight (int), origin (chr), dest (chr), air_time
#>   (dbl), distance (dbl), hour (dbl), minute (dbl)
```

To learn more, read the [Non-standard evaluation](http://cran.r-project.org/web/packages/dplyr/vignettes/nse.html) vignette. This new approach is powered by the [lazyeval package](https://github.com/hadley/lazyeval) which provides all the tools needed to implement NSE consistently and correctly. I now understand how to implement NSE consistently and correctly, and I'll be using the same approach everywhere.

## Database backends

The database backend system has been completely overhauled in order to make it possible to add backends in other packages, and to support a much wider range of databases. If you're interested in implementing a new dplyr backend, please check out `vignette("new-sql-backend")` - it's really not that much work.

The first package to take advantage of this system is [MonetDB.R](http://cran.r-project.org/web/packages/MonetDB.R), which now provides the MonetDB backend for dplyr.

## Other changes

As well as the big new features described here, dplyr 0.3 also fixes many bugs and makes numerous minor improvements. See the [release notes](https://github.com/hadley/dplyr/releases/tag/v0.3) for a complete list of the changes.

