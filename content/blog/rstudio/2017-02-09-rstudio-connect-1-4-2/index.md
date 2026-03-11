---
title: RStudio Connect 1.4.2
people:
  - Jeff Allen
date: '2017-02-09'
categories:
- News
- RStudio Connect
tags:
- Connect
- R
- RStudio Connect
slug: rstudio-connect-1-4-2
blogcategories:
- Products and Technology
- Company News and Events
events: blog
ported_from: rstudio
port_status: raw
---


We're excited to announce the latest release of [RStudio Connect: version 1.4.2](https://www.rstudio.com/products/connect/). This release includes a number of notable features including an overhauled interface for parameterized R Markdown reports.

![Enhanced Parameterized R Markdown Reports](https://rstudioblog.files.wordpress.com/2017/02/screen-shot-2017-02-07-at-9-06-03-am.png)

<p class="caption">Enhanced Parameterized R Markdown Reports</p>

The most notable feature in this release is the ability to publish [parameterized R Markdown](https://rmarkdown.rstudio.com/developer_parameterized_reports.html) reports that are easier for anyone to customize. If you're unfamiliar, parameterized R Markdown reports allow you to inject input parameters into your R Markdown document to alter what analysis the report performs. The parameters of your R Markdown report are now visible on the left-hand sidebar, allowing users to easily tweak the inputs to the document and quickly view the output in the browser.

Users even have the opportunity to create private versions of the report which they can schedule to run again, email, or save and revisit in the browser. Of course, you can continue to use the wide variety of output formats (notebooks, dashboards, books, and others) while using parameterized R Markdown.

In addition to the parameterized report overhaul, there are some other notable features included in this release.

  * **Content private by default** - Content is set to private ("Just Me") by default. Users can still change the visibility of their content before publishing, as before.

  * **Execute R as the authenticated viewer** - You can now choose to have some applications execute their underlying R process as the authenticated viewer currently looking at the app. This allows applications to access any data or resource that the associated user has access to on the server. Requires PAM authentication. [More details here](http://docs.rstudio.com/connect/1.4.2/admin/process-management.html#process-management-runas-current).

Other important features include:

  * Show progress indicator when updating a report.

  * Users can now filter content to include only items that they can edit or view.

  * Users now only count against the named user license limit after they log in for the first time.

  * Added support for global "System Messages" that can display an HTML message to your users on the landing pages. [Details here](http://docs.rstudio.com/connect/1.4.2/admin/server-management.html#system-messages).

  * Updated packrat to gain more transparency on package build errors.

  * Updated the list of SSL ciphers to correspond with modern best-practices.

If you haven't yet had a chance to download and try [RStudio Connect](https://rstudio.com/products/connect) we encourage you to do so. RStudio Connect is the best way to share all the work that you do in R (Shiny apps, R Markdown documents, plots, dashboards, etc.) with collaborators, colleagues, or customers.

You can find more details or download a 45 day evaluation of the product at <https://www.rstudio.com/products/connect/>. Additional resources can be found below.

  * [RStudio Connect home page & downloads](https://www.rstudio.com/products/connect/)

  * [RStudio Connect Admin Guide](http://docs.rstudio.com/connect/admin/)

  * [What IT needs to know about RStudio Connect](https://www.rstudio.com/wp-content/uploads/2016/01/RSC-IT-Q-and-A.pdf)

  * [Pricing](https://www.rstudio.com/pricing/#ConnectPricing)

  * [An online preview of RStudio Connect](https://beta.rstudioconnect.com/connect/)

