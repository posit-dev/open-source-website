---
date: '2018-03-14'
description: "Data wrangling is too often the most time-consuming part of data science and applied statistics. Two tidyverse packages, tidyr and dplyr, help make data manipulation tasks easier. Keep your R code clean and clear and reduce the cognitive load required for common but often complex data science tasks. \n\n`dplyr` docs: dplyr.tidyverse.org/reference/\n- http://dplyr.tidyverse.org/reference/setops.html\n- http://dplyr.tidyverse.org/reference/join.html\n\n----------------\n\nPt. 1: What is data wrangling? Intro, Motivation, Outline, Setup https://youtu.be/jOd65mR1zfw\n- /01:44 Intro and what’s covered\nGround Rules:\n- /02:40 What’s a tibble\n- /04:50 Use View\n- /05:25 The Pipe operator: \n- /07:20 What do I mean by data wrangling? \n\nPt. 2: Tidy Data and tidyr https://youtu.be/1ELALQlO-yM\n- /00:48 Goal 1 Making your data suitable for R\n- /01:40 `tidyr` “Tidy” Data introduced and motivated\n- /08:10 `tidyr::gather` \n- /12:30 `tidyr::spread`\n- /15:23 `tidyr::unite` \n- /15:23 `tidyr::separate`\n\nPt. 3: Data manipulation tools: `dplyr` https://youtu.be/Zc_ufg4uW4U\n- /00.40 setup\n- /02:00 `dplyr::select`\n- /03:40 `dplyr::filter`\n- /05:05 `dplyr::mutate`\n- /07:05 `dplyr::summarise`\n- /08:30 `dplyr::arrange`\n- /09:55 Combining these tools with the pipe (Setup for the Grammar of Data Manipulation)\n- /11:45 `dplyr::group_by`\n\nPt. 4: Working with Two Datasets: Binds, Set Operations, and Joins https://youtu.be/AuBgYDCg1Cg\nCombining two datasets together\n- 00.42 `dplyr::bind_cols`\n- 01:27 `dplyr::bind_rows`\n- 01:42 Set operations\n`dplyr::union`, `dplyr::intersect`, `dplyr::set_diff`\n- 02:15 joining data - `dplyr::left_join`, `dplyr::inner_join`, -\n `dplyr::right_join`, `dplyr::full_join`,\n\n______________________________________________________________\n\nCheatsheets: https://www.rstudio.com/resources/cheatsheets/ \n\nDocumentation:\n`tidyr` docs: tidyr.tidyverse.org/reference/\n- `tidyr` vignette: https://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html\n`dplyr` docs: http://dplyr.tidyverse.org/reference/\n- `dplyr` one-table vignette: https://cran.r-project.org/web/packages/dplyr/vignettes/dplyr.html\n- `dplyr` two-table (join operations) vignette: https://cran.r-project.org/web/packages/dplyr/vignettes/two-table.html \n\n______________________________________________________________"
image: thumbnail.jpg
people: []
resource_type: video
resources: []
software:
- cheatsheets
- dplyr
- rstudio
- tibble
- tidyr
- tidyverse
- tidyverse.org
tags:
- grammar of data manipulation
- data science
- data wrangling
- applied statistics
- statistics
- rstudio
- data manipulation
- joins
- merge
- rstats
- two tables
- two tibbles
- two datasets
- two data.frames
- two dataframes
- two tables at the same time
- intersect
- union
- setdiff
- left_join
- right_join
- full_join
- anti_join
title: 'Working with Two Datasets: Binds, Set Operations, and Joins  -- Pt 4 Intro to Data Manipulation'

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 8
  date: '2018-03-14T20:25:00Z'
  definition: hd
  description: "Data wrangling is too often the most time-consuming part of data science and applied statistics. Two tidyverse packages, tidyr and dplyr, help make data manipulation tasks easier. Keep your R code clean and clear and reduce the cognitive load required for common but often complex data science tasks. \n\n`dplyr` docs: dplyr.tidyverse.org/reference/\n- http://dplyr.tidyverse.org/reference/setops.html\n- http://dplyr.tidyverse.org/reference/join.html\n\n----------------\n\nPt. 1: What is data wrangling? Intro, Motivation, Outline, Setup https://youtu.be/jOd65mR1zfw\n- /01:44 Intro and what’s covered\nGround Rules:\n- /02:40 What’s a tibble\n- /04:50 Use View\n- /05:25 The Pipe operator: \n- /07:20 What do I mean by data wrangling? \n\nPt. 2: Tidy Data and tidyr https://youtu.be/1ELALQlO-yM\n- /00:48 Goal 1 Making your data suitable for R\n- /01:40 `tidyr` “Tidy” Data introduced and motivated\n- /08:10 `tidyr::gather` \n- /12:30 `tidyr::spread`\n- /15:23 `tidyr::unite` \n- /15:23 `tidyr::separate`\n\nPt. 3: Data manipulation tools: `dplyr` https://youtu.be/Zc_ufg4uW4U\n- /00.40 setup\n- /02:00 `dplyr::select`\n- /03:40 `dplyr::filter`\n- /05:05 `dplyr::mutate`\n- /07:05 `dplyr::summarise`\n- /08:30 `dplyr::arrange`\n- /09:55 Combining these tools with the pipe (Setup for the Grammar of Data Manipulation)\n- /11:45 `dplyr::group_by`\n\nPt. 4: Working with Two Datasets: Binds, Set Operations, and Joins https://youtu.be/AuBgYDCg1Cg\nCombining two datasets together\n- 00.42 `dplyr::bind_cols`\n- 01:27 `dplyr::bind_rows`\n- 01:42 Set operations\n`dplyr::union`, `dplyr::intersect`, `dplyr::set_diff`\n- 02:15 joining data - `dplyr::left_join`, `dplyr::inner_join`, -\n `dplyr::right_join`, `dplyr::full_join`,\n\n______________________________________________________________\n\nCheatsheets: https://www.rstudio.com/resources/cheatsheets/ \n\nDocumentation:\n`tidyr` docs: tidyr.tidyverse.org/reference/\n- `tidyr` vignette: https://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html\n`dplyr` docs: http://dplyr.tidyverse.org/reference/\n- `dplyr` one-table vignette: https://cran.r-project.org/web/packages/dplyr/vignettes/dplyr.html\n- `dplyr` two-table (join operations) vignette: https://cran.r-project.org/web/packages/dplyr/vignettes/two-table.html \n\n______________________________________________________________"
  duration: 443
  has_captions: false
  language: en
  last_updated: '2026-03-04T14:51:29.959238+00:00'
  like_count: 0
  playlist: ''
  software:
  - cheatsheets
  - dplyr
  - rstudio
  - tibble
  - tidyr
  - tidyverse
  - tidyverse.org
  tags:
  - grammar of data manipulation
  - data science
  - data wrangling
  - applied statistics
  - statistics
  - rstudio
  - data manipulation
  - joins
  - merge
  - rstats
  - two tables
  - two tibbles
  - two datasets
  - two data.frames
  - two dataframes
  - two tables at the same time
  - intersect
  - union
  - setdiff
  - left_join
  - right_join
  - full_join
  - anti_join
  thumbnail: https://i.ytimg.com/vi/AuBgYDCg1Cg/maxresdefault.jpg
  title: 'Working with Two Datasets: Binds, Set Operations, and Joins  -- Pt 4 Intro to Data Manipulation'
  url: https://www.youtube.com/watch?v=AuBgYDCg1Cg
  view_count: 17450
---
image: thumbnail.jpg

