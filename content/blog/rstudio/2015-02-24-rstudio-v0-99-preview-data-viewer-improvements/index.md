---
title: 'RStudio v0.99 Preview: Data Viewer Improvements'
people:
  - Jonathan McPherson
date: '2015-02-24'
categories:
- RStudio IDE
tags:
- data
- preview
- rstudio
- viewer
- RStudio IDE
slug: rstudio-v0-99-preview-data-viewer-improvements
blogcategories:
- Products and Technology
- Open Source
events: blog
ported_from: rstudio
port_status: raw
---


RStudio's data viewer provides a quick way to look at the contents of data frames and other column-based data in your R environment. You invoke it by clicking on the grid icon in the Environment pane, or at the console by typing `View(mydata)`.

![grid icon](https://rstudioblog.files.wordpress.com/2015/02/screen-shot-2015-02-23-at-1-28-17-pm.png)

As part of the [RStudio Preview Release](https://www.rstudio.com/products/rstudio/download/preview/), we've completely overhauled RStudio's data viewer with modern features provided in part by a new interface built on [DataTables](http://www.datatables.net/).

### No Row Limit

While the data viewer in 0.98 was limited to the first 1,000 rows, you can now view all the rows of your data set. RStudio loads just the portion of the data you're looking at into the user interface, so things won't get sluggish even when you're working with large data sets.

![no row limit](https://rstudioblog.files.wordpress.com/2015/02/screen-shot-2015-02-23-at-1-03-13-pm.png)

We've also added fixed column headers, and support for column labels imported from SPSS and other systems.

### Sorting and Filtering

RStudio isn't designed to act like a spreadsheet, but sometimes it's helpful to do a quick sort or filter to get some idea of the data's characteristics before moving into reproducible data analysis. Towards that end, we've built some basic sorting and filtering into the new data viewer.

#### Sorting

Click a column once to sort data in ascending order, and again to sort in descending order. For instance, how big is the biggest diamond?

![sorting](https://rstudioblog.files.wordpress.com/2015/02/screen-shot-2015-02-23-at-11-53-35-am.png)

To clear all sorts and filters on the data, click the upper-left column header.

#### Filtering

Click the new _Filter_ button to enter Filter mode, then click the white filter value box to filter a column. You might, for instance, want to look at only at smaller diamonds:

![filter](https://rstudioblog.files.wordpress.com/2015/02/screen-shot-2015-02-23-at-12-02-04-pm.png)

Not all data types can be filtered; at the moment, you can filter only numeric types, characters, and factors.

You can also stack filters; for instance, let's further restrict this view to small diamonds with a Very Good cut:

![filter factor](https://rstudioblog.files.wordpress.com/2015/02/screen-shot-2015-02-23-at-12-03-29-pm.png)

#### Full-Text Search

You can search the full text of your data frame using the new Search box in the upper right. This is useful for finding specific records; for instance, how many people named John were born in 2013?

![full-text search](https://rstudioblog.files.wordpress.com/2015/02/screen-shot-2015-02-23-at-12-13-04-pm.png)

### Live Update

If you invoke the data viewer on a variable as in `View(mydata)`, the data viewer will (in most cases) automatically refresh whenever data in the variable changes.

You can use this feature to watch data change as you manipulate it. It continues to work even when the data viewer is popped out, a configuration that combines well with multi-monitor setups.

We hope these improvements help make you understand your data more quickly and easily. Try out the [RStudio Preview Release](https://www.rstudio.com/products/rstudio/download/preview/) and let us know what you think!

