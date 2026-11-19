---
date: '2026-10-06'
description: 'Learn pharmacometrics in R with nlmixr2. We build a population pharmacokinetic (PopPK) model from sparse neonatal phenobarbital data, then simulate flat and weight-based dosing to see which regimen keeps preterm infants in the therapeutic window.


  📖 Full blog post with code: TBD


  Matthew Fidler and Janice Goh walk through a reproducible pharmacometrics workflow in R using 155 phenobarbital concentrations from 59 preterm infants. Clinicians gave 589 doses during routine care and drew few blood samples: 51 of the 59 infants have three or fewer. The dataset (Grasela & Donn, 1985) ships with nlmixr2 as pheno_sd, so you can run every step yourself.


  The clinical question is whether a flat dose sized for the average 1.5 kg infant is safe for a 900 g baby.


  IN THIS VIDEO

  - Treat a PK model as a nonlinear mixed-effects model with a system of ODEs as its mean function

  - Write an nlmixr2 model with ini() and model() blocks

  - Fit a one-compartment model with SAEM and read the clearance and volume estimates alongside their between-subject variability (BSV)

  - Add allometric weight covariates with model piping, cutting BSV on clearance from 37% to 17% and on volume from 47% to 18%

  - Select covariates automatically with the experimental VAE estimation method in nlmixr2 7.0

  - Check the model with individual fits and a prediction-corrected visual predictive check (VPC)

  - Simulate both regimens from the fitted model object with rxode2''s rxSolve()


  KEY RESULT

  The target phenobarbital concentration was 15 to 40 mg/L. A flat regimen (30 mg load + 1.9 mg every 12 h) put 1.5 kg infants on target but overdosed 0.7 kg infants (median 41 mg/L). At 3.1 kg, fewer than 4% of infants reached the target range. A weight-based regimen (20 mg/kg load + 1.25 mg/kg every 12 h) kept 96% or more of simulated infants in range from 0.7 to 3.1 kg.


  CHAPTERS

  00:00 The clinical question: dosing preterm infants

  00:00 Pharmacometrics for people who know mixed models

  00:00 Exploring the pheno_sd dataset

  00:00 Writing your first nlmixr2 model

  00:00 Adding weight as a covariate (allometric scaling)

  00:00 Automated covariate selection with VAE

  00:00 Model diagnostics: individual fits and VPC

  00:00 Simulating flat vs. weight-based dosing

  00:00 The nlmixr2 ecosystem: babelmixr2, nonmem2rx, monolix2rx

  00:00 Getting started


  FAQ

  What is pharmacometrics?

  Pharmacometricians build mathematical models of how drugs move through the body and act on it, then use those models to choose a dose, a schedule, and the patients who need something different. Sponsors and regulators base the dosing sections of drug labels on these models.


  What is nlmixr2?

  nlmixr2 is a free, open-source R package for nonlinear mixed-effects modeling. You can fit population PK/PD models and simulate from them without leaving R.


  Does nlmixr2 work with NONMEM and Monolix?

  Yes. babelmixr2 runs the same nlmixr2 model in NONMEM or Monolix. nonmem2rx and monolix2rx import existing NONMEM and Monolix runs into R.


  Why use weight-based dosing in neonates?

  Drug clearance and volume of distribution scale with body size. The infants in this dataset weigh 0.6 to 3.6 kg, and a flat dose produced a 3.5-fold exposure gradient across that range in simulation.


  RESOURCES

  - Install: install.packages("nlmixr2")

  - nlmixr2 website: https://nlmixr2.org

  - nlmixr2 7.0 release: https://blog.nlmixr2.org/blog/2026-08-05-nlmixr2-7/

  - Model library (nlmixr2lib): https://github.com/nlmixr2/nlmixr2lib

  - babelmixr2: https://nlmixr2.github.io/babelmixr2/

  - nonmem2rx: https://nlmixr2.github.io/nonmem2rx/

  - rxode2: https://nlmixr2.github.io/rxode2/

  - Blog source code: https://github.com/nlmixr2/blog

  - Windows users need Rtools: https://cran.r-project.org/bin/windows/Rtools/


  DISCLAIMER

  This teaching example uses a 1985 dataset with one compartment and one covariate. It is not clinical dosing guidance. Clinicians and pharmacists manage real neonatal phenobarbital dosing and account for postnatal age and maturation.


  DATA SOURCE

  Grasela TH Jr, Donn SM. Neonatal population pharmacokinetics of phenobarbital derived from routine clinical data. Dev Pharmacol Ther. 1985;8(6):374-383.


  #Pharmacometrics #RStats #nlmixr2 #PopPK #Pharmacokinetics'
image: thumbnail.jpg
people: []
resource_type: video
resources: []
software: []
tags:
- rstudio
- data science
- machine learning
- python
- stats
- tidyverse
- data visualization
- data viz
- ggplot
- coding
- connect
- server pro
- shiny
- rmarkdown
- package manager
- CRAN
- interoperability
- serious data science
- dplyr
- ggplot2
- github
- data wrangling
- tidy data
- lazy evaluation
- tidymodels
- statistics
- debugging
- programming education
- rstats
- open source
- OSS
- pharmacometrics
- nlmixr2
- poppk
- pk modeling in r
- pediatric dosing
- r for pharma
- pharmacokinetic modeling
- pharmacometrics in r
title: 'Pharmacometrics in R: Population PK Modeling with nlmixr2'

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 2
  date: '2026-10-06T19:06:04Z'
  definition: hd
  description: 'Learn pharmacometrics in R with nlmixr2. We build a population pharmacokinetic (PopPK) model from sparse neonatal phenobarbital data, then simulate flat and weight-based dosing to see which regimen keeps preterm infants in the therapeutic window.


    📖 Full blog post with code: TBD


    Matthew Fidler and Janice Goh walk through a reproducible pharmacometrics workflow in R using 155 phenobarbital concentrations from 59 preterm infants. Clinicians gave 589 doses during routine care and drew few blood samples: 51 of the 59 infants have three or fewer. The dataset (Grasela & Donn, 1985) ships with nlmixr2 as pheno_sd, so you can run every step yourself.


    The clinical question is whether a flat dose sized for the average 1.5 kg infant is safe for a 900 g baby.


    IN THIS VIDEO

    - Treat a PK model as a nonlinear mixed-effects model with a system of ODEs as its mean function

    - Write an nlmixr2 model with ini() and model() blocks

    - Fit a one-compartment model with SAEM and read the clearance and volume estimates alongside their between-subject variability (BSV)

    - Add allometric weight covariates with model piping, cutting BSV on clearance from 37% to 17% and on volume from 47% to 18%

    - Select covariates automatically with the experimental VAE estimation method in nlmixr2 7.0

    - Check the model with individual fits and a prediction-corrected visual predictive check (VPC)

    - Simulate both regimens from the fitted model object with rxode2''s rxSolve()


    KEY RESULT

    The target phenobarbital concentration was 15 to 40 mg/L. A flat regimen (30 mg load + 1.9 mg every 12 h) put 1.5 kg infants on target but overdosed 0.7 kg infants (median 41 mg/L). At 3.1 kg, fewer than 4% of infants reached the target range. A weight-based regimen (20 mg/kg load + 1.25 mg/kg every 12 h) kept 96% or more of simulated infants in range from 0.7 to 3.1 kg.


    CHAPTERS

    00:00 The clinical question: dosing preterm infants

    00:00 Pharmacometrics for people who know mixed models

    00:00 Exploring the pheno_sd dataset

    00:00 Writing your first nlmixr2 model

    00:00 Adding weight as a covariate (allometric scaling)

    00:00 Automated covariate selection with VAE

    00:00 Model diagnostics: individual fits and VPC

    00:00 Simulating flat vs. weight-based dosing

    00:00 The nlmixr2 ecosystem: babelmixr2, nonmem2rx, monolix2rx

    00:00 Getting started


    FAQ

    What is pharmacometrics?

    Pharmacometricians build mathematical models of how drugs move through the body and act on it, then use those models to choose a dose, a schedule, and the patients who need something different. Sponsors and regulators base the dosing sections of drug labels on these models.


    What is nlmixr2?

    nlmixr2 is a free, open-source R package for nonlinear mixed-effects modeling. You can fit population PK/PD models and simulate from them without leaving R.


    Does nlmixr2 work with NONMEM and Monolix?

    Yes. babelmixr2 runs the same nlmixr2 model in NONMEM or Monolix. nonmem2rx and monolix2rx import existing NONMEM and Monolix runs into R.


    Why use weight-based dosing in neonates?

    Drug clearance and volume of distribution scale with body size. The infants in this dataset weigh 0.6 to 3.6 kg, and a flat dose produced a 3.5-fold exposure gradient across that range in simulation.


    RESOURCES

    - Install: install.packages("nlmixr2")

    - nlmixr2 website: https://nlmixr2.org

    - nlmixr2 7.0 release: https://blog.nlmixr2.org/blog/2026-08-05-nlmixr2-7/

    - Model library (nlmixr2lib): https://github.com/nlmixr2/nlmixr2lib

    - babelmixr2: https://nlmixr2.github.io/babelmixr2/

    - nonmem2rx: https://nlmixr2.github.io/nonmem2rx/

    - rxode2: https://nlmixr2.github.io/rxode2/

    - Blog source code: https://github.com/nlmixr2/blog

    - Windows users need Rtools: https://cran.r-project.org/bin/windows/Rtools/


    DISCLAIMER

    This teaching example uses a 1985 dataset with one compartment and one covariate. It is not clinical dosing guidance. Clinicians and pharmacists manage real neonatal phenobarbital dosing and account for postnatal age and maturation.


    DATA SOURCE

    Grasela TH Jr, Donn SM. Neonatal population pharmacokinetics of phenobarbital derived from routine clinical data. Dev Pharmacol Ther. 1985;8(6):374-383.


    #Pharmacometrics #RStats #nlmixr2 #PopPK #Pharmacokinetics'
  duration: 675
  has_captions: false
  language: en
  last_updated: '2026-11-12T12:18:01.684986+00:00'
  like_count: 18
  playlist: ''
  tags:
  - rstudio
  - data science
  - machine learning
  - python
  - stats
  - tidyverse
  - data visualization
  - data viz
  - ggplot
  - coding
  - connect
  - server pro
  - shiny
  - rmarkdown
  - package manager
  - CRAN
  - interoperability
  - serious data science
  - dplyr
  - ggplot2
  - github
  - data wrangling
  - tidy data
  - lazy evaluation
  - tidymodels
  - statistics
  - debugging
  - programming education
  - rstats
  - open source
  - OSS
  - pharmacometrics
  - nlmixr2
  - poppk
  - pk modeling in r
  - pediatric dosing
  - r for pharma
  - pharmacokinetic modeling
  - pharmacometrics in r
  thumbnail: https://i.ytimg.com/vi/ZNHOT_AjmYY/maxresdefault.jpg
  title: 'Pharmacometrics in R: Population PK Modeling with nlmixr2'
  url: https://www.youtube.com/watch?v=ZNHOT_AjmYY
  view_count: 1498
---

