---
title: SparkR preview by Vincent Warmerdam
people:
  - Garrett Grolemund
date: '2015-05-28'
categories:
  - MLOps and Admin
tags:
  - big data
  - Spark
  - SparkR
slug: sparkr-preview-by-vincent-warmerdam
blogcategories:
  - Training and Education
ported_from: rstudio
port_status: in-progress
languages: ["R"]
ported_categories:
  - Training
---


This is a guest post by Vincent Warmerdam of [koaning.io](http://koaning.io​).

# SparkR preview in Rstudio

Apache Spark is the hip new technology on the block. It allows you to write scripts in a functional style and the technology behind it will allow you to run iterative tasks very quickly on a cluster of machines. It's benchmarked to be quicker than hadoop for most machine learning use cases (by a factor between 10-100) and soon Spark will also have support for the R language. As of April 2015, SparkR has been merged into Apache Spark and is shipping with a new version in an upcoming release (1.4) due early summer 2015. In the meanwhile, you can use this tutorial to go ahead and get familiar with the current version of SparkR.

**Disclaimer** : although you will be able to use this tutorial to write Spark jobs right now with R, the new api due this summer will most likely have breaking changes.

## Running Spark Locally

The main feature of Spark is the resilient distributed dataset, which is a dataset that can be queried in memory, in parallel on a cluster of machines. You don't need a cluster of machines to get started with Spark though. Even on a single machine, Spark is able to efficiently use any configured resources. To keep it simple we will ignore this configuration for now and do a quick one-click install. You can use devtools to download and install Spark with SparkR.

```r
library(devtools)
install_github("amplab-extras/SparkR-pkg", subdir="pkg")
```

This might take a while. But after the installation, the following R code will run Spark jobs for you:

```r
library(magrittr)
library(SparkR)

sc <- sparkR.init(master="local")

sc %>%
  parallelize(1:100000) %>%
  count
```

This small program generates a list, gives it to Spark (which turns it into an RDD, Spark's Resilient Distributed Dataset structure) and then counts the number of items in it. SparkR exposes the RDD API of Spark as distributed lists in R, which plays very nicely with **magrittr**. As long as you follow the API, you don't need to worry much about parallelizing for performance for your programs.

### A more elaborate example

Spark also allows for grouped operations, which might remind you a bit of dplyr.

```r
nums = runif(100000) * 10

sc %>%
  parallelize(nums) %>%
  map(function(x) round(x)) %>%
  filterRDD(function(x) x %% 2) %>%
  map(function(x) list(x, 1)) %>%
  reduceByKey(function(x,y) x + y, 1L) %>%
  collect
```

The Spark API will look very 'functional' to programmers used to functional programming languages (which should come to no suprise if you know that Spark is written in Scala). This script will do the following;

  1. it will create a RRD Spark object from the original data

  2. it will map each number to a rounded number

  3. it will filter all even numbers out or the RDD

  4. next it will create key/value pairs that can be counted

  5. it then reduces the key value pairs (the 1L is the number of partitions for the resulting RDD)

  6. and it collects the results

Spark will have started running services locally on your computer, which can be viewed at `http://localhost:4040/stages/`. You should be able to see all the jobs you've run here. You will also see which jobs have failed with the error log.

### Bootstrapping with Spark

These examples are nice, but you can also use the power of Spark for more common data science tasks. Let's sample a dataset to generate a large RDD, which we will then summarise via bootstrapping. Instead of parallelizing numbers, I will now parallelize dataframe samples.

```r
sc <- sparkR.init(master="local")

sample_cw <- function(n, s){
  set.seed(s)
  ChickWeight[sample(nrow(ChickWeight), n), ]
}

data_rdd <- sc %>%
  parallelize(1:200, 20) %>%
  map(function(s) sample_cw(250, s))
```

For the `parallelize` function we can assign the number of partitions Spark can use for the resulting RDD. My `s` argument ensures that each partition will use a different random seed when sampling. This `data_rdd` is useful, because it can be reused for multiple purposes.

You can use it to estimate the mean of the weight.

```r
data_rdd %>%
  map(function(x) mean(x$weight)) %>%
  collect %>%
  as.numeric %>%
  hist(20, main="mean weight, bootstrap samples")
```

Or you can use it to perform bootstrapped regressions.

```r
train_lm <- function(data_in){
  lm(data=data_in, weight ~ Time)
}

coef_rdd <- data_rdd %>%
  map(train_lm) %>%
  map(function(x) x$coefficients)

get_coef <- function(k) {
  code_rdd %>%
    map(function(x) x[k]) %>%
    collect %>%
    as.numeric
}

df <- data.frame(intercept = get_coef(1), time_coef = get_coef(2))
df$intercept %>% hist(breaks = 30, main="beta coef for intercept")
df$time_coef %>% hist(breaks = 30, main="beta coef for time")
```

The slow part of this tree of operations is the creation of the data, because this has to occur locally through R. A more common use case for Spark would be to load a large dataset from S3 which connects to a large EC2 cluster of Spark machines.

### More power?

Running Spark locally is nice and will already allow for parallelism, but the real profit can be gained by running Spark on a cluster of computers. The nice thing is that Spark automatically comes with a script that will automate the provisioning of a Spark cluster on Amazon AWS.

To get a cluster started; start up an EC2 cluster with the supplied ec2 folder from [Apache's Spark github repo](https://github.com/apache/spark/). A more elaborate tutorial can be found [here](https://spark.apache.org/docs/latest/ec2-scripts.html), but if you already are an Amazon user, provisioning a cluster on Amazon is as simple as calling a one-liner:

    ./spark-ec2 \
    --key-pair=spark-df \
    --identity-file=/path/spark-df.pem \
    --region=eu-west-1 \
    -s 3 \
    --instance-type c3.2xlarge \
    launch my-spark-cluster

If you ssh in the master node that has just been setup you can run the following code:

    cd /root
    git clone https://github.com/amplab-extras/SparkR-pkg.git
    cd SparkR-pkg
    SPARK_VERSION=1.2.1 ./install-dev.sh
    cp -a /root/SparkR-pkg/lib/SparkR /usr/share/R/library/
    /root/spark-ec2/copy-dir /root/SparkR-pkg
    /root/spark/sbin/slaves.sh cp -a /root/SparkR-pkg/lib/SparkR /usr/share/R/library/

### Launch SparkR on a Cluster

Finally to launch SparkR and connect to the Spark EC2 cluster, we run the following code on the master machine:

    MASTER=spark://:7077 ./sparkR

The hostname can be retrieved using:

    cat /root/spark-ec2/cluster-url

You can check on the status of your cluster via Spark's Web UI at `http://:8080`.

## The future

Everything described in this document is subject to changes with the next Spark release, but should help you feel familiar on how Spark works. There will be R support for Spark, less so for low level RDD operations but more so for its distributed machine learning algorithms as well as DataFrame objects.

The support for R in the Spark universe might be a game changer. R has always been great on doing exploratory and interactive analysis on small to medium datasets. With the addition of Spark, R can become a more viable tool for big datasets.

June is the current planned release date for Spark 1.4 which will allow R users to run data frame operations in parallel on the distributed memory of a cluster of computers. All of which is completely open source.

It will be interesting to see what possibilities this brings for the R community.

