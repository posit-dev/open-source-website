---
title: dbplyr 1.1.0
people:
  - Hadley Wickham
date: '2017-06-27'
categories:
  - Data Wrangling
slug: dbplyr-1-1-0
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


I'm pleased to announce the release of the [dbplyr](http://github.com/hadley/dbplyr/) package, which now contains all dplyr code related to connecting to databases. This shouldn't affect you-as-a-user much, but it makes dplyr simpler, and makes it easier to release improvements just for database related code.

You can install the latest version of dbplyr with:

```r
install.packages("dbplyr")
```

## DBI and dplyr alignment

The biggest change in this release is that dplyr/dbplyr works much more directly with DBI database connections. This makes it much easier to switch between low-level queries written in SQL, and high-level data manipulation functions written with dplyr verbs.

To connect to a database, first use `DBI::dbConnect()` to create a database connection. For example, the following code connects to a temporary, in-memory, SQLite database, then uses DBI to copy over some data.

```r
con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")
DBI::dbWriteTable(con, "iris", iris)
#> [1] TRUE
DBI::dbWriteTable(con, "mtcars", mtcars)
#> [1] TRUE
```

With this connection in hand, you can execute hand-written SQL queries:

```r
DBI::dbGetQuery(con, "SELECT count() FROM iris")
#>   count()
#> 1     150
```

Or you can let dplyr generate the SQL for you:

```r
iris2 <- tbl(con, "iris")

species_mean <- iris2 %>%
  group_by(Species) %>%
  summarise_all(mean)

species_mean %>% show_query()
#> <SQL>
#> SELECT `Species`, AVG(`Sepal.Length`) AS `Sepal.Length`, AVG(`Sepal.Width`) AS `Sepal.Width`, AVG(`Petal.Length`) AS `Petal.Length`, AVG(`Petal.Width`) AS `Petal.Width`
#> FROM `iris`
#> GROUP BY `Species`
species_mean
#> # Source:   lazy query [?? x 5]
#> # Database: sqlite 3.11.1 [:memory:]
#>      Species Sepal.Length Sepal.Width Petal.Length Petal.Width
#>        <chr>        <dbl>       <dbl>        <dbl>       <dbl>
#> 1     setosa        5.006       3.428        1.462       0.246
#> 2 versicolor        5.936       2.770        4.260       1.326
#> 3  virginica        6.588       2.974        5.552       2.026
```

This alignment is made possible thanks to the hard work of [Kirill Muller](https://github.com/krlmlr) who has been working to make [DBI backends](https://www.r-consortium.org/blog/2017/05/15/improving-dbi-a-retrospect) more consistent, comprehensive, and easier to use. This work has been funded by the [R Consortium](https://www.r-consortium.org) and will [continue this year](https://www.r-consortium.org/blog/2017/04/03/q1-2017-isc-grants) with improvements to backends for the two major open source databases MySQL/MariaDB and PostgreSQL.

(You can continue to the old style `src_mysql()`, `src_postgres()`, and `src_sqlite()` functions, which still live in dplyr, but I recommend that you switch to the new style for new code)

## SQL translation

We've also worked to improve the translation of R code to SQL. Thanks to [@hhoeflin](https://github.com/hhoeflin), dbplyr now has a basic SQL optimiser that considerably reduces the number of subqueries needed in many expressions. For example, the following code used to generate three subqueries, but now generates idiomatic SQL:

```r
con %>%
  tbl("mtcars") %>%
  filter(cyl > 2) %>%
  select(mpg:hp) %>%
  head(10) %>%
  show_query()
#> <SQL>
#> SELECT `mpg` AS `mpg`, `cyl` AS `cyl`, `disp` AS `disp`, `hp` AS `hp`
#> FROM `mtcars`
#> WHERE (`cyl` > 2.0)
#> LIMIT 10
```

At a lower-level, dplyr now:

  * Can translate `case_when()`:

```r
library(dbplyr)
translate_sql(case_when(x > 1 ~ "big", y < 2 ~ "small"), con = con)
#> <SQL> CASE
#> WHEN (`x` > 1.0) THEN ('big')
#> WHEN (`y` < 2.0) THEN ('small')
#> END
```

  * Has better support for type coercions:

```r
translate_sql(as.character(cyl), con = con)
#> <SQL> CAST(`cyl` AS TEXT)
translate_sql(as.integer(cyl), con = con)
#> <SQL> CAST(`cyl` AS INTEGER)
translate_sql(as.double(cyl), con = con)
#> <SQL> CAST(`cyl` AS NUMERIC)
```

  * Can more reliably translate `%IN%`:

```r
translate_sql(x %in% 1:5, con = con)
#> <SQL> `x` IN (1, 2, 3, 4, 5)
translate_sql(x %in% 1L, con = con)
#> <SQL> `x` IN (1)
translate_sql(x %in% c(1L), con = con)
#> <SQL> `x` IN (1)
```

You can now use `in_schema()` to refer to tables in schema: `in_schema("my_schema_name", "my_table_name")`. You can use the result of this function anywhere you could previously use a table name.

We've also included better translations for Oracle, MS SQL Server, Hive and Impala. We're working to add support for more databases over time, but adding support on your own is surprisingly easy. Submit an issue to [dplyr](https://github.com/tidyverse/dplyr/issues) and we'll help you get started.

These are just the highlights: you can see the full set of improvements and bug fixes in the [release notes](https://github.com/tidyverse/dbplyr/releases/tag/v1.0.0)

## Contributors

As with all R packages, this is truly a community effort. A big thanks goes to all those who contributed code or documentation to this release: [Austen Head](https://github.com/austenhead), [Edgar Ruiz](https://github.com/edgararuiz), [Greg Freedman Ellis](https://github.com/gergness), [Hannes Mühleisen](https://github.com/hannesmuehleisen), [Ian Cook](https://github.com/ianmcook), [Karl Dunkle Werner](https://github.com/karldw), [Michael Sumner](https://github.com/mdsumner), [Mine Cetinkaya-Rundel](https://github.com/mine-cetinkaya-rundel), [@shabbybanks](https://github.com/shabbybanks) and [Sergio Oller](https://github.com/zeehio)

## Vision

Since you've read this far, I also wanted to touch on RStudio's vision for databases. Many analysts have most of their data in databases, and making it as easy as possible to get data out of the database and into R makes a huge difference. Thanks to the community, R already has strong tools for talking to the popular open source databases. But support for connecting to enterprise databases and solving enterprise challenges has lagged somewhat. At RStudio we are actively working to solve these problems.

As well as dbplyr and DBI, we are working on many other pain points in the database ecosystem. You'll hear much more about these packages in the future, but I wanted to touch on the highlights so you can see where we are heading. These pieces are not yet as integrated as they should be, but they are valuable by themselves, and we will continue to work to make a seamless database experience, that is as good as (or better than!) any other environment.

  * The [odbc](https://github.com/rstats-db/odbc) package provides a DBI compliant backend for any database with an ODBC driver. Compared to the existing RODBC package, odbc is faster (~3x for reading, ~2x for writing), translates date/time data types, and is under active development.RStudio is also planning on providing best-of-breed ODBC drivers for the most important enterprise databases to our Pro customers. If you've felt the pain of connecting to your enterprise database and would like to learn more, please schedule a meeting with our [sales team](https://rstudio.youcanbook.me/).

  * You should never record database credentials in your R scripts, so we are working on safer ways to store them that don't add a lot of extra hassle. One piece of the puzzle is the [keyring](https://github.com/gaborcsardi/keyring) package, which allows you to securely store information in your system keychain, and only decrypt it when needed.Another piece of the puzzle is the [config](https://github.com/rstudio/config) package, which makes it easy to parameterise your database connection credentials so that you can connect to your testing database when experimenting locally, and your production database when you [deploy your code](https://www.rstudio.com/products/connect/).

  * Connecting to databases from Shiny can be challenging because you don't want a fresh connection every for every user action (because that's slow), and you don't want one connection per app (because that's unreliable). The [pool](https://github.com/rstudio/pool) package allows you to manage a shared pool of connections for your app, giving you both speed and reliability.

  * We're also working to make sure all of these pieces are easily used from the IDE and inside R Markdown. One neat feature that you might not have heard about is support for [SQL chunks](https://rmarkdown.rstudio.com/authoring_knitr_engines.html#sql) in R Markdown.

If any of these pieces sound interesting, please stay tuned to the blog for more upcoming announcements. Please also check out out new database website: <https://db.rstudio.com>. Over time, this website will expand to document all database best practices, so you can find everything you need in one place.

