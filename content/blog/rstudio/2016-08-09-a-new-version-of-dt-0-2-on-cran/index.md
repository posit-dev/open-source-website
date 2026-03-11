---
title: A New Version of DT (0.2) on CRAN
people:
  - Yihui Xie
date: '2016-08-09'
categories:
- Packages
slug: a-new-version-of-dt-0-2-on-cran
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
events: blog
ported_from: rstudio
port_status: raw
---


The R package[ **DT**](http://rstudio.github.io/DT) v0.2 is on [CRAN](https://cran.rstudio.com/web/packages/DT/) now. You may install it from CRAN via `install.packages('DT')` or update your R packages if you have already installed it before. It has been over a year since the last CRAN release of **DT**, and there have been a lot of changes in both **DT** and the upstream [DataTables](http://datatables.net/blog/2015-08-13) library. You may read the [release notes](https://github.com/rstudio/DT/releases/tag/v0.2) to know all changes, and we want to highlight two major changes here:

  * Two extensions "TableTools" and "ColVis" have been removed from DataTables, and a new extension named "Buttons" was added. See [this page](http://rstudio.github.io/DT/extensions.html) for examples.

  * For tables in the server-side processing mode (the default mode for tables in Shiny), the selected row indices are integers instead of characters (row names) now. This is for consistency with the client-side mode (which returns integer indices). In many cases, it does not make much difference if you index an R object with integers or names, and we hope this will not be a breaking change to your Shiny apps.

In terms of new features added in the new version of **DT**, the most notable ones are:

  * Besides row selections, you can also select columns or cells. Please note the implementation is _not_ based on the "[Select](https://datatables.net/extensions/select)" extension of DataTables, so not all features of "Select" are available in **DT**. You can find examples of row/column/cell selections on [this page](http://rstudio.github.io/DT/shiny.html).

  * There are a number of new functions to modify an existing table instance in a Shiny app without rebuilding the full table widget. One significant advantage of this feature is it will be much faster and more efficient to update certain aspects of a table, e.g., you can change the table caption, or set the global search keyword of a table without making **DT** to create the whole table from scratch. You can even replace the data object behind the table on the fly (using `DT::replaceData()`), and after the data is updated, the table state can be preserved (e.g., sorting and filtering can remain the same).

  * A few formatting functions such as `formatSignif()` and `formatString()` were also added to the package.

As always, you are welcome to test the new release and we will appreciate your feedback. Please file bug reports to [Github](https://github.com/rstudio/DT/issues), and you may ask questions on [StackOverflow](http://stackoverflow.com/questions/tagged/dt) using the `DT` tag.

