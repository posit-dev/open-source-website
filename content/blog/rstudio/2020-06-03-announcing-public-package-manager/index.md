---
title: Announcing Public Package Manager and v1.1.6
people:
  - Sean Lopp
date: '2020-07-01'
slug: announcing-public-package-manager
categories:
- RStudio Package Manager
tags:
- packages
- RStudio Package Manager
- RStudio Package Manager
resources:
- name: public-package-manager
  src: public-package-manager.png
  title: The homepage of the public package manager site
blogcategories:
- Products and Technology
events: blog
ported_from: rstudio
port_status: in-progress
---


Today we are excited to release version 1.1.6 of RStudio Package Manager and announce
https://packagemanager.rstudio.com. This service builds on top of the work done by CRAN, to offer the R community:  

- Access to **pre-compiled packages on Linux** via `install.packages` resulting in [significantly faster](https://blog.rstudio.com/2019/11/07/package-manager-v1-1-no-interruptions/) package install times on Linux systems including cloud servers, CI/CD systems, and Docker containers.  
- **Historical checkpoints for CRAN** enabling reproducible work, and even [time travel](https://blog.rstudio.com/2019/01/30/time-travel-with-rstudio-package-manager-1-0-4/), by freezing package dependencies with a one-line repository option. 
- Expanded **Windows support for older versions of R**, allowing you to access the latest versions of packages on older versions of R without compiling from source.

We invite everyone to try this service, but please note we do not currently
support package binaries for Mac OS though we are considering adding support in
the future. The easiest way to get started is by visiting the [Package Manager
Setup Page](https://packagemanager.rstudio.com/client/#/repos/1/overview). You
can also view [frequently asked
questions](https://support.rstudio.com/hc/en-us/articles/360046703913) or [learn
more about RStudio Package
Manager](https://rstudio.com/products/package-manager).

### Relationship to CRAN

This service builds off of the work done by CRAN and is a supplement to
RStudio’s [popular CRAN mirror](https://cran.rstudio.com). If CRAN were a
brewery, Package Manager would be your local liquor store; Package Manager
wouldn't be possible without CRAN, but we hope it makes it a little easier to
install packages without having to go to the (literal) source each time.

For **package authors**, before a package is available on Package Manager it must be
accepted, tested, and distributed on CRAN. Package Manager watches for those
updates and then carefully builds updated or new packages on additional operating systems
and R versions, finally adding them as a versioned checkpoint.

For **R users**, Package Manager acts like a regular CRAN mirror, ensuring all
the code you know how to write automatically works. Note that Package Manager
can lag behind CRAN by a few days, so if you need the latest packages you can
add both Package Manager and CRAN to your repo option.


### Community Integrations 

In addition to using the Public Package Manager directly, R users can benefit
from community integrations that access the service automatically:

- The [renv](https://github.com/rstudio/renv) package helps R users manage
package environments over time, and is able to use the  service to provide faster
install times and increase cross-platform project portability.

- The [actions](https://github.com/r-lib/actions) package provides GitHub
Actions for package authors taking advantage of CI/CD workflows such as
automated testing. The package uses Public Package Manager to speed up actions
and eliminate redundant package compilation.

- The popular [rocker](https://www.rocker-project.org/) project gives R users a
convenient way to work with Docker. This ecosystem increasingly takes advantage
of Public Package Manager to provide faster package installs within a container
as well as versioned installs for reproducible research.

If your community project would benefit from Public Package Manager please
[create a topic
](https://community.rstudio.com/c/r-admin/package-manager?tags=package-manager%2Cpublic-rspm)
on the RStudio Community.

### Support, Legal Terms, and Feedback

Please consult the [RStudio Terms of
Use](https://rstudio.com/about/rstudio-service-terms-of-use/) prior to use. If
you use R in an organization, we recommend [evaluating RStudio Package
Manager](https://rstudio.com/products/package-manager) which includes all the
benefits of the public Package Manager plus additional controls and features for
professional data science teams: the ability to serve packages in offline
environments, access to curated subsets of CRAN, and the ability to share
private R packages.

RStudio does not provide direct support for this service you can get help through RStudio Community. The best way to ask a question is to [create a
topic](https://community.rstudio.com/c/r-admin/package-manager?tags=package-manager%2Cpublic-rspm)
on RStudio Community after reviewing the
[FAQ](https://support.rstudio.com/hc/en-us/articles/360046703913). This forum
is also the best place to leave suggestions or feedback, we're eager to learn
how we can better support your needs!

If you are interested in learning more about how Package Manager works, these
open source repositories provide information on how we [build and distribute
R](https://github.com/rstudio/r-builds), handle [system
requirements](https://github.com/rstudio/r-system-requirements), and [manage our
build environment](https://github.com/rstudio/r-docker). Package Manager relies
on the tireless work of a team of engineers, thousands of compute hours, and
TBs of storage and network IO.

The RStudio Package Manager [admin guide](https://docs.rstudio.com/rspm/admin)
also provides details on how Package Manager [interacts with
CRAN](https://docs.rstudio.com/rspm/admin/repositories/#repo-syncing), how it
[serves binary packages](https://docs.rstudio.com/rspm/admin/serving-binaries/),
and details the [additional
options](https://docs.rstudio.com/rspm/admin/getting-started/configuration/)
available for on-premise use.


### New Updates in RStudio Package Manager v1.1.6

In addition to https://packagemanager.rstudio.com, the 1.1.6 release offers the community and customers incremental updates including:  
- Access to an [API to easily integrate Package   Manager](https://packagemanager.rstudio.com/__api__/swagger/index.html) with other systems and services  
- Support for R 4.0 and Ubuntu 20   
- More robust access and debugging when distributing packages from Git (applicable to on-premise customers only)  

Please review the full [release notes](https://docs.rstudio.com/rspm/news/) and consider [upgrading to the latest
version](https://docs.rstudio.com/rpm/installation/). 



