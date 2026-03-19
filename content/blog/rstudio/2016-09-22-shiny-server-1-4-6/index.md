---
title: Shiny Server (Pro) 1.4.6
people:
  - Joe Cheng
date: '2016-09-22'
categories:
- Shiny
tags:
- Security
- Shiny
slug: shiny-server-1-4-6
blogcategories:
- Products and Technology
ported_from: rstudio
port_status: in-progress
---


We've just released Shiny Server and Shiny Server Pro 1.4.6. Relative to 1.4.2, our previously blogged-about version, the 1.4.6 release primarily includes bug fixes, and mitigations for low-severity security issues found by penetration testing. The full list of changes is after the jump.

If you're running a Shiny Server Pro release that is older than 1.4.3 _and_ are configured to use SSL/TLS, it's especially important that you upgrade, as the versions of Node.js that are bundled with Shiny Server Pro 1.4.3 and earlier include vulnerable versions of OpenSSL.

**Shiny Server (Open Source):** [Download now](https://www.rstudio.com/products/shiny/download-server/)

**Shiny Server Pro:** If you already have a license or evaluation key, please [upgrade now](https://www.rstudio.com/products/shiny/download-commercial/). Otherwise, you can [start a free 45-day evaluation](https://www.rstudio.com/products/shiny-server-pro/evaluation/).

<!-- more -->

### Shiny Server Pro 1.4.6

Bug fix release.

  * Fix a bug where a 404 response on some URLs could cause the server to exit with an unhandled exception.

### Shiny Server Pro 1.4.5

Security release to fix minor issues raised in penetration test results.

  * Add `disable_login_autocomplete` directive that can be used to instruct browsers not to attempt to autocomplete on the login screen. Note that servers can only suggest this behavior to browsers (and in particular, Google Chrome chooses not to comply, as its developers argue that disabling autocomplete decreases security rather than increasing it).

  * Add opt-in clickjacking protection via `frame_options` directive. Login and /admin URLs now served with `X-Frame-Options: DENY` (the former can be opted out with an `auth_frame_options allow;` directive).

  * Fix open redirection on __login__. Previously, a URL created with malicious intent could cause you to go to an arbitrary URL after successful login. Now, it is only possible to be redirected to a path on Shiny Server.

  * Add Cross-Site Request Forgery (CSRF) protection to login and other POST operations.

### Shiny Server Pro 1.4.4

  * Fix fatal EBADF error that could cause server crashes.

  * Updated PAM integration to resolve bug with asynchronous PAM modules like pam_ldap, pam_vas, and nss_ldap.

  * Upgrade to Node.js v0.10.46 (security patches).

### Shiny Server Pro 1.4.3

  * Added proxied authentication mechanism via the `auth_proxy` option.

  * Upgrade to Node.js v0.10.45 (primarily for updated OpenSSL).

