---
title: RStudio Connect 1.5.0 - Introducing Tags!
people:
  - Jeff Allen
date: '2017-05-23'
categories:
- News
- RStudio Connect
tags:
- Connect
- R
- RStudio Connect
slug: rstudio-connect-1-5-0-introducing-tags
blogcategories:
- Products and Technology
- Company News and Events
events: blog
ported_from: rstudio
port_status: raw
---


We're excited to announce a powerful new ability to organize content in [RStudio Connect: version 1.5.0](https://www.rstudio.com/products/connect/). Tags allow publishers to arrange what they've published and enable users to find and discover the content most relevant to them. The release also includes a newly designed (and customizable!) landing page and multiple important security enhancements.

![New landing page in RStudio Connect v1.5.0](https://rstudioblog.files.wordpress.com/2017/05/screen-shot-2017-05-23-at-11-58-21-am.png)

### Tagging Content with a Custom Tag Schema

Tags can be used to manage and organize servers that have hundreds or even thousands of pieces of content published to them. Administrators can define a custom tag schema tailored to their organization. Publishers can then organize their content using tags, allowing all users to find the content they want by navigating through the tag schema.

See more details in the video below:

http://fantastic.wistia.com/medias/m1onaqyodg?embedType=async&videoFoam=true&videoWidth=640

### New Landing Page

The default landing page has been given a fresh look. Even better, administrators can now customize the landing page that logged out users will see when they visit the server. More details [here](http://docs.rstudio.com/connect/1.5.0/admin/custom-landing.html).

### Security Enhancements

This release includes multiple important security enhancements, so we recommend deploying this update as soon as possible. Specifically, this release adds protection for cross-site request forgery (CSRF) attacks and fixes two bugs around account management that could have been used to grant an account more permissions than it should have. These bugs were identified internally and we are not aware of any instances of these issues being exploited against a customer's server.

Other notable changes this release:

  * `[Authentication].Lifetime` can be used to define the duration of a user's session (the lifetime of their cookie) when they log in via web browser. It still defaults to 30 days.

  * Servers configured to use password authentication can now choose to disable user self-registration using the `[Password].SelfRegistration` setting. By default, this feature is still enabled.

  * Added experimental support for using PostgreSQL instead of SQLite as Connect's database. If you're interested in helping to test this feature, please contact [support@rstudio.com](mailto:support@rstudio.com).

  * Allow user and group names to contain periods.

  * Added support for the [config](https://github.com/rstudio/config) package. More details [here](http://docs.rstudio.com/connect/1.5.0/admin/process-management.html#using-the-config-package).

  * Formally documented the configuration settings that support being reloaded via a `HUP` signal. Settings now mention "Reloadable: true" in the documentation if they support reloading.

  * Renamed the "Performance" tab for Shiny applications to "Runtime."

  * Further improve database performance in high-traffic environments.

> #### Upgrade Planning
> 
> You can expect the installation and startup of v1.5.4 to be completed in under a minute. Previously authenticated users will need to login again when they visit the server again.
> 
> If you’re upgrading from a release older than 1.4.6, be sure to consider the “Upgrade Planning” notes from those other releases, as well.

If you haven't yet had a chance to download and try [RStudio Connect](https://rstudio.com/products/connect) we encourage you to do so. RStudio Connect is the best way to share all the work that you do in R (Shiny apps, R Markdown documents, plots, dashboards, etc.) with collaborators, colleagues, or customers.

You can find more details or download a 45 day evaluation of the product at <https://www.rstudio.com/products/connect/>. Additional resources can be found below.

  * [RStudio Connect home page & downloads](https://www.rstudio.com/products/connect/)

  * [RStudio Connect Admin Guide](http://docs.rstudio.com/connect/admin/)

  * [What IT needs to know about RStudio Connect](https://www.rstudio.com/wp-content/uploads/2016/01/RSC-IT-Q-and-A.pdf)

  * [Detailed news and changes between each version](http://docs.rstudio.com/connect/news/)

  * [Pricing](https://www.rstudio.com/pricing/#ConnectPricing)

  * [An online preview of RStudio Connect](https://beta.rstudioconnect.com/connect/)

