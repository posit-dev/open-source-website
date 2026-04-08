---
title: Design patterns for action buttons
description: "New Shiny article: five design patterns for action buttons using observeEvent() and eventReactive()."
auto-description: true
people:
  - Garrett Grolemund
date: '2015-04-07'
categories:
  - Interactive Apps
tags:
  - Article
  - Shiny
  - RStudio
slug: design-patterns-for-action-buttons
blogcategories:
  - Products and Technology
  - Open Source
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
ported_categories:
  - Shiny
---


![action-button](https://rstudioblog.files.wordpress.com/2015/04/action-button.png)

Action buttons can be tricky to use in Shiny because they work differently than other widgets. Widgets like sliders and select boxes maintain a value that is easy to use in your code. But the value of an action button is arbitrary. What should you do with it? Did you know that you should almost always call the value of an action button from `observeEvent()` or `eventReactive()`?

The newest article at the [Shiny Development Center](https://shiny.rstudio.com/articles/action-buttons.html) explains how action buttons work, and it provides five useful patterns for working with action buttons. These patterns also work well with action links.

Read the article [here](https://shiny.rstudio.com/articles/action-buttons.html).

