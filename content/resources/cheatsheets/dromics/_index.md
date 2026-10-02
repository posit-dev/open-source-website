---
title: DRomics
image: page-1.png
resource_type: cheatsheet
by: community
date: '2023-01-01'
description: Fit dose-response models to omics data, compute benchmark doses, and visualize results for multi-level biological annotation.
download_url: DRomics.pdf
people:
- Aurélie Siberchicot
thumbnails:
- page-1.png
languages:
- R
---

DRomics provides a structured workflow for analyzing dose-response relationships in omics datasets, including microarray, RNA-seq, continuous omics, and anchoring data. The workflow covers data import and preprocessing, selection of significantly responsive items, dose-response model fitting, benchmark dose (BMD) calculation, and bootstrap confidence intervals.

## What's covered
- Format of data – identifiers, doses, and signal columns
- Step 1 – import, check, and pretreatment (`microarraydata()`, `RNAseqdata()`, `PCAdataplot()`)
- Step 2 – selection of significantly responsive items (`itemselect()`)
- Step 3 – dose-response modelling (`drcfit()`)
- Step 4 – computation of benchmark doses (`bmdcalc()`)
- Step 5 – bootstrap confidence intervals (`bmdboot()`)
- Typical workflow script
- BMD plot – `bmdplot()` and `bmdplotwithgradient()`
- Trend plot – `trendplot()`
- Sensitivity plot – `sensitivityplot()`
- Dose-response curves plot – `curvesplot()`
