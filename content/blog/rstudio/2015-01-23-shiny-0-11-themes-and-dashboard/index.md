---
title: Shiny 0.11, themes, and dashboard
people:
  - Winston Chang
date: '2015-01-23'
categories:
- News
- Packages
- Shiny
slug: shiny-0-11-themes-and-dashboard
blogcategories:
- Products and Technology
- Company News and Events
- Open Source
tags:
- Packages
- Shiny
events: blog
ported_from: rstudio
port_status: raw
---


Shiny version 0.11 is available now! Notable changes include:

  * Shiny has migrated from Bootstrap 2 to Bootstrap 3 for its web front end. More on this below.

  * The old [jsliders](https://github.com/egorkhmelev/jslider) have been replaced with [ion.rangeSlider](https://github.com/IonDen/ion.rangeSlider). These sliders look better, are easier for users to interact with, and support updating more fields from the server side.

  * There is a new `passwordInput()` which can be used to create password fields.

  * New `observeEvent()` and `eventReactive()` functions greatly streamline the use of `actionButton` and other inputs that act more like events than reactive inputs.

For a full set of changes, see the [NEWS](http://cran.rstudio.com/web/packages/shiny/NEWS) file. To install, run:

```r
install.packages("shiny")
```

We've also posted an [article](http://shiny.rstudio-staging.com/articles/upgrade-0.11.html) with notes on upgrading to 0.11.

#### Bootstrap 3 migration

In all versions of Shiny prior to 0.11, Shiny has used the Bootstrap 2 framework for its web front-end. Shiny generates HTML that is structured to work with Bootstrap, and this makes it easy to create pages with sidebars, tabs, dropdown menus, mobile device support, and so on.

The Bootstrap development team stopped development on the Bootstrap 2 series after version 2.3.2, which was released over a year ago, and has since focused their efforts on Bootstrap 3. The new version of Bootstrap builds on many of the same underlying ideas, but it also has many small changes – for example, many of the CSS class names have changed.

In Shiny 0.11, we've moved to Bootstrap 3. For most Shiny users, the transition will be seamless; the only differences you'll see are slight changes to fonts and spacing.

If, however, you customized any of your code to use features specific to Bootstrap 2, then you may need to update your code to work with Bootstrap 3 (see the [Bootstrap migration guide](http://getbootstrap.com/migration/) for details). If you don't want to update your code right away, you can use the [shinybootstrap2](https://github.com/rstudio/shinybootstrap2) package for backward compatibility with Bootstrap 2 – using it requires adding just two lines of code. If you do use shinybootstrap2, we suggest using it just as an interim solution until you update your code for Bootstrap 3, because Shiny development going forward will use Bootstrap 3.

Why is Shiny moving to Bootstrap 3? One reason is support: as mentioned earlier, Bootstrap 2 is no longer developed and is no longer supported. Another reason is that there is dynamic community of actively-developed Bootstrap 3 themes. (Themes for Bootstrap 2 also exist, but there is less development activity.) Using these themes will allow you to customize the appearance of a Shiny app so that it doesn't just look like... a Shiny app.

We've also created a package that make it easy to use Bootstrap themes: [shinythemes](http://rstudio.github.io/shinythemes/). Here's an example using the included Flatly theme:

![flatly](https://rstudioblog.files.wordpress.com/2015/01/flatly.png)

See the [shinythemes site](http://rstudio.github.io/shinythemes/) for more screenshots and instructions on how to use it.

We're also working on [shinydashboard](http://rstudio.github.io/shinydashboard/), a package that makes it easy to create dashboards. Here's an example dashboard that also uses the [leaflet](http://rstudio.github.io/leaflet/) package.

![buses](https://rstudioblog.files.wordpress.com/2015/01/buses.png)

The shinydashboard package still under development, but feel free to try it out and give us feedback.

