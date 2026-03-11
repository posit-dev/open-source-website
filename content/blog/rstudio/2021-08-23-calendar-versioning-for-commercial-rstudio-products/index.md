---
title: Announcing Calendar Based Versioning for All Commercial RStudio Products
people:
  - Ferit Albukrek
date: '2021-08-30'
slug: calendar-versioning-for-commercial-rstudio-products
blogcategories:
  - Products and Technology
tags:
  - RStudio Workbench
  - Connect
  - RStudio Package Manager
  - Drivers
description: RStudio is shifting to a calendar-based versioning scheme for future releases of all our commercial products. This change will make it easier for users to understand the age of a specific release, where a release fits into our support cycles, which releases contain new features and bug fixes. 
events: blog
alttext: open calendar pages
image: thumbnail.jpg
ported_from: rstudio
port_status: raw
---
<sup>Photo by[ Eric Rothermel](https://unsplash.com/@erothermel?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on[ Unsplash](https://unsplash.com/s/photos/calendar?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)</sup>

RStudio is shifting to a calendar-based versioning scheme for future releases of all our commercial products.

We are making this transition to deliver a more transparent experience for our customers:

* **The age of a given release will be self-evident** from its version label.
* **Customers can rely on support for a consistent and predictable time period**. (Previously the support window was heavily influenced by how rapidly new releases superseded prior ones.)
* **Customers will be able to easily determine which releases contain new features** (as opposed to bug fixes), based on consistent standards for releasing new editions across all our products.

In this new scheme version labels are derived from the date of release using the YYYY.MM.patch format where

* YYYY is the four digit year
* MM is the two digit month
* patch is an integer that starts at zero and gets incremented each time non-functional improvements (e.g.: bug fixes, performance improvements, etc…) are made to the product.

We call the YYYY.MM portion of the version label the **edition** of the product. We will release a new edition of the product with a .0 patch number when new features are added and/or breaking changes have been made. Each **edition** will be supported for 18 months and the most recent edition will be supported regardless of its age.

Our [support agreement](https://www.rstudio.com/about/support-agreement/) has been revised to align with the new calendar versioning scheme. The changes will generally result in a more generous support window for both past and future versions. Please see our [Support page](https://www.rstudio.com/support/) for more details on these support windows.

To receive email notifications for RStudio professional product releases, patches, security information, and general product support updates, subscribe to the **Product Information** list by visiting the RStudio [subscription management portal](https://rstudio.com/about/subscription-management/).
