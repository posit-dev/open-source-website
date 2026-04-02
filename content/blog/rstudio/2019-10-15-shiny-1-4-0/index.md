---
title: Shiny 1.4.0
description: "Shiny 1.4.0: trailing commas now work in UI functions like div() and span()."
auto-description: true
people:
  - Winston Chang
date: '2019-10-15'
slug: shiny-1-4-0
categories:
  - Interactive Apps
tags:
  - Shiny
  - Packages
  - RStudio
blogcategories:
  - Products and Technology
  - Open Source
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
ported_categories:
  - Packages
  - Shiny
---



Shiny 1.4.0 has been released! This release mostly focuses on under-the-hood fixes, but there are a few user-facing changes as well.

If you've written a Shiny app before, you've probably encountered errors like this:

```R
div("Hello", "world!", )
#> Error in tag("div", list(...)) : argument is missing, with no default
```

This is due to a trailing comma in `div()`. It's very easy to accidentally add trailing commas when you're writing and debugging a Shiny application.

In Shiny 1.4.0, you'll no longer get this error -- it will just work with trailing commas. This is true for `div()` and all other HTML tag functions, like `span()`, `p()`, and so on.


The new version of Shiny also lets you control the whitespace between HTML tags. Previously, if there were two adjacent tags, like the two spans in `div(a("Visit this link", href="path/"), span("."))`, whitespace would always be inserted between them, resulting in output that renders as "Visit this link .".

Here's what the generated HTML looks like:

```R
div(a("Visit this link", href = "path/"), span("."))
#> <div>
#>   <a href="path/">Visit this link</a>
#>   <span>.</span>
#> </div>
```

Now, you can use the `.noWS` parameter to remove the spacing between tags, so you can create output that renders as "Visit this link.":

```R
div(a("Visit this link", href = "path/", .noWS = "after"), span("."))
#> <div>
#>   <a href="path/">Visit this link</a><span>.</span>
#> </div>
```

The `.noWS` parameter can take one or more other values to control whitespace in other ways:

* `"before"` suppresses whitespace before the opening tag.
* `"after"` suppresses whitespace after the closing tag.
* `"after-begin"` suppresses whitespace between the opening tag and its first child. (In the example above, the `<span>` tags are children of the `<div>`.
* `"after-begin"` suppresses whitespace between the last child and the closing tag.

(These changes actually come from version 0.4.0 of the htmltools package, but most users will encounter these functions via Shiny, and the documentation in Shiny has been updated to reflect the changes.)

## Breaking changes

We've updated from jQuery 1.12.4 to 3.4.1. There's a small chance that JavaScript code will behave slightly differently with the new version of jQuery, so if you encounter a compatibility issue, you can use the old version of jQuery with `options(shiny.jquery.version=1)`. Note that this option will go away some time in the future, so if you find that you need to use it, please make sure to update your JavaScript code to work with jQuery 3.

For the full set of changes in this version of Shiny, please see [this page](http://shiny.rstudio-staging.com/reference/shiny/1.4.0/upgrade.html).

