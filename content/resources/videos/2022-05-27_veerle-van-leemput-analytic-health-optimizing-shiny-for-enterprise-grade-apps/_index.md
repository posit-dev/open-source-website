---
date: '2022-05-27'
description: '❓Can you use Shiny in production?

  A: Yes, you definitely can.


  ✨ Link to slides: https://github.com/RStudioEnterpriseMeetup/Presentations/blob/main/VeerlevanLeemput-OptimizingShiny-20220525.pdf


  ✨ Packages mentioned:

  ⬢ shiny: https://shiny.rstudio.com/

  ⬢ pins: https://pins.rstudio.com/

  ⬢ plumber: https://www.rplumber.io/

  ⬢ blastula: https://github.com/rstudio/blastula

  ⬢ callR: https://github.com/r-lib/callr

  ⬢ shinyloadtest: https://rstudio.github.io/shinyloadtest/

  ⬢ shinycannon: https://github.com/rstudio/shinycannon

  ⬢ shinytest2: https://rstudio.github.io/shinytest2/

  ⬢ feather: https://github.com/wesm/feather

  ⬢ shinipsum: https://github.com/ThinkR-open/shinipsum

  ⬢ bs4Dash: https://rinterface.github.io/bs4Dash/index.html


  Timestamps:

  2:44 - Start of presentation

  5:41 - What qualifies as an enterprise-grade app?

  10:46 - UI first / user experience / prototyping

  13:20 - Separating code into separate scripts and creating code that''s easy to test

  17:15 - Golem

  19:28 - Functionize your code

  20:50 - Rhino package, framework for developing enterprise-grade apps at speed

  22:33 - Infrastructure, how do you bring this to your users? (lots of ways to do this. They do this with R, pins, plumber, rmd, blastula, and Posit Connect on Azure)

  31:17 - Optimizing Shiny (process configuration, cache, callR, API, feather)

  47:35 - Testing your app (shinyloadtest and shinycannon)

  50:23 - Testing for outcomes (shinytest2)

  52:15 - Monitor app performance & usage (blastula, shinycannon, usage metrics with Shiny app)


  Questions:

  57:38 - What''s the benefit of using pins rather than pulling the data from your database?

  59:30 - Are there package license considerations you had to think about when monetizing shiny applications?

  1:00:45 - Do you use promises to scale the application? (they use CallR)

  1:01:49 - For beginners, golem or rhino?

  1:02:50 - The myth is that only Python can be used for production apps, what made you choose to use R?

  1:05:12 - Is feather strictly better than using JSON?

  1:06:38 - Where do you see the line between BI (business intelligence) and Shiny for your applications?

  1:08:36 - Any tips for enterprise-grade UI development? Making beautiful apps (bs4Dash app)

  1:10:25 - Have you found an upper limit for users?

  1:12:19 - Any tips for more dynamic data? (optimizing database helps here)

  1:13:50 - Where do you install shinycannon? (on our development Linux server)

  1:15:00 - Can you share other resources or examples of code? (Slides here with resources: https://github.com/RStudioEnterpriseMeetup/Presentations/blob/main/VeerlevanLeemput-OptimizingShiny-20220525.pdf)


  For upcoming events: rstd.io/community-events-calendar

  Info on Posit Connect: https://www.rstudio.com/products/connect/

  To chat with Posit: rstd.io/chat-with-rstudio'
image: thumbnail.jpg
people: []
resource_type: video
resources: []
software:
- blastula
- callr
- plumber
- rstudio
- Shiny
- shinyloadtest
- shinytest2
tags: []
title: Veerle van Leemput | Analytic Health | Optimizing Shiny for enterprise-grade apps

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 2
  date: '2022-05-27T15:10:49Z'
  definition: hd
  description: '❓Can you use Shiny in production?

    A: Yes, you definitely can.


    ✨ Link to slides: https://github.com/RStudioEnterpriseMeetup/Presentations/blob/main/VeerlevanLeemput-OptimizingShiny-20220525.pdf


    ✨ Packages mentioned:

    ⬢ shiny: https://shiny.rstudio.com/

    ⬢ pins: https://pins.rstudio.com/

    ⬢ plumber: https://www.rplumber.io/

    ⬢ blastula: https://github.com/rstudio/blastula

    ⬢ callR: https://github.com/r-lib/callr

    ⬢ shinyloadtest: https://rstudio.github.io/shinyloadtest/

    ⬢ shinycannon: https://github.com/rstudio/shinycannon

    ⬢ shinytest2: https://rstudio.github.io/shinytest2/

    ⬢ feather: https://github.com/wesm/feather

    ⬢ shinipsum: https://github.com/ThinkR-open/shinipsum

    ⬢ bs4Dash: https://rinterface.github.io/bs4Dash/index.html


    Timestamps:

    2:44 - Start of presentation

    5:41 - What qualifies as an enterprise-grade app?

    10:46 - UI first / user experience / prototyping

    13:20 - Separating code into separate scripts and creating code that''s easy to test

    17:15 - Golem

    19:28 - Functionize your code

    20:50 - Rhino package, framework for developing enterprise-grade apps at speed

    22:33 - Infrastructure, how do you bring this to your users? (lots of ways to do this. They do this with R, pins, plumber, rmd, blastula, and Posit Connect on Azure)

    31:17 - Optimizing Shiny (process configuration, cache, callR, API, feather)

    47:35 - Testing your app (shinyloadtest and shinycannon)

    50:23 - Testing for outcomes (shinytest2)

    52:15 - Monitor app performance & usage (blastula, shinycannon, usage metrics with Shiny app)


    Questions:

    57:38 - What''s the benefit of using pins rather than pulling the data from your database?

    59:30 - Are there package license considerations you had to think about when monetizing shiny applications?

    1:00:45 - Do you use promises to scale the application? (they use CallR)

    1:01:49 - For beginners, golem or rhino?

    1:02:50 - The myth is that only Python can be used for production apps, what made you choose to use R?

    1:05:12 - Is feather strictly better than using JSON?

    1:06:38 - Where do you see the line between BI (business intelligence) and Shiny for your applications?

    1:08:36 - Any tips for enterprise-grade UI development? Making beautiful apps (bs4Dash app)

    1:10:25 - Have you found an upper limit for users?

    1:12:19 - Any tips for more dynamic data? (optimizing database helps here)

    1:13:50 - Where do you install shinycannon? (on our development Linux server)

    1:15:00 - Can you share other resources or examples of code? (Slides here with resources: https://github.com/RStudioEnterpriseMeetup/Presentations/blob/main/VeerlevanLeemput-OptimizingShiny-20220525.pdf)


    For upcoming events: rstd.io/community-events-calendar

    Info on Posit Connect: https://www.rstudio.com/products/connect/

    To chat with Posit: rstd.io/chat-with-rstudio'
  duration: 4601
  has_captions: true
  language: en
  last_updated: '2026-03-04T14:51:27.219783+00:00'
  like_count: 78
  playlist: ''
  software:
  - blastula
  - callr
  - plumber
  - rstudio
  - Shiny
  - shinyloadtest
  - shinytest2
  tags: []
  thumbnail: https://i.ytimg.com/vi/mgCQZmJdQaI/maxresdefault.jpg
  title: Veerle van Leemput | Analytic Health | Optimizing Shiny for enterprise-grade apps
  url: https://www.youtube.com/watch?v=mgCQZmJdQaI
  view_count: 2091
---
image: thumbnail.jpg

