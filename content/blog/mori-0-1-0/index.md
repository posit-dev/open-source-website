---
title: 'mori: Shared memory for R objects'
date: 2026-04-23T00:00:00.000Z
people:
  - Charlie Gao
description: >
  mori is a new R package for sharing R objects across processes via OS-level
  shared memory. Parallel workers get zero-copy, lazy ALTREP access to the same
  physical pages — share once, read anywhere.
image: featured.jpg
image-alt: >
  Macro close-up of a computer RAM module, showing the blue circuit board and
  metallic connectors in sharp detail with a shallow depth-of-field blur.
topics:
  - Best Practices
software:
  - mori
languages:
  - R
tags:
  - Parallelism
photo:
  url: https://unsplash.com/photos/macro-shot-photo-of-a-computer-ram-lYxQ5F9xBDM
  author: Liam Briese
nohero: false
hidesubscription: false
---


We're pleased to announce the first CRAN release of [mori](https://shikokuchuo.net/mori/).

Until now, parallel R has meant serializing your data to every worker and duplicating it in each worker's RAM. Eight workers × 1 GB is 8 GB, plus the serialization, transfer, and deserialization cost to get it there. R processes don't share memory --- each has its own heap, so data crosses between them through a serialization pipe.

mori changes that. It places an R object once into OS-level shared memory and lets every process on the machine read the same physical pages directly --- with no data copying between processes.

``` r
install.packages("mori")
```

mori is built on R's [ALTREP](https://svn.r-project.org/R/branches/ALTREP/ALTREP.html) (Alternative Representation) framework, which lets a package expose a custom vector backend that reads its data from somewhere other than ordinary R memory --- a memory map, a database, a compressed store, or in this case, OS shared memory.

## How it looks

The entry point is `share()`. You pass it an R object, you get back a shared version of it that you can use the same way as the original:

``` r
library(mori)

set.seed(42)
x <- share(rnorm(1e6))
mean(x)
```

    [1] 0.0005737398

`share()` works on atomic vector types, lists, and data frames --- it writes them directly into shared memory with attributes preserved. In practice that also covers tibbles, data.tables, factors, dates, and matrices, since they're built on those types. Environments, functions, S4 objects, and external pointers are passed through as the original object --- `share()` skips them, since their references don't map naturally to shared pages.

The returned object is an ALTREP view into shared memory --- it costs no additional RAM beyond the original region. It also serializes compactly: instead of sending the full 8 MB payload, mori's ALTREP hooks serialize shared objects as their shared-memory name, just over 100 bytes on the wire.

``` r
x |> serialize(NULL) |> length()
```

    [1] 124

That compact serialization is what makes the rest of the picture work.

## Parallel workers, one copy

<img src="mori-diagram.svg" data-fig-alt="Diagram: share() writes an R object once into OS-level shared memory; multiple worker processes each memory-map the same region via zero-copy ALTREP wrappers, so every worker sees the same physical pages with no deserialization." />

mori pairs naturally with [mirai](https://mirai.r-lib.org/). When you send a shared object to a local daemon, only the shared-memory name crosses the wire; the daemon maps the same physical pages and sees the full data with no deserialization cost. The same is true for any other parallel backend that uses R serialization.

Here's the motivating case --- a bootstrap across eight workers on a 200 MB data frame:

``` r
library(mirai)
library(purrr)

daemons(8)

df <- as.data.frame(matrix(rnorm(25e6), ncol = 5))
shared_df <- share(df)

boot <- \(i) colMeans(data[sample(nrow(data), replace = TRUE), ])

# Without mori — each daemon deserializes its own copy
system.time(
  map(1:8, in_parallel(\(i) boot(i), boot = boot, data = df))
)
```

       user  system elapsed 
      0.409   3.102  10.015 

``` r
# With mori — each daemon maps the same shared memory
system.time(
  map(1:8, in_parallel(\(i) boot(i), boot = boot, data = shared_df))
)
```

       user  system elapsed 
      0.001   0.001   4.784 

``` r
daemons(0)
```

The payload each daemon receives is ~300 bytes instead of 200 MB --- roughly 700,000× smaller. There's a ~2× wall-clock saving on this run, and eight workers now share a single 200 MB copy in memory instead of materializing one each. The function is the same; the savings come from not copying data that's already in RAM.

`share()` itself is paid once upfront --- roughly the cost of one serialization to write into shared memory. Daemons don't pay a deserialize cost on the other end, since they read the same physical memory directly --- so even a single send is a net win, and the savings compound with every additional daemon.

The wall-clock gap depends on how much of the run is data transfer versus compute. On cheap per-task work --- bootstrap, cross-validation, parameter sweeps --- serialization dominates and the wall-clock win is largest; as each task involves more substantial compute, the ratio shrinks, although we always get the memory saving.

Lists and data frames travel element-wise too: sending a single column of a shared data frame transmits only that element's reference, not the whole data frame.

``` r
daemons(3)

x <- share(list(a = rnorm(1e6), b = rnorm(1e6), c = rnorm(1e6)))

mirai_map(x, \(v) lobstr::obj_size(v) |> format())[.flat]
```

          a       b       c 
    "840 B" "840 B" "840 B" 

``` r
daemons(0)
```

## What this unlocks

Anywhere parallel R workers process the same large dataset, `share()` removes the per-worker copy:

- A [Shiny](https://shiny.posit.co/) dashboard where every worker process reads from one shared reference dataset instead of loading its own.
- A [tidymodels](https://www.tidymodels.org/) `tune_grid()` sweep --- or a [targets](https://docs.ropensci.org/targets/) pipeline branching over model variants --- where every fit reads the same training data without copying it.
- Bootstrap, Monte Carlo, or permutation work dispatched across [mirai](https://mirai.r-lib.org/) or [crew](https://wlandau.github.io/crew/), where thousands of iterations all read from one shared dataset.

The pattern is the same in each case: call `share()` on your dataset once, then pass the result wherever you'd normally pass the data. Parallel dispatches that hit the serialization path transmit only the reference, not the data.

## Access and lifetime

A shared data frame lives in a single shared region, but ALTREP columns are only materialized when touched. A task that reads three columns out of one hundred pays for three --- character vectors are lazier still, with per-element access. Workers only pay for the data they actually touch.

Shared memory is tied to R's garbage collector. As long as the shared object (or anything extracted from it) is live in R, the data stays available; when the last reference is dropped, it's freed automatically with no manual cleanup. The process that called `share()` needs to hold its reference until a consumer has mapped a view --- from that point on, the view itself keeps the shared memory alive.

Mutations go through R's normal copy-on-write: editing a value inside a shared vector produces a private copy of that one vector, leaving the rest of the shared region untouched.

``` r
x <- share(rnorm(1e6))
lobstr::obj_size(x)
```

    960 B

``` r
x[1] <- 0  # local mutation materializes a private copy
lobstr::obj_size(x)
```

    8.00 MB

## Sharing by name

If you want to access a shared region from another process without going through serialization at all, you can pass its name directly:

``` r
x <- share(1:1e6)

nm <- shared_name(x)
nm
```

    [1] "/mori_2426_4"

``` r
# Works from another process; same session here to demonstrate
y <- map_shared(nm)
identical(x[], y[])
```

    [1] TRUE

Handy when the consumer needs to attach by name rather than receive the shared object through R's serialization path.

## How mori fits

R has had partial answers to cross-process data sharing before. [bigmemory](https://CRAN.R-project.org/package=bigmemory) offers shared `big.matrix` objects --- effective, but limited to numeric matrices. [SharedObject](https://bioconductor.org/packages/SharedObject/) on Bioconductor targets a similar goal with its own memory-sharing machinery, oriented around BiocParallel workflows. [Arrow](https://arrow.apache.org/docs/r/)'s memory-mapped Parquet gives zero-copy columnar reads across processes, though the data lives on disk. On Unix, `parallel::mclapply` gets shared memory via fork copy-on-write (until a worker writes to a page), with the usual fork caveats (unsafe in GUI sessions, with open DB connections, or alongside multithreaded libraries), and with no equivalent on Windows.

mori is usable across any backend that plugs into R's standard serialization --- mirai, future, parallel, foreach, callr --- with no special cooperation required. Atomic vectors, lists, and character vectors are all supported, with lazy per-element access preserved in every process. Lifetimes are managed by R's garbage collector: shared regions are freed automatically when the last reference drops. And mori itself is pure C --- POSIX shared memory on Linux and macOS, Win32 file mapping on Windows, nothing beyond the package to install.

## Try it

mori is [available from CRAN](https://CRAN.R-project.org/package=mori). The [package website](https://shikokuchuo.net/mori/) has a walkthrough of the mirai integration and full reference documentation. mori is designed to slot quietly into existing parallel-R workflows --- anywhere a worker currently receives a big dataset, `share()` it first and you're done. It complements [mirai](https://mirai.r-lib.org/): mirai handles async evaluation and daemon coordination, mori handles shared access to the data those daemons work on.

The package is in the experimental lifecycle stage while the API settles, so feedback and issue reports on [GitHub](https://github.com/shikokuchuo/mori/issues) are very welcome.
