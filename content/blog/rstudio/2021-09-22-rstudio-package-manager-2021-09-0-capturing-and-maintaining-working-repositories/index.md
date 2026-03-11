---
title: "RStudio Package Manager 2021.09.0 - Capturing and Maintaining Working Repositories"
people:
  - Daniel Petzold
  - Brian Deitte
date: '2021-09-22'
slug: rstudio-package-manager-2021-09-0-capturing-and-maintaining-working-repositories
categories:
  - Featured
  - RStudio Package Manager
tags:
  - RStudio Package Manager
description: This release adds new management, service, and configuration options to RStudio Package Manager. Highlights include a more versatile repository calendar, more flexibility in serving multiple binary package versions, and more options for configuring git sources.
blogcategories:
- Products and Technology
alttext: big interlocking gears
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: raw
---
<caption>
Photo by <a href="https://unsplash.com/@timmossholder?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer">Tim Mossholder</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"  target="_blank" rel="noopener noreferrer">Unsplash</a>
</caption>


This release adds new management, service, and configuration options to RStudio Package Manager. Highlights include a more versatile repository calendar, more flexibility in serving multiple binary package versions, and more options for configuring git sources.

Packages are critical to data science, but keeping them in sync and working together at scale is often a challenging, frustrating task. <a href="https://www.rstudio.com/products/package-manager" target = "_blank" rel = "noopener noreferrer">RStudio Package Manager</a> is our pro offering that simplifies package management across your team, department, or entire organization for reproducible, maintainable, and secure code repositories. This release includes improvements on our management, service, and configuration options, such as: 

* A new, more flexible repository calendar.  Users can now freeze to any date in the repository's history, and frozen repository URLs now include the snapshot date in YYYY-MM-DD format.
* More flexibility in serving multiple binary package versions. RStudio Package Manager can now serve binary packages for new R versions and operating systems without upgrading to a new version.
* More configuration options when using git sources. You can now edit the SSH key, git URL, branch, and subdirectories of existing sources. You can also now use a file to watch for changes.
* Improvements in logging standardization and usability. Logs now work more like other RStudio team products, including being available through journalclt.
* Support for the Bioconductor books repository.
* Many important bug fixes.

Check out more in our <a href="https://docs.rstudio.com/rspm/news/#rstudio-package-manager-2021090" target = "_blank" rel = "noopener noreferrer">release notes</a> to learn more details and click <a href="https://www.rstudio.com/products/package-manager/download-commercial/" target = "_blank" rel = "noopener noreferrer">here</a> to upgrade today.

> NOTE on versioning: As part of this release, we’ve moved to calendar-based versioning. <a href="https://blog.rstudio.com/2021/08/30/calendar-versioning-for-commercial-rstudio-products/" target = "_blank" rel = "noopener noreferrer">See this blog post</a> for details.

**For more information**

* For an overview of best practices for open source package management, check out this free webinar, <a href="https://www.rstudio.com/resources/webinars/managing-packages-for-open-source-data-science/" target = "_blank" rel = "noopener noreferrer">Managing Packages for Open Source Data Science</a>, and <a href="https://blog.rstudio.com/2021/05/06/pkg-mgmt-admins/" target = "_blank" rel = "noopener noreferrer">this series of blog posts</a>.
* For more information on RStudio Package Manager, see the <a href="https://www.rstudio.com/products/package-manager/" target = "_blank" rel = "noopener noreferrer">RStudio Package Manager product page</a>.
