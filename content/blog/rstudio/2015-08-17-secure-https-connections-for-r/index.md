---
title: Secure HTTPS Connections for R
people:
  - RStudio Team
date: '2015-08-17'
categories:
- News
- RStudio IDE
slug: secure-https-connections-for-r
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: in-progress
---


Traditionally, the mechanisms for obtaining R and related software have used standard HTTP connections. This isn't ideal though, as without a secure (HTTPS) connection there is less assurance that you are downloading code from a legitimate source rather than from another server posing as one.

Recently there have been a number of changes that make it easier to use HTTPS for installing R, RStudio, and packages from CRAN:

  1. Downloads of R from the main CRAN website now use HTTPS;

  2. Downloads of RStudio from our website now use HTTPS; and

  3. It is now possible to install packages from CRAN over HTTPS.

There are a number of ways to ensure that installation of packages from CRAN are performed using HTTPS. The [most recent version of R](https://cran.rstudio.com/)  (v3.2.2) makes this the default behavior. The [most recent version of RStudio](https://www.rstudio.com/products/rstudio/download/) (v0.99.473) also attempts to configure secure downloads from CRAN by default (even for older versions of R). Finally, any version of R or RStudio can use secure HTTPS downloads by making some configuration changes as described in the [Secure Package Downloads for R](https://support.rstudio.com/hc/en-us/articles/206827897) article in our Knowledge Base.

## Configuring Secure Connections to CRAN

While the simplest way to ensure secure connections to CRAN is to run the updated versions mentioned above, it's important to note that it is **not necessary to upgrade R or RStudio** to achieve this end. Rather, two configuration changes can be made:

  1. The R `download.file.method` option needs to specify a method that is capable of HTTPS; and

  2. The CRAN mirror you are using must be capable of HTTPS connections (not all of them are).

The specifics of the required changes for various products, platforms, and versions of R are described in-depth in the [Secure Package Downloads for R](https://support.rstudio.com/hc/en-us/articles/206827897) article in our Knowledge Base.

## Recommendations for RStudio Users

We've made several changes to RStudio IDE to ensure that HTTPS connections are used throughout the product:

  1. The default `download.file.method` option is set to an HTTPS compatible method (with a warning displayed if a secure method can't be set);

  2. The configured CRAN mirror is tested for HTTPS compatibility and a warning is displayed if the mirror doesn't support HTTPS;

  3. HTTPS is used for user selection of a non-default CRAN mirror;

  4. HTTPS is used for in-product documentation links;

  5. HTTPS is used when checking for updated versions of RStudio (applies to desktop version only); and

  6. HTTPS is used when downloading [Rtools](https://cran.r-project.org/bin/windows/Rtools/) (applies to desktop version only).

If you are running RStudio on the desktop we strongly recommend that you [update to the latest version](https://www.rstudio.com/products/rstudio/download/) (v0.99.473).

## Recommendations for Server Administrators

If you are running RStudio Server it's possible to make the most important security enhancements by changing your configuration rather than updating to a new version. The [Secure Package Downloads for R](https://support.rstudio.com/hc/en-us/articles/206827897) article in our Knowledge Base provides documentation on how do this.

In this case in-product documentation links and user selection of a non-default CRAN mirror will continue to use HTTP rather than HTTPS however these are less pressing concerns than CRAN package installation. If you'd like these functions to also be performed over HTTPS then you should upgrade your server to the [latest version](https://www.rstudio.com/products/rstudio/download/) of RStudio.

If you are running Shiny Server we recommend that you modify your configuration to support HTTPS package downloads as described in the [Secure Package Downloads for R](https://support.rstudio.com/hc/en-us/articles/206827897) article.

