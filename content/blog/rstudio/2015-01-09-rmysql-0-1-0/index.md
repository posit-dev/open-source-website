---
title: RMySQL 0.10.0
people:
  - Hadley Wickham
date: '2015-01-09'
slug: rmysql-0-1-0
blogcategories:
- Products and Technology
- Open Source
tags:
ported_from: rstudio
port_status: in-progress
software: ["rmysql"]
languages: ["R"]
categories:
  - Data Wrangling
ported_categories:
  - Packages
---


[Jeroen Ooms](http://jeroenooms.github.io) and I are very pleased to announce a new version of RMySQL, the R package that allows you to talk to MySQL (and MariaDB) databases. We have taken over maintenance from [Jeffrey Horner](http://biostat.mc.vanderbilt.edu/wiki/Main/JeffreyHorner), who has done a great job of maintaining the package of the last few years, but no longer has time to look after it. Thanks for all your hard work Jeff!

## Using RMySQL

```r
library(DBI)

# Connect to a public database that I'm running on Google's
# cloud SQL service. It contains a copy of the data in the
# datasets package.
con <-  dbConnect(RMySQL::MySQL(),
  username = "public",
  password = "F60RUsyiG579PeKdCH",
  host = "173.194.227.144",
  port = 3306,
  dbname = "datasets"
)

# Run a query
dbGetQuery(con, "SELECT * FROM mtcars WHERE cyl = 4 AND mpg < 23")
#>       row_names  mpg cyl  disp  hp drat    wt  qsec vs am gear carb
#> 1    Datsun 710 22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
#> 2      Merc 230 22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
#> 3 Toyota Corona 21.5   4 120.1  97 3.70 2.465 20.01  1  0    3    1
#> 4    Volvo 142E 21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2

# It's polite to let the database know when you're done
dbDisconnect(con)
#> [1] TRUE
```

It's generally a bad idea to put passwords in your code, so instead of typing them directly, you can create a file called `~/.my.cnf` that contains

    [cloudSQL]
    username=public
    password=F60RUsyiG579PeKdCH
    host=173.194.227.144
    port=3306
    database=datasets

Then you can connect with:

```r
con <-  dbConnect(RMySQL::MySQL(), group = "cloudSQL")
```

## Changes in this release

RMySQL 0.10.0 is mostly a cleanup release. RMySQL is one of the oldest packages on CRAN, and according to the timestamps, it is older than many recommended packages, and only slightly younger than MASS! That explains why a facelift was well overdue.

The most important change is an improvement to the build process so that CRAN binaries are now available for Windows and OS X Mavericks. This should make your life much easier if you're on one of these platforms. We'd love your feedback on the new build scripts. There have been many problems in the past, so we'd like to know that this client works well across platforms and versions of MySQL server.

Otherwise, the changes update RMySQL for DBI 0.3 compatibility:

  * Internal `mysql*()` functions are no longer exported. Please use the corresponding DBI generics instead.

  * RMySQL gains transaction support with `dbBegin()`, `dbCommit()`, and `dbRollback()`. (But note that MySQL does not allow data definition language statements to be rolled back.)

  * Added method for `dbFetch()`. Please use this instead of `fetch()`. `dbFetch()` now returns a 0-row data frame (instead of an 0-col data frame) if there are no results.

  * Added methods for `dbIsValid()`. Please use these instead of `isIdCurrent()`.

  * `dbWriteTable()` has been rewritten. It uses a better quoting strategy, throws errors on failure, and only automatically adds row names only if they're strings. (NB: `dbWriteTable()` also has a method that allows you load files directly from disk - this is likely to be faster if your file is one of the formats supported.)

For a complete list of changes, please see the full [release notes](https://github.com/rstats-db/RMySQL/releases/tag/v0.10).

