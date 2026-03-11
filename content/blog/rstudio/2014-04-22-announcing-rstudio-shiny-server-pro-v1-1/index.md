---
title: Announcing RStudio Shiny Server Pro v1.1
people:
  - Roger Oberg
date: '2014-04-22'
categories:
- News
- Shiny
tags:
- R
- shiny
- shiny server pro
- v1.1
- Shiny
slug: announcing-rstudio-shiny-server-pro-v1-1
blogcategories:
- Products and Technology
- Company News and Events
events: blog
ported_from: rstudio
port_status: raw
---


We are happy to announce the availability of v1.1 of [RStudio Shiny Server Pro](https://www.rstudio.com/shiny/server/), our commercial server for deploying [Shiny](https://shiny.rstudio.com/) applications.  In this release we took your feedback and made it easier for you to integrate Shiny Server Pro into your production environments.  With Shiny Server Pro v1.1 you now can:

  * Control access to your applications with Google Authentication (OAuth2).

  * Create sessions and authenticate with PAM ([auth_pam](http://rstudio.github.io/shiny-server/latest/#pam-authentication) and [pam_sessions_profile](http://rstudio.github.io/shiny-server/latest/#pam-sessions)).

  * Set the version of R that is used per application and/or per user

  * Customize page templates for directory listings and error pages.

  * Monitor service health and get additional metrics with a new health check endpoint.

  * Provide custom environment variables to a Shiny process using Bash profiles

  * Configure apps to run using the authenticated user's account with custom environment variables from Bash or PAM

  * Launch Shiny apps with a prefix command such as 'nice' allowing you to prioritize compute resources per application or  per user

If you haven't tried Shiny Server Pro yet, download a copy [here](https://www.rstudio.com/shiny/server/pro).

