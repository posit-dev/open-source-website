---
title: Shiny 0.4.0 now available
people:
  - Winston Chang
date: '2013-02-22'
slug: shiny-0-4-0-now-available
blogcategories:
- Products and Technology
- Open Source
tags:
- Shiny
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
categories:
  - Interactive Apps
ported_categories:
  - Shiny
---


Shiny version 0.4.0 is now available on [CRAN](http://cran.r-project.org/web/packages/shiny/index.html). The most visible change is that the API has been slightly simplified. Your existing code will continue to work, although Shiny will print messages about how to migrate your code. Migration should be straightforward, as described below. It will take a bit of work to switch to the new API, but we think it's worth it in the long run, because the new interface is somewhat simpler, and because it offers a better mapping between function names and reactive programming concepts.

We've also updated the [Shiny tutorial](http://rstudio.github.com/shiny/tutorial/) to reflect the changes, and we've also added a some new content explaining Shiny's reactive programming model in depth. If you want to have a better understanding of how Shiny works, see the sections under _Understanding Reactivity_, starting with the [Reactivity Overview](http://rstudio.github.com/shiny/tutorial/#reactivity-overview).

Another new feature is that Shiny now suspends outputs when they aren't visible on the user's web browser. For example, if your Shiny application has multiple tabs or conditional panels, Shiny will only run the calculations and send data for the currently-visible tabs and panels. This new feature will reduce network traffic and computational load on the server, resulting in a faster application.

<!-- more -->

Here's what has changed, and how to migrate to the new API:

  * `reactive()` takes expressions as input, instead of functions.
**Old style:** `reactive(function() { ... })`
**New style:** `reactive({ ... })`

  * `reactiveText`, `reactivePlot`, and so on, have been replaced with `renderText`, `renderPlot`, etc. They also now take expressions instead of functions.
**Old style:** `reactiveText(function() { ... })`
**New style:** `renderText({ ... })`

  * `observe()` also takes expressions instead of functions:
**Old style** `observe(function() { ... })`
**New style:** `observe({ ... })`

If for some reason you want to save an unevaluated expression in a variable and then give it to, `reactive()`, `renderText()`, and so on, you can quote the expression and then use the `quote=TRUE` option:

```r
my_expr <- quote({ input$num + 1 })
renderText(my_expr, quote=TRUE)
```

If you still have any issues migrating, please feel free to ask questions on the [Shiny-discuss](https://groups.google.com/forum/?fromgroups#!forum/shiny-discuss) mailing list.

