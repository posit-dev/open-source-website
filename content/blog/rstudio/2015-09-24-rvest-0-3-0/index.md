---
title: rvest 0.3.0
people:
  - Hadley Wickham
date: '2015-09-24'
categories:
- Packages
- tidyverse
slug: rvest-0-3-0
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
- tidyverse
events: blog
ported_from: rstudio
port_status: in-progress
---


I'm pleased to announce rvest 0.3.0 is now available on CRAN. [Rvest](https://blog.rstudio.com/2014/11/24/rvest-easy-web-scraping-with-r/) makes it easy to scrape (or harvest) data from html web pages, inspired by libraries like [beautiful soup](http://www.crummy.com/software/BeautifulSoup/). It is designed to work with [pipes](https://github.com/smbache/magrittr) so that you can express complex operations by composed simple pieces. Install it with:

```r
install.packages("rvest")
```

## What's new

The biggest change in this version is that rvest now uses the [xml2](https://blog.rstudio.com/2015/04/21/xml2/) package instead of [XML](https://cran.r-project.org/web/packages/XML/index.html). This makes rvest much simpler, eliminates memory leaks, and should improve performance a little.

A number of functions have changed names to improve consistency with other packages: most importantly `html()` is now `read_html()`, and `html_tag()` is now `html_name()`. The old versions still work, but are deprecated and will be removed in rvest 0.4.0.

`html_node()` now throws an error if there are no matches, and a warning if there's more than one match. I think this should make it more likely to fail clearly when the structure of the page changes. If you don't want this behaviour, use `html_nodes()`.

There were a number of other bug fixes and minor improvements as described in the [release notes](https://github.com/hadley/rvest/releases/tag/v0.3.0).

