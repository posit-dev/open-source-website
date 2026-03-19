---
title: pool package on CRAN
people:
  - Bárbara Borges Ribeiro
date: '2017-11-17'
slug: pool-0-1-3
categories:
  - Interactive Apps
tags:
  - Databases
  - Shiny
  - Packages
  - RStudio
blogcategories:
  - Products and Technology
  - Open Source
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
ported_categories:
  - Packages
  - Shiny
---


The [pool package](https://github.com/rstudio/pool) makes it easier for Shiny developers to connect to databases. Up until now, there wasn't a clearly good way to do this. As a Shiny app author, if you connect to a database globally (outside of the server function), your connection won't be robust because all sessions would share that connection (which could leave most users hanging when one of them is using it, or even all of them if the connection breaks). But if you try to connect each time that you need to make a query (e.g. for every reactive you have), your app becomes a lot slower, as it can take in the order of seconds to establish a new connection. The `pool` package solves this problem by taking care of when to connect and disconnect, allowing you to write performant code that automatically reconnects to the database only when needed.

So, if you are a Shiny app author who needs to connect and interact with databases inside your apps, keep reading because this package was created to make your life easier.

## What the `pool` package does
The `pool` package adds a new level of abstraction when connecting to a database: instead of directly fetching a connection from the database, you will create an object (called a "pool") with a reference to that database. The pool holds a number of connections to the database. Some of these may be currently in-use and some of these may be idle, waiting for a new query or statement to request them. Each time you make a query, you are querying the pool, rather than the database. Under the hood, the pool will either give you an idle connection that it previously fetched from the database or, if it has no free connections, fetch one and give it to you. You never have to create or close connections directly: the pool knows when it should grow, shrink or keep steady. You only need to close the pool when you’re done.

Since `pool` integrates with both `DBI` and `dplyr`, there are very few things that will be new to you, if you're already using either of those packages. Essentially, you shouldn't feel the difference, with the exception of creating and closing a "Pool" object (as opposed to connecting and disconnecting a "DBIConnection" object). See [this copy-pasteable app](https://github.com/rstudio/pool#usage) that uses `pool` and `dplyr` to query a MariaDB database (hosted on AWS) inside a Shiny app.

Very briefly, here's how you'd connect to a database, write a table into it using `DBI`, query it using `dplyr`, and finally disconnect (you must have `DBI`, `dplyr` and `pool` installed and loaded in order to be able to run this code):

```r
conn <- dbConnect(RSQLite::SQLite(), dbname = ":memory:")
dbWriteTable(conn, "quakes", quakes)
tbl(conn, "quakes") %>% select(-stations) %>% filter(mag >= 6)
## # Source:   lazy query [?? x 4]
## # Database: sqlite 3.19.3 [:memory:]
##      lat   long depth   mag
##    <dbl>  <dbl> <int> <dbl>
## 1 -20.70 169.92   139   6.1
## 2 -13.64 165.96    50   6.0
## 3 -15.56 167.62   127   6.4
## 4 -12.23 167.02   242   6.0
## 5 -21.59 170.56   165   6.0

dbDisconnect(conn)
```

And here's how you'd do the same using `pool`:

```r
pool <- dbPool(RSQLite::SQLite(), dbname = ":memory:")
dbWriteTable(pool, "quakes", quakes)
tbl(pool, "quakes") %>% select(-stations) %>% filter(mag >= 6)
## # Source:   lazy query [?? x 4]
## # Database: sqlite 3.19.3 [:memory:]
##      lat   long depth   mag
##    <dbl>  <dbl> <int> <dbl>
## 1 -20.70 169.92   139   6.1
## 2 -13.64 165.96    50   6.0
## 3 -15.56 167.62   127   6.4
## 4 -12.23 167.02   242   6.0
## 5 -21.59 170.56   165   6.0

poolClose(pool)
```

## What problem `pool` was created to solve
As mentioned before, the goal of the `pool` package is to abstract away the logic of connection management and the performance cost of fetching a new connection from a remote database. These concerns are especially prominent in interactive contexts, like Shiny apps. (So, while this package is of most practical value to Shiny developers, there is no harm if it is used in other contexts.)

The rest of this post elaborates some more on the specific problems of connection management inside of Shiny, and how `pool` addresses them.

### The connection management spectrum
When you’re connecting to a database, it's important to manage your connections: when to open them (taking into account that this is a potentially long process for remote databases), how to keep track of them, and when to close them. This is always true, but it becomes especially relevant for Shiny apps, where not following best practices can lead to many slowdowns (from inadvertently opening too many connections) and/or many leaked connections (i.e. forgetting to close connections once you no longer need them). Over time, leaked connections could accumulate and substantially slow down your app, as well as overwhelming the database itself.

Oversimplifying a bit, we can think of connection management in Shiny as a spectrum ranging from the extreme of just having one connection per app (potentially serving several sessions of the app) to the extreme of opening (and closing) one connection for each query you make. Neither of these approaches is great: the former is fast, but not robust, and the reverse is true for the latter. 

In particular, opening only one connection per app makes it fast (because, in the whole app, you only fetch one connection) and your code is kept as simple as possible. However:

- it cannot handle simultaneous requests (e.g. two sessions open, both querying the database at the same time);
- if the connection breaks at some point (maybe the database server crashed), you won’t get a new connection (you have to exit the app and re-run it);
- finally, if you are not quite at this extreme, and you use more than one connection per app (but fewer than one connection per query), it can be difficult to keep track of all your connections, since you’ll be opening and closing them in potentially very different places.

While the other extreme of opening (and closing) one connection for each query you make resolves all of these points, it is terribly slow (each time we need to access the database, we first have to fetch a connection), and you need a lot more (boilerplate) code to connect and disconnect the connection within each reactive/function.

If you'd like to see actual code that illustrates these two approaches, check [this section of the `pool` README](https://github.com/rstudio/pool#context-and-motivation).

### The best of both worlds
The `pool` package was created so that you don't have to worry about this at all. Since `pool` abstracts away the logic of connection management, for the vast majority of cases, you never have to deal with connections directly. Since the pool “knows” when it should have more connections and how to manage them, you have all the advantages of the second approach (one connection per query), without the disadvantages. You are still using one connection per query, but that connection is always fetched and returned to the pool, rather than getting it from the database directly. This is a whole lot faster and more efficient. Finally, the code is kept just as simple as the code in the first approach (only one connection for the entire app), since you don't have to continuously call `dbConnect` and `dbDisconnect`.

## Feedback
This package has quietly been around for a year and it's now finally on CRAN, following lots of the changes in the database world (both in `DBI` and `dplyr`). All `pool`-related feedback is welcome. Issues (bugs and features requests) can be posted to the [github tracker](https://github.com/rstudio/pool/issues). Requests for help with code or other questions can be posted to [community.rstudio.com/c/shiny](https://community.rstudio.com/c/shiny), which I check regularly (they can, of course, also be posted to [Stack Overflow](https://stackoverflow.com/), but I'm extremely likely to miss it).

