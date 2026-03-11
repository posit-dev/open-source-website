---
title: 'RStudio v0.99 Preview: Code Diagnostics'
people:
  - RStudio Team
date: '2015-04-28'
categories:
- RStudio IDE
slug: rstudio-v0-99-preview-code-diagnostics
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: raw
---


In RStudio v0.99 we've made a major investment in R source code analysis. This work resulted in significant improvements in [code completion](https://blog.rstudio.com/2015/02/23/rstudio-v0-99-preview-code-completion/), and in the latest [preview release](https://www.rstudio.com/products/rstudio/download/preview/) enable a new inline code diagnostics feature that highlights various issues in your R code as you edit.

For example, here we're getting a diagnostic that notes that there is an extra parentheses:

![Screen Shot 2015-04-08 at 12.04.14 PM](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-08-at-12-04-14-pm.png)

Here the diagnostic indicates that we've forgotten a comma within a shiny UI definition:

![diagnostics-comma](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-28-at-11-29-46-am.png)

This diagnostic flags an unknown parameter to a function call:

![Screen Shot 2015-04-08 at 11.50.07 AM](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-08-at-11-50-07-am.png)

This diagnostic indicates that we've referenced a variable that doesn't exist and suggests a fix based on another variable in scope:

![Screen Shot 2015-04-08 at 4.23.49 PM](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-08-at-4-23-49-pm.png)

A wide variety of diagnostics are supported, including optional diagnostics for code style issues (e.g. the inclusion of unnecessary whitespace). Diagnostics are also available for several other languages including C/C++, JavaScript, HTML, and CSS.

### Configuring Diagnostics

By default, code in the current source file is checked whenever it is saved, as well as if the keyboard is idle for a period of time. You can tweak this behavior using the **Code** -> **Diagnostics** options:

![diagnostics-options](https://rstudioblog.files.wordpress.com/2015/04/screen-shot-2015-04-28-at-11-37-34-am.png)

Note that several of the available diagnostics are disabled by default. This is because we're in the process of refining their behavior to eliminate "false negatives" where correct code is flagged as having a problem. We'll continue to improve these diagnostics and enable them by default when we feel they are ready.

### Trying it Out

You can try out the new code diagnostics by downloading the latest [preview release](https://www.rstudio.com/products/rstudio/download/preview/) of RStudio. This feature is a work in progress and we're particularly interested in feedback on how well it works. Please also let us know if there are common coding problems which you think we should add new diagnostics for. We hope you try out the preview and [let us know](https://support.rstudio.com/) how we can make it better.

