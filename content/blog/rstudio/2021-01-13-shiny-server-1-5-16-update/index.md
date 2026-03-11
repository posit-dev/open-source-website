---
title: Shiny Server 1.5.16 Update
people:
  - Kelly O'Briant
date: '2021-01-13'
slug: shiny-server-1-5-16-update
categories:
  - Featured
tags:
  - Shiny Server Pro
blogcategories:
  - Products and Technology
  - Open Source
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: raw
---

## Important Security Notice

A vulnerability was discovered in Shiny Server that could allow the download of published application source code directly from the server. This issue affects both Shiny Server Pro and the open source Shiny Server product.

**We recommend upgrading to the new version immediately.** If this is not possible, please contact [support@rstudio.com](mailto:support@rstudio.com) who will supply an interim fix that can be applied to the configuration.

### Release Notes

In addition to the important security patch described above, the following items have been addressed in this release:

* Fixed an issue where a failure in a certain phase of R process launching would result in a broken process being treated as a normal process, and repeatedly used to (unsuccessfully) serve new clients.
* In accordance with the RStudio Platform Support strategy, this release drops support for RedHat/CentOS 6. 
* Upgrades Node.js to 12.20.0.

Review the full [Shiny Server Pro Release Notes](https://support.rstudio.com/hc/en-us/articles/215642837-Shiny-Server-Pro-Release-History).

## Upgrade Instructions

### Shiny Server Pro

To perform an upgrade, download the newer package and install it using your package manager. Existing configuration settings are respected. Instructions are available for the following operating systems:

* [RedHat/CentOS](https://rstudio.com/products/shiny/download-commercial/redhat-centos/)
* [Ubuntu](https://rstudio.com/products/shiny/download-commercial/ubuntu/)
* [SLES/openSUSE](https://rstudio.com/products/shiny/download-commercial/suse/)

Please contact our [Support Team](mailto:support@rstudio.com) if you encounter any issues with the upgrade process. 

### Shiny Server Open Source 

To upgrade open source Shiny Server, download the newer package and install it using your package manager. Existing configuration settings are respected. Instructions are available for the following operating systems:

* [RedHat/CentOS](https://rstudio.com/products/shiny/download-server/redhat-centos/)
* [Ubuntu](https://rstudio.com/products/shiny/download-server/ubuntu/)
* [SLES/openSUSE](https://rstudio.com/products/shiny/download-server/suse/)
