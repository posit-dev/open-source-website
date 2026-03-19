---
title: Shiny Server 0.4
people:
  - RStudio Team
date: '2013-12-03'
categories:
- Shiny
slug: shiny-server-0-4
blogcategories:
- Products and Technology
- Open Source
tags:
- Shiny
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
---


Today, we're excited to announce the release of [Shiny Server version 0.4](http://rstudio.com/shiny/server/) as well as the availability of a beta version of Shiny Server Professional Edition.

Shiny Server is a platform for hosting Shiny Applications over the Web and has undergone substantial work in the past few months. We have fixed many bugs, added stability enhancements, and have created [pre-built installers](https://www.rstudio.com/shiny/server/) for Ubuntu 12.04 (and later) and RedHat/CentOS 5 and 6. The new installers will drastically simplify the process of installing and configuring Shiny Server on these distributions. For other platforms you can use the updated [instructions to build from source](https://github.com/rstudio/shiny-server/wiki/Building-Shiny-Server-from-Source).

Important note for current Shiny Server users: We are no longer relying on npm to distribute the software. If you had previously installed version 0.3.x using npm, you must uninstall the old version before upgrading. Follow [these instructions](http://rstudio.github.io/shiny-server/latest/#upgrading-from-shiny-server-0.3.5) to uninstall the old version before upgrading to the new.

We hope this new version will allow you to deploy your Shiny applications even more efficiently. Please reach out on the [mailing list](https://groups.google.com/forum/?fromgroups=#!forum/shiny-discuss) to let us know what you think or if you have any problems.

### Shiny Server Pro beta

We've recently begun beta testing of Shiny Server Professional Edition. This product adds features that make it easier for an enterprise to scale, tune, monitor and receive support for production environments.  Shiny Server Pro will include the ability to configure a Shiny application with more than one process, and control the number of concurrent users per application. It adds an administrative dashboard to monitor and gain insight into your applications, and includes integrations with a variety of authentication systems including LDAP and Active Directory.

If you're interested in finding out more about Shiny Server Pro, or being a participant in our beta please register [here](https://www.rstudio.com/shiny/server/pro).

Thank you for your help in making Shiny Server a better product.  We hope you enjoy Shiny Server 0.4 and look forward to getting your feedback.

