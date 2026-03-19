---
title: Shiny 0.10.2
people:
  - Yihui Xie
date: '2014-10-02'
categories:
  - Interactive Apps
tags:
  - Datatables
  - Internet explorer
  - Shiny
  - Packages
  - RStudio
slug: shiny-0-10-2
blogcategories:
  - Products and Technology
  - Open Source
ported_from: rstudio
port_status: in-progress
software: ["progress", "shiny-r"]
languages: ["R"]
ported_categories:
  - Packages
  - Shiny
---


[Shiny v0.10.2](http://cran.rstudio.com/package=shiny) has been released to CRAN. To install it:

```r
install.packages('shiny')
```

This version of Shiny requires R 3.0.0 or higher (note the [current version of R](http://cran.rstudio.com/) is 3.1.1). R 2.15.x is no longer supported.

Here are the most prominent changes:

  * File uploading via `fileInput()` now works for Internet Explorer 8 and 9. Note, however, that IE 8/9 do not support multiple files from a single file input. If you need to upload multiple files, you must use one file input for each file. Unlike in modern web browsers, no progress bar will display when uploading files in IE 8/9.

  * Shiny now supports single-file applications: instead of needing two separate files, `server.R` and `ui.R`, you can now create an application with single file named `app.R`. This also makes it easier to distribute example Shiny code, because you can run an entire app by simply copying and pasting the code for a single-file app into the R console. Here's a simple example of a single-file app:

```r
## app.R
server <- function(input, output) {
  output$distPlot <- renderPlot({
    hist(rnorm(input$obs), col = 'darkgray', border = 'white')
  })
}

ui <- shinyUI(fluidPage(
  sidebarLayout(
    sidebarPanel(
      sliderInput("obs", "Number of observations:",
                  min = 10, max = 500, value = 100)
    ),
    mainPanel(plotOutput("distPlot"))
  )
))

shinyApp(ui = ui, server = server)
```

See the [single-file app article](https://shiny.rstudio.com/articles/single-file.html) for more.

  * We've added progress bars, which allow you to indicate to users that something is happening when there's a long-running computation. The progress bar will show at the top of the browser window, as shown here:

![progress](https://rstudioblog.files.wordpress.com/2014/10/progress.png)

Read the [progress bar article](https://shiny.rstudio.com/articles/progress.html) for more.

  * We've upgraded the DataTables Javascript library from 1.9.4 to 1.10.2. We've tried to support backward compatibility as much as possible, but this might be a breaking change if you've customized the DataTables options in your apps. This is because some option names have changed; for example, `aLengthMenu` has been renamed to `lengthMenu`. Please read [the article on DataTables](https://shiny.rstudio.com/articles/datatables.html) on the Shiny website for more information about updating Shiny apps that use DataTables 1.9.4.

In addition to the changes listed above, there are some smaller updates:

  * Searching in DataTables is case-insensitive and the search strings are not treated as regular expressions by default now. If you want case-sensitive searching or regular expressions, you can use the configuration options `search$caseInsensitive` and `search$regex`, e.g. `renderDataTable(..., options = list(search = list(caseInsensitve = FALSE, regex = TRUE)))`.

  * Shiny has switched from reference classes to R6.

  * Reactive log performance has been greatly improved.

  * Exported `createWebDependency`. It takes an `htmltools::htmlDependency` object and makes it available over Shiny's built-in web server.

  * Custom output bindings can now render `htmltools::htmlDependency` objects at runtime using `Shiny.renderDependencies()`.

Please read the [NEWS](https://github.com/rstudio/shiny/blob/master/NEWS) file for a complete list of changes, and let us know if you have any [comments](https://groups.google.com/forum/#!forum/shiny-discuss) or [questions](http://stackoverflow.com/questions/tagged/shiny).

