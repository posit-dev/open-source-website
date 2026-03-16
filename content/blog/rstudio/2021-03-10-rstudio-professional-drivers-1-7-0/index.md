---
title: "RStudio Professional Drivers 1.7.0"
people:
  - Ricardo Andrade
  - Nathan Stephens
date: '2021-03-10'
slug: pro-drivers-1-7-0-release
description: Announcing the 1.7.0 release of the RStudio Professional Drivers, which includes security updates, a preview release of the Snowflake driver, an updated Oracle driver, and other changes.
categories:
  - News
  - RStudio IDE
  - RStudio Connect
tags:
  - security
  - data
  - data science
  - drivers
  - dplyr
  - databases
alttext: a photo of a race car driver smiling in his car
blogcategories:
- Company News and Events 
- Products and Technology
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: in-progress
---

Data security is a strategic imperative in most organizations. In a world where data is under constant threat of malicious attacks, the security of your data pipeline is critical. One of the easiest ways to keep your data secure is by applying the latest software updates to your systems. This release of the [RStudio Professional Drivers](https://rstudio.com/products/drivers/) contains important updates that will help keep your data connections secure and easy to manage. Updating the drivers literally takes minutes and can help prevent future security and administrative issues. *We strongly encourage all customers to upgrade to the 1.7.0 release of the RStudio Professional Drivers*.

RStudio offers ODBC database drivers to all current customers using our professional products at no additional charge, so that data scientists and organizations can take full advantage of their data. The drivers are an important part of our effort to promote [interoperability](https://blog.rstudio.com/2020/07/15/interoperability-maximize-analytic-investments/) between systems and data science languages like R and Python. All our drivers are commercially licensed and covered by our support program. For a full list of changes in this release refer to the [release notes](https://docs.rstudio.com/drivers/1.7.0/release-notes/).

## Introducing the Snowflake driver

This release of the drivers includes a preview of the Snowflake driver. Snowflake is a popular "data warehouse-as-a-service" that runs in the cloud. This preview release provides full ODBC support for Snowflake, but offers limited capabilities with certain packages like `dbplyr`. We will make another announcement when the Snowflake driver is ready for all types of workloads.

## MongoDB security updates

For those using MongoDB, we strongly recommend you upgrade your driver. A security vulnerability was found in the [Schema Editor](https://www.simba.com/products/MongoDB/doc/v2/SchemaEditor_UserGuide/content/schemaeditor/3.0/intro.htm), which enables users to create and modify schema definitions for NoSQL data stores. As a result, we will no longer ship the Schema Editor with the MongoDB driver. We encourage all customers to upgrade this driver even if they are not using the Schema Editor. For those who are not able to upgrade we recommend [uninstalling the MongoDB driver](https://support.rstudio.com/hc/en-us/articles/360063916613).

## Updating Oracle Instant Client

The latest Oracle driver depends on Oracle Instant Client version 19.x, whereas the previous Oracle driver depends on version 12.x. If you are connecting to Oracle you **must** upgrade. Please follow the installation instructions in our [docs](https://docs.rstudio.com/pro-drivers/installation/). Note that the Oracle Instant Client is a dependency you license and install directly from Oracle.

## An early notice on driver deprecations

When vendors end support for databases, RStudio also ends support for those databases. You can receive email notifications for upcoming deprecations by subscribing to *Product Information* in the [RStudio subscription management](https://rstudio.com/about/subscription-management/) portal. Be aware that the following databases will no longer be supported in upcoming years: Oracle 12.2 (March 2022); and Netezza (April 2023).






