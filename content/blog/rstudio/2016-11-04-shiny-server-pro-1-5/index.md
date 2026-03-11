---
title: Shiny Server (Pro) 1.5
people:
  - Joe Cheng
date: '2016-11-04'
categories:
- Shiny
slug: shiny-server-pro-1-5
blogcategories:
- Products and Technology
tags:
- Shiny
events: blog
ported_from: rstudio
port_status: raw
---


[Shiny Server 1.5.1.834 and Shiny Server Pro 1.5.1.760 are now available.](https://www.rstudio.com/products/shiny/shiny-server/)

The Shiny Server 1.5.x release family upgrades our underlying Node.js engine from 0.10.47 to 6.9.1. The impetus for this change was not stability or performance, but because the 0.10.x release family has reached the end of its life.

We highly recommend that you test on a staging server before upgrading production Shiny Server 1.4.x machines to 1.5. You should always do this for any production-critical software, but it's particularly important for this release, due to the magnitude of changes to Node.js that we've absorbed in one big gulp. (We've done thorough end-to-end testing of this release, but there's no substitute for testing with your own apps, on your own servers.)

Some small bug fixes are also included in this release. See the [release notes](https://support.rstudio.com/hc/en-us/articles/215642837-Shiny-Server-Pro-Release-History) for more details.

#### The beginning of the end for Ubuntu 12.04 and Red Hat 5

While we still support Ubuntu 12.04 and Red Hat 5 today, we'll be moving on from these very old releases in a few months. Both of these distributions will end-of-life in April 2017, and will stop receiving bug fixes and security fixes from their vendors at that time. If you're using Shiny Server with one of these platforms, we recommend that you start planning your upgrade.

