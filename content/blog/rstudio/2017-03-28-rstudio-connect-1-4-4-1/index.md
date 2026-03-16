---
title: RStudio Connect 1.4.4.1
people:
  - Jeff Allen
date: '2017-03-28'
categories:
- News
- RStudio Connect
tags:
- Connect
- R
- RStudio Connect
slug: rstudio-connect-1-4-4-1
blogcategories:
- Products and Technology
- Company News and Events
events: blog
ported_from: rstudio
port_status: in-progress
---


We're excited to announce the release of [RStudio Connect: version 1.4.4.1](https://www.rstudio.com/products/connect/). This release includes the ability to manage different versions of your work on RStudio Connect.

![Managing old versions of deployed content in RStudio Connect](https://rstudioblog.files.wordpress.com/2017/03/screen-shot-2017-03-27-at-4-55-53-pm.png)

**Rollback / Roll Forward**
The most notable feature of this release is the ability to "rollback" to a previously deployed version of your work or "roll forward" to a more recent version of your work.

You can also download a particular version, perhaps as a starting place for a new report or application, and delete old versions that you want to remove from the server.

Other important features allow you to:

  * Specify the number of versions to retain. You can alter the setting `Applications.BundleRetentionLimit` to specify how many versions of your applications you want to keep on disk. By default, we retain all bundles eternally.

  * Limit the number of scheduled reports that will be run concurrently using the `Applications.ScheduleConcurrency` setting. This setting will help ensure that your server isn't overwhelmed by too many reports all scheduled to run at the same time of day. The default is set to 2.

  * Create a printable view of your content with a new "Print" menu option.

  * Notify users of unsaved changes before they take an action in parameterized reports.

The release also includes numerous security and stability improvements.

If you haven't yet had a chance to download and try [RStudio Connect](https://rstudio.com/products/connect) we encourage you to do so. RStudio Connect is the best way to share all the work that you do in R (Shiny apps, R Markdown documents, plots, dashboards, etc.) with collaborators, colleagues, or customers.

You can find more details or download a 45 day evaluation of the product at <https://www.rstudio.com/products/connect/>. Additional resources can be found below.

  * [RStudio Connect home page & downloads](https://www.rstudio.com/products/connect/)

  * [RStudio Connect Admin Guide](http://docs.rstudio.com/connect/admin/)

  * [What IT needs to know about RStudio Connect](https://www.rstudio.com/wp-content/uploads/2016/01/RSC-IT-Q-and-A.pdf)

  * [Detailed news and changes between each version](http://docs.rstudio.com/connect/news/)

  * [Pricing](https://www.rstudio.com/pricing/#ConnectPricing)

  * [An online preview of RStudio Connect](https://beta.rstudioconnect.com/connect/)

