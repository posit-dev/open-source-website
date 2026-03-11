---
title: Announcing RStudio Professional Drivers
people:
  - Nathan Stephens
date: '2017-10-16'
slug: announcing-rstudio-professional-drivers
categories:
- News
- Shiny
- RStudio IDE
- RStudio Connect
tags:
- data
- data science
- Workbench
- Shiny Server Pro
- RStudio
- drivers
- dplyr
- databases
- RStudio Connect
- RStudio IDE
- Shiny
blogcategories:
- Products and Technology
- Company News and Events
events: blog
ported_from: rstudio
port_status: raw
---


Today we are excited to announce the availability of [RStudio Professional Drivers](https://www.rstudio.com/products/drivers/). There are, of course, many ways to connect to [Databases using R](http://db.rstudio.com). RStudio Professional Drivers are specifically intended for use with our professional products, including [RStudio Server Pro](https://www.rstudio.com/products/rstudio-server-pro/), [Shiny Server Pro](https://www.rstudio.com/products/shiny-server-pro/), and [RStudio Connect](https://www.rstudio.com/products/connect/). These data connectors combined with enhancements to [dplyr](http://dplyr.tidyverse.org/), the [odbc](https://github.com/rstats-db/odbc) package, and the [RStudio IDE](https://blog.rstudio.com/2017/08/16/rstudio-preview-connections/) provide a comprehensive suite of tools for accessing and analyzing data with your enterprise systems.

## Connect to popular data sources

[RStudio Professional Drivers](https://www.rstudio.com/products/drivers/) help you connect to some of the most popular databases. Available for download today are ODBC drivers for Microsoft SQL Server, Oracle, PostgreSQL, Apache Hive, Apache Impala, and Salesforce. We will add several more drivers over the coming months. Don’t see your database listed? Please contact our [sales team](https://rstudio.youcanbook.me/) to let us know what you would like us to add.

<img src="/blog-images/2017-09-08-driver-logos.png" alt="RStudio Professional Driver Logos" style="width: 70%"/>

## Professional advantages 

[RStudio Professional Drivers](https://www.rstudio.com/products/drivers/) are intended for customers who need standards-based, supported data connectors that are easy to install and work with our professional products. They provide the following advantages:

* __Professional__. We deliver professional ODBC drivers that are supported along with our pro products. Use these drivers when you run R and Shiny with your production systems.
* __Coverage__. We connect you to some of the most popular databases available today, and we are committed to increasing the number of data connectors we support in the future.
* __Consistency__. Use the same data connectors everywhere you use RStudio professional products. Develop and publish your content with the same set of data connectors systemwide.
* __Convenience__. Our drivers are easy to install and designed to work with our products. This means no more headaches trying to configure third party drivers and packages with your system.

## Using RStudio Server Pro

If you are an existing customer, you can use [RStudio Professional Drivers](https://www.rstudio.com/products/drivers/) with your current version of [RStudio Server Pro](https://www.rstudio.com/products/rstudio-server-pro/). The latest version of RStudio Server Pro (v1.1) has integrated support for using these drivers with [Data Connections]({{< relref "2017-08-16-rstudio-preview-connections.md" >}}). When you install the drivers onto your server, [RStudio Server Pro](https://www.rstudio.com/products/rstudio-server-pro/) will automatically discover your drivers and populate the Connections wizard. Once you establish a connection you can browse your data source catalog and schema in the Connections tab.

<img src="/blog-images/2017-08-16-connection_create.png" alt="RStudio Connection wizard" style="width: 70%"/>

## Using RStudio Connect and Shiny Server Pro

Many Shiny applications and R Markdown documents are designed with database backends. With [RStudio Professional Drivers](https://www.rstudio.com/products/drivers/) you can develop and publish your content using the same data connectors systemwide. These drivers also ensure that your production ready applications are backed by professional software and support. Use these drivers when you run Shiny in production with [Shiny Server Pro](https://www.rstudio.com/products/shiny-server-pro/) or [RStudio Connect](https://www.rstudio.com/products/connect/).

## Using our open source products

[RStudio Professional Drivers](https://www.rstudio.com/products/drivers/) are intended for customers who need supported data connectors that are easy to install and work with our professional products. But alternative options exist for various data sources. The [RStudio IDE](https://blog.rstudio.com/2017/08/16/rstudio-preview-connections/), the [odbc](https://github.com/rstats-db/odbc) package, and [dplyr](http://dplyr.tidyverse.org/) will still work when you bring your own ODBC driver. To learn more about best practices when using data connectors, see our new website, [Databases using R](http://db.rstudio.com).

_If you are a current customer or if you are evaluating RStudio professional products, you can download [RStudio Professional Drivers](https://www.rstudio.com/products/drivers/) today for no additional charge. If you are interested to learn more about how RStudio professional products can help you and your organization, please contact our [sales team](https://rstudio.youcanbook.me/) for more information or email us at info@rstudio.com._

