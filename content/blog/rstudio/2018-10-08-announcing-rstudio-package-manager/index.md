---
title: 'Announcing RStudio Package Manager '
people:
  - Sean Lopp
date: '2018-10-17'
slug: announcing-rstudio-package-manager
categories:
- News
- RStudio Package Manager
tags:
- RStudio Package Manager
blogcategories:
- Products and Technology
- Company News and Events
events: blog
ported_from: rstudio
port_status: in-progress
---


We’re excited to announce the general availability of our newest RStudio professional product, [RStudio Package Manager](https://rstudio.com/products/package-manager). RStudio Package Manager helps your team, department, or entire organization centralize and organize R packages.

Get started with the [45 day evaluation](https://rstudio.com/products/package-manager/eval) today!

With more than 13,000 packages in the R ecosystem, managing the packages you and your teams need can be challenging. R users naturally want the latest, but everyone benefits from reproducibility, stability, and security in production code.

![](/blog-images/rspm-overview.png)

RStudio Package Manager is an on-premises server product that allows R users and IT to work together to create a central repository for R packages.  RStudio Package Manager supports your team wherever they run R, from bash scripts and Docker containers to RStudio, RStudio Server (Pro), Shiny Server (Pro), and RStudio Connect.


![](/blog-images/rspm-stakeholders.png)

Administrators set up the server using a scriptable command line interface (CLI), and R users install packages from the server with their existing tools.

![](/blog-images/rspm-release-setup.png)


We’ve spent the last year working with alpha and beta customers to ensure RStudio Package Manager is ready to meet the needs of your development and production use cases. 

### CRAN

If you’re an R user, you know about CRAN. If you’re someone who helps R users get access to CRAN, you probably know about network exceptions on every production node. With RStudio Package Manager, you can enable your R users to access CRAN without requiring a network exception on every production node. You can also automate CRAN updates on your schedule. You can choose to optimize disk usage and only download the packages you need or, alternatively, download everything up-front for completely offline networks. 

Currently, RStudio Package Manager does not serve binary packages from CRAN -- only source packages. This limitation won't affect server-based users, but may impact desktop users. Future versions of RStudio Package Manager will address this limitation.

![](/blog-images/rspm-release-cran.png)

### Subsets of CRAN

We know some projects call for even tighter restrictions. RStudio Package Manager helps admins create approved subsets of CRAN packages, and ensures that those subsets stay stable even as packages are added or updated over time. 

![](/blog-images/rspm-release-cmd.png)

### Internal Packages and Packages from GitHub

Sharing internal R code has never been easier. Administrators can add internal packages using the CLI. If your internal packages live in Git, RStudio Package Manager can automatically track your Git repositories and make commits or tagged releases accessible to users. The same tools make it painless to supplement CRAN with R packages from GitHub. 

![](/blog-images/rspm-release-git.png)

### Optimized for R

Regardless of your use case, RStudio Package Manager provides a seamless experience optimized for R users. Packages are versioned, automatically keeping older versions accessible to users, tools like Packrat, and platforms like RStudio Connect.

![](/blog-images/rspm-release-archive.png)

RStudio Package Manager also versions the repositories themselves, preserving the ability to always return the same set of R packages or receive the latest versions.

![](/blog-images/rspm-release-repoversion.png)

RStudio Package Manager records usage statistics. These metrics help administrators conduct audits and give R users an easy way to discover popular and useful packages.

![](/blog-images/rspm-release-usage.png)

### Download Today

Get started with the [45-day evaluation](https://rstudio.com/products/package-manager/eval) or check out our [demo server](http://demo.rstudiopm.com). Read the [admin guide](http://docs.rstudio.com/rspm/admin) for answers to more questions and a guide to installation and setup. [Contact Sales](mailto:sales@rstudio.com) for more information.


	

