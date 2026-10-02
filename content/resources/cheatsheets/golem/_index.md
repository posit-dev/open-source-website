---
title: golem
image: page-1.png
resource_type: cheatsheet
by: community
date: '2019-06-01'
description: Build, maintain, and deploy production-grade Shiny applications as R packages using the golem framework.
download_url: golem.pdf
thumbnails:
- page-1.png
languages:
- R
---

golem is an opinionated framework for creating robust Shiny applications structured as R packages. It scaffolds a standardized project layout and provides helper functions across the full development lifecycle: initial setup, day-to-day module and asset development, and deployment to multiple targets.

## What's covered
- Create a golem – via RStudio New Project wizard or `golem::create_golem()`
- Set up your golem – `fill_desc()`, `set_golem_options()`, recommended tests and dependencies
- Launch and inspect the app – `dev/run_dev.R`, `document_and_reload()`
- Customise – add Shiny modules (`add_module()`), JS files, CSS files, built-in JS functions
- Exhibit your golem locally – `remotes::install_local()`
- Deploy to RStudio products – `add_rstudioconnect_file()`, `add_shinyappsio_file()`
- Deploy with Docker – `add_dockerfile()`, `add_dockerfile_shinyproxy()`
- Tips and tricks – `print_dev()`, `make_dev()`, `browser_button()`
