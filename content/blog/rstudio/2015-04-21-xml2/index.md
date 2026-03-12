---
title: Parse and process XML (and HTML) with xml2
people:
  - Hadley Wickham
date: '2015-04-21'
categories:
- Packages
slug: xml2
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
events: blog
ported_from: rstudio
port_status: in-progress
---


I'm pleased to announced that the first version of xml2 is now available on CRAN. Xml2 is a wrapper around the comprehensive [libxml2](http://xmlsoft.org) C library that makes it easier to work with XML and HTML in R:

  * Read XML and HTML with `read_xml()` and `read_html()`.

  * Navigate the tree with `xml_children()`, `xml_siblings()` and `xml_parent()`. Alternatively, use xpath to jump directly to the nodes you're interested in with `xml_find_one()` and `xml_find_all()`. Get the full path to a node with `xml_path()`.

  * Extract various components of a node with `xml_text()`, `xml_attrs()`, `xml_attr()`, and `xml_name()`.

  * Convert to list with `as_list()`.

  * Where appropriate, functions support namespaces with a global url -> prefix lookup table. See `xml_ns()` for more details.

  * Convert relative urls to absolute with `url_absolute()`, and transform in the opposite direction with `url_relative()`. Escape and unescape special characters with `url_escape()` and `url_unescape()`.

  * Support for modifying and creating xml documents in planned in a future version.

This package owes a debt of gratitude to [Duncan Temple Lang](http://www.stat.ucdavis.edu/~duncan/) who's XML package has made it possible to use XML with R for almost 15 years!

## Usage

You can install it by running:

```r
install.packages("xml2")
```

(If you're on a mac, you might need to wait a couple of days - CRAN is busy rebuilding all the packages for R 3.2.0 so it's running a bit behind.)

Here's a small example working with an inline XML document:

```r
library(xml2)
x <- read_xml("<foo>
  <bar>text <baz id = 'a' /></bar>
  <bar>2</bar>
  <baz id = 'b' />
</foo>")

xml_name(x)
#> [1] "foo"
xml_children(x)
#> {xml_nodeset (3)}
#> [1] <bar>text <baz id="a"/></bar>
#> [2] <bar>2</bar>
#> [3] <baz id="b"/>

# Find all baz nodes anywhere in the document
baz <- xml_find_all(x, ".//baz")
baz
#> {xml_nodeset (2)}
#> [1] <baz id="a"/>
#> [2] <baz id="b"/>
xml_path(baz)
#> [1] "/foo/bar[1]/baz" "/foo/baz"
xml_attr(baz, "id")
#> [1] "a" "b"
```

## Development

Xml2 is still under active development. If notice any problems (including crashes), please try the [development version](https://github.com/hadley/xml2), and if that doesn't work, [file an issue](https://github.com/hadley/xml2/issues).

