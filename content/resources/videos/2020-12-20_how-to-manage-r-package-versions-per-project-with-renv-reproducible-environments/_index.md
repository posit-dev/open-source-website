---
date: '2020-12-20'
description: 'renv gives every R project its own package library and a lockfile recording the exact version of everything in it. Without that, all your projects share one library, so updating a package for one project silently changes the others, and code that ran last year stops running. renv init sets a project up, renv snapshot records the current state to renv.lock, and renv restore rebuilds that exact state on another machine or at a later date. With Kevin Ushey, who maintains the package.


  What you will learn

  - Why an R project that worked six months ago stops working

  - What Packrat did, and what renv changed

  - How R decides where to look for a package, and what a library path is

  - Why one shared library across every project causes the problem

  - What renv init does to a project

  - What renv snapshot records, and what a lockfile actually contains

  - How renv restore rebuilds an environment somewhere else

  - How the global package cache avoids storing the same package many times


  Chapters

  0:00 What this talk covers

  0:40 The problem: why an R project breaks later

  1:17 What Packrat was, and what it taught us

  4:08 How R finds packages: the lay of the land

  5:13 What a library path is

  8:13 The challenge: one library, many projects

  10:01 The solution: a project library and a lockfile

  10:51 Initialising renv in a project

  13:09 Saving and loading the project state

  13:41 snapshot: recording what you have

  14:42 What a lockfile records, with an example

  15:56 restore: rebuilding the environment

  17:48 The global package cache

  19:15 How package installation works with renv


  Learn more

  renv: https://rstudio.github.io/renv/

  Introduction to renv: https://rstudio.github.io/renv/articles/renv.html

  Posit Package Manager: https://posit.co/products/enterprise/package-manager/


  Recorded in 2020. renv is actively maintained and the workflow shown is current.'
image: thumbnail.jpg
people:
- Kevin Ushey
resource_type: video
resources: []
software:
- packrat
- renv
- rstudio
tags:
- renv
- renv r
- r package versions
- reproducible environment r
- r project environment
- renv lockfile
- renv snapshot
- renv restore
- package management r
- packrat
- reproducibility in r
- kevin ushey
- posit
title: 'How to Manage R Package Versions per Project with renv: Reproducible Environments'

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 13
  date: '2020-12-20T08:00:13Z'
  definition: hd
  description: 'renv gives every R project its own package library and a lockfile recording the exact version of everything in it. Without that, all your projects share one library, so updating a package for one project silently changes the others, and code that ran last year stops running. renv init sets a project up, renv snapshot records the current state to renv.lock, and renv restore rebuilds that exact state on another machine or at a later date. With Kevin Ushey, who maintains the package.


    What you will learn

    - Why an R project that worked six months ago stops working

    - What Packrat did, and what renv changed

    - How R decides where to look for a package, and what a library path is

    - Why one shared library across every project causes the problem

    - What renv init does to a project

    - What renv snapshot records, and what a lockfile actually contains

    - How renv restore rebuilds an environment somewhere else

    - How the global package cache avoids storing the same package many times


    Chapters

    0:00 What this talk covers

    0:40 The problem: why an R project breaks later

    1:17 What Packrat was, and what it taught us

    4:08 How R finds packages: the lay of the land

    5:13 What a library path is

    8:13 The challenge: one library, many projects

    10:01 The solution: a project library and a lockfile

    10:51 Initialising renv in a project

    13:09 Saving and loading the project state

    13:41 snapshot: recording what you have

    14:42 What a lockfile records, with an example

    15:56 restore: rebuilding the environment

    17:48 The global package cache

    19:15 How package installation works with renv


    Learn more

    renv: https://rstudio.github.io/renv/

    Introduction to renv: https://rstudio.github.io/renv/articles/renv.html

    Posit Package Manager: https://posit.co/products/enterprise/package-manager/


    Recorded in 2020. renv is actively maintained and the workflow shown is current.'
  duration: 1250
  has_captions: false
  language: ''
  last_updated: '2026-11-12T12:18:01.684986+00:00'
  like_count: 251
  people:
  - Kevin Ushey
  playlist: ''
  software:
  - packrat
  - renv
  - rstudio
  tags:
  - renv
  - renv r
  - r package versions
  - reproducible environment r
  - r project environment
  - renv lockfile
  - renv snapshot
  - renv restore
  - package management r
  - packrat
  - reproducibility in r
  - kevin ushey
  - posit
  thumbnail: https://i.ytimg.com/vi/yjlEbIDevOs/hqdefault.jpg
  title: 'How to Manage R Package Versions per Project with renv: Reproducible Environments'
  url: https://www.youtube.com/watch?v=yjlEbIDevOs
  view_count: 9098
---
image: thumbnail.jpg

