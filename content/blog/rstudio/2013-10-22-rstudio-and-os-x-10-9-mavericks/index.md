---
title: RStudio and OS X 10.9 Mavericks
people:
  - RStudio Team
date: '2013-10-22'
categories:
- RStudio IDE
slug: rstudio-and-os-x-10-9-mavericks
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: in-progress
---


**UPDATE**: [RStudio OS X Mavericks Issues Resolved](https://blog.rstudio.com/2013/11/12/rstudio-os-x-mavericks-issues-resolved/)

This post is now out of date (see link above for information on getting a version of RStudio that works with OS X Mavericks).

* * *

Today Apple released [OS X 10.9 "Mavericks"](http://www.apple.com/osx/). If you are a Mac user and considering updating to the new OS  there are some RStudio compatibility issues to consider before you update.

As a result of a problem between Mavericks and the user interface toolkit underlying RStudio ([Qt](http://qt-project.org/)) the RStudio IDE is very slow in painting and user interactions  when running under Mavericks. We are following up with both Qt and Apple on resolving the compatibility issue. In the meantime there is a workaround available in the v0.98.443 release of RStudio that can be downloaded here:

<https://www.rstudio.com/ide/download/preview>

This version of RStudio detects when it is running on OS X Mavericks and in that case bypasses the use of Qt. Rather, a version of RStudio Server is run locally and connected to by a special RStudioIDE browser window. There are several differences you'll notice when running in this mode:

  1. Only one instance of RStudio can be run at a time.

  2. The Mac native menubar is not used. Rather, the main menu appears inside the RStudio frame.

  3. Mac native file open and save dialogs are not used. Rather, internal versions of the dialogs are used.

  4. Finder file associations activate RStudio however don't open the targeted file(s).

  5. The copy plot to clipboard function is not available.

  6. During a shutdown of Mac OS X when RStudio is running the current project's Workspace is not saved automatically (however source files are).

We're hoping that the underlying problem in OS X 10.9 is resolved in a future update or alternatively the Qt toolkit is updated to address the issue. If and when that occurs we'll release a new version of RStudio that restores the previous RStudio behavior on OS X 10.9.

