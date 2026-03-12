---
title: RStudio Connect 1.7.8 - Put a pin in it!
people:
  - Sean Lopp
date: '2019-09-23'
slug: rstudio-connect-1-7-8-put-a-pin-in-it
categories:
- News
- RStudio Connect
tags:
- Connect
- RStudio Connect
blogcategories:
- Products and Technology
- Company News and Events
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: in-progress
---


This release adds new workflows for data scientists and improved production
settings for administrators. For data scientists, it used to be hard to use the
same data or R objects in different content, and even harder to update those
resources regularly. This release enables you to pin objects in Connect to solve
these challenges. For administrators, we've reduced the most common sources of
publishing failures and significantly improved error handling. All together,
version 1.7.8 makes it even easier for data scientist teams to share and
leverage their work with the enterprise.

## Updates for Users

### Experimental Support for [Pins](https://rstudio.github.io/pins)

{{< figure src="rsc-178-pins.png" alt= "Pins Support in RStudio Connect">}}

The [`pins`](https://rstudio.github.io/pins) R package provides a way for R
users to easily share resources using RStudio Connect. Your resources may be
text files (CSV, JSON, etc.), R objects (`.Rds`, `.Rda`, etc.), or any other
type of files you want to share. Sharing these files can be useful in many
situations, for example:

1. Multiple pieces of content require the same data. Rather than copying
   that data, each piece of content references a single source of truth hosted
   on RStudio Connect.

2. Content depends on processed datasets or model objects that need to be regularly updated.
   Rather than redeploying the content each time the information changes, use a
   pinned resource and update only the dataset or model. The update can be automated using a
   scheduled R Markdown document. Other deployed content will read the newest data on
   each run.

3. You need to share resources that aren't structured for traditional tools
   like databases. For example, models saved as R objects aren't easy to store
   in a database. Rather than using email or file systems to share these R objects,
   use RStudio Connect to host these resources as pins.

Refer to the [RStudio Connect user
guide](https://docs.rstudio.com/connect/1.7.8/user/pins.html) or the [pins website](https://rstudio.github.io/pins/articles/boards-rsconnect.html) for more
information.

### Example APIs for Model Serving 

{{< figure src="rsc-178-apis.gif" alt= "API Monitoring in RStudio Connect">}}

RStudio Connect makes it easy for data scientists to share models written in R
with other teams as RESTFul APIs. As part of the 1.7.8 release, we've expanded
our documentation to help teams approach model management with the following
examples:

1. The [end-to-end use](https://solutions.rstudio.com/model-management/overview/) of RStudio Connect to train, deploy, monitor, and A/B test a model. 

2. Add [additional logging](https://solutions.rstudio.com/examples/rest-apis-overview/#log-details-about-api-requests-and-responses) to API requests in order to track latency, performance, input parameters, and route popularity.

## Updates for Administrators

### Deployment Error Logging

{{< figure src="rsc-178-errors.png" alt= "Better Error Logs">}}

We've overhauled the RStudio Connect deployment process for R code. RStudio
Connect now captures errors and surfaces specific error codes and
recommendations. All publishing methods see these improvements including
push-button publishing, Git-backed deployment, or custom workflows using the
Connect Server API.

A glossary of the error codes and recommendations is available [here](https://docs.rstudio.com/connect/1.7.8/user/publishing.html#error-codes).

### R Package Repositories

By default, RStudio Connect attempts to install R packages from the package
repositories that were used in the development environment. In some cases, you
may wish to specify different behavior and tell RStudio Connect where it should
look for R packages:  

- Your developers install packages from a public CRAN mirror, but your production server must use an internal CRAN mirror.  
- You use an isolated network for your production server, so RStudio Connect can not access the package repository used on the development network.  
- You want to use RStudio Package Manager's package binaries in production.
 
The [Admin Guide](https://docs.rstudio.com/connect/1.7.8/admin/getting-started.html#getting-started-rspm) describes how to configure the package repositories RStudio Connect should use for R.

### Usage Scorecard and Feedback

{{< figure src="rsc-178-scorecard.png" alt= "Usage Scorecard in Connect">}}

Like you, we're committed to expanding the influence of data science in the
enterprise. A new usage scorecard on the Admin Dashboard's Metrics page helps
you understand how your team uses RStudio Connect and what additional
capabilities may be available. We have made it easy for you to share this
scorecard with RStudio, providing feedback that will help us further improve
RStudio Connect.

## Deprecations and Breaking Changes

- **SECURITY:** New Timeout Defaults -  The `Authentication.Lifetime` and `Authentication.Inactivity` settings have new default values that are in line with industry best practices. These settings control how frequently a user must refresh their log in to RStudio Connect. The new default values are shorter ensuring users are authenticated more frequently.

- **BREAKING CHANGE:** External Package Check - On start up, RStudio Connect now checks to ensure every R packages listed as external in the configuration file is available in every version of R on the system. Any missing packages will cause RStudio Connect to fail to start. This check prevents unexpected deployment and runtime failures for content. You can opt out of this check by setting `Packages.ExternalCheckIsFatal` to `false`.  

- **BREAKING CHANGE:** R Markdown Rendering Errors - R errors that occur during R Markdown rendering now stop the deployment process with an error. Previously, R errors would result in the error message being rendered as part of the document contents. The previous behavior can be restored by setting chunk options for the R code chunk in the Rmd file, e.g. `{r error=TRUE warning=TRUE}`.  

- **PLATFORM SUPPORT:** Trusty -  RStudio Connect 1.7.8 is the last release that will support Ubuntu 14.04 Trusty. Please refer to the [RStudio Platform Support](https://www.rstudio.com/about/platform-support/) policy for more information.  

- **PLATFORM SUPPORT:** REHL 8 -  RStudio Connect 1.7.8 is the first release to support Red Hat Enterprise Linux 8. Refer to the [RStudio Connect Admin Guide](https://docs.rstudio.com/connect/1.7.8/admin/getting-started.html#installation-redhat) for more information. 

- **BREAKING CHANGE:** These previously deprecated settings have been removed; see the [release notes](https://docs.rstudio.com/connect/news/) for more details: `LoadBalancing.EnforceMinRsconnectVersion`, `Applications.ExplicitPublishing`, `Authorization.UsersListingMinRole`, and `Password.UserInfoEditableBy`.  

- **DEPRECATIONS:** The following settings have been deprecated and will be removed in the next release; see the [release notes](https://docs.rstudio.com/connect/news/) for more details: `Applications.DisabledProtocols`, `OAuth2.AllowedDomains`, and `OAuth2.AllowedEmails`.  

Refer to the [full release notes](https://docs.rstudio.com/connect/news/) for
more information on all of the changes and bug fixes in this release.

## Upgrade Planning

> Please take special note of the breaking changes above, especially the new check
> for external packages. Aside from the deprecations and breaking changes above,
> there are no other special considerations and upgrading should require less than
> five minutes. If you are upgrading from an earlier version, be sure to consult
> the release notes for the intermediate releases, as well.

## Get Started with RStudio Connect

If you haven't yet had a chance to download and try [RStudio
Connect](https://rstudio.com/products/connect/), we encourage you to do so.
RStudio Connect is the best way to share all the work that you do in R (Shiny
apps, R Markdown documents, plots, dashboards, Plumber APIs, etc.) with
collaborators, colleagues, or customers.

You can find more details or download a 45-day evaluation of the product at
[https://www.rstudio.com/products/connect/](https://www.rstudio.com/products/connect/).
Additional resources can be found below.

- [RStudio Connect home page & downloads](https://www.rstudio.com/products/connect/)
- [RStudio Connect Administration Guide](http://docs.rstudio.com/connect/admin/)
- [Detailed news and changes between each version](http://docs.rstudio.com/connect/news/)
- [Pricing](https://www.rstudio.com/pricing/)

