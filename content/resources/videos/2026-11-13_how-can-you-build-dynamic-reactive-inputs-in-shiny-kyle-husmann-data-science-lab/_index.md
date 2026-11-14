---
date: '2026-11-13'
description: 'You can use the irid package, which complements Shiny, to help you build interactive, dynamically-changing reactive inputs and outputs that wont overwhelm or overly complicate your Shiny app.


  The Data Science Lab is a live weekly call. Register at pos.it/dslab! Discord invites go out each week on lives calls. We''d love to have you! It''s is an open, messy space for learning and asking questions. Think of it like pair coding with a friend or two. Learn something new, and share what you know to help others grow.


  On this Lab, Kyle Husmann, software engineer at Posit, talks about his new irid package, which brings ideas from modern JavaScript component frameworks to Shiny, especially Solid.js, which pioneered fine-grained reactivity where each change updates only the specific DOM node it’s bound to.


  Hosting crew from Posit: Libby Heeren

  Recorded: August 11, 2026


  Kyle Husmann''s socials and urls:

  https://bsky.app/profile/kylehusmann.bsky.social

  https://github.com/khusmann

  https://kylehusmann.com


  Resources mentioned in video and/or the chat:

  {irid} website and docs: https://irid.kylehusmann.com/

  {irid} GitHub repo: https://github.com/khusmann/irid

  Temperature converter app example in {irid}: https://irid.kylehusmann.com/apps/temperature/index.html?_shinylive-mode=editor-terminal-viewer

  More {irid} examples: https://irid.kylehusmann.com/articles/examples.html

  To Do List example app using {irid}: https://irid.kylehusmann.com/apps/todo/index.html?_shinylive-mode=editor-terminal-viewer

  {irid} package vignette on CRAN: https://cran.rstudio.com/web//packages/irid/vignettes/irid.html

  React JS: https://legacy.reactjs.org/

  shinystan: https://mc-stan.org/shinystan/

  Using bslib in Shiny: https://shiny.posit.co/r/articles/build/themes/

  Shiny for Python: https://shiny.posit.co/py/

  Mastering Shiny book (free): https://mastering-shiny.org/

  What is reactivity? (from Mastering Shiny book): https://mastering-shiny.org/basic-reactivity.html


  Timestamps

  00:00 Introduction

  03:33 Interactivity and reactivity in standard Shiny

  06:08 "Why did you make irid and what does it look like?"

  06:57 Live coding a base Shiny app

  10:13 Adding reactivity in Shiny and UI/server split challenges

  12:57 Introducing {irid} and single-function app architecture

  16:18 "Is this like implementing Shiny for Python''s express mode, but in R?"

  17:11 Hooking up reactive values in irid

  20:25 Dynamically styling HTML elements with reactive values

  21:50 "What if you type something that isn''t a color?" (can we break this?)

  22:31 Circular observers and "update chasing" in Shiny

  25:48 "Is it an anonymous function or a reference to the reactive value?"

  28:57 Demoing the To Do list app in irid

  32:44 "Can we build our own Shiny inputs using HTML widgets?"

  33:15 Demoing the CodeMirror editor widget in irid

  35:55 Full tag tree re-renders vs. surgical DOM updates

  38:09 Demoing the bidirectional temperature converter

  39:19 Reviewing the To Do app source code

  42:20 Using conditional logic (when) and list loops (each)

  44:33 Component functions vs. traditional Shiny modules

  47:11 "Component functions that handle UI and server reactivity sound like modules?"

  47:44 Demoing the nested questions quiz builder

  48:54 "Why did you call it Irid?"

  49:19 Interoperability: Running irid components inside Shiny

  50:41 "Do you have any specific recommendations when you want to convert an existing Shiny app to use irid?"

  51:19 Exploring documentation, templates, and Claude skills for irid

  53:56 Diagnosing app freezes and refresh loops in complex apps

  55:26 "Is the GitHub repo the best place for feedback?"'
image: thumbnail.jpg
people: []
resource_type: video
resources: []
software:
- bslib
- rstudio
- shiny-python
- shiny-r
tags: []
title: How can you build dynamic reactive inputs in Shiny? | Kyle Husmann | Data Science Lab

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 0
  date: '2026-11-13T02:00:23Z'
  definition: hd
  description: 'You can use the irid package, which complements Shiny, to help you build interactive, dynamically-changing reactive inputs and outputs that wont overwhelm or overly complicate your Shiny app.


    The Data Science Lab is a live weekly call. Register at pos.it/dslab! Discord invites go out each week on lives calls. We''d love to have you! It''s is an open, messy space for learning and asking questions. Think of it like pair coding with a friend or two. Learn something new, and share what you know to help others grow.


    On this Lab, Kyle Husmann, software engineer at Posit, talks about his new irid package, which brings ideas from modern JavaScript component frameworks to Shiny, especially Solid.js, which pioneered fine-grained reactivity where each change updates only the specific DOM node it’s bound to.


    Hosting crew from Posit: Libby Heeren

    Recorded: August 11, 2026


    Kyle Husmann''s socials and urls:

    https://bsky.app/profile/kylehusmann.bsky.social

    https://github.com/khusmann

    https://kylehusmann.com


    Resources mentioned in video and/or the chat:

    {irid} website and docs: https://irid.kylehusmann.com/

    {irid} GitHub repo: https://github.com/khusmann/irid

    Temperature converter app example in {irid}: https://irid.kylehusmann.com/apps/temperature/index.html?_shinylive-mode=editor-terminal-viewer

    More {irid} examples: https://irid.kylehusmann.com/articles/examples.html

    To Do List example app using {irid}: https://irid.kylehusmann.com/apps/todo/index.html?_shinylive-mode=editor-terminal-viewer

    {irid} package vignette on CRAN: https://cran.rstudio.com/web//packages/irid/vignettes/irid.html

    React JS: https://legacy.reactjs.org/

    shinystan: https://mc-stan.org/shinystan/

    Using bslib in Shiny: https://shiny.posit.co/r/articles/build/themes/

    Shiny for Python: https://shiny.posit.co/py/

    Mastering Shiny book (free): https://mastering-shiny.org/

    What is reactivity? (from Mastering Shiny book): https://mastering-shiny.org/basic-reactivity.html


    Timestamps

    00:00 Introduction

    03:33 Interactivity and reactivity in standard Shiny

    06:08 "Why did you make irid and what does it look like?"

    06:57 Live coding a base Shiny app

    10:13 Adding reactivity in Shiny and UI/server split challenges

    12:57 Introducing {irid} and single-function app architecture

    16:18 "Is this like implementing Shiny for Python''s express mode, but in R?"

    17:11 Hooking up reactive values in irid

    20:25 Dynamically styling HTML elements with reactive values

    21:50 "What if you type something that isn''t a color?" (can we break this?)

    22:31 Circular observers and "update chasing" in Shiny

    25:48 "Is it an anonymous function or a reference to the reactive value?"

    28:57 Demoing the To Do list app in irid

    32:44 "Can we build our own Shiny inputs using HTML widgets?"

    33:15 Demoing the CodeMirror editor widget in irid

    35:55 Full tag tree re-renders vs. surgical DOM updates

    38:09 Demoing the bidirectional temperature converter

    39:19 Reviewing the To Do app source code

    42:20 Using conditional logic (when) and list loops (each)

    44:33 Component functions vs. traditional Shiny modules

    47:11 "Component functions that handle UI and server reactivity sound like modules?"

    47:44 Demoing the nested questions quiz builder

    48:54 "Why did you call it Irid?"

    49:19 Interoperability: Running irid components inside Shiny

    50:41 "Do you have any specific recommendations when you want to convert an existing Shiny app to use irid?"

    51:19 Exploring documentation, templates, and Claude skills for irid

    53:56 Diagnosing app freezes and refresh loops in complex apps

    55:26 "Is the GitHub repo the best place for feedback?"'
  duration: 3415
  has_captions: true
  language: en
  last_updated: '2026-11-14T05:08:23.669741+00:00'
  like_count: 13
  playlist: ''
  software:
  - bslib
  - rstudio
  - shiny-python
  - shiny-r
  tags: []
  thumbnail: https://i.ytimg.com/vi/m-EHamzqOZE/maxresdefault.jpg
  title: How can you build dynamic reactive inputs in Shiny? | Kyle Husmann | Data Science Lab
  url: https://www.youtube.com/watch?v=m-EHamzqOZE
  view_count: 949
---

