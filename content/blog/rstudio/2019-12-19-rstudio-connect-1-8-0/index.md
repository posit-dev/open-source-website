---
title: 'RStudio Connect 1.8.0 '
people:
  - Sean Lopp
date: '2020-01-22'
slug: rstudio-connect-1-8-0
categories:
- RStudio Connect
tags:
- Connect
- RStudio Connect
blogcategories:
- Products and Technology
events: blog
nohero: true
image: thumbnail.png
ported_from: rstudio
port_status: raw
---


RStudio Connect helps data science teams quickly make an impact by enabling them
to publicize reports, models, dashboards, and applications created in R and
Python with business stakeholders. The 1.8.0 release makes it even easier for
teams to start sharing.

For **Data Scientists**, highlights include:

- [Python Support](#python-support): Improvements that make it easier to share Jupyter Notebooks and mixed R and Python content.
- [pins](#pins): An easy way to share data, models, and other objects. 
- [Custom Emails](#custom-emails): Use code to create beautiful emails with plots and results inline.


For **DevOps / IT Administrators**, 1.8.0 makes it easier to support data science teams in
production:

- [SAML](https://docs.rstudio.com/connect/admin/authentication.html#authentication-saml): Seamless single sign-on integration.
- [Schedule Content Calendar](#scheduled-content-calendar): Audit content schedules in production.

For **Data Science Leaders**, 1.8.0 simplifies onboarding new team members and eases
collaboration:

- [Jump Start Examples](#jump-start-examples): Learn new ways to use RStudio Connect and onboard new users.
- [Git-centered Deployment](#git-centered-deployments): Utilize Git-centric deployment workflows. 

To learn more about all the ways RStudio Connect makes it easy to connect your
Data Science team with your decision makers, visit [our
website](https://rstudio.com/products/connect). An easy way to get started is
with the [RStudio Team Quickstart](https://rstudio.com/quickstart) to experience
all of RStudio's products on an easy-to-use virtual machine, or begin a free [45-day evaluation](https://rstudio.com/products/connect/) of RStudio Connect.

### Python Support 

{{< figure src="rsc-180-jupyter1.png" alt= "Publish Options in Jupyter">}}

RStudio Connect has supported both R and Python for over a year, and during this time we've made [significant improvements](https://github.com/rstudio/rsconnect-jupyter/blob/master/CHANGELOG.md). Data scientists can now [publish
Jupyter Notebooks with a single click](https://docs.rstudio.com/rsconnect-jupyter/) or
by using version control. Data scientists who use both R and Python also have more
flexibility, helping them deploy mixed content using the [reticulate R
package](https://rstudio.github.io/reticulate).

{{< figure src="rsc-180-jupyter2.png" alt= "Publish a Jupyter Notebook to RStudio Connect">}}

### Pins

The [pins](https://rstudio.github.io/pins) package makes it easy to share data, models, and other objects on RStudio Connect. Pins are especially useful if you have data that regularly updates; simply schedule an R Markdown document to process your data and pin your results or model. Once pinned, your reports, applications, and APIs can automatically pull the updates. [Learn more](https://pins.rstudio.com/articles/boards-rsconnect.html) or [see an example](https://rviews.rstudio.com/2019/10/17/deploying-data-with-pins/).

{{< figure src="rsc-178-pins.png" alt= "Pins Support in RStudio Connect">}}

### Custom Emails

Sending plots, tables, and results inline in an email is a powerful way for data scientists to make an impact. RStudio Connect customers use custom emails to send daily reminders, conditional alerts, and to track key metrics. The latest release of the [blastula package](https://rich-iannone.github.io/blastula/) makes it even easier for data scientists to specify these emails programmatically: 

```r
if (demand_forecast > 1000) {
  render_connect_email(input = "alert-supply-team-email.Rmd") %>%
  attach_connect_email(
    subject = sprintf("ALERT: Forecasted increase of %g units", increase),
    attach_output = TRUE,
    attachments = c("demand_forecast_data.csv")
  )
} else {
  suppress_scheduled_email() 
}
```

{{< figure src="rsc-180-email.png" alt= "Custom Emails from RStudio Connect">}}

Learn more [here](https://solutions.rstudio.com/2019/12/30/rstudio-connect-custom-emails-with-blastula/)!

### Jump Start Examples

A common challenge facing data science teams is onboarding new users. Data
scientists have to learn new tools, methods, and often a new domain. We've
created a set of examples to help data scientists learn common best practices. A
new tutorial in the product helps users publish different data products, which is
particularly helpful for data scientists exploring new content types, such as
reports, models, or datasets.

{{< figure src="rsc-180-jumpstart.png" alt= "Jump Start Examples">}}

### Git-centered Deployments

RStudio Connect's push-button publishing is a convenient and simple way for data
scientists to share their work. However, some teams prefer Git-centric
workflows, especially when deploying content in production. RStudio Connect
[supports these
workflows](https://docs.rstudio.com/connect/1.8.0/user/git-backed/), making it
effortless for data science teams to adopt version control best practices without
maintaining additional infrastructure or remembering complex workflows. Data
scientists simply commit to Git, and RStudio Connect will update the content,
saving you any extra steps.

{{< figure src="rsc-176-git-deploy.png" alt= "Create New Content from Git Repository in RStudio Connect">}}

### Scheduled Content Calendar

For system and application administrators, RStudio Connect makes it simple to
audit data science work. For data science teams, one powerful application of
RStudio Connect is the ability to schedule tasks. These tasks can be everything
from simple ETL jobs to daily reports. In 1.8.0, we've made it easier for
administrators to track these tasks across all publishers in a single place.
This new view makes it possible to identify conflicts or times when the server
is being overbooked.

{{< figure src="rsc-174-schedules.png" alt= "View Scheduled Content">}}

## Security Updates & Deprecations

- RStudio Connect no longer supports Ubuntu 14.04 LTS (Trusty Tahr).
- The `Postgres.URL` database connection URL will always use a nonempty `Postgres.Password `value as its password. Previous releases would use the password only when a `{$}` placeholder was present. Support for the `Postgres.URL` placeholder `{$}` is deprecated and will be removed in a future release.
- Duplicate user names are now accepted in some conditions for LDAP, SAML, and proxied authentication providers. See the [release notes] for details.
- Support for TLS 1.3. Access to this TLS version is available without additional configuration.
- The setting `HTTPS.ExcludedCiphers` has been removed and is no longer supported. The `HTTPS.MinimumTLS` setting should be used to specify a minimum accepted TLS version. We recommend running a secure proxy when your organization has more complex HTTPS requirements.
- The deprecated setting `Applications.DisabledProtocols` has been removed. Use `Applications.DisabledProtocol` instead. Multiple values should be placed one per line with this new setting.
- The deprecated settings `OAuth2.AllowedDomains` and `OAuth2.AllowedEmails` have been removed. Use `OAuth2.AllowedDomain` and `OAuth2.AllowedEmail` instead. Multiple values should be placed one per line with these new settings.
- TensorFlow Model API deployment supports models created with TensorFlow up to version 1.15.0. A systems administrator will need to update the version of `libtensorflow.so` installed on your RStudio Connect system.

For more information about all the updates available in RStudio Connect 1.8.0,
we recommend consulting the [release posts for the 1.7 series](https://blog.rstudio.com/categories/rstudio-connect). 

This release also includes numerous bug fixes, the full [release notes](https://doc.rstudio.com/connect/news) document all of the changes. Some of our favorites:

- The “Info” panel for Jupyter notebook content includes a summary of recent usage.
- Python-based content can now use an application RunAs setting. 
- Scheduled reports no longer run multiple times if the application and database clocks disagree, or in the case of concurrent rendering attempts in a multi-node installation.


> ## Upgrade Planning
> Aside from the deprecations and breaking changes listed above,
> there are no other special considerations, and upgrading should require less than
> five minutes. If you are upgrading from a version earlier than 1.7.8, be sure to consult
> the release notes for the intermediate releases, as well.


## Get Started with RStudio Connect

If you haven't yet had a chance to download and try [RStudio
Connect](https://rstudio.com/products/connect/), we encourage you to do so.
RStudio Connect is the best way to share all the work that you do in R and Python with
collaborators, colleagues, or customers.

You can find more details or download a 45-day evaluation of the product at
[https://www.rstudio.com/products/connect/](https://www.rstudio.com/products/connect/).
Additional resources can be found below:

- [RStudio Connect home page & downloads](https://www.rstudio.com/products/connect/)
- [RStudio Connect Administration Guide](http://docs.rstudio.com/connect/admin/)
- [Detailed news and changes between each version](http://docs.rstudio.com/connect/news/)
- [Pricing](https://www.rstudio.com/pricing/)
