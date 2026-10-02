---
title: oSCR
image: page-1.png
resource_type: cheatsheet
by: community
date: '2019-12-01'
description: Fit spatial capture-recapture models to estimate wildlife population density and detection probability.
download_url: oSCR.pdf
people:
- Gabriela Palomo-Munoz
thumbnails:
- page-1.png
- page-2.png
- page-3.png
languages:
- R
---

The oSCR package (pronounced "Oscar") implements spatial capture-recapture (SCR) models for wildlife population analysis. Following a workflow modeled after the unmarked package, users format encounter and trap-deployment data into a `scrFrame`, define the state space, fit likelihood-based models, and post-process results to obtain density and detection estimates.

## What's covered
- Getting the package – GitHub installation with `install_github("jaroyle/oSCR")`
- Format sampling data – encounter data file (edf), trap deployment file (tdf), `data2oscr()`, `scrFrame` structure and summary
- Create the state space – `make.ssDF()` with varying buffer and spatial resolution
- Modelling framework – single-session, multi-session, sex-structured, and multi-session sex-structured models
- Analyze the data – likelihood-based model fitting with AIC model selection
- Post-processing output – `get.real()` for back-transforming density, detection, and sigma estimates
