---
title: 'sparklyr 0.5: Livy and dplyr improvements'
people:
  - Javier Luraschi
date: '2017-01-24'
tags:
- Livy
- Spark
- sparklyr
slug: sparklyr-0-5
blogcategories:
- Products and Technology
- Open Source
ported_from: rstudio
port_status: in-progress
languages: ["R"]
categories:
  - Data Wrangling
  - MLOps & Admin
ported_categories:
  - Packages
---


We're happy to announce that version 0.5 of the [sparklyr package](https://cran.rstudio.com/package=sparklyr) is now available on CRAN. The new version comes with many improvements over the first release, including:

  * **Extended dplyr** support by implementing: `do()` and `n_distinct()`.

  * **New functions** including `sdf_quantile()`, `ft_tokenizer()` and `ft_regex_tokenizer()`.

  * **Improved compatibility**, sparklyr now respects the value of the 'na.action' R option and `dim()`, `nrow()` and `ncol()`.

  * **Experimental** support for [Livy](http://livy.io/) to enable clients, including [RStudio](https://www.rstudio.com/products/rstudio/), to connect remotely to [Apache Spark](http://spark.apache.org/).

  * **Improved connections** by simplifying initialization and providing error diagnostics.

  * **Certified** sparklyr, [RStudio Server Pro](https://www.rstudio.com/products/rstudio-server-pro2/) and [ShinyServer Pro](https://www.rstudio.com/products/shiny-server-pro/) with [Cloudera](http://www.cloudera.com/).

  * **Updated** [spark.rstudio.com](http://spark.rstudio.com) with new [deployment examples](https://spark.rstudio.com/deployment_examples.html) and a sparklyr [cheatsheet](https://spark.rstudio.com/images/sparklyr-cheatsheet.pdf).

Additional changes and improvements can be found in the [sparklyr NEWS](https://github.com/rstudio/sparklyr/blob/master/NEWS.md) file.

For questions or feedback, please feel free to open a [sparklyr github issue](https://github.com/rstudio/sparklyr/issues) or a [sparklyr stackoverflow question](http://stackoverflow.com/questions/tagged/sparklyr).

## Extended dplyr support

`sparklyr 0.5` adds supports for `n_distinct()` as a faster and more concise equivalent of `length(unique(x))` and also adds support for `do()` as a convenient way to perform multiple serial computations over a `group_by()` operation:

```r
library(sparklyr)
sc <- spark_connect(master = "local")
mtcars_tbl <- copy_to(sc, mtcars, overwrite = TRUE)

by_cyl <- group_by(mtcars_tbl, cyl)
fit_sparklyr <- by_cyl %>%
   do(mod = ml_linear_regression(mpg ~ disp, data = .))

# display results
fit_sparklyr$mod
```

In this case, `.` represents a Spark DataFrame, which allows us to perform operations at scale (like this linear regression) for a small set of groups. However, since each group operation is performed sequentially, it is not recommended to use `do()` with a large number of groups. The code above performs multiple linear regressions with the following output:

```
[[1]]
Call: ml_linear_regression(mpg ~ disp, data = .)

Coefficients:
 (Intercept)         disp
19.081987419  0.003605119

[[2]]
Call: ml_linear_regression(mpg ~ disp, data = .)

Coefficients:
(Intercept)        disp
 40.8719553  -0.1351418

[[3]]
Call: ml_linear_regression(mpg ~ disp, data = .)

Coefficients:
(Intercept)        disp
22.03279891 -0.01963409
```

It's worth mentioning that while `sparklyr` provides comprehensive support for `dplyr`, `dplyr` is not strictly required while using `sparklyr`. For instance, one can make use of `DBI` without `dplyr` as follows:

```r
library(sparklyr)
library(DBI)

sc <- spark_connect(master = "local")
sdf_copy_to(sc, iris)
dbGetQuery(sc, "SELECT * FROM iris LIMIT 4")
```
```
  Sepal_Length Sepal_Width Petal_Length Petal_Width Species
1          5.1         3.5          1.4         0.2  setosa
2          4.9         3.0          1.4         0.2  setosa
3          4.7         3.2          1.3         0.2  setosa
4          4.6         3.1          1.5         0.2  setosa
5          5.0         3.6          1.4         0.2  setosa
```

## New functions

The new `sdf_quantile()` function computes approximate quantiles (to some relative error), while the new `ft_tokenizer()` and `ft_regex_tokenizer()` functions split a string by white spaces or regex patterns.

For example, `ft_tokenizer()` can be used as follows:

```r
library(sparklyr)
library(janeaustenr)
library(dplyr)

sc %>%
  spark_dataframe() %>%
  na.omit() %>%
  ft_tokenizer(input.col = "text", output.col = "tokens") %>%
  head(4)
```

Which produces the following output:

```
                   text                book     tokens
                  <chr>               <chr>     <list>
1 SENSE AND SENSIBILITY Sense & Sensibility <list [3]>
2                       Sense & Sensibility <list [1]>
3        by Jane Austen Sense & Sensibility <list [3]>
4                       Sense & Sensibility <list [1]>
```

Tokens can be further processed through, for instance, [HashingTF](http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.ml.feature.HashingTF).

## Improved compatibility

'na.action' is a parameter accepted as part of the 'ml.options' argument, which defaults to `getOption("na.action", "na.omit")`. This allows `sparklyr` to match the behavior of R while processing NA records, for instance, the following linear model drops NA record appropriately:

```r
library(sparklyr)
library(dplyr)
library(nycflights13)

sc <- spark_connect(master = "local")
flights_clean <- na.omit(copy_to(sc, flights))

ml_linear_regression(
  flights_tbl
  response = "dep_delay",
  features = c("arr_delay", "arr_time"))
```
```
* Dropped 9430 rows with 'na.omit' (336776 => 327346)
Call: ml_linear_regression(flights_tbl, response = "dep_delay",
                           features = c("arr_delay", "arr_time"))

Coefficients:
 (Intercept)    arr_delay     arr_time
6.1001212994 0.8210307947 0.0005284729
```

In addition, `dim()`, `nrow()` and `ncol()` are now supported against Spark DataFrames.

## Livy connections

[Livy](http://livy.io/), _"An Open Source REST Service for Apache Spark (Apache License)"_, is now available in `sparklyr 0.5` as an **experimental** feature. Among many scenarios, this enables connections from the RStudio desktop to Apache Spark when Livy is available and correctly configured in the remote cluster.

## Livy running locally

To work with Livy locally, `sparklyr` supports `livy_install()` which installs Livy in your local environment, this is similar to `spark_install()`. Since Livy is a service to enable remote connections into Apache Spark, the service needs to be started with `livy_service_start()`. Once the service is running, `spark_connect()` needs to reference the running service and use `method = "Livy"`, then `sparklyr` can be used as usual. A short example follows:

```r
livy_install()
livy_service_start()

sc <- spark_connect(master = "http://localhost:8998",
                    method = "livy")
copy_to(sc, iris)

spark_disconnect(sc)
livy_service_stop()
```

## Livy running in HDInsight

[Microsoft Azure](https://azure.microsoft.com/) supports Apache Spark clusters configured with Livy and protected with basic authentication in [HDInsight clusters](https://azure.microsoft.com/en-us/services/hdinsight/). To use `sparklyr` with HDInsight clusters through Livy, first create the HDInsight cluster with Spark support:

![hdinsight-azure](https://rstudioblog.files.wordpress.com/2017/01/hdinsight-azure.png)Creating Spark Cluster in Microsoft Azure HDInsight

Once the cluster is created, you can connect with `sparklyr` as follows:

```r
library(sparklyr)
library(dplyr)

config <- livy_config(user = "admin", password = "password")
sc <- spark_connect(master = "https://dm.azurehdinsight.net/livy/",
                    method = "livy",
                    config = config)

copy_to(sc, iris)
```

From a desktop running RStudio, the remote connection looks like this:

![rstudio-hdinsight-azure.png](https://rstudioblog.files.wordpress.com/2017/01/rstudio-hdinsight-azure.png)

## Improved connections

`sparklyr 0.5` no longer requires internet connectivity to download additional [Apache Spark packages](https://spark-packages.org/). This enables connections in secure clusters that do not have internet access or while on the go.

Some community members reported a generic _"Ports file does not exists"_ error while connecting with `sparklyr 0.4`. In `0.5`, we've deprecated the ports file and improved error reporting. For instance, the following invalid connection example throws: a descriptive error, the `spark-submit` parameters and logging information that helps us troubleshoot connection issues.

```
> library(sparklyr)
> sc <- spark_connect(master = "local",
                      config = list("sparklyr.gateway.port" = "0"))
Error in force(code) :
  Failed while connecting to sparklyr to port (0) for sessionid (5305):
  Gateway in port (0) did not respond.
  Path: /spark-1.6.2-bin-hadoop2.6/bin/spark-submit
  Parameters: --class, sparklyr.Backend, 'sparklyr-1.6-2.10.jar', 0, 5305

---- Output Log ----
16/12/12 12:42:35 INFO sparklyr: Session (5305) starting

---- Error Log ----
```

Additional technical details can be found in the [sparklyr gateway socket](https://github.com/rstudio/sparklyr/pull/238) pull request.

## Cloudera certification

[sparklyr](https://cran.rstudio.com/package=sparklyr) 0.4, sparklyr 0.5, [RStudio Server Pro 1.0](https://www.rstudio.com/products/rstudio-server-pro2/) and [ShinyServer Pro 1.5](https://www.rstudio.com/products/shiny-server-pro/) went through [Cloudera's certification](http://www.cloudera.com/partners/certified-technology.html) and are now certified with [Cloudera](http://www.cloudera.com/). Among various benefits, authentication features like [Kerberos](https://en.wikipedia.org/wiki/Kerberos_(protocol)), have been tested and validated against secured clusters.

For more information see [Cloudera's partner listings](http://www.cloudera.com/partners/partners-listing.html?q=rstudio).

