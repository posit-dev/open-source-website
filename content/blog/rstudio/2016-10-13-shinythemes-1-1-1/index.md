---
title: shinythemes 1.1.1
people:
  - Winston Chang
date: '2016-10-13'
slug: shinythemes-1-1-1
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


If there's one word that could describe the default styling of Shiny applications, it might be "minimalist." Shiny's UI components are built using the Bootstrap web framework, and unless the appearance is customized, the application will be mostly white and light gray.

Fortunately, it's easy to add a bit of flavor to your Shiny application, with the [shinythemes](https://rstudio.github.io/shinythemes/) package. We've just released version 1.1.1 of shinythemes, which includes many new themes from [bootswatch.com](http://bootswatch.com/), as well as a theme selector which you can use to test out different themes on a live Shiny application.

Here's an example of the theme selector in use (try out the app [here](https://gallery.shinyapps.io/117-shinythemes/)):

![theme-selector](https://rstudioblog.files.wordpress.com/2016/10/theme-selector.gif)

* * *

To install the latest version of shinythemes, run:

```r
install.packages("shinythemes")
```

To use the theme selector, all you need to do is add this somewhere in your app's UI code:

```r
shinythemes::themeSelector()
```

Once you've chosen which theme you want, all you need to do is use the `theme` argument of the `bootstrapPage`, `fluidPage`, `navbarPage`, or `fixedPage` functions. If you want to use "cerulean", you would do this:

```r
fluidPage(theme = shinytheme("cerulean"),
  ...
)
```

To learn more and see screenshots of the different themes, visit the [shinythemes web page](https://rstudio.github.io/shinythemes/). Enjoy!

