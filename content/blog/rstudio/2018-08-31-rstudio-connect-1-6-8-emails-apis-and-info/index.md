---
title: RStudio Connect 1.6.8 - Emails, APIs, and Titles
people:
  - Sean Lopp
date: '2018-09-20'
slug: rstudio-connect-1-6-8-emails-apis-and-titles
categories:
- RStudio Connect
tags:
- Connect
- RStudio Connect
blogcategories:
- Products and Technology
events: blog
ported_from: rstudio
port_status: raw
---


RStudio Connect 1.6.8 includes additions to custom emails, new user endpoints in the RStudio Connect Server API, support for content descriptions and title changes, and important security and authentication improvements.

<image src="/blog-images/rsc-168-email.png", height=400px>

## Updates

- **R Markdown Reports** have access to environment variables containing [metadata about the report on RStudio Connect](http://docs.rstudio.com/connect/1.6.8/user/r-markdown.html#r-markdown-including-urls).  This addition is especially important for [custom emails](http://docs.rstudio.com/connect/1.6.8/user/r-markdown.html#r-markdown-email-customization).  In case you missed it, recent versions of RStudio Connect allow data scientists to distribute beautiful emails that can include plots, tables, and dynamically generated text.  The new metadata can be used to craft an email that includes a link back to the original report or dashboard. 

<image src="/blog-images/rsc-168-footer.png", width=350px>

- **Users in the Connect Server API** RStudio Connect v1.6.6 introduced the ability to list user information with the [Connect Server API](http://docs.rstudio.com/connect/1.6.8/api). Version 1.6.8 extends the Server API to include endpoints for creating users and updating users. These endpoints can be used with PAM, proxy, or  built-in authentication providers. Future releases will include API support for LDAP/AD and OAuth authentication. As an example, if you are using proxy authentication, you can now programmatically create a user and give them access to content before they log in. The API request can specify all of a user's attributes or only some. Users will be asked to complete their profile on first login. See the new [admin documentation](http://docs.rstudio.com/connect/1.6.8/admin/user-management.html#user-provisioning) on user provisioning for more information.

```bash
 curl -v -X POST https://connect.example.com/__api__/v1/users
     -H "Content-Type: application/json" 
     -H "Authentication: Key ***API_KEY***" 
     -d '{
             "username": "john_doe",
             "first_name": "John",
             "last_name": "Doe",
             "email": "jdoe@example.com"
         }'
```


- **Content Titles and Descriptions**  The “Info” settings panel allows publishers and collaborators to edit the content title or - new this release - add a content description. The title and description are visible to viewers with access to the content and administrators.  Future RStudio Connect releases will add support for content images, and incorporate all of this information into the content listing page - stay tuned!

<image src="/blog-images/rsc-168-info.png", width=350px>

*Note*: At this time, changing the content title in RStudio Connect does not update the title in the RStudio IDE publish dialog.


## Security & Authentication Changes

- **TLS Versions** RStudio Connect now supports the `HTTPS.MinimumTLS` [configuration setting](http://docs.rstudio.com/connect/1.6.8/admin/appendix-configuration.html#appendix-configuration-https) which can be used to change the TLS version in use. Specific TLS ciphers can be prohibited using the `HTTPS.ProhibitedCiphers` configuration setting. Before you consider making your server more restrictive, ensure that all supported clients (both browsers *and* R) support the more restrictive settings.

- **LDAP / Active Directory Groups** For LDAP or AD installations, administrators should add the [`LDAP.GroupUniqueIdAttribute`](http://docs.rstudio.com/connect/1.6.8/admin/authentication.html#ldap-or-ad-configuration-settings) to identify which directory attribute uniquely identifies a group. Existing installations will continue working, but an upcoming release will require this setting on start-up.

- The [CLI `usermanager` utility](http://docs.rstudio.com/connect/1.6.8/admin/cli.html#cli-usermanager) has improved support for group management and offers better support for installations using LDAP/AD.


## Deprecations & Breaking Changes

- **Breaking Change** The configuration value `Server.SenderEmail` is validated at start-up and invalid email addresses will prevent RStudio Connect from starting.

- **Breaking Change** `Applications.EnvironmentBlacklist`, deprecated in 1.6.6, has been removed in favor of `Applications.ProhibitedEnvironment`. 

- **Breaking Change** `LDAP.WhitelistedLoginGroups`, deprecated in v1.6.6, has been removed in favor of `LDAP.PermittedLoginGroups`.

- The `xhr-streaming` SockJS protocol has been disabled for Microsoft Edge to fix a bug where Shiny applications became unresponsive. Shiny applications will fall back to a different protocol automatically and will work without any changes.


Please review the [full release notes](http://docs.rstudio.com/connect/news)

> #### Upgrade Planning
> If you use LDAP or Active Directory, please take note of the LDAP changes described above and in the release notes. Aside from the  deprecations and breaking changes above, there are no other special considerations and upgrading should only take few seconds. If you are upgrading from an earlier version, be sure to consult the release notes for the intermediate releases, as well.

If you haven't yet had a chance to download and try [RStudio Connect](https://rstudio.com/products/connect/), we encourage you to do so. RStudio Connect is the best way to share all the work that you do in R (Shiny apps, R Markdown documents, plots, dashboards, Plumber APIs, etc.) with collaborators, colleagues, or customers.

You can find more details or download a 45-day evaluation of the product at [https://www.rstudio.com/products/connect/](https://www.rstudio.com/products/connect/). Additional resources can be found below.
 
 - [RStudio Connect home page & downloads](https://www.rstudio.com/products/connect/)
 - [RStudio Connect Admin Guide](http://docs.rstudio.com/connect/admin/)
 - [What IT needs to know about RStudio Connect](https://www.rstudio.com/wp-content/uploads/2016/01/RSC-IT-Q-and-A.pdf)
 - [Detailed news and changes between each version](http://docs.rstudio.com/connect/news/)
 - [Pricing](https://www.rstudio.com/pricing/#ConnectPricing)
 - [An online preview of RStudio Connect](https://beta.rstudioconnect.com/connect/)







