---
title: bigrquery 0.4.0
people:
  - Hadley Wickham
date: '2017-06-26'
categories:
  - Data Wrangling
slug: bigrquery-0-4-0
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - RStudio
ported_from: rstudio
port_status: in-progress
software: ["bigrquery"]
languages: ["R"]
ported_categories:
  - Packages
---


I'm pleased to announce that bigrquery 0.4.0 is now on CRAN. bigrquery makes it possible to talk to [Google's BigQuery](https://cloud.google.com/bigquery/) cloud database. It provides both [DBI](https://cloud.google.com/bigquery/) and [dplyr](http://dplyr.tidyverse.org/) backends so you can interact with BigQuery using either low-level SQL or high-level dplyr verbs.

Install the latest version of bigrquery with:

```r
install.packages("bigrquery")
```

## Basic usage

Connect to a bigquery database using DBI:

```r
library(dplyr)

con <- DBI::dbConnect(dbi_driver(),
  project = "publicdata",
  dataset = "samples",
  billing = "887175176791"
)
DBI::dbListTables(con)
#> [1] "github_nested"   "github_timeline" "gsod"            "natality"
#> [5] "shakespeare"     "trigrams"        "wikipedia"
```

(You'll be prompted to authenticate interactively, or you can use a service token with `set_service_token()`.)

Then you can either submit your own SQL queries or use dplyr to write them for you:

```r
shakespeare <- con %>% tbl("shakespeare")
shakespeare %>%
  group_by(word) %>%
  summarise(n = sum(word_count))
#> 0 bytes processed
#> # Source:   lazy query [?? x 2]
#> # Database: BigQueryConnection
#>            word     n
#>           <chr> <int>
#>  1   profession    20
#>  2       augury     2
#>  3 undertakings     3
#>  4      surmise     8
#>  5     religion    14
#>  6     advanced    16
#>  7     Wormwood     1
#>  8    parchment     8
#>  9      villany    49
#> 10         digs     3
#> # ... with more rows
```

## New features

  * dplyr support has been updated to require dplyr 0.7.0 and use dbplyr. This means that you can now more naturally work directly with DBI connections. dplyr now translates to modern BigQuery SQL which supports a broader set of translations. Along the way I also fixed a vareity of SQL generation bugs.

  * New functions `insert_extract_job()` makes it possible to extract data and save in google storage, and `insert_table()` allows you to insert empty tables into a dataset.

  * All POST requests (inserts, updates, copies and `query_exec`) now take `...`. This allows you to add arbitrary additional data to the request body making it possible to use parts of the BigQuery API that are otherwise not exposed. `snake_case` argument names are automatically converted to `camelCase` so you can stick consistently to snake case in your R code.

  * Full support for DATE, TIME, and DATETIME types (#128).

There were a variety of bug fixes and other minor improvements: see the [release notes](https://github.com/rstats-db/bigrquery/releases/tag/v0.4.0) for full details.

## Contributors

bigrquery a community effort: a big thanks go to [Christofer Bäcklin](https://github.com/backlin), [Jarod G.R. Meng](https://github.com/jarodmeng) and [Akhmed Umyarov](https://github.com/realAkhmed) for their pull requests. Thank you all for your contributions!

