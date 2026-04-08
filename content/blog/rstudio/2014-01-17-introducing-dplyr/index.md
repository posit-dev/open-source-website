---
title: Introducing dplyr
description: "dplyr: a new package for fast data manipulation with a consistent API that works on local data frames and remote databases."
auto-description: true
people:
  - Hadley Wickham
date: '2014-01-17'
categories:
  - Data Wrangling
slug: introducing-dplyr
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - RStudio
ported_from: rstudio
port_status: in-progress
software: ["dplyr"]
languages: ["R"]
ported_categories:
  - Packages
---


`dplyr` is a new package which provides a set of tools for efficiently manipulating datasets in R. `dplyr` is the next iteration of `plyr`, focussing on only data frames. `dplyr` is faster, has a more consistent API and should be easier to use. There are three key ideas that underlie `dplyr`:

  1. Your time is important, so [Romain Francois](http://romainfrancois.blog.free.fr/) has written the key pieces in [Rcpp](http://www.rcpp.org/) to provide blazing fast performance. Performance will only get better over time, especially once we figure out the best way to make the most of multiple processors.

  2. Tabular data is tabular data regardless of where it lives, so you should use the same functions to work with it. With `dplyr`, anything you can do to a local data frame you can also do to a remote database table. PostgreSQL, MySQL, SQLite and Google bigquery support is built-in; adding a new backend is a matter of implementing a handful of S3 methods.

  3. The bottleneck in most data analyses is the time it takes for you to figure out what to do with your data, and dplyr makes this easier by having individual functions that correspond to the most common operations (`group_by`, `summarise`, `mutate`, `filter`, `select` and `arrange`). Each function does one only thing, but does it well.

Lets compare `plyr` and `dplyr` with a little example, using the `Batting` dataset from the fantastic [`Lahman`](http://cran.us.r-project.org/web/packages/Lahman/) package which makes the complete Lahman baseball database easily accessible from R. Pretend we want to find the five players who have batted in the most games in all of baseball history.

In `plyr`, we might write code like this:

```r
library(Lahman)
library(plyr)

games <- ddply(Batting, "playerID", summarise, total = sum(G))
head(arrange(games, desc(total)), 5)
```

We use `ddply()` to break up the `Batting` dataframe into pieces according to the `playerID` variable, then apply `summarise()` to reduce the player data to a single row. Each row in `Batting` represents one year of data for one player, so we figure out the total number of games with `sum(G)` and save it in a new variable called `total`. We sort the result so the most games come at the top and then use `head()` to pull off the first five.

In `dplyr`, the code is similar:

```r
library(Lahman)
library(dplyr)

players <- group_by(Batting, playerID)
games <- summarise(players, total = sum(G))
head(arrange(games, desc(total)), 5)
```

But now grouping is now a top level operation performed by `group_by()`, and `summarise()` works directly on the grouped data, rather than being called from inside another function. The other big difference is speed. `plyr` took about 7s on my computer, and `dplyr` took 0.2s, a 35x speed-up. This is common when switching from plyr to dplyr, and for many operations you'll see a 20x-1000x speedup.

`dplyr` provides another innovation over `plyr`: the ability to chain operations together from left to right with the `%.%` operator. This makes `dplyr` behave a little like a grammar of data manipulation:

```r
Batting %.%
  group_by(playerID) %.%
  summarise(total = sum(G)) %.%
  arrange(desc(total)) %.%
  head(5)
```

Read more about it in the help, `?"%.%"`.

If this small example has whet your interest, you can learn more from the built-in vignettes. First install `dplyr` with `install.packages("dplyr")`, then run:

  * [`vignette("introduction", package = "dplyr")`](http://cran.rstudio.com/web/packages/dplyr/vignettes/introduction.html) to learn how the main verbs of `dplyr` work with data frames.

  * [`vignette("databases", package = "dplyr")`](http://cran.rstudio.com/web/packages/dplyr/vignettes/databases.html) to learn how to work with databases from dplyr.

You can track development progress at <http://github.com/hadley/dplyr>, report bugs at <http://github.com/hadley/dplyr/issues> and get help with data manipulation challenges at <https://groups.google.com/group/manipulatr>. If you ask a question specifically about `dplyr` on StackOverflow, please tag it with `dplyr` and I'll make sure to read it.

