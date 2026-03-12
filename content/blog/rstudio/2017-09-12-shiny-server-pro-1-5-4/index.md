---
title: Shiny Server (Pro) 1.5.4
people:
  - Alan Dipert
date: '2017-09-12'
slug: shiny-server-pro-1-5-4
categories:
- Shiny
tags:
- shiny server pro
- shiny
- Shiny
blogcategories:
- Products and Technology
events: blog
ported_from: rstudio
port_status: in-progress
---


[Shiny Server 1.5.4.869 and Shiny Server Pro 1.5.4.872 are now available.](https://www.rstudio.com/products/shiny/shiny-server/)

Both the new Shiny Server and Shiny Server Pro releases include bug fixes and enhancements, and we recommend upgrading at your earliest convenience.

### Shiny Server 1.5.4.869

* [Clickjacking protection](http://docs.rstudio.com/shiny-server/#clickjacking-protection) can now be enabled using the `frame_options` directive. This directive was already available in Shiny Server Pro, but is now available in Shiny Server as well.
* A bug that caused `"Error: Can't set headers after they are sent."` to appear in error logs was fixed.
* Several bugs in `license-manager` were fixed.

### Shiny Server Pro 1.5.4.872

* The "utilization scheduler" component, which manages the way requests are routed to R processes, has been significantly improved. It has been made more robust, and applications now respond more efficiently to increased load.
* `auth_pam`: The performance of multiple simultaneous logins was improved.
* `auth_ldap`: A bug was fixed that caused LDAP to return no groups when a username contained a backslash.

