---
title: RStudio Connect v1.5.4 - Now Supporting Plumber!
people:
  - Jeff Allen
date: '2017-08-03'
slug: rstudio-connect-v1-5-4-plumber
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


We're thrilled to announce support for hosting [Plumber APIs](https://www.rplumber.io/) in [RStudio Connect: version 1.5.4](https://www.rstudio.com/products/connect/). Plumber is an R package that allows you to define web APIs by adding special annotations to your existing R code -- allowing you to make your R functions accessible to other systems. 

Below you can see the auto-generated "swagger" interface for a web API written using Plumber.

![The auto-generated "swagger" interface for a web API written using Plumber.](/blog-images/rsc-154-plumber.png)

### Develop Web APIs using Plumber

The open-source [Plumber R package](https://rplumber.io/) enables you to create web APIs by merely adding special comments to your existing functions. These APIs can then be leveraged from other systems in your organization. For instance, you could query some functions written in R from a Java or Python application. Or you could develop a client for your API in JavaScript and allow users to interact with your R functions from a web browser.

Like Shiny applications, RStudio Connect supports one-step publishing, access controls, logging, and scaling for Plumber APIs. Visit [the documentation](http://docs.rstudio.com/connect/1.5.4/user/publishing.html#publishing-plumber-apis) for guidance on publishing APIs to RStudio Connect.

Users may now create and manage personal API keys that will allow them to programmatically access APIs that require authentication; see [the user guide](http://docs.rstudio.com/connect/1.5.4/user/api-keys.html) for more details.

Other notable changes this release:

 - **Content search** - On the content listing page, you can now search across all deployed content by title.
 - Official support for using **PostgreSQL** databases instead of SQLite. When configured appropriately, PostgreSQL can offer better performance. You can find documentation on configuration and the built-in database migration tool [here](http://docs.rstudio.com/connect/1.5.4/admin/database-provider.html#changing-database-provider).
 - **No customization of external usernames** - When a username is obtained from an external authentication provider like LDAP, RStudio Connect will no longer offer the user an opportunity to customize the associated internal username. Previously this situation could occur if the username obtained from the external provider included a special character that RStudio Connect didn’t allow in usernames. Now,  whatever username is provided from the external provider will be used without complaint.  See [the admin guide](http://docs.rstudio.com/connect/1.5.4/admin/authentication.html#auth-username-requirements) for more details.
 - **Upgraded our licensing software** - 1.5.4 includes new licensing software that will minimize user issues and report errors more clearly when they do occur. This release also includes experimental support for floating licenses which can be used to support transient servers that might be running in Docker or another virtualized environment. Please contact [support@rstudio.com](mailto:support@rstudio.com) if you're interested in helping test this feature.
 - Added a **health check endpoint** to make monitoring easier. See [the admin guide](http://docs.rstudio.com/connect/1.5.4/admin/server-management.html#health-check) for more details.
 - Added support for **Shiny reconnects**. This enables users to [reconnect to existing Shiny sessions](https://shiny.rstudio.com/articles/reconnecting.html) after brief network interruptions. This feature is not yet enabled by default but you can turn it on by setting `[Client].ReconnectTimeout` to something like `15s`.
 - The `[Authentication].Inactivity` setting can now be used to **log users out after a period of inactivity**. By default this feature is disabled, meaning users will remain logged in until their session expires, as controlled by the `[Authentication].Lifetime` setting. Additionally, we now do a better job of detecting when the user is logged out and immediately send them to the login page.
 - Support **external R packages**. This allows you to install an R package in the global system library and have deployed content use that package rather than trying to rebuild the package itself. This can be used as a workaround for packages that can't be installed correctly using Packrat, but should be viewed as a last resort, since this practice decreases the reproducibility and isolation of your content. See [the admin guide](http://docs.rstudio.com/connect/1.5.4/admin/package-management.html#external-package-installation) for more details.
 - If they exist, inject `http_proxy` and `https_proxy` environment variables into all child R processes. More documentation available [here](http://docs.rstudio.com/connect/1.5.4/admin/package-management.html#proxy-configuration).
 - RStudio Connect now **presents a warning when it is not using HTTPS**. This is to remind users and administrators that it is insecure the send sensitive information like usernames and passwords over a non-secured connection. See [the admin guide](http://docs.rstudio.com/connect/1.5.4/admin/appendix-configuration.html#appendix-configuration-https) for more information on how to configure your server to use HTTPS. Alternatively, if you’re handling SSL termination outside of Connect and want to disable this warning, you can set `[Http].NoWarning = true`.
 - RStudio Connect no longer leaves any R processes running when you stop the service. When the `rstudio-connect` service is restarted or stopped, all running R jobs are immediately interrupted.
 - **LDAP group queries are now cached** for approximately ten seconds. This can significantly improve the load time of Shiny applications and other resources when using an LDAP server that contains many users or groups. Additionally, LDAP user searching has been improved to better handle certain configurations.

You can see the full release notes for RStudio Connect 1.5.4 [here](http://docs.rstudio.com/connect/1.5.4/news/).

> #### Upgrade Planning
> You can expect the installation and startup of v1.5.4 to be completed in under a minute. Previously authenticated users will need to login again when they visit the server again. 
>
> If your server is not using Connect’s HTTPS capabilities, your users will see a warning about using an insecure configuration. If you’re doing SSL termination outside of Connect, you should configure `[Http].NoWarning=true` to remove this warning.
> 
> If you’re upgrading from a release older than 1.5.0, be sure to consider the “Upgrade Planning” notes from those other releases, as well.

If you haven't yet had a chance to download and try [RStudio Connect](https://rstudio.com/products/connect) we encourage you to do so. RStudio Connect is the best way to share all the work that you do in R (Shiny apps, R Markdown documents, plots, dashboards, Plumber APIs, etc.) with collaborators, colleagues, or customers.

You can find more details or download a 45 day evaluation of the product at [https://www.rstudio.com/products/connect/](https://www.rstudio.com/products/connect/). Additional resources can be found below.
 
 - [RStudio Connect home page & downloads](https://www.rstudio.com/products/connect/)
 - [RStudio Connect Admin Guide](http://docs.rstudio.com/connect/admin/)
 - [What IT needs to know about RStudio Connect](https://www.rstudio.com/wp-content/uploads/2016/01/RSC-IT-Q-and-A.pdf)
 - [Detailed news and changes between each version](http://docs.rstudio.com/connect/news/)
 - [Pricing](https://www.rstudio.com/pricing/#ConnectPricing)
 - [An online preview of RStudio Connect](https://beta.rstudioconnect.com/connect/)


