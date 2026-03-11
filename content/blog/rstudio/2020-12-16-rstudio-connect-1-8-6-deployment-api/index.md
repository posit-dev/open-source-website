---
title: RStudio Connect 1.8.6 - Deployment API
people:
  - Kelly O'Briant
date: '2020-12-16'
slug: rstudio-connect-1-8-6-deployment-api
categories:
  - RStudio Connect
tags:
  - Connect
resources:
- name: connect
  src: Rstudio-Connect.jpeg
  title: RStudio Connect
blogcategories:
- Products and Technology
events: blog
nohero: true
image: thumbnail.jpg
ported_from: rstudio
port_status: raw
---
## Automate deployment with the RStudio Connect Server API

With RStudio Connect, your team can publish straight from the desktop or server IDE with the push of a button or orchestrate a fully customized deployment pipeline. While push-button publishing is powerful and convenient, it's not the ideal solution for all organizations. Data science teams need tools that can help traditional IT administrators understand how to provide sophisticated oversight for the deployment and management of data science artifacts. RStudio Connect aims to be the solution for those challenges. 

This API update makes programmatic deployment workflows more useful by introducing new content management options like the ability to set environment variables, custom URL paths, and detailed access permissions on first publish. We’ve made many of the internal RStudio Connect Server API capabilities public with this release, so there should be something new and exciting for all the analytic administrators, deployment engineers, and DevOps-minded folks to enjoy. 

### Public APIs for Content Deployment

Programmatic deployment workflows are now fully supported with the release of `/v1` API endpoints (previously `/v1/experimental`). The pattern for basic deployment is unchanged and can be used for any type of content supported by RStudio Connect. 

Content deployment can be customized, but follows a general framework:

1. Create a new content item (`POST /v1/content`) or identify an existing content item to update. 
2. Create a bundle capturing your code and its dependencies.
3. Upload the bundle archive to RStudio Connect (`POST /v1/content/{guid}/bundles`).
4. **New!** Optionally, set environment variables that the content needs at runtime (`PATCH /v1/content/{guid}/environment`).
5. Deploy (activate) that bundle (`POST /v1/content/{guid}/deploy`) and monitor its progress.
6. Poll for updates to a task; obtain the latest information about a dispatched operation (`GET /v1/tasks/{id}`).
7. **New!** Optionally, add viewer groups or collaborators (`POST /v1/content/{guid}/permissions`), set a custom vanity URL path (`PUT /v1/content/{guid}/vanity`), and add tags for organization and discoverability (`POST /v1/content/{guid}/tags`).

To learn more, follow along with basic deployment scenarios and example code in the RStudio Connect API Cookbook:

- [Deploying Content](https://docs.rstudio.com/connect/1.8.6/cookbook/deploying/)
- [Managing Content](https://docs.rstudio.com/connect/1.8.6/cookbook/content/)
- [Organizing Content](https://docs.rstudio.com/connect/1.8.6/cookbook/organizing/)
- [Sharing Content](https://docs.rstudio.com/connect/1.8.6/cookbook/sharing/)

### New Environment Variable Management API

When developing content for RStudio Connect, publishers should never place secrets (keys, tokens, passwords, etc.) in the code itself. Sensitive information should be protected through the use of environment variables. These variables have traditionally required configuration through the RStudio Connect dashboard, a method which can result in a failed initial deployment. 

The new API can be used to configure environment variables for a specified content item programmatically:

- Set environment variables with `PUT /v1/content/{guid}/environment` (removes any existing environment variables)
- Add, update, or delete environment variables with `PATCH /v1/content/{guid}/environment`

Read more about setting environment variables programmatically in the [RStudio Connect API Cookbook](https://docs.rstudio.com/connect/1.8.6/cookbook/deploying/#setting-environment-variables).

### Redeployments 

Based on feedback we received from users of the experimental deployment APIs, improvements have been made to the workflow for updating existing content items. Redeployment requires that an API client provide the correct unique content identifier for the item you want to update. For convenience, the RStudio Connect API now provides a method for retrieving that content identifier using the combination of content name and owner.

Read more about deploying new versions of content in the [RStudio Connect API Cookbook](https://docs.rstudio.com/connect/1.8.6/cookbook/deploying/#deploying-versions/).


### Advanced Deployments 

The experimental bundle management APIs for moving content items from one Connect server to another are now fully supported `v1` workflows as well. In situations where your organization has more than one RStudio Connect server for different stages of development, this pattern can be used to automate the promotion content (e.g., from staging to production). Once content exists on the production server, you may want to reduce the risk of pushing updates to it by adopting a blue-green deployment strategy. Blue-green is a system for creating separation between deployment and release by maintaining two copies of a content item in production (a blue and a green). The new `/vanity` endpoint can be used to assign a custom URL path to one version while making changes to the other, swapping the URL assignment whenever you want to redirect user traffic. 

Read more about advanced deployment patterns in the [RStudio Connect API Cookbook](https://docs.rstudio.com/connect/1.8.6/cookbook/promoting/). 

### A note about `/experimental` endpoints 

Those who are familiar with the existing content deployment API patterns may have questions about what these new API changes mean. Questions like, 

_"I already built deployment pipelines using the experimental APIs -- will everything break?"_

**Your scripts will not break upon upgrading to 1.8.6.** The `/v1/experimental` endpoints for content deployment are now labeled as **"Deprecated"**, but they have not been removed. In most cases the update from experimental to `/v1` should not require extensive changes. Please refer to the API documentation site to learn more about our [API versioning and deprecation policies](https://docs.rstudio.com/connect/1.8.6/api/#overview--versioning-of-the-api) .

<h3 align="center"><a href="https://rstudio.chilipiper.com/book/rsc-demo">See RStudio Connect in Action</a></h3>

> #### RStudio Connect 1.8.6
> - Return to the general announcement post to learn about more features and [updates here](https://blog.rstudio.com/2020/12/16/rstudio-connect-1-8-6/).
> - For upgrade planning notes, continue reading [more here](https://blog.rstudio.com/2020/12/16/rstudio-connect-1-8-6-admin-digest/).
