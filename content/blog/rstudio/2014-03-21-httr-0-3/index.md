---
title: httr 0.3
people:
  - Hadley Wickham
date: '2014-03-21'
categories:
  - Data Wrangling
slug: httr-0-3
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - RStudio
ported_from: rstudio
port_status: in-progress
software: ["httr"]
languages: ["R"]
ported_categories:
  - Packages
---


We're very pleased to announce the release of httr 0.3. httr makes it
easy to work with modern web apis so that you can work with web data
almost as easily as local data. For example, this code shows how might
find the most recently asked question about R on stackoverflow:

````r
# install.packages("httr")
library(httr)

# Find the most recent R questions on stackoverflow
r <- GET(
  "http://api.stackexchange.com",
  path = "questions",
  query = list(
    site = "stackoverflow.com",
    tagged = "r"
  )
)

# Check the request succeeded
stop_for_status(r)

# Automatically parse the json output
questions <- content(r)
questions$items[[1]]$title
#> [1] "Remove NAs from data frame without deleting entire rows/columns"
````

httr 0.3 recieved a major overhaul to OAuth support. OAuth is a modern
standard for authentication used when you want to allow a service (i.e R
package) access to your account on a website. This version of httr
provides an improved initial authentication experience and supports
caching so that you only need to authenticate once per project. A big
thanks goes to Craig Citro (Google) who contributed a lot of code and
ideas to make this possible.

httr 0.3 also includes many other bug fixes and minor improvements. You
can read about these in the [github release notes](https://github.com/hadley/httr/releases/tag/v0.3).

