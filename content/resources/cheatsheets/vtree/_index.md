---
title: Examining nested subsets with vtree
image: page-1.png
resource_type: cheatsheet
by: community
date: '2019-06-01'
description: Display nested variable subsets as a tree to count and summarize data subgroups.
download_url: vtree.pdf
people:
- Nick Barrowman
thumbnails:
- page-1.png
languages:
- R
---

vtree creates graphical displays of nested subsets of a data frame, organizing observations into
a tree by combinations of variable categories. It supports custom numerical summaries, pruning
of branches, pattern tables, and flexible text and image formatting.

## What's covered
- Basic usage – calling `vtree` with one or more variable names
- Summaries – `%mean%`, `%SD%`, `%sum%`, `%median%`, `%freqpct%`, `%npct%`, `%list%`
- Pruning – `prune`, `keep`, `prunebelow`, `follow`
- Variable specification – suffixes (`#`, `*`, `@`) and prefixes (`is.na:`, `i:`, `any:`, `all:`)
- Labels – `labelvar`, `labelnode`, `showvarnames`, `showlegend`, `title`
- Pattern trees and tables – `pattern=T`, `ptable=T`
- Image settings – `imagewidth`, `imageheight`, `pxwidth`
- Frequencies and percentages – `vp`, `showpct`, `showcount`
- Text formatting – `splitwidth`, bold, italic, color markup
