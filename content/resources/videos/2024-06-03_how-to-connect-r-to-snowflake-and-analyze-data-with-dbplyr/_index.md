---
date: '2024-06-03'
description: 'To analyse Snowflake data in R, connect with DBI, create references to the tables you need, then work with them using ordinary dplyr verbs. dbplyr translates that dplyr code into SQL and runs it inside Snowflake, so the data never leaves the warehouse and nothing is pulled into memory until you ask for it. This demo runs Posit Workbench as a native app on Snowpark Container Services, builds a marketing analysis and ends with a Shiny app over the same tables. With James Blair.


  What you will learn

  - How to get a dataset from the Snowflake Marketplace

  - How to start an RStudio Pro session running natively on Snowpark Container Services

  - How to connect to Snowflake from R with DBI, and what the connection needs

  - How to create a reference to a table without loading it

  - What dbplyr does: why a dplyr chain becomes SQL that runs in the warehouse

  - Why nothing is collected into memory until you ask for it, and what that saves

  - How to build a visualisation on top of a warehouse query

  - How to put a Shiny app over the same tables so other people can explore them


  Chapters

  0:00 What this demo builds

  0:32 Getting the data from the Snowflake Marketplace

  1:36 Starting an RStudio Pro session on Snowpark Container Services

  2:08 Cloning the code from GitHub

  3:12 Connecting to Snowflake with DBI

  3:44 Creating references to tables

  4:17 Why the data stays in Snowflake: dbplyr and lazy queries

  4:49 Filtering and building the final view

  5:21 Visualising web traffic by domain

  6:25 Calculating pages per session

  6:57 A Shiny app over the same data

  8:01 Why this matters: governed data, faster insight


  Learn more

  dbplyr: https://dbplyr.tidyverse.org

  Databases with R: https://solutions.posit.co/connections/db/

  Posit and Snowflake: https://posit.co/solutions/snowflake/

  Posit Workbench: https://posit.co/products/enterprise/workbench/'
image: thumbnail.jpg
people:
- James Blair
resource_type: video
resources: []
software:
- dbi
- dbplyr
- dplyr
- rstudio
- shiny-r
- tidyverse
- tidyverse.org
tags:
- r snowflake
- connect r to snowflake
- sql and r
- r sql
- dbplyr
- databases with r
- snowpark container services
- posit workbench
- r data warehouse
- dplyr sql
- enterprise data science
- snowflake marketplace
- posit
title: How to Connect R to Snowflake and Analyze Data with dbplyr

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 3
  date: '2024-06-03T19:54:58Z'
  definition: hd
  description: 'To analyse Snowflake data in R, connect with DBI, create references to the tables you need, then work with them using ordinary dplyr verbs. dbplyr translates that dplyr code into SQL and runs it inside Snowflake, so the data never leaves the warehouse and nothing is pulled into memory until you ask for it. This demo runs Posit Workbench as a native app on Snowpark Container Services, builds a marketing analysis and ends with a Shiny app over the same tables. With James Blair.


    What you will learn

    - How to get a dataset from the Snowflake Marketplace

    - How to start an RStudio Pro session running natively on Snowpark Container Services

    - How to connect to Snowflake from R with DBI, and what the connection needs

    - How to create a reference to a table without loading it

    - What dbplyr does: why a dplyr chain becomes SQL that runs in the warehouse

    - Why nothing is collected into memory until you ask for it, and what that saves

    - How to build a visualisation on top of a warehouse query

    - How to put a Shiny app over the same tables so other people can explore them


    Chapters

    0:00 What this demo builds

    0:32 Getting the data from the Snowflake Marketplace

    1:36 Starting an RStudio Pro session on Snowpark Container Services

    2:08 Cloning the code from GitHub

    3:12 Connecting to Snowflake with DBI

    3:44 Creating references to tables

    4:17 Why the data stays in Snowflake: dbplyr and lazy queries

    4:49 Filtering and building the final view

    5:21 Visualising web traffic by domain

    6:25 Calculating pages per session

    6:57 A Shiny app over the same data

    8:01 Why this matters: governed data, faster insight


    Learn more

    dbplyr: https://dbplyr.tidyverse.org

    Databases with R: https://solutions.posit.co/connections/db/

    Posit and Snowflake: https://posit.co/solutions/snowflake/

    Posit Workbench: https://posit.co/products/enterprise/workbench/'
  duration: 514
  has_captions: false
  language: en
  last_updated: '2026-11-12T12:18:01.684986+00:00'
  like_count: 54
  people:
  - James Blair
  playlist: ''
  software:
  - dbi
  - dbplyr
  - dplyr
  - rstudio
  - shiny-r
  - tidyverse
  - tidyverse.org
  tags:
  - r snowflake
  - connect r to snowflake
  - sql and r
  - r sql
  - dbplyr
  - databases with r
  - snowpark container services
  - posit workbench
  - r data warehouse
  - dplyr sql
  - enterprise data science
  - snowflake marketplace
  - posit
  thumbnail: https://i.ytimg.com/vi/b-H0KdXOvGU/maxresdefault.jpg
  title: How to Connect R to Snowflake and Analyze Data with dbplyr
  url: https://www.youtube.com/watch?v=b-H0KdXOvGU
  view_count: 2701
---
image: thumbnail.jpg

