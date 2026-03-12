---
title: "Introducing sparklyr.flint: A time-series extension for sparklyr"
description: |
  We are pleased to announce that sparklyr.flint, a sparklyr extension for analyzing time series at scale with Flint, is now available on CRAN. Flint is an open-source library for working with time-series in Apache Spark which supports aggregates and joins on time-series datasets.
date: 2020-09-07
categories:
  - R
  - Time Series
author:
  - name: Yitao Li
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com
people:
  - Yitao Li
image: thumbnail.png
ported_from: ai
port_status: raw
---



In this blog post, we will showcase [`sparklyr.flint`](https://cran.r-project.org/web/packages/sparklyr.flint/index.html), a brand new [`sparklyr`](https://sparklyr.ai) extension providing a simple and intuitive R interface to the [`Flint`](https://github.com/twosigma/flint) time series library. `sparklyr.flint` is available on [CRAN](https://cran.r-project.org/web/packages/sparklyr.flint/index.html) today and can be installed as follows:

``` r
install.packages("sparklyr.flint")
```

The first two sections of this post will be a quick bird's eye view on `sparklyr` and `Flint`, which will ensure readers unfamiliar with `sparklyr` or `Flint` can see both of them as essential building blocks for `sparklyr.flint`. After that, we will feature `sparklyr.flint`'s design philosophy, current state, example usages, and last but not least, its future directions as an open-source project in the subsequent sections.

# Quick Intro to `sparklyr`

`sparklyr` is an open-source R interface that integrates the power of distributed computing from [Apache Spark](https://spark.apache.org) with the familiar idioms, tools, and paradigms for data transformation and data modelling in R. It allows data pipelines working well with non-distributed data in R to be easily transformed into analogous ones that can process large-scale, distributed data in Apache Spark.

Instead of summarizing everything `sparklyr` has to offer in a few sentences, which is impossible to do, this section will solely focus on a small subset of `sparklyr` functionalities that are relevant to connecting to Apache Spark from R, importing time series data from external data sources to Spark, and also simple transformations which are typically part of data pre-processing steps.

### Connecting to an Apache Spark cluster

The first step in using `sparklyr` is to connect to Apache Spark. Usually this means one of the following:

- Running Apache Spark locally on your machine, and connecting to it to test, debug, or to execute quick demos that don't require a multi-node Spark cluster:

  ``` r
  library(sparklyr)

  sc <- spark_connect(master = "local", version = "2.4.4")
  ```

- Connecting to a multi-node Apache Spark cluster that is managed by a cluster manager such as [YARN](https://spark.apache.org/docs/latest/running-on-yarn.html), e.g.,

  ``` r
  library(sparklyr)

  sc <- spark_connect(master = "yarn-client", spark_home = "/usr/lib/spark")
  ```

### Importing external data to Spark

Making external data available in Spark is easy with `sparklyr` given the large number of data sources `sparklyr` supports. For example, given an R dataframe, such as

::: {.cell}

``` r
dat <- data.frame(id = seq(10), value = rnorm(10))
```

:::

the command to copy it to a Spark dataframe with 3 partitions is simply

::: {.cell}

``` r
sdf <- copy_to(sc, dat, name = "unique_name_of_my_spark_dataframe", repartition = 3L)
```

:::

Similarly, there are options for ingesting data in CSV, JSON, ORC, AVRO, and many other well-known formats into Spark as well:

::: {.cell}

``` r
sdf_csv <- spark_read_csv(sc, name = "another_spark_dataframe", path = "file:///tmp/file.csv", repartition = 3L)
# or
sdf_json <- spark_read_json(sc, name = "yet_another_one", path = "file:///tmp/file.json", repartition = 3L)
# or spark_read_orc, spark_read_avro, etc
```

:::

### Transforming a Spark dataframe

With `sparklyr`, the simplest and most readable way to transformation a Spark dataframe is by using `dplyr` verbs and the pipe operator (`%>%`) from [magrittr](https://cran.r-project.org/web/packages/magrittr/index.html).

`Sparklyr` supports a large number of `dplyr` verbs. For example,

::: {.cell}

``` r
sdf <- sdf %>%
  dplyr::filter(!is.null(id)) %>%
  dplyr::mutate(value = value ^ 2)
```

:::

Ensures `sdf` only contains rows with non-null IDs, and then squares the `value` column of each row.

That's about it for a quick intro to `sparklyr`. You can learn more in [sparklyr.ai](https://sparklyr.ai), where you will find links to reference material, books, communities, sponsors, and much more.

# What is `Flint`?

`Flint` is a powerful open-source library for working with time-series data in Apache Spark. First of all, it supports efficient computation of aggregate statistics on time-series data points having the same timestamp (a.k.a `summarizeCycles` in `Flint` nomenclature), within a given time window (a.k.a., `summarizeWindows`), or within some given time intervals (a.k.a `summarizeIntervals`). It can also join two or more time-series datasets based on inexact match of timestamps using asof join functions such as `LeftJoin` and `FutureLeftJoin`. The author of `Flint` has outlined many more of `Flint`'s major functionalities in [this article](https://databricks.com/blog/2018/09/11/introducing-flint-a-time-series-library-for-apache-spark.html), which I found to be extremely helpful when working out how to build `sparklyr.flint` as a simple and straightforward R interface for such functionalities.

Readers wanting some direct hands-on experience with Flint and Apache Spark can go through the following steps to run a minimal example of using Flint to analyze time-series data:

- First, install Apache Spark locally, and then for convenience reasons, define the `SPARK_HOME` environment variable. In this example, we will run Flint with Apache Spark 2.4.4 installed at `~/spark`, so:

  ``` bash
  export SPARK_HOME=~/spark/spark-2.4.4-bin-hadoop2.7
  ```

- Launch Spark shell and instruct it to download `Flint` and its Maven dependencies:

  ``` bash
  "${SPARK_HOME}"/bin/spark-shell --packages=com.twosigma:flint:0.6.0
  ```

- Create a simple Spark dataframe containing some time-series data:

  ``` scala
  import spark.implicits._

  val ts_sdf = Seq((1L, 1), (2L, 4), (3L, 9), (4L, 16)).toDF("time", "value")
  ```

- Import the dataframe along with additional metadata such as time unit and name of the timestamp column into a `TimeSeriesRDD`, so that `Flint` can interpret the time-series data unambiguously:

  ``` scala
  import com.twosigma.flint.timeseries.TimeSeriesRDD

  val ts_rdd = TimeSeriesRDD.fromDF(
    ts_sdf
  )(
    isSorted = true, // rows are already sorted by time
    timeUnit = java.util.concurrent.TimeUnit.SECONDS,
    timeColumn = "time"
  )
  ```

- Finally, after all the hard work above, we can leverage various time-series functionalities provided by `Flint` to analyze `ts_rdd`. For example, the following will produce a new column named `value_sum`. For each row, `value_sum` will contain the summation of `value`s that occurred within the past 2 seconds from the timestamp of that row:

  ``` scala
  import com.twosigma.flint.timeseries.Windows
  import com.twosigma.flint.timeseries.Summarizers

  val window = Windows.pastAbsoluteTime("2s")
  val summarizer = Summarizers.sum("value")
  val result = ts_rdd.summarizeWindows(window, summarizer)

  result.toDF.show()
  ```

<!-- -->

        +-------------------+-----+---------+
        |               time|value|value_sum|
        +-------------------+-----+---------+
        |1970-01-01 00:00:01|    1|      1.0|
        |1970-01-01 00:00:02|    4|      5.0|
        |1970-01-01 00:00:03|    9|     14.0|
        |1970-01-01 00:00:04|   16|     29.0|
        +-------------------+-----+---------+

     In other words, given a timestamp `t` and a row in the result having `time` equal to `t`, one can notice the `value_sum` column of that row contains sum of `value`s within the time window of `[t - 2, t]` from `ts_rdd`.

# Intro to `sparklyr.flint`

The purpose of `sparklyr.flint` is to make time-series functionalities of `Flint` easily accessible from `sparklyr`. To see `sparklyr.flint` in action, one can skim through the example in the previous section, go through the following to produce the exact R-equivalent of each step in that example, and then obtain the same summarization as the final result:

- First of all, install `sparklyr` and `sparklyr.flint` if you haven't done so already.

  ``` r
  install.packages("sparklyr")
  install.packages("sparklyr.flint")
  ```

- Connect to Apache Spark that is running locally from `sparklyr`, but remember to attach `sparklyr.flint` before running `sparklyr::spark_connect`, and then import our example time-series data to Spark:

  ``` r
  library(sparklyr)
  library(sparklyr.flint)

  sc <- spark_connect(master = "local", version = "2.4")
  sdf <- copy_to(sc, data.frame(time = seq(4), value = seq(4)^2))
  ```

- Convert `sdf` above into a `TimeSeriesRDD`

  ``` r
  ts_rdd <- fromSDF(sdf, is_sorted = TRUE, time_unit = "SECONDS", time_column = "time")
  ```

- And finally, run the 'sum' summarizer to obtain a summation of `value`s in all past-2-second time windows:

  ``` r
  result <- summarize_sum(ts_rdd, column = "value", window = in_past("2s"))

  print(result %>% collect())
  ```

  ``` r
  ## # A tibble: 4 x 3
  ##   time                value value_sum
  ##   <dttm>              <dbl>     <dbl>
  ## 1 1970-01-01 00:00:01     1         1
  ## 2 1970-01-01 00:00:02     4         5
  ## 3 1970-01-01 00:00:03     9        14
  ## 4 1970-01-01 00:00:04    16        29
  ```

# Why create a `sparklyr` extension?

The alternative to making `sparklyr.flint` a `sparklyr` extension is to bundle all time-series functionalities it provides with `sparklyr` itself. We decided that this would not be a good idea because of the following reasons:

- Not all `sparklyr` users will need those time-series functionalities
- `com.twosigma:flint:0.6.0` and all Maven packages it transitively relies on are quite heavy dependency-wise
- Implementing an intuitive R interface for `Flint` also takes a non-trivial number of R source files, and making all of that part of `sparklyr` itself would be too much

So, considering all of the above, building `sparklyr.flint` as an extension of `sparklyr` seems to be a much more reasonable choice.

# Current state of `sparklyr.flint` and its future directions

Recently `sparklyr.flint` has had its first successful release on CRAN. At the moment, `sparklyr.flint` only supports the `summarizeCycle` and `summarizeWindow` functionalities of `Flint`, and does not yet support asof join and other useful time-series operations. While `sparklyr.flint` contains R interfaces to most of the summarizers in `Flint` (one can find the list of summarizers currently supported by `sparklyr.flint` in [here](https://cran.r-project.org/web/packages/sparklyr.flint/sparklyr.flint.pdf)), there are still a few of them missing (e.g., the support for `OLSRegressionSummarizer`, among others).

In general, the goal of building `sparklyr.flint` is for it to be a thin "translation layer" between `sparklyr` and `Flint`. It should be as simple and intuitive as possibly can be, while supporting a rich set of `Flint` time-series functionalities.

We cordially welcome any open-source contribution towards `sparklyr.flint`. Please visit https://github.com/r-spark/sparklyr.flint/issues if you would like to initiate discussions, report bugs, or propose new features related to `sparklyr.flint`, and https://github.com/r-spark/sparklyr.flint/pulls if you would like to send pull requests.

# Acknowledgement

- First and foremost, the author wishes to thank Javier ([@javierluraschi](https://github.com/javierluraschi)) for proposing the idea of creating `sparklyr.flint` as the R interface for `Flint`, and for his guidance on how to build it as an extension to `sparklyr`.

- Both Javier ([@javierluraschi](https://github.com/javierluraschi)) and Daniel ([@dfalbel](https://github.com/dfalbel)) have offered numerous helpful tips on making the initial submission of `sparklyr.flint` to CRAN successful.

- We really appreciate the enthusiasm from `sparklyr` users who were willing to give `sparklyr.flint` a try shortly after it was released on CRAN (and there were quite a few downloads of `sparklyr.flint` in the past week according to CRAN stats, which was quite encouraging for us to see). We hope you enjoy using `sparklyr.flint`.

- The author is also grateful for valuable editorial suggestions from Mara ([@batpigandme](https://github.com/batpigandme)), Sigrid ([@skeydan](https://github.com/skeydan)), and Javier ([@javierluraschi](https://github.com/javierluraschi)) on this blog post.

Thanks for reading!
