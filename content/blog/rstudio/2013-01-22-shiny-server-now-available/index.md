---
title: Shiny Server now available
people:
  - Joe Cheng
date: '2013-01-22'
categories:
  - Interactive Apps
slug: shiny-server-now-available
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Shiny
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
ported_categories:
  - Shiny
---


[Shiny](http://rstudio.com/shiny/) makes it easy to develop interactive web applications that run on your own machine. But by itself, it isn't designed to make your applications available to all comers over the internet (or intranet). You can't run more than one Shiny application on the same port, and if your R process crashes or exits for any reason, your service becomes unavailable.

Our solution is Shiny Server, the application server for Shiny. Using Shiny Server, you can host multiple Shiny applications, as well as static web content, on a Linux server and make them available over the internet. You can specify what applications are available at what URL, or configure Shiny Server to let anyone with a user account on the server deploy their own Shiny applications. For more details, see our [previous blog post](https://blog.rstudio.com/2012/12/04/shiny-update/).

**Shiny Server is available as a public beta today.** Follow the instructions on [our GitHub project page](https://github.com/rstudio/shiny-server#shiny-server) to get started now!

