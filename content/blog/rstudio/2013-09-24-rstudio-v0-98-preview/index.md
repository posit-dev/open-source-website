---
title: RStudio v0.98 Preview (Debugging Tools and More)
people:
  - RStudio Team
date: '2013-09-24'
categories:
- RStudio IDE
slug: rstudio-v0-98-preview
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: in-progress
---


We're very pleased to announce that a [preview release](https://www.rstudio.com/ide/download/preview) of RStudio IDE v0.98 is available for download now. Major highlights of the new release include debugging tools, many improvements to environment/workspace browsing, and a new way to create HTML5 presentations using R Markdown. As usual there are also many small improvements and bug fixes. We'll talk about some of the more interesting new features below, otherwise check out the [release notes](https://www.rstudio.com/ide/docs/release_notes_v0.98.html) for full details.

### Debugging Tools

We've done lots of work to add R debugging tools to the IDE, including:

  * Setting breakpoints within the source editor, both inside and outside functions

  * Stepping through code line by line

  * Inspecting object values and the call stack during debugging

  * An error inspector for quick access to tracebacks and the debugger after runtime errors

  * Tight integration with traditional R debugging tools, such as `browser()` and `debug()`

Here's a screenshot of the IDE after hitting an editor breakpoint:

![RStudioDebugger](https://rstudioblog.files.wordpress.com/2013/09/rstudiodebugger.png)

Note that execution is stopped at the specified breakpoint, the environment is updated to show the objects within the context where execution was stopped, and commands for line by line stepping, continuing, and aborting the debug session appear in the console.

For more details on how to take advantage of the new tools, see [Debugging with RStudio](https://www.rstudio.com/ide/docs/debugging/overview).

### R Presentations

R Presentations enable easy authoring of HTML5 presentations. R Presentations are based on [R Markdown](https://www.rstudio.com/ide/docs/authoring/using_markdown.html), and include the following features:

  * Easy authoring of HTML5 presentations based on [R Markdown](https://www.rstudio.com/ide/docs/authoring/using_markdown.html)

  * Extensive support for authoring and previewing inside the IDE

  * Many options for customizing layout and appearance

  * Publishing as either a standalone HTML file or to [RPubs](http://rpubs.com/)

Here's a screenshot showing a simple presentation being authored and previewed within the IDE:

![RPresentations](https://rstudioblog.files.wordpress.com/2013/09/rpresentations1.png)

For more details see the documentation on [Authoring R Presentations](https://www.rstudio.com/ide/docs/presentations/overview).

### RStudio Server Pro

With RStudio v0.98 we've added a new Professional Edition of RStudio Server.  New features in RStudio Server Pro include:

  * An administrative dashboard that provides insight into active sessions, server health, and monitoring of system-wide and per-user performance and resource metrics.

  * Authentication using system accounts, ActiveDirectory, LDAP, or Google Accounts.

  * Full support for PAM (including PAM sessions for dynamically provisioning user resources).

  * Ability to establish per-user or per-group CPU priorities and memory limits.

  * HTTP enhancements including support for SSL and keep-alive for improved performance.

  * Ability to restrict access to the server by IP.

  * Customizable server health checks.

  * Suspend, terminate, or assume control of user sessions.

  * Impersonate users for assistance and troubleshooting.

The Professional Edition also includes priority support and a commercial license. You can get more details as well as download a free 45-day evaluation version from the [RStudio Server Professional Preview](https://www.rstudio.com/ide/download/pro-preview) page.

### What's Next

The [preview release](https://www.rstudio.com/ide/download/preview) is feature complete and we expect to release the final version of v0.98 during the next few weeks. After that we'll be focusing on adding features to make it easier to develop and deploy [Shiny web applications](https://www.rstudio.com/shiny/) and expect another release with those features before the end of the year.

