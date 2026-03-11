---
title: Balancing the Load | What's New in RStudio Server Pro?
people:
  - Roger Oberg
date: '2015-01-13'
categories:
- News
- RStudio IDE
tags:
- rstudio
- RStudio IDE
slug: balancing-the-load-whats-new-in-rstudio-server-pro
blogcategories:
- Products and Technology
- Company News and Events
events: blog
ported_from: rstudio
port_status: raw
---


As R users know, we're continuously improving the RStudio IDE.  This includes RStudio Server Pro, where organizations who want to deploy the IDE at scale will find a growing set of features recently enhanced for them.

If you're not already familiar with RStudio Server Pro here's an updated [summary page](https://www.rstudio.com/products/rstudio-server-pro/) and a [comparison](https://www.rstudio.com/products/rstudio/#RStudioServerVersionComparison) to RStudio Server worth checking out. Or you can skip all of that and [download](https://www.rstudio.com/products/rstudio-server-pro/evaluation/) a free 45 day evaluation right now!

**WHAT'S NEW IN RSTUDIO SERVER PRO (v0.98.1091)**

Naturally, the latest RStudio Server Pro has all of the new features found in the open source server version of the RStudio IDE. They include improvements to R Markdown document and Shiny app creation, making R package development easier, better debugging and source editing, and support for Internet Explorer 10 and 11 and RHEL 7.

Recently, we added even more powerful features exclusively for RStudio Server Pro:

  * **Load balancing** based on factors you control. Load balancing ensures R users are automatically assigned to the best available server in a cluster.

  * **Flexible resource allocation** by user or group. Now you can allocate cores, set scheduler priority, control the version(s) of R and enforce memory and CPU limits.

  * **New security enhancements**. Leverage PAM to issue Kerberos tickets, move Google Accounts support to OAuth 2.0, and allow administrators to disable access to various features.

For a full list of what's changed in more depth, make sure to read the RStudio Server Pro [admin guide](https://s3.amazonaws.com/rstudio-server/rstudio-server-pro-0.98.1091-admin-guide.pdf).

**THE RSTUDIO SERVER PRO BASICS**

In addition to the newest features above there are many more that make RStudio Server Pro an upgrade to the open source IDE. Here's a quick list:

  * An administrative dashboard that provides insight into active sessions, server health, and monitoring of system-wide and per-user performance and resources

  * Authentication using system accounts, ActiveDirectory, LDAP, or Google Accounts

  * Full support for the Pluggable Authentication Module (PAM)

  * HTTP enhancements add support for SSL and keep-alive for improved performance

  * Ability to restrict access to the server by IP

  * Customizable server health checks

  * Suspend, terminate, or assume control of user sessions for assistance and troubleshooting

That's a lot to discover! Please [download the newest version of RStudio Server Pro](https://www.rstudio.com/products/rstudio-server-pro/evaluation/) and as always let us know how it's working and what else you'd like to see.

