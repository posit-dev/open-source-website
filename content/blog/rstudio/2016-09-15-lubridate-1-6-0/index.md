---
title: lubridate 1.6.0
people:
  - Hadley Wickham
date: '2016-09-15'
categories:
- Packages
- tidyverse
slug: lubridate-1-6-0
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
- tidyverse
events: blog
ported_from: rstudio
port_status: raw
---


I am pleased to announced lubridate 1.6.0. Lubridate is designed to make working with dates and times as pleasant as possible, and is maintained by [Vitalie Spinu](http://vitalie.spinu.info/). You can install the latest version with:

```r
install.packages("lubridate")
```

This release includes a range of bug fixes and minor improvements. Some highlights from this release include:

  * `period()` and `duration()` constructors now accept character strings and allow a very flexible specification of timespans:

```r
period("3H 2M 1S")
#> [1] "3H 2M 1S"

duration("3 hours, 2 mins, 1 secs")
#> [1] "10921s (~3.03 hours)"

# Missing numerals default to 1.
# Repeated units are summed
period("hour minute minute")
#> [1] "1H 2M 0S"
```

Period and duration parsing allows for arbitrary abbreviations of time units as long as the specification is unambiguous. For single letter specs, `strptime()` rules are followed, so `m` stands for `months` and `M` for `minutes`.

These same rules allows you to compare strings and durations/periods:

```r
"2mins 1 sec" > period("2mins")
#> [1] TRUE
```

  * Date time rounding (with `round_date()`, `floor_date()` and `ceiling_date()`) now supports unit multipliers, like "3 days" or "2 months":

```r
ceiling_date(ymd_hms("2016-09-12 17:10:00"), unit = "5 minutes")
#> [1] "2016-09-12 17:10:00 UTC"
```

  * The behavior of `ceiling_date` for `Date` objects is now more intuitive. In short, dates are now interpreted as time intervals that are physically part of longer unit intervals:

    |day1| ... |day31|day1| ... |day28| ...
    |    January     |   February     | ...

That means that rounding up `2000-01-01` by a month is done to the boundary between January and February which, i.e. `2000-02-01`:

```r
ceiling_date(ymd("2000-01-01"), unit = "month")
#> [1] "2000-02-01"
```

This behavior is controlled by the `change_on_boundary` argument.

  * It is now possible to compare `POSIXct` and `Date` objects:

```r
ymd_hms("2000-01-01 00:00:01") > ymd("2000-01-01")
#> [1] TRUE
```

  * C-level parsing now handles English months and AM/PM indicator regardless of your locale. This means that English date-times are now always handled by lubridate C-level parsing and you don't need to explicitly switch the locale.

  * New parsing function `yq()` allows you to parse a year + quarter:

```r
yq("2016-02")
#> [1] "2016-04-01"
```

The new `q` format is available in all lubridate parsing functions.

See the [release notes](https://github.com/hadley/lubridate/releases/tag/v1.6.0) for the full list of changes. A big thanks goes to everyone who contributed: @[arneschillert](https://github.com/arneschillert), @[cderv](https://github.com/cderv), @[ijlyttle](https://github.com/ijlyttle), @[jasonelaw](https://github.com/jasonelaw), @[jonboiser](https://github.com/jonboiser), and @[krlmlr](https://github.com/krlmlr).

