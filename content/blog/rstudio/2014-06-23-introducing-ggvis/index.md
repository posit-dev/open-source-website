---
title: Introducing ggvis
people:
  - Winston Chang
date: '2014-06-23'
categories:
- Packages
- Shiny
slug: introducing-ggvis
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
- Shiny
events: blog
ported_from: rstudio
port_status: in-progress
---


Our first public release of [ggvis](http://ggvis.rstudio.com/), version 0.3, is now available on CRAN. What is ggvis? It's a new package for data visualization. Like ggplot2, it is built on concepts from the grammar of graphics, but it also adds interactivity, a new data pipeline, and it renders in a web browser. Our goal is to make an interface that's flexible, so that you can compose new kinds of visualizations, yet simple, so that it's accessible to all R users.

**Update:** there was an issue affecting interactive plots in version 0.3. Version 0.3.0.1 fixes the issue. The updated source package is now on CRAN, and Windows and Mac binary packages will be available shortly.

![ggvis_movies](https://rstudioblog.files.wordpress.com/2014/06/ggvis_movies.gif)

ggvis integrates with Shiny, so you can use dynamic, interactive ggvis graphics in Shiny applications. We hope that the combination of ggvis and Shiny will make it easy for you to create applications for interactive data exploration and presentation. ggvis plots are inherently reactive and they render in the browser, so they can take advantage of the capabilities provided by modern web browsers. You can use Shiny's interactive components for interactivity as well as more direct forms of interaction with the plot, such as hovering, clicking, and brushing.

ggvis works seamlessly with [R Markdown v2](/2014/06/18/r-markdown-v2/) and [interactive documents](/2014/06/19/interactive-documents-an-incredibly-easy-way-to-use-shiny/), so you can easily add interactive graphics to your R Markdown documents:

![shiny-doc-ggvis](https://rstudioblog.files.wordpress.com/2014/06/shiny-doc-ggvis1.png)  ![ggvis_density](https://rstudioblog.files.wordpress.com/2014/06/ggvis_density.gif)

And don't worry -- ggvis isn't only meant to be used with Shiny and interactive documents. Because the RStudio IDE is also a web browser, ggvis plots can display in the IDE, like any other R graphics:

![ggvis in RStudio IDE](https://rstudioblog.files.wordpress.com/2014/06/ggvis-screenshot.png)

There's much more to come with ggvis. To learn more, visit the [ggvis website](http://ggvis.rstudio.com/).

Please note that ggvis is still young, and lacks a number of important features from ggplot2. But we're working hard on ggvis and expect many improvements in the months to come.

