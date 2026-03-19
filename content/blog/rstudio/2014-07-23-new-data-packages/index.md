---
title: New data packages
people:
  - Hadley Wickham
date: '2014-07-23'
categories:
- Packages
slug: new-data-packages
blogcategories:
- Products and Technology
- Open Source
tags:
- Packages
ported_from: rstudio
port_status: in-progress
---


I've released four new data packages to CRAN: [babynames](https://github.com/hadley/babynames), [fueleconomy](https://github.com/hadley/fueleconomy), [nasaweather](https://github.com/hadley/nasaweather) and [nycflights13](https://github.com/hadley/nycflights13). The goal of these packages is to provide some interesting, and relatively large, datasets to demonstrate various data analysis challenges in R. The package source code (on github, linked above) is fully reproducible so that you can see some data tidying in action, or make your own modifications to the data.

Below, I've listed the primary dataset found in each package. Most packages also include a number of supplementary datasets that provide additional information. Check out the docs for more details.

  * `babynames::babynames`: US baby name data for each year from 1880 to 2013, the number of children of each sex given each name. All names used 5 or more times are included. 1,792,091 rows, 5 columns (year, sex, name, n, prop). (Source: [Social security administration](http://www.ssa.gov/oact/babynames/limits.html)).

  * `fueleconomy::vehicles`: Fuel economy data for all cars sold in the US from 1984 to 2015. 33,442 rows, 12 variables. (Source: [Environmental protection agency](http://www.fueleconomy.gov/feg/download.shtml))

  * `nasaweather::atmos`: Data from the 2006 ASA data expo. Contains monthly atmospheric measurements from Jan 1995 to Dec 2000 on 24 x 24 grid over Central America. 41,472 observations, 11 variables. (Source: [ASA data expo](http://stat-computing.org/dataexpo/2006/))

  * `nycflights13::flights`: This package contains information about all flights that departed from NYC (i.e., EWR, JFK and LGA) in 2013: 336,776 flights with 16 variables. To help understand what causes delays, it also includes a number of other useful datasets: `weather`, `planes`, `airports`, `airlines`. (Source: [Bureau of transportation statistics](http://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236))

NB: since the datasets are large, I've tagged each data frame with the `tbl_df` class. If you don't use dplyr, this has no effect. If you do use dplyr, this ensures that you won't accidentally print thousands of rows of data. Instead, you'll just see the first 10 rows and as many columns as will fit on screen. This makes interactive exploration much easier.

```r
library(dplyr)
library(nycflights13)
flights
#> Source: local data frame [336,776 x 16]
#>
#>    year month day dep_time dep_delay arr_time arr_delay carrier tailnum
#> 1  2013     1   1      517         2      830        11      UA  N14228
#> 2  2013     1   1      533         4      850        20      UA  N24211
#> 3  2013     1   1      542         2      923        33      AA  N619AA
#> 4  2013     1   1      544        -1     1004       -18      B6  N804JB
#> 5  2013     1   1      554        -6      812       -25      DL  N668DN
#> 6  2013     1   1      554        -4      740        12      UA  N39463
#> 7  2013     1   1      555        -5      913        19      B6  N516JB
#> 8  2013     1   1      557        -3      709       -14      EV  N829AS
#> 9  2013     1   1      557        -3      838        -8      B6  N593JB
#> 10 2013     1   1      558        -2      753         8      AA  N3ALAA
#> ..  ...   ... ...      ...       ...      ...       ...     ...     ...
#> Variables not shown: flight (int), origin (chr), dest (chr), air_time
#>   (dbl), distance (dbl), hour (dbl), minute (dbl)
```

