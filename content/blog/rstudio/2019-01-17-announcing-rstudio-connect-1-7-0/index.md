---
title: RStudio Connect 1.7.0
people:
  - Sean Lopp
date: '2019-01-17'
slug: announcing-rstudio-connect-1-7-0
categories:
- RStudio Connect
tags:
- Connect
- RStudio Connect
blogcategories:
- Products and Technology
events: blog
ported_from: rstudio
port_status: in-progress
---


RStudio Connect is the publishing platform for everything you create in R. In
conversations with our customers, R users were excited to have a central place
to share all their data products, but were facing a tough problem. Their
colleagues working in Python didn't have the same option, leaving their work
stranded on their desktops. Today, we are excited to introduce the ability for
data science teams to publish Jupyter Notebooks and mixed Python and R content to RStudio Connect.

Connect 1.7.0 is a major release that also includes many other significant
improvements, such as programmatic deployment and historical event data.  We
encourage existing customers to [upgrade](https://rstudio.com/products/connect/download-commercial).



We also welcome anyone who has not yet experienced RStudio Connect to [try it
today](https://rstudio.com/products/connect/evaluation)!


{{< figure src="/blog-images/rsc-170-jupyter.png" caption="Publishing to Connect from Jupyter" alt= "Publishing to Connect from Jupyter">}}


## Updates

### Python & R: Reticulated  Apps, APIs, and Reports

RStudio has often provided support for other languages frequently used with R.
Earlier this year, we announced the [reticulate R
package](https://rstudio.github.io/reticulate/) and [IDE
support](https://blog.rstudio.com/2018/10/09/rstudio-1-2-preview-reticulated-python)
for creating projects that use R and Python. Now, these projects are fully
supported in RStudio Connect, as well. Whether you’re creating a reticulated Shiny app, a
Plumber API that calls Python, or an R Markdown document that mixes Python and
R, RStudio Connect will automatically re-create both the R and Python
environments!

{{< figure src="/blog-images/rsc-170-api.png" caption="Reticulated API with Python Environment Logs" alt= "Reticulated API with Python Environment Logs">}}
	

Note: Server administrators need to add a [Python
configuration](https://docs.rstudio.com/connect/1.6.11/admin/python.html)
for RStudio Connect.


### Jupyter Notebooks

Data science teams in the enterprise can include people who use RStudio, Jupyter
Notebooks, or both. Now RStudio, Jupyter, and JupyterHub users can publish and
share the data products they create every day in one convenient place. Jupyter
Notebooks can be published to RStudio Connect using a [Jupyter
extension](https://docs.rstudio.com/rsconnect-jupyter).
Notebooks are published as static HTML files, or the notebook source can be
published. When the source is included,  RStudio Connect automatically restores
the Python environment and the Jupyter Notebooks can be re-executed, emailed,
and scheduled.



### Programmatic Deployment
	
As data products become critical to organizations, RStudio Connect users have
requested more flexible deployment options. Enterprise workflows sometimes
require approvals to publish to production environments. For example, content
stored in Git may be published to separate QA or Production environments based on
IT approvals.

In RStudio Connect 1.7.0, we’ve added support for [programmatic
deployment](https://docs.rstudio.com/connect/1.7.0/user/cookbook.html#cookbook-deploying)
in the [RStudio Connect Server
API](https://docs.rstudio.com/connect/1.7.0/api/#content). These new APIs let
your deployment engineers craft custom deployment workflows. We have created
[example scripts](https://github.com/rstudio/connect-api-deploy-shiny) showing
how to use the content APIs to deploy a Shiny application.


{{< figure src="/blog-images/rsc-170-handoff.png" caption="Architecture Diagrams for Deployment Strategies" alt= "Architecture Diagrams for Deployment Strategies">}}

### Historical Event Data

RStudio Connect now [collects and surfaces
data](https://docs.rstudio.com/connect/1.7.0/admin/historical-information.html#historical_events)
you can use to answer how often your data product is being viewed, whether it
needs updating, and who is using it. For reports, dashboards, plots, and
notebooks, RStudio Connect records “who, what, and when” for each visit. This
data is available to publishers and admins through the [Connect Server
API](https://docs.rstudio.com/connect/1.7.0/api/#instrumentation). We’ve
created a [sample dashboard](https://github.com/sol-eng/connect-usage) you can
use out of the box or as a launch pad for your own analysis!

{{< figure src="/blog-images/rsc-170-dash.png" caption="Dashboard of 30-day Usage Metrics" alt= "Dashboard of 30-day Usage Metrics">}}


### Security & Authentication Changes

- **Bundle Uploads** Better protection against malicious bundle uploads that
previously may have written outside the content directory.


- **Brute-force Protection** A brute force attack protection has been added for
interactive authentication attempts.


- **User Profiles**  Admins can now prevent users from editing their profiles for all
authentication providers. Additionally, Connect better handles email values
supplied by authentication providers, fixing a bug that would prevent users from
logging in. See the [release notes](http://docs.rstudio.com/connect/news) for details.


- **Audit Improvements** All modifications to users and groups done via the
`usermanager` utility are reported in the audit logs.


- **Unique Users** RStudio Connect better enforces unique users. The `usermanager` utility has
multiple updates, making it easier to fix broken user accounts.


- **Proxied Auth Improvements** Installations using a custom authentication
provider can provide [complete user profiles through proxy headers](https://docs.rstudio.com/connect/1.7.0/admin/authentication.html#authentication-proxy),
removing the need for users or admins to update profiles manually or via the
Connect Server API.


- **Programmatic Group Management** The [Connect Server API](https://docs.rstudio.com/connect/1.7.0/api/#groups)
can be used to create and manage groups for installations using Password or OAuth2 authentication methods.


### Deprecations & Breaking Changes


- **Breaking**  The deprecated `OAuth2.DiscoveryEndpoint` configuration value has been
removed.


- **Deprecation**  The configuration setting `Password.UserInfoEditableBy` is
deprecated in favor of `Authorization.UserInfoEditableBy`. Future releases will
remove the setting entirely.


Please review the [full release notes](https://docs.rstudio.com/connect/news)

> #### Upgrade Planning
> Please note the breaking changes and deprecations above. If you are interested in adding Python support (for Jupyter Notebooks or Reticulated Python & R content), please follow the instructions to configure [Python for RStudio Connect](https://docs.rstudio.com/connect/1.7.0/admin/python.html). Upgrading to 1.7.0 from 1.6.10 can take upwards of ten minutes due to a data migration. If you are upgrading from an earlier version, be sure to consult the release notes for the intermediate releases, as well.

If you haven't yet had a chance to download and try [RStudio
Connect](https://rstudio.com/products/connect/), we encourage you to do so.
RStudio Connect is the best way to share all your data science work (Shiny apps,
R Markdown documents, Jupyter Notebooks,  plots, dashboards, Plumber APIs, etc.)
with collaborators, colleagues, or customers.

You can find more details or download a 45-day evaluation of the product at
[https://www.rstudio.com/products/connect/](https://www.rstudio.com/products/connect/).
Additional resources can be found below.

- [RStudio Connect home page & downloads](https://www.rstudio.com/products/connect/)
- [RStudio Connect Admin Guide](http://docs.rstudio.com/connect/admin/)
- [Detailed news and changes between each version](http://docs.rstudio.com/connect/news/)
- [Pricing](https://www.rstudio.com/pricing/#ConnectPricing)
- [An online preview of RStudio Connect](https://beta.rstudioconnect.com/connect/)








