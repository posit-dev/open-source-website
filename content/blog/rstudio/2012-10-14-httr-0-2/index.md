---
title: 'New version of httr: 0.2'
people:
  - Hadley Wickham
date: '2012-10-14'
categories:
  - Data Wrangling
slug: httr-0-2
blogcategories:
  - Products and Technology
  - Open Source
tags:
  - Packages
ported_from: rstudio
port_status: in-progress
software: ["httr"]
languages: ["R"]
ported_categories:
  - Packages
---


We're happy to announce a new version of httr, a package designed to make it easy to work with web APIs. Httr is a wrapper around [RCurl](http://www.omegahat.org/RCurl/), and provides:

  * functions for the most important http verbs: `GET`, `HEAD`, `PATCH`, `PUT`, `DELETE` and `POST`.

  * automatic cookie handing across requests, connection sharing, and standard SSL config.

  * a request object which captures the body of the request along with request status, cookies, headers, timings and other useful information.

  * easy ways to access the response as a raw vector, a character vector, or parsed into an R object (for html, xml, json, png and jpeg).

  * wrapper functions for the most common configuration options: `set_cookies`, `add_headers`, `authenticate`, `use_proxy`, `verbose`, `timeout`.

  * support for OAuth 1.0 and 2.0. Use `oauth1.0_token` and `oauth2.0_token` to get user tokens, and `sign_oauth1.0` and `sign_oauth2.0`to sign requests. The demos directory has six demos of using OAuth: three for 1.0 (linkedin, twitter and vimeo) and three for 2.0 (facebook, github, google).

Track httr's development on [github](https://github.com/hadley/httr), and see what's [new in this version](https://github.com/hadley/httr/blob/master/NEWS).

