---
title: RStudio Connect 1.7.2
people:
  - Kelly O'Briant
date: '2019-03-22'
slug: announcing-rstudio-connect-1-7-2
categories:
- RStudio Connect
tags:
- Connect
- RStudio Connect
blogcategories:
- Products and Technology
ported_from: rstudio
port_status: raw
---


RStudio Connect 1.7.2 is ready to download, and this release contains some
long-awaited functionality that we are excited to share. Several authentication
and user-management tooling improvements have been added, including the ability
to change authentication providers on an existing server, new group support
options, and the official introduction of SAML as a supported authentication
provider (currently a beta feature\*). But that’s not all... keep reading to
learn about great additions to the RStudio Connect UI, updates to Python
support, and a brand new Admin dashboard view for tracking scheduled content.

{{< figure src="/blog-images/rsc-172-content.png" caption="Content Expanded View - Improve discoverability with descriptions and images" alt= "Content Expanded View">}}

## Updates

### Authentication Migration Tools

It is now possible to delete users, transfer content ownership, and change
authentication mechanisms for users and groups in RStudio Connect. This enables
several workflows that were previously impossible:

- Migrate authentication providers when prompted by IT
- Transition a Proof-of-Concept environment with “starter” authentication into a production context
- Clean up and remove users who are no longer relevant for the system

All of this functionality is available with the [usermanager CLI
tool](https://docs.rstudio.com/connect/admin/cli.html#cli-usermanager). A
specific walkthrough of these workflows is available in the [RStudio Connect
Admin
Guide](https://docs.rstudio.com/connect/admin/authentication.html#change-auth-provider).

### Group Support for PAM and Proxied Authentication

Group support has been enabled for all authentication providers in RStudio
Connect. The following grid illustrates the type of group support available for
the different authentication providers:

| Authentication Provider | Local Groups | Remote Groups |
|-------------------------|--------------|---------------|
| Password | Yes | |
| LDAP / Active Directory |	| Yes |
| SAML | Yes | |
| Google OAuth2	| Yes	|	|
| PAM	| Yes	|	|
| Proxied Authentication | Yes | Yes |

LDAP and Active Directory groups are managed by the authentication provider
(i.e., are configured and maintained in your LDAP or Active Directory server).
For the other authentication providers, groups are stored and managed inside
RStudio Connect. They can be managed in the groups UI (under People) or via the
[RStudio Connect Server API](https://docs.rstudio.com/connect/api/#groups).

### SAML Authentication (Beta Release)

RStudio Connect now supports using SAML as an authentication provider to
support single sign-on (SSO). If you use SAML as an
authentication provider, we encourage you to try this feature in your test
environment by integrating with your SAML Identity Provider. Any feedback you
have to share will be appreciated.

>\*SAML integration is a Beta feature of RStudio Connect. Beta features are
>supported and unlikely to face breaking changes in a future release. Any
>issues found in the feature will be addressed during the regular release
>schedule; they will not result in immediate patches or hotfixes. We encourage
>customers to try these features and welcome any feedback, but recommend the
>feature not be used in production until it is in general availability.

### View Scheduled Content

Administrators can now review all scheduled content in the RStudio Connect
dashboard. The Scheduled Content view helps you understand how server resources
will be used over time. Scheduled content can be filtered by frequency of
execution, letting you focus on the items that run most often.

{{< figure src="/blog-images/rsc-172-scheduledUI.png" alt= "View and filter scheduled content">}}

### Usage Metrics Summaries

A summary of recent usage is shown to content owners and administrators within
the “Info” settings panel in the RStudio Connect dashboard. Metrics are
displayed for Shiny applications and rendered/static content; they are not
available for other content types.

{{< figure src="/blog-images/rsc-172-usage.png" alt= "Usage Metrics Summaries">}}

Usage data for the content item is summarized to show the last 30 days of
activity across all associated versions and variants. Document content items
will display a chart of the daily visit count and a total visit counter for the
past 30-day period. Shiny applications will have the same statistics displayed,
plus a metric for total user interaction time.

### Python Support

In case you missed it, [RStudio Connect
1.7.0](https://blog.rstudio.com/2019/01/17/announcing-rstudio-connect-1-7-0/)
introduced support for publishing Jupyter Notebooks as well as Shiny
applications, R Markdown reports, and plumber APIs that [combine R and
Python](https://www.rstudio.com/wp-content/uploads/2019/01/Using-Python-with-RStudio-Connect-1.7.0.pdf).
Today, we’re excited to share that publishing Jupyter Notebooks is easier than
ever; start by downloading the
[rsconnect-jupyter](https://pypi.org/project/rsconnect-jupyter/) Notebook
extension, now available on PyPi.

{{< figure src="/blog-images/rsc-172-python.png" alt= "Jupyter Notebook Support">}}

## Additional Updates

- **Generate Diagnostic Reports and Support Bundles** This diagnostic report
  can be used by administrators to verify the status and configuration of your
RStudio Connect instance. The report also helps you work with our support team by collecting information and logs from your environment to help us quickly identify common issues and reduce the amount of time required to resolve them.
See the [Getting Started section of the Admin
Guide](https://docs.rstudio.com/connect/admin/getting-started.html#need-help)
for more information.
- **API Versioning Documentation** The versioning scheme of the Connect Server
  API, including definitions for "experimental" endpoints and a deprecation
strategy, is now included in the [API
Reference](https://docs.rstudio.com/connect/api/) documentation.
- **Expanded Content View** (Screenshot in introduction) Expanded view shows
  content descriptions and images in addition to the information available in
the familiar compact view. It is available to all users who can view the
content list. This expanded view can help viewers navigate and discover the
valuable data products your data science teams create.

## Security & Authentication Changes

- **Browser Configurations** Fixed an issue where certain browser
  configurations caused environment variable values to be stored in the
browser’s autofill cache.
- **OAuth2 Usernames** Rules for generating OAuth2 usernames are documented in
  the Admin Guide section for
[OAuth2](https://docs.rstudio.com/connect/admin/authentication.html#authentication-oauth2).
- **LDAP Usernames** Login failures due to case-sensitivity handling in LDAP
  usernames have been fixed. This fix also applies to proxied authentication
when using a UniqueID distinct from the username.

## Deprecations, Breaking Changes & Bug Fixes

- **Breaking Change** Publishers can no longer create groups. The creation of
  groups by publishers without consent from an administrator made it harder
to ensure limited access to content. All publisher-owned groups currently in existence will remain, but any new group creation by publishers will be blocked. To restore the previous
behavior and allow publishers to create groups, use the new setting:
`Authorization.PublishersCanOwnGroups`
- **Breaking Change** API requests with a malformed GUID in a path segment
  return a `400 Bad Request` HTTP status code rather than a `404 Not Found`.
- **Bug Fix** Shiny App usage historical information had the `started` timestamp
  stored in the local timezone while the `end` timestamp was in UTC. Now both are
stored in UTC; existing records will be adjusted automatically during the course of the upgrade.

Please review the [full release notes](http://docs.rstudio.com/connect/news)

> #### Upgrade Planning
> If you rely on publisher-created groups in RStudio
> Connect, please make note of the breaking changes described above and in the
> release notes.
>
> Due to the bug fix on historical timestamp information for
> Shiny App usage, upgrades could take several minutes depending on the number
> of records to be adjusted.
>
> Aside from the breaking changes above, there are
> no other special considerations. If you are upgrading from an earlier
> version, be sure to consult the release notes for the intermediate releases,
> as well.

If you haven't yet had a chance to download and try [RStudio
Connect](https://rstudio.com/products/connect/), we encourage you to do so.
RStudio Connect is the best way to share all the work that you do in R (Shiny
apps, R Markdown documents, plots, dashboards, Plumber APIs, etc.) with
collaborators, colleagues, or customers.

You can find more details or download a 45-day evaluation of the product at
[https://www.rstudio.com/products/connect/](https://www.rstudio.com/products/connect/).
Additional resources can be found below.

- [RStudio Connect home page & downloads](https://www.rstudio.com/products/connect/)
- [RStudio Connect Admin Guide](http://docs.rstudio.com/connect/admin/)
- [Detailed news and changes between each version](http://docs.rstudio.com/connect/news/)
- [Pricing](https://www.rstudio.com/pricing/#ConnectPricing)
- [An online preview of RStudio Connect](https://beta.rstudioconnect.com/connect/)

