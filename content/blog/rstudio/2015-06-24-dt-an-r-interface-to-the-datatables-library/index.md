---
title: 'DT: An R interface to the DataTables library'
people:
  - Yihui Xie
date: '2015-06-24'
tags:
- DataTables
- htmlwidgets
slug: dt-an-r-interface-to-the-datatables-library
blogcategories:
- Products and Technology
- Open Source
ported_from: rstudio
port_status: in-progress
software: ["dt"]
languages: ["R"]
categories:
  - Visualization
  - Interactive Apps
ported_categories:
  - Packages
---


We are happy to announce a new package **DT** is available on CRAN now. **DT** is an interface to the JavaScript library [DataTables](http://datatables.net/) based on the **[htmlwidgets](http://htmlwidgets.org)** framework, to present rectangular R data objects (such as data frames and matrices) as HTML tables. You can filter, search, and sort the data in the table. See <http://rstudio.github.io/DT/> for the full documentation and examples of this package. To install the package, run

```r
install.packages('DT')
# run DT::datatable(iris) to see a "hello world" example
```

![DataTables](https://rstudioblog.files.wordpress.com/2015/06/screenshot-from-2015-06-17-232010.png)

The main function in this package is `datatable()`, which returns a table widget that can be rendered in R Markdown documents, Shiny apps, and the R console. It is easy to customize the style (cell borders, row striping, and row highlighting, etc), theme (default or Bootstrap), row/column names, table caption, and so on.

<!-- more -->

## DataTables Options

The DataTables library supports a large number of initialization options. Through **DT**, you can specify these options using a list in R. For example, we can disable searching, change the default page length from 10 to 5, and customize the length menu to use page lengths 5, 10, 15, and 20:

```r
library(DT)
datatable(iris, options = list(
  searching = FALSE,
  pageLength = 5,
  lengthMenu = c(5, 10, 15, 20)
))
```

When you need to write literal JavaScript code in these options (e.g. the callback functions), you can use the `JS()` function. An example of the `initComplete` callback:

```r
datatable(iris, options = list(
  initComplete = JS("
    function(settings, json) {
      $(this.api().table().header()).css({
        'background-color': '#000',
        'color': '#fff'
      });
    }")
))
```

Being able to write JavaScript gives you full flexibility to customize the table. However, one of the goals of **DT** is to avoid writing JavaScript in your R scripts, and we hope users can express everything in pure R syntax, so we have provided a few R helper functions in **DT** that essentially generates JavaScript code for users to fulfill some common tasks, such as formatting table columns and cells.

## Formatting Functions

The functions `formatCurrency()`, `formatPercentage()`, `formatRound()`, and `formatDate()` can be used to format table columns. For example, for a data frame with five columns A, B, C, D, and E, we format the columns A and C as euros, B as percentages (rounded to 2 decimal places), round D to 3 decimal places, and format E as date strings (the pipe operator `%>%` comes from the **magrittr** package):

```r
library(DT)
df <- data.frame(
  A = rpois(100, 1e4),
  B = runif(100),
  C = rpois(100, 1e3),
  D = rnorm(100),
  E = Sys.Date() + 1:100
)
datatable(df) %>%
  formatCurrency(c('A', 'C'), '€') %>%
  formatPercentage('B', 2) %>%
  formatRound('D', 3) %>%
  formatDate('E', 'toDateString')
```

![Format table columns](https://rstudioblog.files.wordpress.com/2015/06/screenshot-from-2015-06-18-150030.png)

It is also easy to style the table cells according to their values using the `formatStyle()` function. You can apply different CSS styles to cells, e.g. use bold font for those cells with `Sepal.Length > 5`, gray background for `Sepal.Width <= 3.4` and yellow for `Sepal.Width > 3.4`, and so on. See the [documentation page](http://rstudio.github.io/DT/functions.html) for these formatting functions for more information.

![Format cells](https://rstudioblog.files.wordpress.com/2015/06/screenshot-from-2015-06-18-151117.png)

## Server-side Processing

Interactions with the table can be processed either on the client side (using JavaScript in the web browser), or on the server side. Server-side processing is suitable for large data objects, since filtering, sorting, and pagination can be much faster in R than JavaScript in the browser. In theory, you can use any server-side processing language to process the data, and we have implemented it in R, which you can trivially enable by using **DT** in Shiny apps (the default mode is just server-side processing).

## Column Filters

DataTables does not come with column filters by default. It only provides a global search box. We have added filters for individual columns in **DT**, and you can enable column filters using the argument `filter = 'top'` or `'bottom'` in `datatable()`. Currently, three types of filters are provided:

  * For numeric/date/time columns, [range sliders](http://refreshless.com/nouislider/) are used to filter rows within ranges;

  * For factor columns, [selectize inputs](http://brianreavis.github.io/selectize.js/) are used to display all possible categories, and you can select multiple categories there (note you can also type in the box to search all categories);

  * For character columns, ordinary search boxes are used to match the values you typed in the boxes;

These filters are similar to the ones introduced in the [RStudio 0.99](https://blog.rstudio.com/2015/05/26/new-version-of-rstudio-v0-99/) Data Viewer. Column filters work in both server-side and client-side processing modes. You can enable search result highlighting by the option [searchHighlight = TRUE](http://rstudio.github.io/DT/006-highlight.html).

![Column Filters](https://rstudioblog.files.wordpress.com/2015/06/column-filters.png)

## Shiny

If you have used DataTables before in Shiny (i.e. the functions `dataTableOutput()` and `renderDataTable()`), it should be trivial to switch from Shiny to **DT**. **DT** has provided two functions of the same names, and the usage is very similar. Basically, all you have to do is to load **DT** after **shiny**, so that `dataTableOutput()` and `renderDataTable()` in **DT** can override the functions in **shiny**. If you want to be sure to use the functions in **DT**, you can add the prefix `DT::` to these functions. We will deprecate `dataTableOutput()` and `renderDataTable()` in **shiny** eventually as **DT** becomes mature and stable.

```r
library(shiny)
library(DT)  # make sure you load DT *after* shiny
```

As mentioned before, **DT** uses the server-side processing mode in **shiny**. To go back to client-side processing, you can use `renderDataTable(data, server = FALSE)`.

The first argument of the function `renderDataTable()` can be either a data object (e.g. a data frame), or a table widget object (returned by `datatable()`). The latter form is useful when you need to further process the table widget, e.g. format certain columns or cells.

```r
renderDataTable({
  datatable(iris) %>% formatStyle(
    'Sepal.Width',
    backgroundColor = styleInterval(3.4, c('gray', 'yellow'))
  )
})
```

When a table is rendered in a Shiny app, you can obtain some information about the state of the table via the `input` object in Shiny. For example, for a table output `dataTableOutput('foo')`, the indices of the selected rows can be obtained from `input$foo_rows_selected`, and the indices of rows on the current page are available via `input$foo_rows_current` ([live example](https://yihui.shinyapps.io/DT-info/)). [This page](http://rstudio.github.io/DT/shiny.html) has more information about using **DT** in Shiny.

## DataTables Extensions

DataTables has several extensions, and we have integrated all of them into **DT**. You may enable extensions via the extensions argument of `datatable()`. For example, you can reorder columns using the ColReorder extension, show/hide columns using the ColVis extension, fix certain columns on the left and/or right via FixedColumns when scrolling horizontally in the table, and so on. Please see the [documentation page for extensions](http://rstudio.github.io/DT/extensions.html) for details.

We hope you will enjoy this package, and please [let us know](https://github.com/rstudio/DT/issues) if you have any questions, comments, or feature requests.

