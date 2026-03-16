---
title: RStudio Connect 1.7.6 - Publish Git-backed Content
people:
  - Kristopher Overholt
date: '2019-06-24'
slug: rstudio-connect-1-7-6
categories:
- RStudio Connect
- News
tags:
- Connect
- RStudio Connect
blogcategories:
- Products and Technology
- Company News and Events
events: blog
ported_from: rstudio
port_status: in-progress
---


RStudio Connect 1.7.6 has been released and is now available for download. This
release includes a new publishing method for Git-backed content, the ability for
publishers to manage vanity URLs for applications, full support for all SAML
authentication providers, and other improvements and bug fixes.

{{< figure src="/blog-images/rsc-176-git-header.png" alt= "New Content Dropdown Menu in RStudio Connect">}}

## Updates

### New publishing method for Git-backed content

This release adds the ability for data scientists to deploy content from Git
repositories for individual applications within RStudio Connect.

{{< figure src="/blog-images/rsc-176-git-content.png" alt= "Publish Content from Git to RStudio Connect">}}

This publishing method is designed to allow data scientists to publish directly
from Git repositories to Connect, and have that content get updated at regular
intervals without the need for external CI/CD systems like Jenkins or Travis CI.

{{< figure src="/blog-images/rsc-176-git-deploy.png" alt= "Create New Content from Git Repository in RStudio Connect">}}

This publishing method complements the existing methods of:

- Push-button publishing from the RStudio IDE
- Push-button publishing from Jupyter Notebooks
- Programmatic deployment with CI/CD pipelines using the RStudio Connect Server APIs

Refer to the documentation on Git-Backed Content in the [User
Guide](https://docs.rstudio.com/connect/1.7.6/user/git-backed.html) and
[Administration
Guide](https://docs.rstudio.com/connect/1.7.6/admin/content-management.html#git-backed)
for additional information on the configuration and usage of this new
functionality.

### Publishers can modify vanity URLs for content

Vanity URLs allow administrators to create "vanity paths" for published content
in RStudio Connect, which makes the content available at a customized URL path
rather than a URL path that uses the numeric app ID as an identifier.

{{< figure src="/blog-images/rsc-176-vanity-urls.png" alt= "Modify the Vanity URL/Address for Content in RStudio Connect">}}

This release adds the ability for publishers to modify vanity URLs for published
content without the need for administrators to perform this configuration.

Refer to the documentation on custom vanity URLs in the [User
Guide](https://docs.rstudio.com/connect/1.7.6/user/settings-panel.html#vanity-url)
and [Administration
Guide](https://docs.rstudio.com/connect/1.7.6/admin/appendix-configuration.html#appendix-configuration-authorization)
for additional information on the configuration and usage of this new
`Authorization.PublishersCanManageVanities` setting.

### Ability to isolate viewer permissions and discoverability

This release adds the ability for administrators to configure a global setting
to prevent viewers from seeing any other registered users, groups, or publishers
in RStudio Connect.

{{< figure src="/blog-images/rsc-176-viewer-permissions.png" alt= "Isolate Viewer Permissions in RStudio Connect">}}

This setting is useful for RStudio Connect environments where users with the
viewer role should not able to discover the existence or identities of other
users, groups, or publishers on the server. With this setting enabled, users
with the viewer role will only be able to discover and view published content
that they have been explicitly granted access to.

Refer to the Administration Guide Configuration section on
[Authorization](https://docs.rstudio.com/connect/1.7.6/admin/appendix-configuration.html#appendix-configuration-authorization)
for more information on the `Authorization.ViewersCanOnlySeeThemselves` setting.

### Full support for all SAML providers

RStudio Connect 1.7.4 added [support for SAML-based
authentication](https://blog.rstudio.com/2019/05/14/introducing-saml-in-rstudio-connect/)
and a subset of identity providers. The 1.7.6 release adds support for all
SAML-based identity providers. Refer to the support article on [Getting Started
with SAML in RStudio
Connect](https://support.rstudio.com/hc/en-us/articles/360022321494-Getting-Started-with-SAML-in-RStudio-Connect)
for more information.

### Documentation for Server API Cookbook

The RStudio Connect [Server API
Cookbook](https://docs.rstudio.com/connect/1.7.6/cookbook/) has been made
available as a separate guide and is no longer part of the User Guide.

## Security & Authentication Changes

- **Forgot Password Behavior** -  When using built-in Password authentication,
requesting a password reset via the "forgot password" link no longer fails for
non-existing users, to prevent malicious user enumeration.

- **Email Address Changes** - Changes made to the email addresses in user
profiles done manually or via Connect Server API will cause an email to be sent
to the old email address, so the user is notified about the new email address in
use.

- **Brute-Force Protection** - A protection against brute-force attacks has been
implemented for all authentication attempts against API calls to Connect using
either API keys or tokens. After a failed authentication attempt, the user may
have to wait longer before trying again.

- **Enforced Password Complexity** - Use `Password.MinimumScore` to control how
complex (secure) new passwords must be when using the password authentication
provider. See the [Password Authentication
section](https://docs.rstudio.com/connect/1.7.6/admin/authentication.html#authenticaton-password)
of the Administration Guide for details.

## Deprecations & Breaking Changes

- **Breaking Change** - `Authorization.UsersListingMinRole` has been deprecated
and it should be removed from the configuration file. A warning will be issued
during startup in the `rstudio-connect.log` if the setting is in use. In the
next release, the presence of this setting will prevent RStudio Connect from
starting up. Customers using this setting with any value other than the default
(viewer) should use `Authorization.ViewersCanOnlySeeThemselves = true` instead.

- **Breaking Change** - The `needs_config` field has been removed from the
Content entity of the experimental Server API. All Content fields and endpoints
to interact with content are provided in the Server API Reference.

Refer to the [full release notes](https://docs.rstudio.com/connect/news/) for
more information on all of the changes and bug fixes in this release.

## Upgrade Planning

> If you use the `Authorization.UsersListingMinRole` setting, please take note
> of the changes described above and in the release notes. Aside from the
> deprecations and breaking changes above, there are no other special
> considerations and upgrading should require less than five minutes. If you are
> upgrading from an earlier version, be sure to consult the release notes for
> the intermediate releases, as well.

## Get Started with RStudio Connect

If you haven't yet had a chance to download and try [RStudio
Connect](https://rstudio.com/products/connect/), we encourage you to do so.
RStudio Connect is the best way to share all the work that you do in R (Shiny
apps, R Markdown documents, plots, dashboards, Plumber APIs, etc.) with
collaborators, colleagues, or customers.

You can find more details or download a 45-day evaluation of the product at
[https://www.rstudio.com/products/connect/](https://www.rstudio.com/products/connect/).
Additional resources can be found below.

- [RStudio Connect home page & downloads](https://www.rstudio.com/products/connect/)
- [RStudio Connect Administration Guide](http://docs.rstudio.com/connect/admin/)
- [Detailed news and changes between each version](http://docs.rstudio.com/connect/news/)
- [Pricing](https://www.rstudio.com/pricing/)

