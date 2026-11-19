---
title: Parallel computation
image: page-1.png
resource_type: cheatsheet
by: community
date: '2019-03-01'
description: Run R code in parallel using the parallel, future, foreach, and related packages across multiple CPU cores.
download_url: parallel_computation.pdf
people:
- Ardalan Mirshani
thumbnails:
- page-1.png
languages:
- R
---

This cheat sheet covers the main approaches to parallel computing in R, from the core `parallel` package with `makeCluster()` and `clusterApply()`, to the `future` and `future.apply` packages for asynchronous evaluation, and the `foreach` package with `doParallel` and `doFuture` backends. It also addresses load balancing for uneven task times.

## What's covered
- Splitting strategies – by task or by data; hardware considerations (CPU cores, shared vs. distributed memory)
- Map-reduce vs. master-worker models – Spark/Hadoop vs. snow/foreach approaches
- `parallel` package – `makeCluster()`, `clusterApply()`, `clusterEvalQ()`, `clusterExport()`, `stopCluster()`
- `foreach` – `%do%` (sequential) and `%dopar%` (parallel), `.combine`, `.packages`, `.export`
- `doParallel` – `registerDoParallel()` backend for `foreach`
- `future` – plan strategies, `%<-%` assignment operator
- `future.apply` – `future_lapply()`, `future_sapply()`, `future_apply()`
- `doFuture` – `registerDoFuture()` backend for `foreach`
- Load balancing – `clusterApplyLB()`, `itertools::isplitVector()`
