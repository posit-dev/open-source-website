---
date: '2020-11-01'
description: A number of R packages exist to make computing moving averages on a single numeric series straightforward. But generally “real” life is much messier than that! Try computing a moving average over a twenty-day sliding window when you have a time series with missing data. Oh! By the way, you should also skip over weekends when looking back twenty days. And you know that random holiday that your company celebrates that no one else does? Skip over that too. These are hard but realistic problems, and until now there has been a lack of tools necessary to solve them. In this talk, I’ll present two packages designed to tackle these issues, slide and almanac. slide is a package designed to perform arbitrary sliding window calculations. The simplest example of this would be a moving average. What makes slide unique is its support for sliding relative to an index, such as a date vector, which allows you to correctly compute the boundaries of that twenty day window. almanac is package for creating custom business calendars, and then adjusting dates relative to them. Inspired by lubridate, almanac allows you to shift dates by a set number of “business” days while respecting the weekends and holidays defined by a user-specified calendar. For example, shifting a Friday forward by 1 business day would land on a Monday, unless that Monday happened to be a holiday, in which case the next business day would actually be Tuesday. Together, slide and almanac provide the tooling necessary to solve the problem mentioned earlier. Additionally, because slide works with any arbitrary function, we can use the same procedure to compute rolling regressions, cumulative sums, and any other sliding computation. A 5-minute presentation in our Lightning Talks series
people: []
resource_type: video
resources: []
software:
- lubridate
- rstudio
title: Davis Vaughn | Sliding Windows and Calendars | RStudio (2020)

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 0
  date: '2020-11-01T07:00:07Z'
  definition: hd
  description: A number of R packages exist to make computing moving averages on a single numeric series straightforward. But generally “real” life is much messier than that! Try computing a moving average over a twenty-day sliding window when you have a time series with missing data. Oh! By the way, you should also skip over weekends when looking back twenty days. And you know that random holiday that your company celebrates that no one else does? Skip over that too. These are hard but realistic problems, and until now there has been a lack of tools necessary to solve them. In this talk, I’ll present two packages designed to tackle these issues, slide and almanac. slide is a package designed to perform arbitrary sliding window calculations. The simplest example of this would be a moving average. What makes slide unique is its support for sliding relative to an index, such as a date vector, which allows you to correctly compute the boundaries of that twenty day window. almanac is package for creating custom business calendars, and then adjusting dates relative to them. Inspired by lubridate, almanac allows you to shift dates by a set number of “business” days while respecting the weekends and holidays defined by a user-specified calendar. For example, shifting a Friday forward by 1 business day would land on a Monday, unless that Monday happened to be a holiday, in which case the next business day would actually be Tuesday. Together, slide and almanac provide the tooling necessary to solve the problem mentioned earlier. Additionally, because slide works with any arbitrary function, we can use the same procedure to compute rolling regressions, cumulative sums, and any other sliding computation. A 5-minute presentation in our Lightning Talks series
  duration: 319
  has_captions: false
  language: en
  last_updated: '2026-03-02T20:54:23.073864+00:00'
  like_count: 33
  playlist: ''
  software:
  - lubridate
  - rstudio
  tags:
  - rstudio::conf(2020)
  - Davis Vaughn
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
  thumbnail: https://i.ytimg.com/vi/wb76gXropuw/hqdefault.jpg
  title: Davis Vaughn | Sliding Windows and Calendars | RStudio (2020)
  url: https://www.youtube.com/watch?v=wb76gXropuw
  view_count: 896
---

