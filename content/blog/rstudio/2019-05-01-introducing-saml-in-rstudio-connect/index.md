---
title: Introducing SAML in RStudio Connect
people:
  - Sean Lopp
date: '2019-05-14'
slug: introducing-saml-in-rstudio-connect
categories:
- RStudio Connect
- News
tags:
- Connect
- RStudio Connect
blogcategories:
- Products and Technology
- Company News and Events
events: blog
nohero: true
ported_from: rstudio
port_status: raw
---


RStudio Connect 1.7.4 builds off of the prior release with significant improvements for RStudio Connect administrators. SAML support is available for production, a new admin view of scheduled reports helps identify potential conflicts, additional server APIs support deployment workflows, and our email configuration has been completely re-vamped.

{{< figure src="/blog/images/rsc-174-schedules.png" caption="View Scheduled Content" alt= "View Scheduled Content">}}

## Scheduled Content Calendar

This release includes a new calendar view, pictured above, that helps administrators review all scheduled content in a single place. This view can help administrators identify reports that are running too frequently, or times when multiple reports have overlapping schedules; e.g., Monday at 9am.

## SAML Support

We are very excited to announce the release of SAML 2.0 as a production authentication method for RStudio Connect. This opens the door for integration with common identity providers in the enterprise, along with single-sign-on, multi-factor authentication, and other important security conventions.

As a part of this release, we prepared SAML integration templates to simplify your integration with common cloud identity providers. RStudio Connect also supports the SAML 2.0 protocol for integrations with many other authentication providers or homegrown SAML tools.

|Identity Provider|Status|More Information|
|----|---|----|
|Azure Active Directory|Tested and Integrated|[Azure Portal](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/aad.rstudioconnect?tab=Overview)|
|Okta|Tested & Integrated|[Okta Integration Guide](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-RStudio-Connect.html)|
|OneLogin| Tested & Integrated | Search [OneLogin Portal](https://www.onelogin.com/product/app-catalog) After Login
|Google, JumpCloud, ADFS, WSO2, PingIdentity, Shibboleth | Tested | [Configuration Guide](https://support.rstudio.com/hc/en-us/articles/360022321494)|
| General SAML 2.0 | Supported | [Configuration Guide](https://support.rstudio.com/hc/en-us/articles/360022321494)|
|Duo, Centrify, Auth0 | Supported | [Available in RStudio Connect 1.7.6+](https://support.rstudio.com/hc/en-us/articles/360022321494) |

RStudio Connect’s SAML 2.0 authentication method supports Just-In-Time provisioning, either local or remote group management, Identity Provider metadata, and a handful of other configuration options that can be explored in the RStudio Connect Admin Guide.


## Server APIs

The [Connect Server API](https://docs.rstudio.com/connect/1.7.4/api/) allows teams to interact with RStudio Connect from code. This release lets you programmatically update [updating content settings](https://docs.rstudio.com/connect/1.7.4/user/cookbook.html#cookbook-content) and [manage content bundles](https://docs.rstudio.com/connect/1.7.4/user/cookbook.html#cookbook-promotion). Build a custom workflow, such as promoting content from a staging server to production.

{{< figure src="assets-ci.png" caption="Integrate Connect into CI/CD Toolchains" alt= "CI/CD Toolchains">}}

Learn more about [different approaches to asset deployment](https://solutions.rstudio.com/deploy/promote/), including how to [integrate RStudio Connect into CI/CD toolchains](https://solutions.rstudio.com/deploy/overview/).

## Email Overhaul

RStudio Connect uses email to distribute content, manage user accounts, notify publishers of errors, and more. In order to send emails, administrators must configure Connect to use sendmail or an SMTP client. In prior versions of RStudio Connect, this configuration was done in the RStudio Connect dashboard. Version 1.7.4 and above removes this support in favor of [managing email settings](https://docs.rstudio.com/connect/1.7.4/admin/email-setup.html) with the RStudio Connect configuration file. This change makes setup easier and more consistent for administrators.

> When upgrading to RStudio Connect 1.7.4, administrators should [follow these instructions](https://support.rstudio.com/hc/en-us/articles/360022554513) to migrate email settings to the configuration file.

In addition, RStudio Connect no longer requires email setup. Disabling email can be useful for groups starting a proof-of-concept, or teams running Connect in certain locked-down environments, In these cases, Connect will gracefully disable settings that require email. For full functionality we strongly recommend an email integration.

## Breaking Changes and Deprecations

- Network information is no longer collected and stored at `{Server.DataDir}/metrics/rrd/network-*.rrd`. This information was never used by RStudio Connect and is removed to save storage space.   
- The experimental content API has changed, see the [new API documentation](https://docs.rstudio.com/connect/1.7.4/api/#updateContent) for details.  
- The `[LoadBalancing].EnforceMinRsconnectVersion` setting now defaults to true and has been deprecated. RStudio Connect will now require `rsconnect` version 0.8.3 or above.
- The next version of RStudio Connect will not support discovering R versions through the file `/etc/rstudio/r-versions`. Administrators using this file should migrate this information to the Connect configuration file's [`[Server].RVersion` field](https://docs.rstudio.com/connect/1.7.4/admin/r.html#r-versions).

Please consult the full [release notes](https://docs.rstudio.com/connect/news).

> #### Upgrade Planning
> RStudio Connect 1.7.4 introduces a new upgrade process to facilitate changes
> to the RStudio Connect configuration file. This process requires administrators
> to upgrade RStudio Connect and then update the configuration file, as [described here](https://docs.rstudio.com/connect/1.7.4/admin/appendix-configuration.html#appendix-configuration-migration).
> Specific [instructions](https://support.rstudio.com/hc/en-us/articles/360022554513) for the 1.7.4 upgrade are also available. If
> you are upgrading from an earlier release than 1.7.2, please consult the
> intermediate release notes.

If you haven't yet had a chance to download and try [RStudio
Connect](https://rstudio.com/products/connect/), we encourage you to do so.
RStudio Connect is the best way to share all the work that you do in R and Python (Shiny
apps, R Markdown documents, plots, dashboards, Plumber APIs, Jupyter, etc.) with
collaborators, colleagues, or customers.

You can find more details or download a 45-day evaluation of the product at
[https://www.rstudio.com/products/connect/](https://www.rstudio.com/products/connect/).
Additional resources can be found below.

- [RStudio Connect home page & downloads](https://www.rstudio.com/products/connect/)
- [RStudio Connect Admin Guide](http://docs.rstudio.com/connect/admin/)
- [Detailed news and changes between each version](http://docs.rstudio.com/connect/news/)
- [Pricing](https://www.rstudio.com/pricing/#ConnectPricing)
- [An online preview of RStudio Connect](https://beta.rstudioconnect.com/connect/)

