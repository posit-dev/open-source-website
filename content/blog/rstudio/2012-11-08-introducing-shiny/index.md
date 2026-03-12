---
title: 'Introducing Shiny: Easy web applications in R'
people:
  - Joe Cheng
date: '2012-11-08'
categories:
- Shiny
slug: introducing-shiny
blogcategories:
- Products and Technology
- Open Source
tags:
- Shiny
events: blog
ported_from: rstudio
port_status: in-progress
---


Say hello to [Shiny](https://www.rstudio.com/shiny/), a new R package that we're releasing for public beta testing today.

**Shiny makes it super simple for R users to turn analyses into interactive web applications that anyone can use.** These applications let you specify input parameters using friendly controls like sliders, drop-downs, and text fields; and they can easily incorporate any number of outputs like plots, tables, and summaries.

No HTML or JavaScript knowledge is necessary. If you have some experience with R, you're just minutes away from combining the statistical power of R with the simplicity of a web page:

![Shiny application screenshot](https://rstudioblog.files.wordpress.com/2012/11/heightweight.png)

More details, including live examples and a link to an extensive tutorial, can be found on the [Shiny homepage](https://www.rstudio.com/shiny/).

The Shiny package is free and open source, and is designed primarily to run Shiny applications locally. To share Shiny applications with others, you can send them your application source as a GitHub gist, R package, or zip file (see [details](http://rstudio.github.com/shiny/tutorial/#deployment)). We're also working on a Shiny server that is designed to provide enterprise-grade application hosting, which we'll offer as a subscription-based hosting service and/or commercial software package.

We're really excited about Shiny, and look forward to seeing what kind of applications you come up with!

(Special thanks to [Bryan Lewis](http://illposed.net) for authoring the [websockets](http://cran.r-project.org/web/packages/websockets/index.html) package, which is used heavily by Shiny.)

[Shiny homepage](https://www.rstudio.com/shiny/)

