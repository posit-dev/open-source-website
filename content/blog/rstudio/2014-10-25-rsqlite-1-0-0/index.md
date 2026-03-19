---
title: RSQLite 1.0.0
people:
  - Hadley Wickham
date: '2014-10-25'
categories:
  - Data Wrangling
slug: rsqlite-1-0-0
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
ported_from: rstudio
port_status: in-progress
software: ["rsqlite"]
languages: ["R"]
ported_categories:
  - Packages
---


I'm very pleased to announce a new version of RSQLite 1.0.0. RSQLite is _the_ easiest way to use SQL database from R:

```r
library(DBI)
# Create an ephemeral in-memory RSQLite database
con <- dbConnect(RSQLite::SQLite(), ":memory:")
# Copy in the buit-in mtcars data frame
dbWriteTable(con, "mtcars", mtcars, row.names = FALSE)
#> [1] TRUE

# Fetch all results from a query:
res <- dbSendQuery(con, "SELECT * FROM mtcars WHERE cyl = 4 AND mpg < 23")
dbFetch(res)
#>    mpg cyl  disp  hp drat    wt  qsec vs am gear carb
#> 1 22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
#> 2 22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
#> 3 21.5   4 120.1  97 3.70 2.465 20.01  1  0    3    1
#> 4 21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2
dbClearResult(res)
#> [1] TRUE

# Or fetch them a chunk at a time
res <- dbSendQuery(con, "SELECT * FROM mtcars WHERE cyl = 4")
while(!dbHasCompleted(res)){
  chunk <- dbFetch(res, n = 10)
  print(nrow(chunk))
}
#> [1] 10
#> [1] 1
dbClearResult(res)
#> [1] TRUE

# Good practice to disconnect from the database when you're done
dbDisconnect(con)
#> [1] TRUE
```

RSQLite 1.0.0 is mostly a cleanup release. This means a lot of old functions have been deprecated and removed:

  * `idIsValid()` is deprecated; use `dbIsValid()` instead. `dbBeginTransaction()` is deprecated; use `dbBegin()` instead. Use `dbFetch()` instead of `fetch()`.

  * `dbBuildTableDefinition()` is now `sqliteBuildTableDefinition()` (to avoid implying that it's a DBI generic).

  * Internal `sqlite*()` functions are no longer exported (#20). `safe.write()` is no longer exported.

It also includes a few minor improvements and bug fixes. The most important are:

  * Inlined `RSQLite.extfuns` - use `initExtension()` to load the many useful extension functions.

  * Methods no longer automatically clone the connection is there is an open result set. This was implemented inconsistently in a handful of places. RSQLite is now more forgiving if you forget to close a result set - it will close it for you, with a warning. It's still good practice to clean up after yourself with `dbClearResults()`, but you don't have to.

  * `dbBegin()`, `dbCommit()` and `dbRollback()` throw errors on failure, rather than returning `FALSE`. They all gain a `name` argument to specify named savepoints.

  * `dbWriteTable()` has been rewritten. It uses a better quoting strategy, throws errors on failure, and only automatically adds row names only if they're strings. (NB: `dbWriteTable()` also has a method that allows you load files directly from disk.)

For a complete list of changes, please see the full [release notes](https://github.com/rstats-db/RSQLite/releases/tag/v1.0.0).

