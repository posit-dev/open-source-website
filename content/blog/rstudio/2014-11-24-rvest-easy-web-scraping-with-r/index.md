---
title: 'rvest: easy web scraping with R'
people:
  - Hadley Wickham
date: '2014-11-24'
slug: rvest-easy-web-scraping-with-r
blogcategories:
- Products and Technology
- Open Source
tags:
ported_from: rstudio
port_status: in-progress
software: ["rvest"]
languages: ["R"]
categories:
  - Data Wrangling
ported_categories:
  - Packages
---


rvest is new package that makes it easy to scrape (or harvest) data from html web pages, inspired by libraries like [beautiful soup](http://www.crummy.com/software/BeautifulSoup/). It is designed to work with [magrittr](https://github.com/smbache/magrittr) so that you can express complex operations as elegant pipelines composed of simple, easily understood pieces. Install it with:

```r
install.packages("rvest")
```

## rvest in action

To see rvest in action, imagine we'd like to scrape some information about [The Lego Movie](http://www.imdb.com/title/tt1490017/) from IMDB. We start by downloading and parsing the file with `html()`:

```r
library(rvest)
lego_movie <- html("http://www.imdb.com/title/tt1490017/")
```

To extract the rating, we start with [selectorgadget](http://selectorgadget.com) to figure out which css selector matches the data we want: `strong span`. (If you haven't heard of [selectorgadget](http://selectorgadget.com/), make sure to read `vignette("selectorgadget")` - it's the easiest way to determine which selector extracts the data that you're interested in.) We use `html_node()` to find the first node that matches that selector, extract its contents with `html_text()`, and convert it to numeric with `as.numeric()`:

```r
lego_movie %>%
  html_node("strong span") %>%
  html_text() %>%
  as.numeric()
#> [1] 7.9
```

We use a similar process to extract the cast, using `html_nodes()` to find all nodes that match the selector:

```r
lego_movie %>%
  html_nodes("#titleCast .itemprop span") %>%
  html_text()
#>  [1] "Will Arnett"     "Elizabeth Banks" "Craig Berry"
#>  [4] "Alison Brie"     "David Burrows"   "Anthony Daniels"
#>  [7] "Charlie Day"     "Amanda Farinos"  "Keith Ferguson"
#> [10] "Will Ferrell"    "Will Forte"      "Dave Franco"
#> [13] "Morgan Freeman"  "Todd Hansen"     "Jonah Hill"
```

The titles and authors of recent message board postings are stored in a the third table on the page. We can use `html_node()` and `[[` to find it, then coerce it to a data frame with `html_table()`:

```r
lego_movie %>%
  html_nodes("table") %>%
  .[[3]] %>%
  html_table()
#>                                              X 1            NA
#> 1 this movie is very very deep and philosophical   mrdoctor524
#> 2 This got an 8.0 and Wizard of Oz got an 8.1...  marr-justinm
#> 3                         Discouraging Building?       Laestig
#> 4                              LEGO - the plural      neil-476
#> 5                                 Academy Awards   browncoatjw
#> 6                    what was the funniest part? actionjacksin
```

## Other important functions

  * If you prefer, you can use xpath selectors instead of css: `html_nodes(doc, xpath = "//table//td")`).

  * Extract the tag names with `html_tag()`, text with `html_text()`, a single attribute with `html_attr()` or all attributes with `html_attrs()`.

  * Detect and repair text encoding problems with `guess_encoding()` and `repair_encoding()`.

  * Navigate around a website as if you're in a browser with `html_session()`, `jump_to()`, `follow_link()`, `back()`, and `forward()`. Extract, modify and submit forms with `html_form()`, `set_values()` and `submit_form()`. (This is still a work in progress, so I'd love your feedback.)

To see these functions in action, check out package demos with `demo(package = "rvest")`.

