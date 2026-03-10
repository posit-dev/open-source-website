---
image: thumbnail.jpg
date: '2022-02-09'
description: '00:00 Introduction to Reactlog

  00:44 Viewing Reactlog using an Old Faithful Shiny app

  02:07 The Reactlog interface

  04:31 Walking through a reactive graph with Reactlog

  05:14 Downstream dependency invalidation in Shiny

  06:43 How Shiny "grabs" data

  09:41 How the Reactlog timeline works

  10:46 Switching between idle states in Reactlog

  11:58 Reactlog interactivity - clicking a single item

  13:21 Reactlog with the Pythagoras Theorem app

  15:45 Adding a UI and server value to add Reactlog to your Shiny app

  18:05 Walking through the reactive graph using the Pythagorean Theorem app

  21:07 Append-only behavior of Reactlog

  21:18 Marking a time point in Reactlog

  23:17 Using Reactlog to debug reactivity

  26:55 Resetting our app and testing logic changes

  28:01 Reactlog with a large Shiny app, CRANwhales

  34:10 Freezing reactive values

  36:19 Calculating click count in a Shiny app

  37:10 Click the button, render the plot is bad - see why


  Shiny is an R package from RStudio that makes it incredibly easy to build interactive web applications with R. Behind the scenes, Shiny builds a reactive graph that can quickly become intertwined and difficult to debug. reactlog provides a visual insight into that black box of Shiny reactivity.


  After logging the reactive interactions of a Shiny application, reactlog constructs a directed dependency graph of the Shiny’s reactive state at any time point in the record. The reactlog dependency graph provides users with the ability to visually see if reactive elements are:


  - Not utilized (never retrieved)

  - Over utilized (called independently many times)

  - Interacting with unexpected elements

  - Invalidating all expected dependencies

  - Freezing (and thawing), preventing triggering of future reactivity


  There are many subtle features hidden throughout reactlog. Here is a short list quickly describing what is possible within reactlog:


  - Display the reactivity dependency graph of your Shiny applications

  - Navigate throughout your reactive history to replay element interactions

  - Highlight reactive family trees

  - Filter on reactive family trees

  - Search for reactive elements


  You can read more about reactlog here: https://rstudio.github.io/reactlog/articles/reactlog.html

  And you can learn more about Shiny here: https://shiny.rstudio.com/


  Got questions? The RStudio Community site is a great place to get assistance: https://community.rstudio.com/


  Content: Barret Schloerke (@schloerke)

  Design & editing: Jesse Mostipak (@kierisi)'
people:
- Barret Schloerke
resource_type: video
resources: []
software:
- cranwhales
- reactlog
- rstudio
- Shiny
title: Barret Schloerke || {reactlog} Rundown || RStudio

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 0
  date: '2022-02-09T18:00:35Z'
  definition: hd
  description: '00:00 Introduction to Reactlog

    00:44 Viewing Reactlog using an Old Faithful Shiny app

    02:07 The Reactlog interface

    04:31 Walking through a reactive graph with Reactlog

    05:14 Downstream dependency invalidation in Shiny

    06:43 How Shiny "grabs" data

    09:41 How the Reactlog timeline works

    10:46 Switching between idle states in Reactlog

    11:58 Reactlog interactivity - clicking a single item

    13:21 Reactlog with the Pythagoras Theorem app

    15:45 Adding a UI and server value to add Reactlog to your Shiny app

    18:05 Walking through the reactive graph using the Pythagorean Theorem app

    21:07 Append-only behavior of Reactlog

    21:18 Marking a time point in Reactlog

    23:17 Using Reactlog to debug reactivity

    26:55 Resetting our app and testing logic changes

    28:01 Reactlog with a large Shiny app, CRANwhales

    34:10 Freezing reactive values

    36:19 Calculating click count in a Shiny app

    37:10 Click the button, render the plot is bad - see why


    Shiny is an R package from RStudio that makes it incredibly easy to build interactive web applications with R. Behind the scenes, Shiny builds a reactive graph that can quickly become intertwined and difficult to debug. reactlog provides a visual insight into that black box of Shiny reactivity.


    After logging the reactive interactions of a Shiny application, reactlog constructs a directed dependency graph of the Shiny’s reactive state at any time point in the record. The reactlog dependency graph provides users with the ability to visually see if reactive elements are:


    - Not utilized (never retrieved)

    - Over utilized (called independently many times)

    - Interacting with unexpected elements

    - Invalidating all expected dependencies

    - Freezing (and thawing), preventing triggering of future reactivity


    There are many subtle features hidden throughout reactlog. Here is a short list quickly describing what is possible within reactlog:


    - Display the reactivity dependency graph of your Shiny applications

    - Navigate throughout your reactive history to replay element interactions

    - Highlight reactive family trees

    - Filter on reactive family trees

    - Search for reactive elements


    You can read more about reactlog here: https://rstudio.github.io/reactlog/articles/reactlog.html

    And you can learn more about Shiny here: https://shiny.rstudio.com/


    Got questions? The RStudio Community site is a great place to get assistance: https://community.rstudio.com/


    Content: Barret Schloerke (@schloerke)

    Design & editing: Jesse Mostipak (@kierisi)'
  duration: 2357
  has_captions: true
  language: en
  last_updated: '2026-03-04T14:51:27.561209+00:00'
  like_count: 0
  people:
  - Barret Schloerke
  playlist: ''
  software:
  - cranwhales
  - reactlog
  - rstudio
  - Shiny
  tags:
  - rstudio
  - data science
  - machine learning
  - python
  - stats
  - tidyverse
  - data visualization
  - data viz
  - ggplot
  - technology
  - coding
  - connect
  - server pro
  - shiny
  - rmarkdown
  - package manager
  - CRAN
  - interoperability
  - serious data science
  - dplyr
  - forcats
  - ggplot2
  - tibble
  - readr
  - stringr
  - tidyr
  - purrr
  - github
  - data wrangling
  - tidy data
  - odbc
  - rayshader
  - plumber
  - blogdown
  - gt
  - lazy evaluation
  - tidymodels
  - statistics
  - debugging
  - programming education
  - rstats
  - open source
  - OSS
  - reticulate
  - reactlog
  - reactivity
  thumbnail: https://i.ytimg.com/vi/slXcW99ftk4/maxresdefault.jpg
  title: Barret Schloerke || {reactlog} Rundown || RStudio
  url: https://www.youtube.com/watch?v=slXcW99ftk4
  view_count: 2891
---
image: thumbnail.jpg

