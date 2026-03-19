---
title: httr 1.2.0
people:
  - Hadley Wickham
date: '2016-07-05'
categories:
- Packages
slug: httr-1-2-0
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
software: ["httr"]
languages: ["R"]
---


httr 1.2.0 is now available on CRAN. The httr package makes it easy to talk to web APIs from R. Learn more in the [quick start](http://cran.r-project.org/web/packages/httr/vignettes/quickstart.html) vignette. Install the latest version with:

```r
install.packages("httr")
```

There are a few small new features:

  * New `RETRY()` function allows you to retry a request multiple times until it succeeds, if you you are trying to talk to an unreliable service. To avoid hammering the server, it uses exponential backoff with jitter, as described in <https://www.awsarchitectureblog.com/2015/03/backoff.html>.

  * `DELETE()` gains a body parameter.

  * `encode = "raw"` parameter to functions that accept bodies. This allows you to do your own encoding.

  * `http_type()` returns the content/mime type of a request, sans parameters.

There is one important bug fix:

  * No longer uses use custom requests for standard `POST` requests. This has the side-effect of properly following redirects after `POST`, fixing some login issues in rvest.

httr 1.2.1 includes a fix for a small bug that I discovered shortly after releasing 1.2.0.

For the complete list of improvements, please see the [release notes](https://github.com/hadley/httr/releases/tag/v1.2.0).

