---
title: Shiny 0.10
people:
  - Joe Cheng
date: '2014-06-20'
categories:
  - Interactive Apps
slug: shiny-0-10
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
  - Shiny
  - RStudio
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
ported_categories:
  - Packages
  - Shiny
---


Shiny 0.10 is now available on CRAN.

## Interactive documents

In this release, the biggest changes were under the hood to support the creation of [interactive documents](https://rmarkdown.rstudio.com/authoring_shiny.html). If you haven't had a chance to check out interactive documents, we really encourage you to do so---it may be the [easiest way to learn Shiny](https://blog.rstudio.com/2014/06/19/interactive-documents-an-incredibly-easy-way-to-use-shiny/).

## New layout functions

Three new functions---[`flowLayout()`](https://shiny.rstudio.com/reference/shiny/latest/flowLayout.html), [`splitLayout()`](https://shiny.rstudio.com/reference/shiny/latest/splitLayout.html), and [`inputPanel()`](https://shiny.rstudio.com/reference/shiny/latest/inputPanel.html)---were added for putting UI elements side by side.

  * `flowPanel()` lays out its children in a left-to-right, top-to-bottom arrangement.

  * `splitLayout()` evenly divides its horizontal space among its children (or unevenly divides if cellWidths argument is provided).

  * `inputPanel()` is like `flowPanel()`, but with a light grey background, and is intended for encapsulating small input controls wherever vertical space is at a premium.

A new logical argument `inline` was also added to `checkboxGroupInput()` and `radioButtons()` to arrange check boxes and radio buttons horizontally.

## Custom validation error messages

Sometimes you don't want your reactive expressions or output renderers in server.R to proceed unless certain input conditions are satisfied, e.g. a select input value has been chosen, or a sensible combination of inputs has been provided. In these cases, you might want to stop the render function quietly, or you might want to give the user a custom message. In shiny 0.10.0, we introduced the functions [`validate()` and `need()`](https://shiny.rstudio.com/reference/shiny/latest/validate.html) which you can use to enforce validation conditions. This won't be the last word on input validation in Shiny, but it should be a lot safer and more convenient than how most of us have been doing it.

See the article [Write error messages for your UI with validate](https://shiny.rstudio.com/articles/validation.html) for details and examples.

## Sever-side processing for Selectize input

In the previous release of Shiny, we added support for [Selectize](http://brianreavis.github.io/selectize.js/), a powerful select box widget. At that time, our implementation passed all of the data to the web page and used JavaScript to do any paging, filtering, and sorting. It worked great for small numbers of items but didn't scale well beyond a few thousand items.

For Shiny 0.10, we greatly improved the performance of our existing client-side Selectize binding, but also added a new mode that allows the paging, filtering, and sorting to all happen on the server. Only the results that are actually displayed are downloaded to the client. This approach works well for hundreds of thousands or millions of rows.

For more details and examples, see the article [Using selectize input](https://shiny.rstudio.com/articles/selectize.html) on [shiny.rstudio.com](https://shiny.rstudio.com/).

## htmltools

We also split off Shiny's HTML generating library (`tags` and friends) into a separate [htmltools](http://cran.rstudio.com/web/packages/htmltools/index.html) package. If you're writing a package that needs to generate HTML programmatically, it's far easier and safer to use htmltools than to paste HTML strings together yourself. We'll have more to share about htmltools in the months to come.

## Other changes

  * New [`actionLink()`](https://shiny.rstudio.com/reference/shiny/latest/actionButton.html) input control: behaves like `actionButton()` but looks like a link

  * `renderPlot()` now calls `print()` on its result if it's visible--no more explicit `print()` required for ggplot2

  * Sliders and select boxes now use a fixed horizontal size instead of filling up all available horizontal space; pass `width="100%"` if you need the old behavior

  * The `session` object that can be passed into a server function is now documented: see `?session`

  * New [reactive domains](https://shiny.rstudio.com/reference/shiny/latest/domains.html) feature makes it easy to get callbacks when the current session ends, without having to pass `session` everywhere

  * Thanks to reactive domains, by default, observers now automatically stop executing when the Shiny session that created them ends

  * `shinyUI` and `shinyServer`

For the full list, you can take a look at the [NEWS file](https://raw.githubusercontent.com/rstudio/shiny/v/0/10/0/NEWS). Please let us know if you have any comments or questions.

