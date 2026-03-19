---
title: 'Interactive documents: An incredibly easy way to use Shiny'
people:
  - Garrett Grolemund
date: '2014-06-19'
categories:
- Shiny
- shinyapps.io
slug: interactive-documents-an-incredibly-easy-way-to-use-shiny
blogcategories:
- Products and Technology
- Open Source
tags:
- Shiny
- shinyapps.io
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
---


R Markdown's new [interactive documents](https://rmarkdown.rstudio.com/authoring_shiny.html) provide a quick, light-weight way to use [Shiny](https://shiny.rstudio.com). An interactive document embeds Shiny elements in an [R Markdown](http://rmarkdown.rstudio.com) report. The report becomes "live", a choose your own adventure that readers can control and explore. Interactive documents are easy to create and easy to share.

## Create an interactive document

To create an interactive document use RStudio to create a new R Markdown file, choose the Shiny document template, then click "Run Document" to show a preview:

![storms.002](https://rstudioblog.files.wordpress.com/2014/06/storms-002.png)

[Embed R code chunks](https://rmarkdown.rstudio.com/authoring_rcodechunks.html) in your report where you like. Interactive documents use the same syntax as R Markdown and [knitr](http://yihui.name/knitr/). Set `echo = FALSE`. Your reader won't see the code, just its results.

  ![storms2.001](https://rstudioblog.files.wordpress.com/2014/06/storms2-001.png)

Include [Shiny widgets](https://shiny.rstudio.com/gallery/widgets-gallery.html) and [outputs](https://rmarkdown.rstudio.com/authoring_shiny.html#inputs-and-outputs) in your code chunks. R Markdown will insert the widgets directly into your final document. When a reader toggles a widget, the parts of the document that depend on it will update instantly.

 ![storms.003](https://rstudioblog.files.wordpress.com/2014/06/storms-003.png)

That's it! No extra files are needed.

Note that in order to use interactive documents you should be running the [latest version](https://www.rstudio.com/products/rstudio/) of RStudio (v0.98.932 or higher). Alternatively if you are not using RStudio be sure to follow the directions [here](https://rmarkdown.rstudio.com/authoring_shiny.html#prerequisites) to install all of the required components.

## Share your document

Interactive documents can be run locally on the desktop or be deployed Shiny Server v1.2 or [ShinyApps](http://shinyapps.io/) just like any other Shiny application. See the RMarkdown v2 website for more details on [deploying interactive documents](https://rmarkdown.rstudio.com/authoring_shiny.html#deployment).

## Use pre-packaged tools

Interactive documents make it easy to insert powerful tools into a report. For example, you can insert a kmeans clustering tool into your document with one line of code, as below. `kmeans_cluster` is a widget built from a Shiny app and intended for use in interactive documents.

![storms.004](https://rstudioblog.files.wordpress.com/2014/06/storms-004.png)

You can [build your own widgets](https://rmarkdown.rstudio.com/authoring_shiny_widgets.html) with `shinyApp`, a new function that repackages Shiny apps as functions. `shinyApp` is easy to use. Its first argument takes the code that appears in an app's ui.R file. The second argument takes the code that appears in the app's server.R file. The [source](https://github.com/rstudio/rmdexamples/blob/master/R/kmeans_cluster.R) of `kmeans_cluster` reveals how simple this is.

## Be a hero

Ready to be a hero? You can use the `shinyApp` function to make out of the box widgets that students, teachers, and data scientists will use everyday. Widgets can

  * fit models

  * compare distributions

  * visualize data

  * demonstrate teaching examples

  * act as quizzes or multiple choice questions

  * and more

These widgets are not made yet, they are low hanging fruit for any Shiny developer. If you know how to program with Shiny (or want to learn), and would like to make your mark on R, consider authoring a package that makes widgets available for interactive documents.

## Get started!

To learn more about interactive documents visit <https://rmarkdown.rstudio.com/authoring_shiny.html>.

