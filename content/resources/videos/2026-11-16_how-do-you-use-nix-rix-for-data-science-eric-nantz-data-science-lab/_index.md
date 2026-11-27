---
date: '2026-11-16'
description: 'You can use the {rix} R package as a bridge to Nix, allowing you to define a safe, sandboxed environment using familiar R syntax rather than mastering Nix’s complex DSL (domain-specific language)!


  The Data Science Lab is a live weekly call. Register at pos.it/dslab! Discord invites go out each week on lives calls. We''d love to have you! It''s is an open, messy space for learning and asking questions. Think of it like pair coding with a friend or two. Learn something new, and share what you know to help others grow.


  On this Lab, Eric Nantz, Senior Directory - Innovation Statistics at Eli Lilly & Company, showcases how the {rix} R package, alongside Nix, empowers a data scientist to create reproducible, isolated, and efficient analytical environments.


  NOTE! Eric had some technical difficulties during this recording, so please give us some grace! There are a couple of times where he drops off Zoom because his system crashes (which has nothing to do with Nix or rix, we promise!), but you can follow the timestamps below to get back on track.


  Hosting crew from Posit: Libby Heeren, Isabella Velásquez

  Recorded: September 1, 2026


  Eric Nantz''s socials and urls:


  - Bluesky: https://bsky.app/profile/rpodcast.bsky.social

  - Mastodon: https://podcastindex.social/@rpodcast

  - LinkedIn: https://www.linkedin.com/in/eric-nantz-6621617/

  - GitHub: https://github.com/rpodcast

  - R-Podcast: https://r-podcast.org

  - R Weekly Highlights Podcast: https://serve.podhome.fm/r-weekly-highlights

  - Shiny Developer Series: https://shinydevseries.com


  Resources mentioned in video and/or the chat:


  - NixOS lab management example (nixos-lab): https://github.com/giovantenne/nixos-lab

  - DINUM (France) is switching to NixOS: https://discourse.nixos.org/t/dinum-france-is-switching-to-nixos/77558

  - devenv.sh: https://devenv.sh/

  - Eric''s Nix/{rix} talk from R/Medicine: https://www.youtube.com/watch?v=-NARVwViEwA

  - Slides for Eric''s Nix/{rix} talk: https://rpodcast.github.io/rixshiny-rmed2025/#/title-slide

  - Zero to Nix: https://zero-to-nix.com/

  - What is Nix (Shopify Engineering): https://shopify.engineering/what-is-nix

  - What is Nix (Serokell): https://serokell.io/blog/what-is-nix

  - xkcd: Dependency comic: https://xkcd.com/2347/


  Timestamps:


  00:00 Introduction

  03:04 "Why do we need reproducible environments?"

  05:42 What is Nix?

  06:40 Introducing the {rix} R package

  07:49 Demo: Project-specific R workflows with Nix

  09:05 R Weekly Quarto calendar dashboard demo

  11:15 Declaring dependencies in R with rix()

  12:57 Generating the default.nix configuration file

  15:38 "Does this work with Positron?"

  15:46 "Can you add packages to the environment later?"

  17:06 "Who would find rix most useful?"

  19:57 Building the environment with nix-build

  21:14 Entering the sandbox with nix-shell

  22:20 Connecting IDEs like Positron and VS Code to the Nix shell

  23:57 "How does this work with Quarto and R/Python code chunks?"

  26:22 "Does rix handle transitive dependencies?"

  27:54 The Nix store and immutable packages

  28:50 "What does this mean for packages that are not on CRAN?"

  30:55 Deploying with GitHub Actions and Nix

  31:58 Zoom drop

  35:40 Eric returns!

  34:28 Comparing Nix and rix to renv, arv, and uvr

  40:07 "What is the status of Nix on Windows?"

  41:52 "Are dev containers analogous to Docker?"

  43:27 Zoom drop 2

  45:27 Eric returns again!

  43:48 Using dev containers in Positron

  45:04 "What are your opinions on rix versus devenv.sh?"

  45:53 Collaborating and deploying projects with Nix

  48:29 Bit-for-bit reproducibility: Nix vs. renv restore

  52:01 "Is it harder to use packages that are not on CRAN?"

  54:26 "Can arv and rix be installed on the same system, or do they conflict?"

  55:30 Comparing rix, devenv, and direnv

  57:42 Wrap-up and mentioning Bioconductor packages'
image: thumbnail.jpg
people:
- Isabella Velásquez
resource_type: video
resources: []
software:
- positron
- quarto
- renv
- shiny-r
tags: []
title: How do you use Nix & rix for data science? | Eric Nantz | Data Science Lab

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 2
  date: '2026-11-16T16:00:09Z'
  definition: hd
  description: 'You can use the {rix} R package as a bridge to Nix, allowing you to define a safe, sandboxed environment using familiar R syntax rather than mastering Nix’s complex DSL (domain-specific language)!


    The Data Science Lab is a live weekly call. Register at pos.it/dslab! Discord invites go out each week on lives calls. We''d love to have you! It''s is an open, messy space for learning and asking questions. Think of it like pair coding with a friend or two. Learn something new, and share what you know to help others grow.


    On this Lab, Eric Nantz, Senior Directory - Innovation Statistics at Eli Lilly & Company, showcases how the {rix} R package, alongside Nix, empowers a data scientist to create reproducible, isolated, and efficient analytical environments.


    NOTE! Eric had some technical difficulties during this recording, so please give us some grace! There are a couple of times where he drops off Zoom because his system crashes (which has nothing to do with Nix or rix, we promise!), but you can follow the timestamps below to get back on track.


    Hosting crew from Posit: Libby Heeren, Isabella Velásquez

    Recorded: September 1, 2026


    Eric Nantz''s socials and urls:


    - Bluesky: https://bsky.app/profile/rpodcast.bsky.social

    - Mastodon: https://podcastindex.social/@rpodcast

    - LinkedIn: https://www.linkedin.com/in/eric-nantz-6621617/

    - GitHub: https://github.com/rpodcast

    - R-Podcast: https://r-podcast.org

    - R Weekly Highlights Podcast: https://serve.podhome.fm/r-weekly-highlights

    - Shiny Developer Series: https://shinydevseries.com


    Resources mentioned in video and/or the chat:


    - NixOS lab management example (nixos-lab): https://github.com/giovantenne/nixos-lab

    - DINUM (France) is switching to NixOS: https://discourse.nixos.org/t/dinum-france-is-switching-to-nixos/77558

    - devenv.sh: https://devenv.sh/

    - Eric''s Nix/{rix} talk from R/Medicine: https://www.youtube.com/watch?v=-NARVwViEwA

    - Slides for Eric''s Nix/{rix} talk: https://rpodcast.github.io/rixshiny-rmed2025/#/title-slide

    - Zero to Nix: https://zero-to-nix.com/

    - What is Nix (Shopify Engineering): https://shopify.engineering/what-is-nix

    - What is Nix (Serokell): https://serokell.io/blog/what-is-nix

    - xkcd: Dependency comic: https://xkcd.com/2347/


    Timestamps:


    00:00 Introduction

    03:04 "Why do we need reproducible environments?"

    05:42 What is Nix?

    06:40 Introducing the {rix} R package

    07:49 Demo: Project-specific R workflows with Nix

    09:05 R Weekly Quarto calendar dashboard demo

    11:15 Declaring dependencies in R with rix()

    12:57 Generating the default.nix configuration file

    15:38 "Does this work with Positron?"

    15:46 "Can you add packages to the environment later?"

    17:06 "Who would find rix most useful?"

    19:57 Building the environment with nix-build

    21:14 Entering the sandbox with nix-shell

    22:20 Connecting IDEs like Positron and VS Code to the Nix shell

    23:57 "How does this work with Quarto and R/Python code chunks?"

    26:22 "Does rix handle transitive dependencies?"

    27:54 The Nix store and immutable packages

    28:50 "What does this mean for packages that are not on CRAN?"

    30:55 Deploying with GitHub Actions and Nix

    31:58 Zoom drop

    35:40 Eric returns!

    34:28 Comparing Nix and rix to renv, arv, and uvr

    40:07 "What is the status of Nix on Windows?"

    41:52 "Are dev containers analogous to Docker?"

    43:27 Zoom drop 2

    45:27 Eric returns again!

    43:48 Using dev containers in Positron

    45:04 "What are your opinions on rix versus devenv.sh?"

    45:53 Collaborating and deploying projects with Nix

    48:29 Bit-for-bit reproducibility: Nix vs. renv restore

    52:01 "Is it harder to use packages that are not on CRAN?"

    54:26 "Can arv and rix be installed on the same system, or do they conflict?"

    55:30 Comparing rix, devenv, and direnv

    57:42 Wrap-up and mentioning Bioconductor packages'
  duration: 3541
  has_captions: true
  language: en
  last_updated: '2026-11-27T05:09:08.518909+00:00'
  like_count: 20
  people:
  - Isabella Velásquez
  playlist: ''
  software:
  - positron
  - quarto
  - renv
  - shiny-r
  tags: []
  thumbnail: https://i.ytimg.com/vi/YXSSgnhnJ1M/maxresdefault.jpg
  title: How do you use Nix & rix for data science? | Eric Nantz | Data Science Lab
  url: https://www.youtube.com/watch?v=YXSSgnhnJ1M
  view_count: 1900
---

