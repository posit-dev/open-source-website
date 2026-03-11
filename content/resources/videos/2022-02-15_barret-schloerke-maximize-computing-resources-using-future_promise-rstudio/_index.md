---
image: thumbnail.jpg
date: '2022-02-15'
description: '00:00 Introduction

  01:45 Setting up a multisession using the future package

  02:05 Simulation using two workers

  04:14 Simulation using 10 workers

  05:20 What happens when we run out of workers?

  05:35 How Shiny handles future processes like promises

  07:16 Introduction to future_promise()

  07:45 Demo of the promises package

  09:21 Setting the number of workers

  10:40 Demo of processing without future_promise()

  14:11 Wrapping a slow calculation in a future()

  14:53 Demo of processing using Plumber

  16:25 Considerations on the number of cores to use

  17:21 What happens if we run out of workers?

  19:44 Decrease in execution times using future_promise()


  In an ideal situation, the number of available future workers (future::nbrOfFreeWorkers()) is always more than the number of future::future() jobs. However, if a future job is attempted when the number of free workers is 0, then future will block the current R session until one becomes available.


  The advantage of using future_promise() over future::future() is that even if there aren’t future workers available, the future is scheduled to be done when workers become available via promises. In other words, future_promise() ensures the main R thread isn’t blocked when a future job is requested and can’t immediately perform the work (i.e., the number of jobs exceeds the number of workers).


  You can read more about the promises package here: https://rstudio.github.io/promises/articles/shiny.html

  And you can learn more about Shiny here: https://shiny.rstudio.com/


  Got questions? The RStudio Community site is a great place to get assistance: https://community.rstudio.com/


  Content: Barret Schloerke (@schloerke)

  Design and editing: Jesse Mostipak (@kierisi)'
people:
- Barret Schloerke
resource_type: video
resources: []
software:
- plumber
- rstudio
- Shiny
title: Barret Schloerke || Maximize computing resources using future_promise() || RStudio

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 6
  date: '2022-02-15T18:00:54Z'
  definition: hd
  description: '00:00 Introduction

    01:45 Setting up a multisession using the future package

    02:05 Simulation using two workers

    04:14 Simulation using 10 workers

    05:20 What happens when we run out of workers?

    05:35 How Shiny handles future processes like promises

    07:16 Introduction to future_promise()

    07:45 Demo of the promises package

    09:21 Setting the number of workers

    10:40 Demo of processing without future_promise()

    14:11 Wrapping a slow calculation in a future()

    14:53 Demo of processing using Plumber

    16:25 Considerations on the number of cores to use

    17:21 What happens if we run out of workers?

    19:44 Decrease in execution times using future_promise()


    In an ideal situation, the number of available future workers (future::nbrOfFreeWorkers()) is always more than the number of future::future() jobs. However, if a future job is attempted when the number of free workers is 0, then future will block the current R session until one becomes available.


    The advantage of using future_promise() over future::future() is that even if there aren’t future workers available, the future is scheduled to be done when workers become available via promises. In other words, future_promise() ensures the main R thread isn’t blocked when a future job is requested and can’t immediately perform the work (i.e., the number of jobs exceeds the number of workers).


    You can read more about the promises package here: https://rstudio.github.io/promises/articles/shiny.html

    And you can learn more about Shiny here: https://shiny.rstudio.com/


    Got questions? The RStudio Community site is a great place to get assistance: https://community.rstudio.com/


    Content: Barret Schloerke (@schloerke)

    Design and editing: Jesse Mostipak (@kierisi)'
  duration: 1329
  has_captions: true
  language: en
  last_updated: '2026-03-04T14:51:27.561183+00:00'
  like_count: 0
  people:
  - Barret Schloerke
  playlist: ''
  software:
  - plumber
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
  - promises
  - Barret Schloerke
  - future_promise()
  thumbnail: https://i.ytimg.com/vi/3gtk8uRrrL4/maxresdefault.jpg
  title: Barret Schloerke || Maximize computing resources using future_promise() || RStudio
  url: https://www.youtube.com/watch?v=3gtk8uRrrL4
  view_count: 2323
---
image: thumbnail.jpg

