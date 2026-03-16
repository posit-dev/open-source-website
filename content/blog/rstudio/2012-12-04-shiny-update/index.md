---
title: An update on Shiny
people:
  - Joe Cheng
date: '2012-12-04'
categories:
- Shiny
slug: shiny-update
blogcategories:
- Products and Technology
- Open Source
tags:
- Shiny
events: blog
ported_from: rstudio
port_status: in-progress
---


Last month we released [Shiny](https://www.rstudio.com/shiny/), our new R package for creating interactive web applications. The response from the community has been extremely encouraging--we've received a lot of great feedback that has helped us to make significant improvements to the framework already!

#### Shiny 0.2.3 on CRAN

Starting with Shiny 0.2.3, you can install the latest stable version of Shiny directly from CRAN. Since the initial release, we've added some interesting features to Shiny, most notably the ability to offer [on-the-fly file downloads](http://rstudio.github.com/shiny/tutorial/#downloads). We've also fixed some bugs, including an issue with runGist that caused it to fail on many Windows systems.

Install or upgrade now by running: `install.packages('shiny')`

#### Coming soon: Shiny Server

While Shiny works great today for running apps on your own machine, we indicated in our original blog post that for web-based deployment we'd be offering hosting services and a software package for deploying Shiny applications on a server.

Today we have more details to share about Shiny Server, the software package which will allow you to deploy Shiny applications on your own server:

  * Free and open source ([AGPLv3](http://www.gnu.org/licenses/agpl-3.0.txt) license)

  * Host multiple applications on the same port, with a different URL path per application

  * Allows Shiny applications to work with Internet Explorer 8 and 9

  * Automatically starts and stops R sessions as needed

  * Detects and recovers from crashed R sessions

  * Designed to serve applications directly to browsers, or be proxied behind another web server like Apache/Nginx

  * Works across network gateways and proxies that don't support websockets

Our goal is to begin beta testing by the end of January. Shiny Server will require Linux at launch, though we will likely add Windows and Mac support later.

While we previously said that Shiny Server would be commercial software, we've decided to make it free and open source instead. Later in 2013 we hope to introduce a paid edition of Shiny Server that will include additional features that are targeted at larger organizations.

That's all we have on the Shiny front for now. If you have questions, leave us a comment, or drop by our active and growing community at [shiny-discuss](https://groups.google.com/group/shiny-discuss)!

