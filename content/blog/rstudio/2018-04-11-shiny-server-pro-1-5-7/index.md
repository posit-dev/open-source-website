---
title: Shiny Server (Pro) 1.5.7
people:
  - Joe Cheng
date: '2018-04-11'
slug: shiny-server-pro-1-5-7
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
port_status: raw
---


[Shiny Server 1.5.7.907 and Shiny Server Pro 1.5.7.954 are now available.](https://www.rstudio.com/products/shiny/shiny-server/)

Highlights for this release are a major-version Node upgrade, support for HTTP gzip/deflate compression and (optionally) [secure cookies](https://en.wikipedia.org/wiki/Secure_cookies), and numerous bug fixes. We've also dropped support for some Linux distro versions that have reached their end of life.

### Shiny Server 1.5.7.907

* Upgrade to Node v8.10.0.

* Dropped support for Ubuntu 12.04 and SLES 11.

* Support gzip/deflate compression for HTTP responses. You can disable this if
  necessary with the directive "http_allow_compression no;" at the top level
  of shiny-server.conf.

* Don't color log output if stdout is not a terminal.

### Shiny Server Pro 1.5.7.954

The above changes, plus:

* Rename CSRF token cookie from XSRF-TOKEN to SSP-CSRF, so as not to conflict
  with other Angular apps being served from the same host.

* Fix bug where dashboard could show incorrect or even negative values from RAM
  usage.

* Fix bugs retrieving LDAP/Active Directory groups when group_filter contains
  an extensible match operator (which is the default for auth_active_dir).

* Fix bug where server could crash with "render is not defined".

* Add `secure_cookies always;` directive, which adds the HTTP cookie flag
  "secure" to our session cookies. Note that this should only be used if all
  authenticated apps and the admin dashboard are ONLY accessible via https,
  either through Shiny Server Pro's built-in TLS support or via a proxy.

