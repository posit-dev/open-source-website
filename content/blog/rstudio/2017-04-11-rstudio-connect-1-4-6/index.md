---
title: RStudio Connect 1.4.6
people:
  - Jeff Allen
date: '2017-04-11'
categories:
- News
- RStudio Connect
tags:
- Connect
- R
- RStudio Connect
slug: rstudio-connect-1-4-6
blogcategories:
- Products and Technology
- Company News and Events
events: blog
ported_from: rstudio
port_status: in-progress
---


We're excited to announce the release of [RStudio Connect: version 1.4.6](https://www.rstudio.com/products/connect/). This is an incremental release which features significantly improved startup time and support for server-side Shiny bookmarks.

![Creating a server-side Shiny bookmark in RStudio Connect](https://rstudioblog.files.wordpress.com/2017/04/media-20170407.png)

**Improved Startup & Job Listing Time**

We now track R process jobs in the database which allows us to list and query jobs much more quickly. This decreases the startup time of the RStudio Connect service -- allowing even the busiest of servers to spin up in a matter of seconds. Additionally, operations that involve listing jobs such as viewing process logs for a particular application should be noticeably faster.

**Server-Side Shiny Bookmarks**

Shiny v0.14 introduced a feature by which users could [bookmark the current state of the application](https://shiny.rstudio.com/articles/bookmarking-state.html) by either encoding the state in the URL or saving the state to the server. As of this release, RStudio Connect now supports server-side bookmarking of Shiny applications.

Other notable changes this release:

  * BREAKING: Changed the default for `Authorization.DefaultUserRole` from `publisher` to `viewer`. New users will now be created with a `viewer` account until promoted. The [user roles](http://docs.rstudio.com/connect/1.4.5/admin/user-management.html#user-roles) documentation explains the differences. To restore the previous behavior, set `DefaultUserRole = publisher`. Because viewer users cannot be added as collaborators on content, this means that in order to add a remote user as a collaborator on content you must first create their account, then promote them to a publisher account.

  * Fixed a bug in the previous release that had broken `Applications.ViewerOnDemandReports` and `Applications.ViewerCustomizedReports`. These settings are again functional and allow you to manage the capabilities of a viewer of a parameterized report on the server.

  * Tune the number of concurrent processes to use when building R packages. This is controlled with the `Server.CompilationConcurrency` setting and passed as the value to the make flag `-jNUM`. The default is to permit four concurrent processes. Decrease this setting in low memory environments.

  * The `/etc/rstudio-connect/rstudio-connect.gcfg` file is installed with more restrictive permissions.

  * Log file downloads include a more descriptive file name by default. Previously, we used the naming convention `<jobId>.log`, which resulted in file names like `GBFCaiPE6tegbrEM.log`. Now, we use the naming convention `rstudio-connect.<appId>.<reportId>.<bundleId>.<jobType>.<jobId>.log`, which results in file names like `rstudio-connect.34.259.15.packrat_restore.GBFCaiPE6tegbrEM.log`.

  * Bundle the admin guide and user guide in the product. You can access both from the Documentation tab.

  * Implemented improved, pop-out filtering panel when filtering content, which offers a better experience on small/mobile screens.

  * Improvements to the parameterized report pane when the viewer does not have the authority to render custom versions of the document.

  * Database performance improvements which should improve performance in high-traffic environments.

> #### Upgrade Planning
> 
> The migration of jobs from disk to the database may take a few minutes. The server will be unavailable during this migration which will be performed the first time RStudio Connect v1.4.6 starts. Even on the busiest of servers we would expect this migration to complete in under 5 minutes.

If you haven't yet had a chance to download and try [RStudio Connect](https://rstudio.com/products/connect) we encourage you to do so. RStudio Connect is the best way to share all the work that you do in R (Shiny apps, R Markdown documents, plots, dashboards, etc.) with collaborators, colleagues, or customers.

You can find more details or download a 45 day evaluation of the product at <https://www.rstudio.com/products/connect/>. Additional resources can be found below.

  * [RStudio Connect home page & downloads](https://www.rstudio.com/products/connect/)

  * [RStudio Connect Admin Guide](http://docs.rstudio.com/connect/admin/)

  * [What IT needs to know about RStudio Connect](https://www.rstudio.com/wp-content/uploads/2016/01/RSC-IT-Q-and-A.pdf)

  * [Detailed news and changes between each version](http://docs.rstudio.com/connect/news/)

  * [Pricing](https://www.rstudio.com/pricing/#ConnectPricing)

  * [An online preview of RStudio Connect](https://beta.rstudioconnect.com/connect/)

