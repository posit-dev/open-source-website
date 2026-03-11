---
title: RStudio OS X Mavericks Issues Resolved
people:
  - RStudio Team
date: '2013-11-12'
categories:
- RStudio IDE
slug: rstudio-os-x-mavericks-issues-resolved
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: raw
---


When OS X Mavericks was released last month we were very disappointed to discover a compatibility issue between [Qt ](http://qt-project.org/)(our cross-platform user interface toolkit) and OS X Mavericks that resulted in extremely poor graphics performance.

We now have an updated preview version of RStudio for OS X (v0.98.475) that not only overcomes these issues, but also improves editor, scrolling, and layout performance across the board on OS X (more details below if you are curious):

<https://www.rstudio.com/ide/download/preview>

We were initially optimistic that we could patch Qt to overcome the problems but even with some help from Digia (the organization behind Qt) we never got acceptable performance. Running out of viable options based on Qt, we decided to bypass Qt entirely by implementing the RStudio desktop frame as a native [Cocoa](https://developer.apple.com/technologies/mac/cocoa.html) application.

OS X Mavericks issues aside, we are thrilled with the result of using Cocoa rather than a cross-platform toolkit. RStudio desktop uses [WebKit](http://www.webkit.org/) to render its user-interface, and the Cocoa [WebKit Framework](https://developer.apple.com/library/mac/documentation/cocoa/reference/webkit/objc_classic/_index.html) is substantially faster than the one in Qt.

Please try out the updated preview and let us know if you encounter any issues or problems on our [support forum](http://support.rstudio.org). For those that prefer to wait for the final release of v0.98 we expect that to happen sometime during the next couple of weeks.

