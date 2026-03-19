---
title: httr 0.5
people:
  - Hadley Wickham
date: '2014-09-03'
categories:
- Packages
slug: httr-0-5
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


httr 0.5 is now available on CRAN. The httr packages makes it easy to talk to web APIs from R. Learn more in the [quick start](http://cran.r-project.org/web/packages/httr/vignettes/quickstart.html) vignette.

This release is mostly bug fixes and minor improvements, but there is one major new feature: you can now save response bodies directly to disk.

```r
library(httr)
# Download the latest version of rstudio for windows
url <- "http://download1.rstudio.org/RStudio-0.98.1049.exe"
GET(url, write_disk(basename(url)), progress())
```

There is also some preliminary support for HTTP caching (see `cache_info()` and `rerequest()`). See the [release notes](https://github.com/hadley/httr/releases/tag/v0.5) for complete details.

