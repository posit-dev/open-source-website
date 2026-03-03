---
date: '2024-05-15'
description: 'It’s been years since Shiny evolved to allow asynchronous operations within applications, improving scalability. The introduction of the {promises} package enabled concurrent processing between multiple Shiny sessions, a significant step forward in handling background tasks. However, this did not address the need for intra-session concurrency, where users expect to interact with the application while long-running calculations are executed in the background.


  Recently, we added a new ExtendedTask feature to Shiny to allow for such intra-session concurrency. This new feature provides a different approach for developers to incorporate asynchronous tasks, enabling smoother user interactions during intensive computations. Alongside ExtendedTask, this talk will also discuss newer methods for launching asynchronous tasks, besides the usual {future} package. The focus will be on the practical application and integration of these features into Shiny applications.


  Links mentioned in the video:

  ⬡ Shiny in Production: Principles, practices, and tools, https://youtu.be/Wy3TY0gOmJw?feature=shared


  Timestamps:

  0:20 Make your slow code fast

  1:43 Long-running operations are a problem

  3:28 Inter-session concurrency and intra-session concurrency

  4:24 Introducing ExtendedTask

  5:17 Demo of a slow API using ExtendedTask

  6:13 Slow code example (R)

  7:16 Fix slow code with ExtendedTask (R)

  8:55 Slow code example (Python)

  7:16 Fix slow code with ExtendedTask (Python)

  10:46 Links to get started

  11:06 ExtendedTask backstory intro

  11:28 ExtendedTask vs. Shiny Async

  15:50 How reactive programming works in Shiny

  21:31 How ExtendedTask works in the reactive process

  25:38 What we’re still working on

  26:35 {future} alternatives

  31:47 Wrapping up'
people:
- Joe Cheng
resource_type: video
resources: []
software:
- Intro
- promises
- Shiny
title: Joe Cheng | Managing long-running operations in Shiny | Posit

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 8
  date: '2024-05-15T22:24:15Z'
  definition: hd
  description: 'It’s been years since Shiny evolved to allow asynchronous operations within applications, improving scalability. The introduction of the {promises} package enabled concurrent processing between multiple Shiny sessions, a significant step forward in handling background tasks. However, this did not address the need for intra-session concurrency, where users expect to interact with the application while long-running calculations are executed in the background.


    Recently, we added a new ExtendedTask feature to Shiny to allow for such intra-session concurrency. This new feature provides a different approach for developers to incorporate asynchronous tasks, enabling smoother user interactions during intensive computations. Alongside ExtendedTask, this talk will also discuss newer methods for launching asynchronous tasks, besides the usual {future} package. The focus will be on the practical application and integration of these features into Shiny applications.


    Links mentioned in the video:

    ⬡ Shiny in Production: Principles, practices, and tools, https://youtu.be/Wy3TY0gOmJw?feature=shared


    Timestamps:

    0:20 Make your slow code fast

    1:43 Long-running operations are a problem

    3:28 Inter-session concurrency and intra-session concurrency

    4:24 Introducing ExtendedTask

    5:17 Demo of a slow API using ExtendedTask

    6:13 Slow code example (R)

    7:16 Fix slow code with ExtendedTask (R)

    8:55 Slow code example (Python)

    7:16 Fix slow code with ExtendedTask (Python)

    10:46 Links to get started

    11:06 ExtendedTask backstory intro

    11:28 ExtendedTask vs. Shiny Async

    15:50 How reactive programming works in Shiny

    21:31 How ExtendedTask works in the reactive process

    25:38 What we’re still working on

    26:35 {future} alternatives

    31:47 Wrapping up'
  duration: 1977
  has_captions: true
  language: en
  last_updated: '2026-03-02T20:54:18.754766+00:00'
  like_count: 141
  people:
  - Joe Cheng
  playlist: ''
  software:
  - Intro
  - promises
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
  thumbnail: https://i.ytimg.com/vi/GhX0PcEm3CY/maxresdefault.jpg
  title: Joe Cheng | Managing long-running operations in Shiny | Posit
  url: https://www.youtube.com/watch?v=GhX0PcEm3CY
  view_count: 4645
---

