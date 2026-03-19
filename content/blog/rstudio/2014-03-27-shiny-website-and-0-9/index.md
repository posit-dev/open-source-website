---
title: New Shiny website launched; Shiny 0.9 released
people:
  - Joe Cheng
date: '2014-03-27'
categories:
  - Interactive Apps
slug: shiny-website-and-0-9
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Shiny
  - Shinyapps.io
  - RStudio
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
ported_categories:
  - Shiny
  - shinyapps.io
---


We're excited to introduce to you our new website for Shiny: [shiny.rstudio.com](https://shiny.rstudio.com/)!

[![shiny-rstudio-com](https://rstudioblog.files.wordpress.com/2014/03/shiny-rstudio-com.gif)](https://shiny.rstudio.com/)

We've included [articles](https://shiny.rstudio.com/articles/) on many Shiny-related topics, dozens of [example applications](https://shiny.rstudio.com/gallery/), and an all-new [tutorial](https://shiny.rstudio.com/tutorial/) for getting started.

Whether you're a beginner or expert at Shiny, we hope that having these resources available in one place will help you find the information you need.

**We'd also like to announce Shiny 0.9, now available on CRAN.** This release includes many bug fixes and new features, including:

## New application layout options

Until now, the vast majority of Shiny apps have used a sidebar-style layout. Shiny 0.9 introduces new layout features to:

  1. Make it easy to create custom page layouts using the Bootstrap grid system. See our new [application layout guide](https://shiny.rstudio.com/articles/layout-guide.html) or a [live example](https://shiny.rstudio.com/gallery/plot-plus-three-columns.html).

  2. Provide navigation bars and lists for separating your application into different pages. See [navbarPage](https://shiny.rstudio.com/reference/shiny/latest/navbarPage.html) and [navlistPanel](https://shiny.rstudio.com/reference/shiny/latest/navlistPanel.html), and [this example](https://shiny.rstudio.com/gallery/navbar-example.html).

  3. Enhance [tabsetPanel](https://shiny.rstudio.com/reference/shiny/latest/navlistPanel.html) to allow pill-style tabs, and to let tabs be placed above, below, or to either side of tab content.

  4. Create floating panels and place them relative to the sides of the page, optionally making them draggable. See [absolutePanel](https://shiny.rstudio.com/reference/shiny/latest/absolutePanel.html) or [this example](https://shiny.rstudio.com/gallery/absolutely-positioned-panels.html).

  5. Use [Bootstrap themes](https://www.google.com/webhp?ion=1&espv=2&ie=UTF-8#q=bootstrap+themes) to easily modify the fonts and colors of your application. [Example](https://shiny.rstudio.com/gallery/retirement-simulation.html)

You can see many of these features in action together in [our reimplementation](https://shiny.rstudio.com/gallery/superzip-example.html) of the Washington Post's [interactive article on Super Zips](http://www.washingtonpost.com/sf/local/2013/11/09/washington-a-world-apart/).

## Selectize.js integration

The JavaScript library [selectize.js](https://github.com/brianreavis/selectize.js) provides a much more flexible interface compared to the basic select input. It allows you to type and search in the options, use placeholders, control the number of options/items to show/select, and so on.

![selectize](https://rstudioblog.files.wordpress.com/2014/03/selectize.png)

We have integrated selectize.js in shiny 0.9, and `selectInput` now creates selectize inputs by default. (You can revert back to plain select inputs by passing `selectize=FALSE` to `selectInput`.) For more advanced uses, we have included a new `selectizeInput` function that lets you pass options to selectize.

Please check out [this example](https://demo.shinyapps.io/013-selectize/) to see a subset of features of the selectize input. There is also [an example](https://demo.shinyapps.io/017-select-vs-selectize/) comparing the select and selectize input.

## Showcase mode

Shiny apps can now (optionally) run in a "showcase" mode in which the app's R code can be automatically displayed within the app. Most of the Shiny example apps in our new [gallery](https://shiny.rstudio.com/gallery/) use showcase mode.

[![Showcase example](https://rstudioblog.files.wordpress.com/2014/03/kmeans.png)](https://shiny.rstudio.com/gallery/kmeans-example.html)

As you interact with the application, reactive expressions and outputs in server.R will light up as they execute. This can be helpful in visualizing the reactivity in your app.

See [this article](https://shiny.rstudio.com/articles/display-modes.html) to learn more.

As always, you can install the latest release of Shiny by running this command at the R console:

`install.packages("shiny")`

The complete list of bug fixes and features is available in the [NEWS file](http://cran.r-project.org/web/packages/shiny/NEWS).

We hope you'll find these new features helpful in exploring and understanding your data!

