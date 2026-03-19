---
title: shinydashboard 0.6.0
people:
  - Bárbara Borges Ribeiro
date: '2017-05-18'
slug: shinydashboard-0-6-0
blogcategories:
- Products and Technology
- Open Source
tags:
- Shiny
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
categories:
  - Interactive Apps
ported_categories:
  - Packages
  - Shiny
---


Shinydashboard 0.6.0 is now on CRAN! This release of shinydashboard was aimed at both fixing bugs and also bringing the package up to speed with users' requests and Shiny itself (especially fully bringing [bookmarkable state](https://shiny.rstudio.com/articles/bookmarking-state.html) to shinydashboard's sidebar). In addition to bug fixes and new features, we also added a [new "Behavior" section](https://rstudio.github.io/shinydashboard/behavior.html) to the [shinydashboard website](https://rstudio.github.io/shinydashboard/) to explain this release's two biggest new features, and also to provide users with more material about shinydashboard-specific behavior.

## Sidebar

This release introduces two new sidebar inputs. One of these inputs reports whether the sidebar is collapsed or expanded, and the other input reports which (if any) menu item in the side bar is expanded. In the screenshot below, the Charts tab is expanded.

![](https://rstudioblog.files.wordpress.com/2017/05/sidebar-expanded.png)

These inputs are unusual since they're automatically available without you needing to declare them, and they have a fixed name. The first input is accessible via `input$sidebarCollapsed` and can have only two values: `TRUE`, which indicates that the sidebar is collapsed, and `FALSE`, which indicates that it is expanded (default).

The second input is accessible via `input$sidebarItemExpanded`. If no `menuItem()` in the sidebar is currently expanded, the value of this input is `NULL`. Otherwise, `input$sidebarItemExpanded` holds the value of the `expandedName` of whichever `menuItem()` is currently expanded (`expandedName` is a new argument to `menuItem()`; if none is provided, shinydashboard creates a sensible default).

## Full changes

As usual, you can view the full changelog for shinydashboard in the [NEWS](https://github.com/rstudio/shinydashboard/blob/v0.6.0/NEWS.md) file.

