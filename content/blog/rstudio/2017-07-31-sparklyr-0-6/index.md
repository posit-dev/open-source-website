---
title: 'sparklyr 0.6: Distributed R and external sources'
people:
  - Javier Luraschi
date: '2017-07-31'
slug: sparklyr-0-6
tags:
- Spark
- sparklyr
- Distributed Computing
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


We're excited to announce a new release of the [sparklyr](http://github.com/rstudio/sparklyr/) package, available in [CRAN](https://cran.r-project.org/package=sparklyr) today! `sparklyr 0.6` introduces new features to:

 - **Distribute R** computations using `spark_apply()` to execute arbitrary R code across your Spark cluster. You can now use all of your favorite R packages and functions in a distributed context. 
 - Connect to **External Data Sources** using `spark_read_source()`, `spark_write_source()`, `spark_read_jdbc()` and `spark_write_jdbc()`.
 - **Use the Latest Frameworks** including [dplyr 0.7](https://blog.rstudio.com/2017/06/13/dplyr-0-7-0/), [DBI 0.7](https://cran.r-project.org/package=DBI), [RStudio 1.1](https://www.rstudio.com/products/rstudio/download/preview/) and [Spark 2.2](https://databricks.com/blog/2017/07/11/introducing-apache-spark-2-2.html).
 
and several improvements across:

 - **Spark Connections** add a new [Databricks](https://databricks.com/product/databricks) connection that enables [using sparklyr in Databricks](https://databricks.com/blog/2017/05/25/using-sparklyr-databricks.html) through `mode="databricks"`, add support for [Yarn Cluster](https://spark.apache.org/docs/latest/running-on-yarn.html) through `master="yarn-cluster"` and connection speed was also improved.
 - **Dataframes** add support for `sdf_pivot()`, `sdf_broadcast()`, `cbind()`, `rbind()`, `sdf_separate_column()`, `sdf_bind_cols()`, `sdf_bind_rows()`, `sdf_repartition()` and `sdf_num_partitions()`.
 - **Machine Learning** adds support for multinomial regression in `ml_logistic_regression()`, `weights.column` for GLM, `ml_model_data()` and a new `ft_count_vectorizer()` function for `ml_lda()`.
 - Many other improvements, from initial support for **broom** over `ml_linear_regression()` and `ml_generalized_linear_regression()`, **dplyr** support for `%like%`, `%rlike%` and `%regexp%`, sparklyr **extensions** now support `download_scalac()` to help you install the required Scala compilers while developing extensions, Hive **database** management got simplified with `tbl_change_db()` and `src_databases()` to query and switch between Hive databases. RStudio started a joint effort with [Microsoft](https://www.microsoft.com) to support a **cross-platform Spark installer** under [github.com/rstudio/spark-install](https://github.com/rstudio/spark-install).
 
Additional changes and improvements can be found in the [sparklyr NEWS](https://github.com/rstudio/sparklyr/blob/master/NEWS.md) file.

Updated documentation and examples are available at [spark.rstudio.com](http://spark.rstudio.com). For questions or feedback, please feel free to open a [sparklyr github issue](https://github.com/rstudio/sparklyr/issues) or a [sparklyr stackoverflow question](http://stackoverflow.com/questions/tagged/sparklyr).

## Distributed R##

`sparklyr 0.6` provides support for executing distributed R code through `spark_apply()`. For instance, after connecting and copying some data:

```r message=FALSE
library(sparklyr)
sc <- spark_connect(master = "local")
iris_tbl <- sdf_copy_to(sc, iris)
```

We can apply an arbitrary R function, say `jitter()`, to each column over each row as follows:

```r
iris_tbl %>% spark_apply(function(e) sapply(e[,1:4], jitter))
```
```
# Source: spark<?> [?? x 4]
   Sepal_Length Sepal_Width Petal_Length Petal_Width
          <dbl>       <dbl>        <dbl>       <dbl>
 1         5.10        3.49         1.39       0.208
 2         4.89        2.99         1.40       0.206
 3         4.69        3.21         1.31       0.211
 4         4.61        3.10         1.48       0.181
 5         5.01        3.62         1.39       0.190
 6         5.39        3.88         1.71       0.398
 7         4.60        3.41         1.39       0.318
 8         4.99        3.41         1.48       0.194
 9         4.38        2.89         1.42       0.186
10         4.88        3.10         1.51       0.106
# … with more rows
```

One can also group by columns to apply an operation over each group of rows, say, to perform linear regression over each group as follows:

```r
spark_apply(
  iris_tbl,
  function(e) broom::tidy(lm(Petal_Width ~ Petal_Length, e)),
  names = c("term", "estimate", "std.error", "statistic", "p.value"),
  group_by = "Species"
)
```
```
# Source: spark<?> [?? x 6]
  Species    term         estimate std.error statistic  p.value
  <chr>      <chr>           <dbl>     <dbl>     <dbl>    <dbl>
1 versicolor (Intercept)   -0.0843    0.161     -0.525 6.02e- 1
2 versicolor Petal_Length   0.331     0.0375     8.83  1.27e-11
3 virginica  (Intercept)    1.14      0.379      2.99  4.34e- 3
4 virginica  Petal_Length   0.160     0.0680     2.36  2.25e- 2
5 setosa     (Intercept)   -0.0482    0.122     -0.396 6.94e- 1
6 setosa     Petal_Length   0.201     0.0826     2.44  1.86e- 2
```

Packages can be used since they are automatically distributed to the worker nodes; however, using `spark_apply()` requires R to be installed over each worker node. Please refer to [Distributing R Computations](https://spark.rstudio.com/articles/guides-distributed-r.html) for additional information and examples.

## External Data Sources ##

`sparklyr 0.6` adds support for connecting Spark to databases. This feature is useful if your Spark environment is separate from your data environment, or if you use Spark to access multiple data sources. You can use `spark_read_source()`, `spark_write_source` with any data connector available in [Spark Packages](https://spark-packages.org). Alternatively, you can use `spark_read_jdbc()` and `spark_write_jdbc()` and a JDBC driver with almost any data source.

For example, you can connect to Cassandra using `spark_read_source()`. Notice that the Cassandra connector version needs to match the Spark version as defined in their [version compatibility](https://github.com/datastax/spark-cassandra-connector#version-compatibility) section.

```r eval=FALSE
config <- spark_config()
config[["sparklyr.defaultPackages"]] <- c(
   "datastax:spark-cassandra-connector:2.0.0-RC1-s_2.11")

sc <- spark_connect(master = "local", config = config)

spark_read_source(sc, "emp",
  "org.apache.spark.sql.cassandra",
  list(keyspace = "dev", table = "emp"))
```

To connect to MySQL, one can [download the MySQL connector]( http://dev.mysql.com/downloads/connector/j/) and use `spark_read_jdbc()` as follows:

```r eval=FALSE
config <- spark_config()
config$`sparklyr.shell.driver-class-path` <- 
  "~/Downloads/mysql-connector-java-5.1.41/mysql-connector-java-5.1.41-bin.jar"

sc <- spark_connect(master = "local", config = config)

spark_read_jdbc(sc, "person_jdbc",  options = list(
  url = "jdbc:mysql://localhost:3306/sparklyr",
  user = "root", password = "<password>",
  dbtable = "person"))
```

Notice that the Cassandra connector version needs to match the Spark version as defined in their [version compatibility](https://github.com/datastax/spark-cassandra-connector#version-compatibility) section. See also [crassy](https://github.com/AkhilNairAmey/crassy), an `sparklyr` extension being developed to read data from Cassandra with ease.

## Dataframe Functions ##

`sparklyr 0.6` includes many improvements for working with DataFrames. Here are some additional highlights.

```r
x_tbl <- sdf_copy_to(sc, data.frame(a = c(1,2,3), b = c(2,3,4))) 
y_tbl <- sdf_copy_to(sc, data.frame(b = c(3,4,5), c = c("A","B","C")))
```

### Pivoting DataFrames

It is now possible to pivot (i.e. cross tabulate) one or more columns using `sdf_pivot()`.

```r
sdf_pivot(y_tbl, b ~ c, list(b = "count"))
```
```
# Source: spark<?> [?? x 4]
      b     A     B     C
  <dbl> <dbl> <dbl> <dbl>
1     4   NaN     1   NaN
2     3     1   NaN   NaN
3     5   NaN   NaN     1
```

### Binding Rows and Columns

Binding DataFrames by rows and columns is supported through `sdf_bind_rows()` and `sdf_bind_cols()`:

```r
sdf_bind_rows(x_tbl, y_tbl)
```
```
# Source: spark<?> [?? x 3]
      a     b c    
  <dbl> <dbl> <chr>
1     1     2 NA   
2     2     3 NA   
3     3     4 NA   
4   NaN     3 A    
5   NaN     4 B    
6   NaN     5 C 
```

```r
sdf_bind_cols(x_tbl, y_tbl)
```
```
# Source: spark<?> [?? x 4]
      a   b.x   b.y c    
  <dbl> <dbl> <dbl> <chr>
1     1     2     3 A    
2     3     4     5 C    
3     2     3     4 B 
```

### Separating Columns

Separate lists into columns with ease. This is especially useful when working with model predictions that are returned as lists instead of scalars. In this example, each element in the probability column contains two items. We can use `sdf_separate_column()` to isolate the item that corresponds to the probability that `vs` equals one.

```r message=FALSE
cars <- copy_to(sc, mtcars)
ml_logistic_regression(cars, vs ~ mpg) %>%
    ml_predict(cars) %>%
    sdf_separate_column("probability", list("P[vs=1]" = 2)) %>%
    dplyr::select(`P[vs=1]`)
```
```
# Source: spark<?> [?? x 1]
   `P[vs=1]`
       <dbl>
 1    0.551 
 2    0.551 
 3    0.727 
 4    0.593 
 5    0.313 
 6    0.261 
 7    0.0643
 8    0.841 
 9    0.727 
10    0.361 
# … with more rows
```

## Machine Learning ##

### Multinomial Regression

`sparklyr 0.6` adds support for multinomial regression for Spark 2.1.0 or higher:

```r message=FALSE
iris_tbl %>%
    ml_logistic_regression(Species ~ Sepal_Length + Sepal_Width)
```
```
Formula: Species ~ Sepal_Length + Sepal_Width

Coefficients:
           (Intercept) Sepal_Length Sepal_Width
versicolor      -201.6        73.19      -59.84
virginica       -214.6        75.10      -59.43
setosa           416.2      -148.29      119.27
```

### Improved Text Mining with LDA

`ft_tokenizer()` was introduced in `sparklyr 0.5` but `sparklyr 0.6` introduces `ft_count_vectorizer()` to simplify LDA:

```r message=FALSE
library(janeaustenr)
lines_tbl <- sdf_copy_to(sc,austen_books()[c(1,3),])

lines_tbl %>%
  ft_tokenizer("text", "tokens") %>%
  ft_count_vectorizer("tokens", "features") %>%
  ml_lda(features_col = "features", k = 4)
```

The vocabulary can be printed with:

```r
ml_lda(lines_tbl, ~text, k = 4)$vocabulary
```
```
[1] "jane"        "sense"       "austen"      "sensibility"
```

That's all for now, disconnecting:

```r
spark_disconnect(sc)
```

