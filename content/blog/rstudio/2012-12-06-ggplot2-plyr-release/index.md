---
title: ggplot2 0.9.3 and plyr 1.8 have been released!
people:
  - Winston Chang
date: '2012-12-06'
categories:
- Packages
slug: ggplot2-plyr-release
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
---


We're pleased to announce new versions of ggplot2 (0.9.3) and plyr (1.8).  To get up and running with the new versions, start a clean R session without ggplot2 or plyr loaded, and run `install.packages(c("ggplot2", "gtable", "scales", "plyr"))`. Read on to find out what's new.

## ggplot2 0.9.3

Most of the changes version 0.9.3 are bug fixes. Perhaps the most visible change is that ggplot will now print out warning messages when you use `stat="bin"` and also map a variable to y. For example, these are valid:

```r
ggplot(mtcars, aes(wt, mpg)) + geom_bar(stat = "identity")
ggplot(mtcars, aes(cyl)) + geom_bar(stat = "bin")
```

But this will result in some warnings:

```r
ggplot(mtcars, aes(wt, mpg)) + geom_bar(stat = "bin")
# The default stat for geom_bar is "bin", so this is the same as above:
ggplot(mtcars, aes(wt, mpg)) + geom_bar()
```

The reason for this change is to make behavior more consistent – `stat_bin` generates a y value, and so should not work when you also map a value to y.

For a full list of changes, please see the [NEWS file](http://cran.r-project.org/web/packages/ggplot2/NEWS).

## plyr 1.8

Version 1.8 has 28 improvements and bug fixes. Among the most prominent:

  * All parallel plyr functions gain a `.paropts` argument, a list of options that is passed onto `foreach` which allows you to control parallel execution.

  * `progress_time` is a new progress bar contributed by Mike Lawrence estimates the amount of time remaining before a job is complete

  * The summarise() function now calculates columns sequentially, so you can calculate new columns from other new columns, like this:

```r
   summarise(mtcars, x = disp/10, y = x/10)
```

This behavior is similar to the mutate() function. Please be aware that this could change the behavior of existing code, if any columns of the output have the same name but different values as columns in the input. For example, this will result in different behavior in plyr 1.7 and 1.8:

```r
   summarise(mtcars, disp = disp/10, y = disp*10)
```

In the old version, the y column would equal `mtcars$disp * 10`, and in the new version, it would equal `mtcars$disp`.

  * There are a number of performance improvements: `a*ply` uses more efficient indexing so should be more competitive with `apply`; `d*ply`, `quickdf_df` and `idata.frame` all have performance tweaks which will help a few people out a lot, and a lot of people a little.

For a full list of changes, please see the [NEWS file](http://cran.r-project.org/web/packages/plyr/NEWS).

