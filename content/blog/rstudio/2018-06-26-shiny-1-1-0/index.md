---
title: 'Shiny 1.1.0: Scaling Shiny with async'
people:
  - Joe Cheng
date: '2018-06-26'
categories:
- Packages
- Shiny
tags:
- async
- shiny
- Packages
- Shiny
slug: shiny-1-1-0
blogcategories:
- Products and Technology
- Open Source
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
---


This is a significant release for **[Shiny](https://shiny.rstudio.com)**, with a major new feature that was nearly a year in the making: support for asynchronous operations!

Without this capability, when Shiny performs long-running calculations or tasks on behalf of one user, it stalls progress for all other Shiny users that are connected to the same process. Therefore, Shiny apps that feature long-running calculations or tasks have generally been deployed using many R processes, each serving a small number of users; this works, but is not the most efficient approach. Such applications now have an important new tool in the toolbox to improve performance under load.

Shiny async is implemented via integration with the **[future](https://github.com/HenrikBengtsson/future)** and **[promises](https://rstudio.github.io/promises/)** packages. These two packages are used together:

1. **Use `future` to perform long-running operations in a worker process that runs in the background**, leaving Shiny processes free to serve other users in the meantime. This yields much better responsiveness under load, and much more predictable latency.
2. **Use `promises` to handle the result of each long-running background operation back in the Shiny process**, where additional processing can occur, such as further data manipulation, or displaying to the user via a reactive output.

If your app has a small number of severe performance bottlenecks, you can use this technique to get massively better responsiveness under load. For example, if the `httr::GET` call in this server function takes 30 seconds to complete:

```r
server <- function(input, output, session) {
  r <- reactive({
    httr::GET(url) %>%
      httr::content("parsed")
  })

  output$plot <- renderPlot({
    r() %>%
      ggplot(aes(speed, dist)) + geom_point()
  })
}
```

then the entire R process is stalled for those 30 seconds.

We can rewrite it asynchronously like this:

```r
library(promises)
library(future)
plan(multisession)

server <- function(input, output, session) {
  r <- reactive({
    future(httr::GET(url)) %...>%
      httr::content("parsed")
  })
  
  output$plot <- renderPlot({
    r() %...>% {
      ggplot(., aes(speed, dist)) + geom_point()
    }
  })
}

```

Even if the `httr::GET(url)` takes 30 seconds, the `r` reactive executes almost instantly, and returns control to the caller. The code inside `future(...)` is executed in a different R process that runs in the background, and whenever its result becomes available (i.e. in 30 seconds), the right-hand side of `%...>%` will be executed with that result. (`%...>%` is called a "promise pipe"; it works similarly to a magrittr pipe that knows how to wait for and "unwrap" promises.)

If the original (synchronous) code appeared in a Shiny app, then during that 30 seconds, the R process is stuck dealing with the download and can't respond to any requests being made by other users. But with the async version, the R process only needs to kick off the operation, and then is free to service other requests. This means other users will only have to wait milliseconds, not minutes, for the app to respond.

### Case study

We've created a [detailed case study](https://rstudio.github.io/promises/articles/casestudy.html) that walks through the async conversion of a realistic example app. This app processes low-level logging data from RStudio's CRAN mirrors, to let us explore the heaviest downloaders for each day.

![](https://rstudio.github.io/promises/articles/case-study-tab3.png)

To load test this example app, we launched 50 sessions of simulated load, with a 5 second delay between each launch, and directed this traffic to a single R process. We then rewrote the app to use futures and promises, and reran the load test with this async version. (The tools we used to perform the load testing are not yet publicly available, but you can refer to [Sean Lopp's talk at rstudio::conf 2018](https://www.rstudio.com/resources/videos/scaling-shiny/) for a preview.)

Under these conditions, the finished async version displays significantly lower (mean) response times than the original. In the table below, "HTTP traffic" refers to requests that are made during page load time, and "reactive processing" refers to the time between the browser sending a reactive input value and the server returning updated reactive outputs.

<style>
table td:first-child, table th:first-child {text-align:left !important;}
table td, table th {text-align:right !important;}
</style>

Response type        | Original | Async    | Delta
---------------------|----------|----------|-------
HTTP traffic         | 605 ms   | 139 ms   | -77%
Reactive processing  | 10.7 sec | 3.48 sec | -67%

### Learn more

Visit the [promises](https://rstudio.github.io/promises/) website to learn more, or watch my [recent webinar](https://www.rstudio.com/resources/videos/scaling-shiny-apps-with-async-programming-june-2018/) on Shiny async.

See the [full changelog](https://shiny.rstudio.com/reference/shiny/1.1.0/upgrade.html) for Shiny v1.1.0.

## Related packages

Over the last year, we created or enhanced several other packages to support async Shiny:

- The **[promises](https://rstudio.github.io/promises/)** package (released 2018-04-13) mentioned above provides the actual API you'll use to do async programming in R. We implemented this as a separate package so that other parts of the R community, not just Shiny users, can take advantage of these techniques. The promises package was inspired by the basic ideas of [JavaScript promises](https://developers.google.com/web/fundamentals/primers/promises), but also have significantly improved syntax and extensibility to make them work well with R and Shiny. Currently, promises is most useful when used with the [future](https://cran.r-project.org/package=future) package by [Henrik Bengtsson](https://github.com/HenrikBengtsson).
- **[later](https://cran.r-project.org/package=later)** (released 2017-06-25) adds a low-level feature to R that is critical to async programming: the ability to schedule R code to be executed in the future, within the same R process. You can do all sorts of cool stuff on top of this, as some people are [discovering](https://yihui.name/en/2017/10/later-recursion/).
- **[httpuv](https://cran.r-project.org/package=httpuv)** (1.4.0 released 2018-04-19) has long been the HTTP web server that Shiny, and most other web frameworks for R, sit on top of. Version 1.4.0 adds support for asynchronous handling of HTTP requests, and also adds a dedicated I/O-handling thread for greatly improved performance under load.

In the coming weeks, you can also expect updates for async compatibility to **[htmlwidgets](https://www.htmlwidgets.org)**, **[plotly](https://plot.ly/r/)**, and **[DT](https://rstudio.github.io/DT/)**. Most other HTML widgets will automatically become async compatible once htmlwidgets is updated.


