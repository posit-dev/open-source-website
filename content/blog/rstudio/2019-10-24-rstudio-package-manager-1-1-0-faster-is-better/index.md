---
title: Package Manager 1.1.0 - No Interruptions
people:
  - Sean Lopp
date: '2019-11-07'
slug: package-manager-v1-1-no-interruptions
categories:
- RStudio Package Manager
tags:
- packages
- RSPM
- RStudio Package Manager
blogcategories:
- Products and Technology
events: blog
ported_from: rstudio
port_status: raw
---


No interruptions. That was our team's goal for RStudio Package Manager 1.1.0 - we set
out to make R package installation fast enough that it wouldn't interrupt your
work. More and more data scientists use Linux environments, whether to access extra
horsepower during development or to run production code in containers.
Unfortunately, the rise in Linux environments has seen a corresponding increase
in package installation pain. For Windows and Mac OS, CRAN provides pre-compiled
binary packages that install almost instantly, but the same binaries are not available on
Linux. As a result, data scientists can lose their train of thought, or put off
trying out a new method, all because they have to wait for new packages to compile and install.
New users often face a tedious hour-long setup process before they can try out
environments. IT/DevOps engineers are forced to wait any time they want to
build a new image, deploy to production, or restore an environment.

RStudio Package Manager already makes it easy for an organization to control and
distribute R packages. Now, packages from CRAN can be immediately available for
deployment on Linux systems, through Linux package binaries. These binaries
install significantly faster and are available to all Package Manager clients
wherever your organization uses R. Binaries are supported for a range of R
versions and platforms, for more than 80% of CRAN packages, and they are updated
every week! Binaries make it easier for users to get started, simpler for
admins to manage environments, and make it dramatically easier to implement automation.

<img src="/blog/images/rspm-110-install.gif" caption="Side-by-side install time comparison" alt= "Side-by-side install time comparison">

To see the difference for yourself, try installing a package on your Linux
server using our demo server:

```r
# First, pick your operating system
DISTRO <- 'xenial'  # choices: xenial, bionic, centos7, opensuse42, opensuse15

# Next, install from our demo server
install.packages('dplyr', repos = sprintf('https://demo.rstudiopm.com/cran/__linux__/%s/latest', DISTRO), lib = tempdir())

# Finally, compare to how long it takes to install from CRAN
install.packages('dplyr', repos = 'https://cran.rstudio.com', lib = tempdir())
```

At RStudio, we use these binaries in production every day. Although this [community
post](https://community.rstudio.com/t/faster-package-installs-on-linux-with-package-manager-beta-release/39607)
contains more information about the previous beta, we are excited to announce
that with v1.1.0, the binaries are ready for your production systems. Support is
available for offline or air-gapped environments.

## Other Updates

In addition to adding support for Linux package binaries, the 1.1.0 release
concludes more than a year of updates since the 1.0.0 release, adding:  

- [System dependency](https://blog.rstudio.com/2019/04/18/rstudio-package-manager-1-0-8-system-requirements/) information for R packages  
- [Package READMEs](https://blog.rstudio.com/2019/03/13/rstudio-package-manager-1-0-6-readme/) to help discover documentation  
- A [calendar](https://blog.rstudio.com/2019/01/30/time-travel-with-rstudio-package-manager-1-0-4/) to make version management a breeze  
- Significant improvements for IT, including performance improvements, security updates, and new storage options  

Please review the [full release notes](https://docs.rstudio.com/rspm/news).

> #### Upgrade Planning
> Upgrading to 1.1.0 from 1.0.10 or earlier is a major update but will take less than five minutes. If you are
> upgrading from an earlier version, be sure to consult the release notes for the
> intermediate releases, as well.

Package management is critical for making your data science reproducible, over
time, and across your organization. Wondering where you should start? [Email
us](mailto:sales@rstudio.com), our product team is happy to help!

#### New to RStudio Package Manager? 

[Download](https://rstudio.com/products/package-manager/) the 45-day evaluation
today to see how RStudio Package Manager can help you, your team, and your
entire organization access and organize R packages. Learn more with our [online
demo server](https://demo.rstudiopm.com) or [latest webinar](https://resources.rstudio.com/webinars/introduction-to-the-rstudio-package-manager-sean-lopp).

- [Admin Guide](https://docs.rstudio.com/rspm/admin)
- [Overview PDF](https://www.rstudio.com/wp-content/uploads/2018/07/RStudio-Package-Manager-Overview.pdf)
- [Introductory Webinar](https://resources.rstudio.com/webinars/introduction-to-the-rstudio-package-manager-sean-lopp)
- [Online Demo](https://demo.rstudiopm.com)

