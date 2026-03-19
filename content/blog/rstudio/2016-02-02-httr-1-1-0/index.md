---
title: httr 1.1.0 (and 1.0.0)
people:
  - Hadley Wickham
date: '2016-02-02'
categories:
- Packages
slug: httr-1-1-0
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
---


httr 1.1.0 is now available on CRAN. The httr packages makes it easy to talk to web APIs from R. Learn more in the [quick start](http://cran.r-project.org/web/packages/httr/vignettes/quickstart.html) vignette.

Install the latest version with:

```r
install.packages("httr")
```

When writing this blog post I discovered that I forgot to annouce httr 1.0.0. This was a major release marking the transition from the RCurl package to the [curl](https://github.com/jeroenooms/curl) package, a modern binding to [libcurl](https://curl.haxx.se/libcurl/) written by [Jeroen Ooms](https://jeroenooms.github.io). This makes httr more reliable, less likely to leak memory, and prevents the diabolical "easy handle already used in multi handle" error.

httr 1.1.0 includes a couple of new features:

  * `stop_for_status()`, `warn_for_status()` and (new) `message_for_status()` replace the old `message` argument with a new `task` argument that optionally describes the current task. This allows API wrappers to provide more informative error messages on failure.

  * `http_error()` replaces `url_ok()` and `url_successful()`. `http_error()` more clearly conveys intent and works with urls, responses and status codes.

Otherwise, OAuth support continues to improve thanks to support from the community:

  * [Nathan Goulding](https://github.com/nathangoulding) added RSA-SHA1 signature support to `oauth1.0_token()`. He also fixed bugs in `oauth_service_token()` and improved the caching behaviour of `refresh_oauth2.0()`. This makes httr easier to use with Google's [service accounts](https://developers.google.com/identity/protocols/OAuth2ServiceAccount).

  * [Graham Parsons](https://github.com/grahamrp) added support for HTTP basic authentication to `oauth2.0_token()` with the `use_basic_auth`. This is now the default method used when retrieving a token.

  * [Daniel Lockau](https://github.com/cornf4ke) implemented `user_params` which allows you to pass arbitrary additional parameters to the token access endpoint when acquiring or refreshing a token. This allows you to use httr with Microsoft Azure. He also wrote a demo so you can see exactly how this works.

To see the full list of changes, please read the release notes for [1.0.0](https://github.com/hadley/httr/releases/tag/v1.0.0) and [1.1.0](https://github.com/hadley/httr/releases/tag/v1.1.0).

