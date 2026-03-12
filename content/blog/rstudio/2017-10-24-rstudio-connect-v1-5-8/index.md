---
title: RStudio Connect v1.5.8
people:
  - Jeff Allen
date: '2017-10-24'
slug: rstudio-connect-v1-5-8
categories:
- News
- RStudio Connect
tags:
- Connect
- R
- RStudio Connect
blogcategories:
- Products and Technology
- Company News and Events
events: blog
ported_from: rstudio
port_status: in-progress
---


We're pleased to announce RStudio Connect: version 1.5.8. This release enables reconnects for Shiny applications, more consistent and trustworthy editing of user information, and various LDAP improvements.

![The auto-generated "swagger" interface for a web API written using Plumber.](/blog-images/rsc-154-plumber.png)

The major changes this release include:

 - Enabled **support for Shiny reconnects**. Users of Shiny applications are less likely to be interrupted during brief network hiccups. The `Client.ReconnectTimeout` property specifies how long that session is maintained when there is connectivity trouble. The default setting is `15s`. See https://shiny.rstudio.com/articles/reconnecting.html to learn more about reconnecting to Shiny applications. Disable this feature by giving the `Client.ReconnectTimeout` property a value of `0`.
 - Greater **consistency around editing user information**. Authentication providers that expect user information to come in externally (like LDAP and OAuth) will by default forbid users from editing their information and will automatically refresh user profile information when the user logs in. Other providers now more consistently allow information that was specified when the user created their account to be edited by the user later.
 - The `browseURL` R function is disabled when executing deployed content. Use techniques like the Shiny `shiny::tags$a` function to expose links to application visitors.
 - Support more flexibility when searching for LDAP users and groups with the `[LDAP].UserFilterBase` and `[LDAP].GroupFilterBase` settings.
 - LDAP configuration's `BindDN` password can now be stored in an external file using the new `BindPasswordFile` field. Also made improvements to LDAP group membership lookups.
 - Previously, usernames could not be edited when using the LDAP authentication provider by default or if the `Authentication.RequireExternalUsernames` flag was set to `true`. Now, user email, first name, and last name are also not editable for this configuration.
 - Connect administrators now receive an email as license expiration nears. Email is sent when the license is sixty days from expiring. Disable this behavior through the `Licensing.Expiration` setting.
 - Resolved a bug in the version of the `rebuild-packrat` command-line tool that was released in v1.5.6. Previously, the migration utility would render static content inaccessible. This release fixes this behavior and adds support for running this CLI tool while the RStudio Connect server is online. However, due to the discovery of new defects, the utility is disabled by default and is not recommended for production use until further notice. Those wishing to attempt to use the utility anyway should do so on a staging server that can be safely lost, and all content should be thoroughly tested after it has completed. http://docs.rstudio.com/connect/1.5.8/admin/cli.html#migration-cli
 - Fixed an issue with account confirmations and password resets for servers using non-UTC time zones.
 - LDAP now updates user email, first name, and last name every time a user logs in.
 - Fix an issue when performing the `LOGIN` SMTP authentication mechanism.
 - BREAKING: Changed the default value for `PAM.AuthenticatedSessionService` to `su`. Previously, on some distributions of Linux, setting `PAM.ForwardPassword` to `true` could present PAM errors to users when running applications as the current user if the `AuthenticatedSessionService` was not configured. System administrators who had previously edited the `rstudio-connect` PAM service for use in `ForwardPassword` mode should update the `PAM.AuthenticatedSessionService` configuration option. See:http://docs.rstudio.com/connect/1.5.8/admin/process-management.html#pam-credential-caching-kerberos
 - BREAKING: The format of the RStudio Connect package file names have changed. Debian package file names have the form `rstudio-connect_1.2.3-7_amd64.deb`. RPM package file names have the form `rstudio-connect-1.2.3-7.x86_64.rpm`. In addition, the RPM meta-data will have a "version" of `1.2.3` and a "release" of `7` for this file name. Previously, the RPM would have had a "version" of `1.2.3-7`.

You can see the full release notes for RStudio Connect 1.5.8 [here](http://docs.rstudio.com/connect/1.5.8/news/).

> #### Upgrade Planning
> There are no special precautions to be aware of when upgrading from v1.5.6. You can expect the installation and startup of v1.5.8 to be complete in under a minute. 
>
> If you’re upgrading from a release older than v1.5.6, be sure to consider the “Upgrade Planning” notes from those other releases, as well.

If you haven't yet had a chance to download and try [RStudio Connect](https://rstudio.com/products/connect) we encourage you to do so. RStudio Connect is the best way to share all the work that you do in R (Shiny apps, R Markdown documents, plots, dashboards, Plumber APIs, etc.) with collaborators, colleagues, or customers.

You can find more details or download a 45 day evaluation of the product at [https://www.rstudio.com/products/connect/](https://www.rstudio.com/products/connect/). Additional resources can be found below.
 
 - [RStudio Connect home page & downloads](https://www.rstudio.com/products/connect/)
 - [RStudio Connect Admin Guide](http://docs.rstudio.com/connect/admin/)
 - [What IT needs to know about RStudio Connect](https://www.rstudio.com/wp-content/uploads/2016/01/RSC-IT-Q-and-A.pdf)
 - [Detailed news and changes between each version](http://docs.rstudio.com/connect/news/)
 - [Pricing](https://www.rstudio.com/pricing/#ConnectPricing)
 - [An online preview of RStudio Connect](https://beta.rstudioconnect.com/connect/)


