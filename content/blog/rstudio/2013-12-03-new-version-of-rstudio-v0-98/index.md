---
title: New Version of RStudio (v0.98)
people:
  - RStudio Team
date: '2013-12-03'
categories:
- RStudio IDE
slug: new-version-of-rstudio-v0-98
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: in-progress
---


We're pleased to announce that the final version of RStudio v0.98 is [available for download](https://www.rstudio.com/ide/download) now. Highlights of the new release include:

  * An [interactive debugger](https://www.rstudio.com/ide/docs/debugging/overview) for R that is tightly integrated with base R debugging tools (browser, recover, etc.)

  * Numerous improvements to the Workspace pane (which is now called the Environment pane).

  * [R Presentations](https://www.rstudio.com/ide/docs/presentations/overview) for easy authoring of HTML5 presentations that include R code, output, and graphics.

  * A new [Viewer pane](https://www.rstudio.com/ide/docs/advanced/viewer_pane) for displaying local web content (e.g. graphical output from packages like googleVis).

  * Additional support for developing and running [Shiny](https://www.rstudio.com/shiny) web applications.

  * Substantially improved UI performance on Mac OS X.

  * A [Professional Edition](https://www.rstudio.com/ide/server/) of RStudio Server with many new capabilities for enterprise deployment.

There are also lots of smaller improvements and bug fixes across the product, check out the [release notes](https://www.rstudio.com/ide/docs/release_notes_v0.98.html) for full details.

### Debugging Tools

The feature we're most excited about is the addition of a full interactive debugger to the IDE. Noteworthy capabilities of the debugger include:

  * Setting breakpoints within the source editor, both inside and outside functions

  * Stepping through code line by line

  * Inspecting object values and the call stack during debugging

  * An error inspector for quick access to tracebacks and the debugger after runtime errors

  * Tight integration with traditional R debugging tools, such as `browser()` and `debug()`

Here's a screenshot of the IDE after hitting an editor breakpoint:

![RStudioDebugger](https://rstudioblog.files.wordpress.com/2013/09/rstudiodebugger.png)

For more details on how to take advantage of the new debugging tools, see [Debugging with RStudio](https://www.rstudio.com/ide/docs/debugging/overview).

### Environment Pane

The Workspace pane is now called the Environment pane and has numerous improvements, including:

  * Browse any environment on the search path

  * Filtering by name/value

  * Expand lists, data frames, and S4 objects inline

  * Use `str()` to display object values

  * Optional grid view sortable by various attributes

  * Many other small correctness and robustness enhancements

### R Presentations

R Presentations enable easy authoring of HTML5 presentations. R Presentations are based on [R Markdown](https://www.rstudio.com/ide/docs/authoring/using_markdown.html), and include the following features:

  * Easy authoring of HTML5 presentations based on [R Markdown](https://www.rstudio.com/ide/docs/authoring/using_markdown.html)

  * Extensive support for authoring and previewing inside the IDE

  * Many options for customizing layout and appearance

  * Publishing as either a standalone HTML file or to [RPubs](http://rpubs.com/)

Here's a screenshot showing a simple presentation being authored and previewed within the IDE:

![RPresentations](https://rstudioblog.files.wordpress.com/2013/09/rpresentations1.png)

For more details see the documentation on [Authoring R Presentations](https://www.rstudio.com/ide/docs/presentations/overview).

### Viewer Pane

RStudio now includes a Viewer pane that can be used to view local web content. This includes both static web content or even a local web application created using [Shiny](https://www.rstudio.com/shiny), [Rook](http://cran.rstudio.com/web/packages/Rook/index.html), or [OpenCPU](https://public.opencpu.org/). This is especially useful for packages that have R bindings to Javascript data visualization libraries.

The [googleVis](http://lamages.blogspot.com/2013/11/googlevis-047-with-rstudio-integration.html) and [rCharts](http://www.youtube.com/watch?v=wi2fUKqHtpM) packages have already been updated to take advantage of the Viewer pane. Here's a screenshot of the googleVis integration:

![googleVis](https://rstudioblog.files.wordpress.com/2013/11/googlevis1.png)

We're hopeful that there will be many more compelling uses of the Viewer. For more details see the article [Extending RStudio with the Viewer Pane](https://www.rstudio.com/ide/docs/advanced/viewer_pane).

### Shiny Integration

We've added a number of features to support development of [Shiny](https://www.rstudio.com/shiny/) web applications, including:

  * The ability to develop and run Shiny applications on RStudio Server (localhost and websocket proxying is handled automatically)

  * Running Shiny applications within an IDE pane (see the discussion of the Viewer pane below for details)

  * Create a new Shiny application from within the New Project dialog

  * Debugging of Shiny applications using the new RStudio debugging tools.

### Mac UI Framework

In RStudio v0.98 we also migrated our Mac [WebKit](http://en.wikipedia.org/wiki/WebKit) engine from a cross-platform framework (Qt) to [Cocoa](http://en.wikipedia.org/wiki/Cocoa_(API)). The original motivation for this was compatibility problems between Qt and OS X Mavericks, but as it turned out the move to Cocoa WebKit yielded substantially faster editor, scrolling, layout, and graphics performance across the board. If you are a Mac user you'll find everything about the product snappier in v0.98.

In the next major version of RStudio we're hoping to make comparable improvements in performance on both Linux and Windows by using a more modern WebKit on those platforms as well.

### RStudio Server Professional Edition

Over the years we've gotten lots of feedback from larger organizations deploying RStudio Server on the features they'd like to see for production deployments of the server. With RStudio v0.98 we're introducing a new Professional Edition of RStudio Server that incorporates much of this feedback. Highlights include:

  * An administrative dashboard that provides insight into active sessions, server health, and monitoring of system-wide and per-user performance and resource metrics.

  * Authentication using system accounts, ActiveDirectory, LDAP, or Google Accounts.

  * Full support for PAM (including PAM sessions for dynamically provisioning user resources).

  * Ability to establish per-user or per-group CPU priorities and memory limits.

  * HTTP enhancements including support for SSL and keep-alive for improved performance.

  * Ability to restrict access to the server by IP.

  * Customizable server health checks.

  * Suspend, terminate, or assume control of user sessions.

  * Impersonate users for assistance and troubleshooting.

The RStudio Server product page has [full details](https://www.rstudio.com/ide/server/) on the Professional Edition, and an [evaluation version](https://www.rstudio.com/ide/download/server-pro-evaluation.html) of the server is also available for download.

### New Support Site

With this release we're also introducing a brand new support and documentation website, please [visit us](http://support.rstudio.com) there with questions, feedback, as well as what other improvements you'd like to see in the product.

