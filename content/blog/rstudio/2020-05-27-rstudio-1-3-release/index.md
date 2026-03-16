---
title: RStudio 1.3 Released
people:
  - Jonathan McPherson
date: '2020-05-27'
slug: rstudio-1-3-release
categories:
- RStudio IDE
resources:
- name: screenshot
  src: rstudio-1-3-screenshot.png
  title: Screenshot of RStudio 1.3 showing a few of the new features.
blogcategories:
- Products and Technology
- Open Source
tags:
- RStudio IDE
events: blog
ported_from: rstudio
port_status: in-progress
---


Today we're excited to announce the general release of RStudio 1.3. This release features many major improvements to the IDE, including:

- Dramatically improved **accessibility** for sight-impaired users, which also upgrades keyboard navigation, contrast ratios, and visibility for everyone.
- A real-time **spell-checking engine**, with suggestions, customizable dictionaries, and a built-in whitelist for common data science terms.
- Extensible, in-IDE **tutorials** powered by the [`learnr` package](https://rstudio.github.io/learnr/).
- **Settings and preferences** are now stored in plain text files you can back up or manage with other tools; they can also be applied globally to all users on an RStudio Server.
- Improved compatibility with **R 4.0** and **iPad OS 13.1**.
- Many improvements to **RStudio Server security**, including idle timeouts and hardening against common types of attacks.
- Dozens of small productivity improvements, including **autosave**, **global replace**, **customizable file templates**, **Shiny jobs**, and more.

If you've purchased the Professional version of RStudio, this release also has some new capabilities for you:

- **RStudio Desktop Pro** can now function as a client for RStudio Server Pro; run your R session on your server with the convenience of native desktop windows and menus. 
- A new **user manager** on the Admin Dashboard makes it easy to manage licensed users on RStudio Server Pro.
- Many small improvements to the **Kubnernetes** and **Slurm** Job Launcher plugins.

See our [blog series on RStudio 1.3](/categories/rstudio-ide) for articles describing a selection of the new capabilities in detail, and the [RStudio 1.3 Release Notes](https://rstudio.com/products/rstudio/release-notes/) for a comprehensive list of features and bugfixes in this release.

A special thanks to [Dr Jonathan Godfrey](https://www.massey.ac.nz/massey/expertise/profile.cfm?stref=416430) and [JooYoung Seo](https://www.jooyoungseo.com/) for their insight into the new accessibility features, and to the hundreds of community members who helped us shape this release with their ideas, bugfixes, and contributions. We couldn't do this without you! Please [download the new release](https://rstudio.com/products/rstudio/download/) and let us know what you think on our [community forum](https://community.rstudio.com/c/rstudio-ide). 


