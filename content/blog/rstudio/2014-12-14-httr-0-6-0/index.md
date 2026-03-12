---
title: httr 0.6.0
people:
  - Hadley Wickham
date: '2014-12-14'
slug: httr-0-6-0
events: blog
ported_from: rstudio
port_status: in-progress
---


httr 0.6.0 is now available on CRAN. The httr packages makes it easy to talk to web APIs from R. Learn more in the [quick start](http://cran.r-project.org/web/packages/httr/vignettes/quickstart.html) vignette.

This release is mostly bug fixes and minor improvements. The most important are:

  * `handle_reset()`, which allows you to reset the default handle if you get the error "easy handle already used in multi handle".

  * `write_stream()` which lets you process the response from a server as a stream of raw vectors (#143).

  * `VERB()` allows to you send a request with a custom http verb.

  * `brew_dr()` checks for common problems. It currently checks if your `libcurl` uses NSS. This is unlikely to work so it gives you some advice on how to fix the problem (thanks to Dirk Eddelbuettel for debugging this problem and suggesting a remedy).

  * Added support for Google OAuth2 [service accounts](https://developers.google.com/accounts/docs/OAuth2ServiceAccount). (#119, thanks to help from @siddharthab). See `?oauth_service_token` for details.

I've also switched from RC to R6 (which should make it easier to extend OAuth classes for non-standard OAuth implementations), and tweaked the use of the backend SSL certificate details bundled with httr. See the [release notes](https://github.com/hadley/httr/releases/tag/v0.6) for complete details.

