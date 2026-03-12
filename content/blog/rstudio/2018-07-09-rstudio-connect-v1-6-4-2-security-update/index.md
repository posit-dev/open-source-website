---
title: RStudio Connect v1.6.4.2 - Security Update
people:
  - Jeff Allen
date: '2018-07-09'
slug: rstudio-connect-v1-6-4-2-security-update
categories:
- RStudio Connect
- News
tags:
- Connect
- Security
- R
- RStudio Connect
blogcategories:
- Products and Technology
- Company News and Events
events: blog
ported_from: rstudio
port_status: in-progress
---


A security vulnerability in a third-party library used by RStudio Connect was uncovered during a security audit last week. We have confirmed that this vulnerability has not been used against any of the RStudio Connect instances we host, and are unaware of it being exploited on any customer deployments. Under certain conditions, this vulnerability could compromise the session of a user that was tricked into visiting a specially crafted URL. The issue affects all versions of RStudio Connect up to and including 1.6.4.1, but none of our other products. We have prepared a hotfix: [v1.6.4.2](https://www.rstudio.com/products/connect/).

RStudio remains committed to providing the most secure product possible. We regularly perform internal security audits against RStudio Connect in order to ensure the product’s security.

As part of the responsible disclosure process, we will provide additional details about the vulnerability and how to ensure that you have not been affected, in the coming weeks once customers have had time to update their systems. For now, **please update your RStudio Connect installations to version 1.6.4.2 as soon as possible**.

