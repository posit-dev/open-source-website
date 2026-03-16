---
title: Shiny Server (Pro) 1.5.6
people:
  - Alan Dipert
date: '2017-12-11'
slug: shiny-server-pro-1-5-6
categories:
- Shiny
tags:
- shiny server pro
- shiny
- Shiny
blogcategories:
- Products and Technology
events: blog
ported_from: rstudio
port_status: in-progress
---


[Shiny Server 1.5.6.875 and Shiny Server Pro 1.5.6.902 are now available.](https://www.rstudio.com/products/shiny/shiny-server/)

This release of Shiny Server Pro includes floating license support and Shiny Server contains a small enhancement to the way errors are displayed. We recommend upgrading at your earliest convenience.

### Shiny Server 1.5.6.875

* Use HTTPS for Google Fonts on error page, which resolves insecure content errors on some browser when run behind SSL.
(PR [#322](https://github.com/rstudio/shiny-server/pull/322))

### Shiny Server Pro 1.5.6.902

This release adds **floating license** support through the `license_type` configuration directive.
Full documentation can be found at [http://docs.rstudio.com/shiny-server/#floating-licenses](http://docs.rstudio.com/shiny-server/#floating-licenses).

Floating licensing allows you to run fully licensed copies of Shiny Server Pro easily in ephemeral instances, such as Docker containers, virtual machines, and EC2 instances. Instances don’t have to be individually licensed, and you don’t have to manually activate and deactivate a license in each instance. Instead, a lightweight license server distributes temporary licenses ("leases") to each instance, and the instance uses the license only while it’s running.

This model is perfect for environments in which Shiny Server Pro instances are frequently created and destroyed on demand, and only requires that you purchase a license for the maximum number of concurrent instances you want to run.
