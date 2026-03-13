---
date: '2017-08-02'
description: 'Connecting to an external database from R can be challenging. This is made worse when you need to interact with a database from a live Shiny application. To demystify this process, I''ll do two things.

  First, I''ll talk about best practices when connecting to a database from Shiny. There are three important packages that help you with this and I''ll weave them into this part of the talk. The DBI package does a great job of standardizing how to establish a connection, execute safe queries using SQL (goodbye SQL injections!) and close the connection. The dplyr package builds on top of this to make even easier to connect to databases and extract data, since it allows users to query the database using regular dplyr syntax in R (no SQL knowledge necessary). Yet a third package, pool, exists to help you when using databases in Shiny applications, by taking care of connection management, and often resulting in better performance.

  Second, I''ll demo these concepts in practice by showing how we can connect to a database from Shiny to create a CRUD application. I will show the application running and point out specific parts of the code (which will be publicly available).'
image: thumbnail.jpg
people: []
resource_type: video
resources: []
software:
- DBI
- dplyr
- Shiny
tags:
- RStudio
- RProgramming
- Databases
- dplyr
- odbc
- DBI
- pool
- shiny
title: Interacting with Databases by Bárbara Borges from Shiny from useR! Brussels 2017

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 0
  date: '2017-08-02T20:05:17Z'
  definition: hd
  description: 'Connecting to an external database from R can be challenging. This is made worse when you need to interact with a database from a live Shiny application. To demystify this process, I''ll do two things.

    First, I''ll talk about best practices when connecting to a database from Shiny. There are three important packages that help you with this and I''ll weave them into this part of the talk. The DBI package does a great job of standardizing how to establish a connection, execute safe queries using SQL (goodbye SQL injections!) and close the connection. The dplyr package builds on top of this to make even easier to connect to databases and extract data, since it allows users to query the database using regular dplyr syntax in R (no SQL knowledge necessary). Yet a third package, pool, exists to help you when using databases in Shiny applications, by taking care of connection management, and often resulting in better performance.

    Second, I''ll demo these concepts in practice by showing how we can connect to a database from Shiny to create a CRUD application. I will show the application running and point out specific parts of the code (which will be publicly available).'
  duration: 1016
  has_captions: false
  language: en
  last_updated: '2026-03-04T14:51:30.323309+00:00'
  like_count: 0
  playlist: ''
  software:
  - DBI
  - dplyr
  - Shiny
  tags:
  - RStudio
  - RProgramming
  - Databases
  - dplyr
  - odbc
  - DBI
  - pool
  - shiny
  thumbnail: https://i.ytimg.com/vi/ywXZp7guvRE/maxresdefault.jpg
  title: Interacting with Databases by Bárbara Borges from Shiny from useR! Brussels 2017
  url: https://www.youtube.com/watch?v=ywXZp7guvRE
  view_count: 8328
---
image: thumbnail.jpg

