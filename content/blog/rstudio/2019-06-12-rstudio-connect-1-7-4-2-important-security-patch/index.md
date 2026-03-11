---
title: RStudio Connect 1.7.4.2 - Important Security Patch
people:
  - Sean Lopp
date: '2019-06-13'
slug: rstudio-connect-1-7-4-2-important-security-patch
categories:
- RStudio Connect
tags:
- Connect
- News
- RStudio Connect
blogcategories:
- Products and Technology
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: raw
---


This RStudio Connect patch release addresses an urgent security update and an important bug fix.

- **Security Update: Password Authentication**  
A vulnerability has been identified for customers using RStudio Connect's built-in [password authentication](https://docs.rstudio.com/connect/1.7.4.2/admin/authentication.html#authentication-password). Due to the risks involved, **password authentication will now require the configuration setting [`Server.Address`](https://docs.rstudio.com/connect/1.7.4.2/admin/appendix-configuration.html#appendix-configuration-server) for operations that will send emails**. If this setting is not configured an error will occur for these operations. More detailed information about the vulnerability will be released in a future post. We have received no reports of impacted customers, but we recommend customers using password authentication upgrade immediately.


- **Bug Fix: SLES Installer**  
Prior versions of RStudio Connect used a shared RPM installer for SLES and RedHat. This installer was found to be incompatible for customers upgrading to SUSE Linux Enterprise Server 12 SP4 and SUSE Linux Enterprise Server 15. This version introduces a separate installer for SUSE systems. See the [download page](https://rstudio.com/products/connect/download-commercial) for details.  


> **Upgrade Planning**  
> There are no special considerations when upgrading from RStudio Connect v1.7.4 to this 
> patch release. Upgrades should take less than five minutes. If you are upgrading from an older release, please
> consult the intermediate [release notes](https://docs.rstudio.com/connect/news). 

More information on the new features added in RStudio Connect 1.7.4 is available in a [prior post](https://blog.rstudio.com/2019/05/14/introducing-saml-in-rstudio-connect/).

