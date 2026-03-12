---
title: Shiny 0.10.1
people:
  - Yihui Xie
date: '2014-08-01'
categories:
- Packages
- Shiny
tags:
- shiny
- Unicode
- UTF-8
- Packages
- Shiny
slug: shiny-0-10-1
blogcategories:
- Products and Technology
- Open Source
events: blog
ported_from: rstudio
port_status: in-progress
---


[Shiny v0.10.1](http://cran.rstudio.com/package=shiny) has been released to CRAN. You can either install it from a CRAN mirror, or update it if you have installed a previous version.

```r
install.packages('shiny', repos = 'http://cran.rstudio.com')
# or update your installed packages
# update.packages(ask = FALSE, repos = 'http://cran.rstudio.com')
```

The most prominent change in this patch release is that we added full Unicode support on Windows. Shiny apps running on Windows must use the UTF-8 encoding for ui.R and server.R (also the optional global.R, README.md, and DESCRIPTION) if they contain non-ASCII characters. See this article for details and [examples](https://shiny.rstudio.com/gallery/unicode-characters.html): <https://shiny.rstudio.com/articles/unicode.html>

![Chinese characters in a shiny app](https://shiny.rstudio.com/gallery/images/screenshots/unicode-characters.png)

<p class="caption">Chinese characters in a shiny app</p>

Please note although we require UTF-8 for the app components, UTF-8 is not a general requirement for any other files. If you read/write text files in an app, you are free to use any encoding you want, e.g. you can `readLines('foo.txt', encoding = 'Windows-1252')`. The article above has explained it in detail.

Other changes include:

  * `runGitHub()` also allows the `'username/repo'` syntax now, which is equivalent to `runGitHub('repo', 'username')`. ([#427](https://github.com/rstudio/shiny/issues/427))

  * `navbarPage()` now accepts a `windowTitle` parameter to set the web browser page title to something other than the title displayed in the navbar.

  * Added an `inline` argument to `textOutput()`, `imageOutput()`, `plotOutput()`, and `htmlOutput()`. When `inline = TRUE`, these outputs will be put in `span()` instead of the default `div()`. This occurs automatically when these outputs are created via the inline expressions (e.g. ``r renderText(expr)``) in R Markdown documents. See an R Markdown example at <https://shiny.rstudio.com/gallery/inline-output.html> ([#512](https://github.com/rstudio/shiny/pull/512))

  * Added support for option groups in the select/selectize inputs. When the `choices` argument for `selectInput()`/`selectizeInput()` is a list of sub-lists and any sub-list is of length greater than 1, the HTML tag `<optgroup>` will be used. See an example at [here](https://shiny.rstudio.com/gallery/option-groups-for-selectize-input.html) ([#542](https://github.com/rstudio/shiny/pull/542))

Please let us know if you have any [comments](https://groups.google.com/forum/#!forum/shiny-discuss) or [questions](http://stackoverflow.com/questions/tagged/shiny).

