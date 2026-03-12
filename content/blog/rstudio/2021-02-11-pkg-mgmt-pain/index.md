---
title: 'Painful Package Management'
people:
  - Alex K Gold
date: '2021-02-11'
slug: pkg-mgmt-pain
description: Data science teams are often frustrated by poorly-designed or nonexistent approaches to R and Python package management. In this post, you'll learn specifically how that pain shows up for data scientists and how to identify your organization's requirements for a better package management plan.
categories:
  - Packages
  - RStudio Package Manager
resources:
- name:  "thumbnail"
  src:   "thumbnail.jpg"
blogcategories:
- Products and Technology
events: blog
alttext: a package on a table
image: thumbnail.jpg
ported_from: rstudio
port_status: in-progress
---
<sup>Photo by <a href="https://unsplash.com/@brandablebox?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Brandable Box</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span></sup>

> *This is the second of three blogs on package management.*
>
> *Registration for our webinar on [Managing Packages for Open-Source Data Science](https://rstudio.com/registration/managing-packages-for-open-source-data-science/) on February 17 is now open.*

If you're a data scientist, you've been hired to generate insights and create assets -- not manage R and Python package environments. But "I spend my day managing packages," or even worse, "I spend my day fighting IT for the packages I need," is an all-too-common refrain.

It doesn't have to be this way. With a little forethought and planning, your organization can adopt a [package management strategy](https://environments.rstudio.com/reproduce.html) that will drastically reduce the amount of hassle data scientists have to endure managing packages.

In this blog post, we'll explore the frustration your data scientists probably feel if your package management plan doesn't provide both flexibility to get work done and structure to ensure reproducibility. Then we'll dig into the first step to make it better: determining your organization's package management requirements.

## When Package Management is Pain

When package management isn't going well, data scientists or engineers are usually the first ones to feel the sting. Here are some of the ways data scientists experience bad package management plans:

-   **It's hard or slow to install packages.** Data scientists often can't find the packages they need from public repositories or aren't empowered to share private packages. Even when it's easy to find packages, they may be slow to install or require system libraries that don't exist.

-   **Data science and IT/Ops feel at odds.** If you're a data scientist, you probably want every package you need **now** without waiting for someone to approve installation. This can put you on a collision course with IT Admins who are concerned about platform security and stability.

-   **Sharing projects and deploying to production are ordeals.** When you share or deploy, you may face a maze of package dependencies and conflicts where reaching success feels more like a roll of the dice than a smooth process.

-   **Reproducing your results is fragile or elusive.** R and Python packages get constant updates, and unless you've planned ahead, new package versions can break old code and create unexpected pitfalls when adding new capabilities.

As we discussed in the [first blog in this series](https://blog.rstudio.com/2021/02/05/pkg-mgmt-prime-directive/), successful package management requires attention from both IT/Admins and data scientists as the process spans both the shared repository and the private library.

That means that **there's no single solution to package management**.

But, these issues **are** solvable by developing a package management plan for your organization. The first step is to clearly identify how packages are managed in your environment and who's responsible.

## Discovering Package Management Requirements

Your organization's package management requirements depend on your organization's size and complexity. In some organizations, package management involves stakeholders from the data science, IT/Ops, security, and other teams.

Virtually all environments share a few requirements. To successfully manage open source packages for data science, **your organization needs**:

-   **A simple way to create and save package sets.** Organizations need a standard way to ensure that data scientists can capture the dependencies for their particular code and save them for later.

-   **The ability to quickly and easily add packages to libraries.** Package management is much smoother when data scientists are confident they can quickly restore a previous working environment when and where they need to.

And depending on your organization, **you might need** the ability to:

-   **Share private (internally-developed) packages.** If your organization is developing and using internal packages, you'll need a way to access and share them in addition to approved packages from public repositories.

-   **Limit the set of packages available in the environment.** Organizations that allow open access to packages from public repositories face very different requirements than those that only allow validated packages.

-   **Do all of the above in an offline or air-gapped context.** If your organization's security policy requires limited or no internet, you'll need to pay special attention to getting data scientists the packages they need.

It's worth taking a minute to think about how your organization currently manages packages and whether you have a way to meet the requirements you face in your organization.

In the (forthcoming) final blog in this series, we'll dive into how to take the requirements you've identified and create your organization's package management plan, including divvying up responsibility for package management between IT Admins and data scientists, and how to use tools like [renv](https://rstudio.github.io/renv/index.html), python virtual environments, and [public](https://packagemanager.rstudio.com) and [private RStudio Package Manager](https://rstudio.com/products/package-manager/) to execute your plan.

> *Please sign up for our [free webinar](https://rstudio.com/registration/managing-packages-for-open-source-data-science/) on February 17 to learn more about managing open source packages for R and Python.*
