---
title: Package Manager 1.1.0.1 Patch Release
people:
  - Sean Lopp
date: '2019-11-26'
slug: package-manager-1-1-0-1-patch-release
categories:
- RStudio Package Manager
- News
tags:
- rspm
- RStudio Package Manager
blogcategories:
- Products and Technology
- Company News and Events
events: blog
ported_from: rstudio
port_status: in-progress
---


Earlier this month we [announced RStudio Package Manager version 1.1.0](https://blog.rstudio.com/2019/11/07/package-manager-v1-1-no-interruptions/), a major
update to RStudio Package Manager that added support for:

- Faster package installs on Linux with pre-compiled binaries  
- Easier installs through the display of system requirements  
- A calendar of repository checkpoints to make it easier to reproduce work  

This patch release updates the 1.1.0 version without introducing any new
features. The 1.1.0.1 patch fixes a bug in the prior release that impacts
performance when serving binary packages from historical checkpoints. There is
also a small chance that an incorrect historical binary could be served
under specific repository and source configurations. These problems were
discovered internally, and no customers reported any impact.

> #### Patch Instructions
> We strongly encourage all customers using version 1.1.0 to apply the patch by
simply by installing version 1.1.0.1 on top of the existing
1.1.0 release.

If you are upgrading from an earlier version, be sure to consult the [release notes](https://doc.rstudio.com/rspm/news) for the intermediate releases, as well.

#### New to RStudio Package Manager? 

[Download](https://rstudio.com/products/package-manager/) the 45-day evaluation
today to see how RStudio Package Manager can help you, your team, and your
entire organization access and organize R packages. Learn more with our [online
demo server](https://demo.rstudiopm.com) or [latest webinar](https://resources.rstudio.com/webinars/introduction-to-the-rstudio-package-manager-sean-lopp).

- [Admin Guide](https://docs.rstudio.com/rspm/admin)
- [Overview PDF](https://www.rstudio.com/wp-content/uploads/2018/07/RStudio-Package-Manager-Overview.pdf)
- [Introductory Webinar](https://resources.rstudio.com/webinars/introduction-to-the-rstudio-package-manager-sean-lopp)
- [Online Demo](https://demo.rstudiopm.com)
