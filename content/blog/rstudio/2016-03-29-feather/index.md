---
title: 'Feather: A Fast On-Disk Format for Data Frames for R and Python, powered by
  Apache Arrow'
people:
  - Hadley Wickham
date: '2016-03-29'
categories:
- Packages
slug: feather
blogcategories:
- Products and Technology
tags:
- Packages
ported_from: rstudio
port_status: in-progress
---


Wes McKinney, Software Engineer, Cloudera
Hadley Wickham, Chief Scientist, RStudio

This past January, we (Hadley and Wes) met and discussed some of the systems challenges facing the Python and R open source communities. In particular, we wanted to see if there were some opportunities to collaborate on tools for improving interoperability between Python, R, and external compute and storage systems.

One thing that struck us was that while R's data frames and Python's pandas data frames utilize very different internal memory representations, they share a very similar semantic model. In both R and Panda's, data frames are lists of named, equal-length columns, which can be numeric, boolean, and date-and-time, categorical (_factors), or _string. Every column can have missing values.

Around this time, the open source community had just started the new Apache [Arrow](http://arrow.apache.org/) project, designed to improve data interoperability for systems dealing with columnar tabular data.

In discussing Apache Arrow in the context of Python and R, we wanted to see if we could use the insights from feather to design a very fast file format for storing data frames that could be used by both languages. Thus, the Feather format was born.

**What is Feather?**

Feather is a fast, lightweight, and easy-to-use binary file format for storing data frames. It has a few specific design goals:

  * Lightweight, minimal API: make pushing data frames in and out of memory as simple as possible

  * Language agnostic: Feather files are the same whether written by Python or R code. Other languages can read and write Feather files, too.

  * High read and write performance. When possible, Feather operations should be bound by local disk performance.

**Code examples**

The Feather API is designed to make reading and writing data frames as easy as possible. In R, the code might look like:

```r
library(feather)
path <- "my_data.feather"
write_feather(df, path)
df <- read_feather(path)
```

Analogously, in Python, we have:

    import feather
    path = 'my_data.feather'
    feather.write_dataframe(df, path)
    df = feather.read_dataframe(path)

**How fast is Feather?**

Feather is extremely fast. Since Feather does not currently use any compression internally, it works best when used with solid-state drives as come with most of today's laptop computers. For this first release, we prioritized a simple implementation and are thus writing unmodified Arrow memory to disk.

To give you an idea, here is a Python benchmark writing an approximately 800MB pandas DataFrame to disk:

    import feather
    import pandas as pd
    import numpy as np
    arr = np.random.randn(10000000) # 10% nulls
    arr[::10] = np.nan
    df = pd.DataFrame({'column_{0}'.format(i): arr for i in range(10)})
    feather.write_dataframe(df, 'test.feather')

On Wes's laptop (latest-gen Intel processor with SSD), this takes:

    In [9]: %time df = feather.read_dataframe('test.feather')
    CPU times: user 316 ms, sys: 944 ms, total: 1.26 s
    Wall time: 1.26 s

    In [11]: 800 / 1.26
    Out[11]: 634.9206349206349

This is effective performance of over 600 MB/s. Of course, the performance you see will depend on your hardware configuration.

And in R (on Hadley's laptop, which is very similar):

```r
library(feather)

x <- runif(1e7)
x[sample(1e7, 1e6)] <- NA # 10% NAs
df <- as.data.frame(replicate(10, x))
write_feather(df, 'test.feather')

system.time(read_feather('test.feather'))
#>   user  system elapsed
#>  0.731   0.287   1.020
```

**How can I get Feather?**

The Feather source code is hosted at <http://github.com/wesm/feather>.

**Installing Feather for R**

Feather is currently available from github, and you can install with:

```r
devtools::install_github("wesm/feather/R")
```

Feather uses C++11, so if you're on windows, you'll need the new [gcc 4.93 toolchain](https://github.com/rwinlib/r-base/wiki/Testing-Packages-with-Experimental-R-Devel-Build-for-Windows). (All going well this will be included in R 3.3.0, which is scheduled for release on April 14. We'll aim for a CRAN release soon after that).

**Installing Feather for Python**

For Python, you can install Feather from PyPI like so:

    $ pip install feather-format

We will look into providing more installation options, such as conda builds, in the future.

**What should you _not_ use Feather for?**

Feather is not designed for long-term data storage. At this time, we do not guarantee that the file format will be stable between versions. Instead, use Feather for quickly exchanging data between Python and R code, or for short-term storage of data frames as part of some analysis.

**Feather, Apache Arrow, and the community**

One of the great parts of Feather is that the file format is language agnostic. Other languages, such as Julia or Scala (for Spark users), can read and write the format without knowledge of details of Python or R.

Feather is one of the first projects to bring the tangible benefits of the Arrow spec to users in the form of an efficient, language-agnostic representation of tabular data on disk. Since Arrow does not provide for a file format, we are using Google's Flatbuffers library (github.com/google/flatbuffers) to serialize column types and related metadata in a language-independent way in the file.

The Python interface uses Cython to expose Feather's C++11 core to users, while the R interface uses Rcpp for the same task.

