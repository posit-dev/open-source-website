---
date: '2026-11-18'
description: "Start small: put your code in small functions inside a package, run `use_testthat()` to set up testing, and write one `test_that()` test that compares a function’s output to what you expect. Then try edge cases like zero or negative input, and use assertthat or cli for clear error messages. You’re probably testing informally already, so this just writes it down, and you can add snapshots, mocking, or the ensure add-in later.\n\nIn this Data Science Lab session, Jacci Ziebert, facilitate a community discussion on the fundamentals and importance of unit testing in R. We begin by addressing the common practice of writing monolithic functions and why modularity is essential for easier debugging and more reliable testing. Jacci does this by showcasing the use of the testthat package to create and run unit tests.\n\nThe Data Science Lab is a live weekly call. Register at pos.it/dslab! Discord invites go out each week on lives calls. We'd love to have you! It's is an open, messy space for learning and asking questions. Think of it like pair coding with a friend or two. Learn something new, and share what you know to help others grow.\n\nOriginally recorded on October 6, 2026.\n\nResources mentioned:\n- Jacci’s unit testing blog post: https://jacciz.github.io/portfolio/projects/unit_testing.html \n- Jacci’s blog post on clean code: https://jacciz.github.io/portfolio/projects/clean_code.html \n- usethis: https://usethis.r-lib.org/\n- testthat: https://testthat.r-lib.org/\n- assertthat: https://github.com/hadley/assertthat\n- waldo: https://waldo.r-lib.org/\n- glue: https://glue.tidyverse.org/\n- rlang: https://rlang.r-lib.org/\n- withr: https://withr.r-lib.org/\n- ensure: https://simonpcouch.github.io/ensure/ \n- cli: https://cli.r-lib.org/reference/index.html\n- cli progress bar! https://cli.r-lib.org/reference/cli_progress_step.html\n- echarts4r: https://echarts4r.john-coene.com/ \n- Positron keybindings: https://positron.posit.co/keyboard-shortcuts.html\n- Plotly for R: https://plotly.com/r/\n- Snapshot testing in R: https://testthat.r-lib.org/articles/snapshotting.html\n- autogradeR : https://math-mcshane.github.io/autogradeR/\n- Ryan McShane's unit testing for student code: https://ryanmcshane.com/talk/ecots_2026/ \n-  Riffomonas/ Pat Schloss' videowhere you write the test failing tests first: https://www.youtube.com/watch?v=TaNvqwMmHus\n- Custom expectations vignette in testthat: https://testthat.r-lib.org/articles/custom-expectation.html\n- Skill for testing R packages: https://github.com/posit-dev/skills/tree/main/r-lib/testing-r-packages\n\n0:00 Welcome to the Data Science Lab\n1:09 Poll: Do you do testing in R?\n3:21 Testober: what's coming (Python and Shiny testing)\n4:35 Why unit test? The \"monolith function\" problem\n9:18 Why modularity and testability help (Jacci's story)\n10:56 Q&A: Does input validation count as testing?\n12:54 Jacci shares her screen: building a test-friendly package\n13:47 Tip: add a Source column in RStudio\n17:06 Helpful packages: usethis, testthat, assertthat, cli\n18:32 Q&A: Package development shortcuts in Positron\n20:23 What a unit test is and setting up with use_testthat()\n23:52 Writing your first tests and testing edge cases\n31:44 Clearer error messages with assertthat\n35:35 Testing that errors and messages show up (expect_error)\n38:24 Snapshot testing with expect_snapshot()\n43:11 Q&A: Embedding values in error messages, and cli\n46:41 Q&A: Reusing tests and mocking functions\n50:22 Generating unit tests with the ensure add-in\n55:23 Agent skills for testing R packages\n58:22 Wrap-up and thank you to Jacci"
image: thumbnail.jpg
people: []
resource_type: video
resources: []
software:
- cli
- positron
- rlang
- rstudio
- shiny-r
- testthat
- tidyverse
- tidyverse.org
- usethis
- waldo
- withr
tags: []
title: How do you get started with unit testing in R? | Jacci Ziebert | Data Science Lab

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 2
  date: '2026-11-18T13:45:26Z'
  definition: hd
  description: "Start small: put your code in small functions inside a package, run `use_testthat()` to set up testing, and write one `test_that()` test that compares a function’s output to what you expect. Then try edge cases like zero or negative input, and use assertthat or cli for clear error messages. You’re probably testing informally already, so this just writes it down, and you can add snapshots, mocking, or the ensure add-in later.\n\nIn this Data Science Lab session, Jacci Ziebert, facilitate a community discussion on the fundamentals and importance of unit testing in R. We begin by addressing the common practice of writing monolithic functions and why modularity is essential for easier debugging and more reliable testing. Jacci does this by showcasing the use of the testthat package to create and run unit tests.\n\nThe Data Science Lab is a live weekly call. Register at pos.it/dslab! Discord invites go out each week on lives calls. We'd love to have you! It's is an open, messy space for learning and asking questions. Think of it like pair coding with a friend or two. Learn something new, and share what you know to help others grow.\n\nOriginally recorded on October 6, 2026.\n\nResources mentioned:\n- Jacci’s unit testing blog post: https://jacciz.github.io/portfolio/projects/unit_testing.html \n- Jacci’s blog post on clean code: https://jacciz.github.io/portfolio/projects/clean_code.html \n- usethis: https://usethis.r-lib.org/\n- testthat: https://testthat.r-lib.org/\n- assertthat: https://github.com/hadley/assertthat\n- waldo: https://waldo.r-lib.org/\n- glue: https://glue.tidyverse.org/\n- rlang: https://rlang.r-lib.org/\n- withr: https://withr.r-lib.org/\n- ensure: https://simonpcouch.github.io/ensure/ \n- cli: https://cli.r-lib.org/reference/index.html\n- cli progress bar! https://cli.r-lib.org/reference/cli_progress_step.html\n- echarts4r: https://echarts4r.john-coene.com/ \n- Positron keybindings: https://positron.posit.co/keyboard-shortcuts.html\n- Plotly for R: https://plotly.com/r/\n- Snapshot testing in R: https://testthat.r-lib.org/articles/snapshotting.html\n- autogradeR : https://math-mcshane.github.io/autogradeR/\n- Ryan McShane's unit testing for student code: https://ryanmcshane.com/talk/ecots_2026/ \n-  Riffomonas/ Pat Schloss' videowhere you write the test failing tests first: https://www.youtube.com/watch?v=TaNvqwMmHus\n- Custom expectations vignette in testthat: https://testthat.r-lib.org/articles/custom-expectation.html\n- Skill for testing R packages: https://github.com/posit-dev/skills/tree/main/r-lib/testing-r-packages\n\n0:00 Welcome to the Data Science Lab\n1:09 Poll: Do you do testing in R?\n3:21 Testober: what's coming (Python and Shiny testing)\n4:35 Why unit test? The \"monolith function\" problem\n9:18 Why modularity and testability help (Jacci's story)\n10:56 Q&A: Does input validation count as testing?\n12:54 Jacci shares her screen: building a test-friendly package\n13:47 Tip: add a Source column in RStudio\n17:06 Helpful packages: usethis, testthat, assertthat, cli\n18:32 Q&A: Package development shortcuts in Positron\n20:23 What a unit test is and setting up with use_testthat()\n23:52 Writing your first tests and testing edge cases\n31:44 Clearer error messages with assertthat\n35:35 Testing that errors and messages show up (expect_error)\n38:24 Snapshot testing with expect_snapshot()\n43:11 Q&A: Embedding values in error messages, and cli\n46:41 Q&A: Reusing tests and mocking functions\n50:22 Generating unit tests with the ensure add-in\n55:23 Agent skills for testing R packages\n58:22 Wrap-up and thank you to Jacci"
  duration: 3579
  has_captions: true
  language: en
  last_updated: '2026-11-27T05:09:08.518909+00:00'
  like_count: 21
  playlist: ''
  software:
  - cli
  - positron
  - rlang
  - rstudio
  - shiny-r
  - testthat
  - tidyverse
  - tidyverse.org
  - usethis
  - waldo
  - withr
  tags: []
  thumbnail: https://i.ytimg.com/vi/y8A8uoWOi-U/maxresdefault.jpg
  title: How do you get started with unit testing in R? | Jacci Ziebert | Data Science Lab
  url: https://www.youtube.com/watch?v=y8A8uoWOi-U
  view_count: 1546
---

