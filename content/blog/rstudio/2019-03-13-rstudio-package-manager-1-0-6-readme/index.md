---
title: RStudio Package Manager 1.0.6 - README
people:
  - Sean Lopp
date: '2019-03-13'
slug: rstudio-package-manager-1-0-6-readme
categories:
- RStudio Package Manager
- News
tags:
- Packages
- RStudio Package Manager
blogcategories:
- Products and Technology
- Company News and Events
- Open Source
events: blog
ported_from: rstudio
port_status: in-progress
---


The 1.0.6 release of RStudio Package Manager helps R users understand packages.
The primary feature in this release is embedded package READMEs, detailed below. 
If you're new to Package Manager, it is an on-premise product built to give teams and organizations reliable and consistent package management. Download an [evaluation
today](https://rstudio.com/products/package-manager).

{{< figure src="/blog-images/rspm-106-readmes.png" caption="View package READMEs in Package Manager" alt= "View package READMEs in Package Manager">}}

## Package READMEs

Many R packages have rich README files that can include:

- An introduction to the package
- Examples for key functions
- Badges to indicate download counts, build status, code coverage, and other metrics
- Other helpful information, like the package's hex sticker!

This information can help a  new user when they are first introduced to a package, or help an experienced user or admin gauge package quality. Package READMEs distill and supplement the rich information available in vignettes, Description files, and help files. 

Starting in version 1.0.6, READMEs are automatically shown alongside the traditional package metadata. For CRAN packages, Package Manager will automatically show a README for the 12,000 CRAN packages that have them. READMEs are also displayed for internal packages [sourced from Git](https://docs.rstudio.com/rspm/1.0.6/admin/repositories.html#git-sources) or [local files](https://docs.rstudio.com/rspm/1.0.6/admin/quickstarts.html#quickstart-local). These READMEs provide an easy way for package authors to document their code for colleagues, publicize new releases and features, and disseminate knowledge to team members. 


## Deprecations, Breaking Changes, and Security Updates

- Version 1.0.6 includes a number of updates to Package Manager's built-in CRAN source. Customers using an internet-connected server *do not need to take any action*. Updates will be applied during the next CRAN sync. *Offline, air-gapped customers should following [these instructions](https://docs.rstudio.com/rspm/1.0.6/admin/air-gapped.html#air-gapped-upgrade) to re-fetch the CRAN data immediately after upgrading, and then run the `rspm sync` command.*

Please consult the full [release notes](https://docs.rstudio.com/rspm/news/).

> #### Upgrade Planning
> Please note the breaking changes and deprecations above. Upgrading to 1.0.6 from
> 1.0.4 will take less than five minutes. There will be a five-to-ten minute delay 
> in the next CRAN sync following the upgrade. If you are upgrading from an earlier 
> version, be sure to consult the release notes for the intermediate releases, as well.

Don't see that perfect feature? Wondering why you should be worried about
package management? 
[Email us](mailto:sales@rstudio.com); our product team is happy to help!

- [Admin Guide](https://docs.rstudio.com/rspm/admin)
- [Overview PDF](https://www.rstudio.com/wp-content/uploads/2018/07/RStudio-Package-Manager-Overview.pdf)
- [Introductory Webinar](https://resources.rstudio.com/webinars/introduction-to-the-rstudio-package-manager-sean-lopp)
- [Online Demo](https://demo.rstudiopm.com)

