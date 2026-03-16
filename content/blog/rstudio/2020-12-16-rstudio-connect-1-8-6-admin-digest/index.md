---
title: RStudio Connect 1.8.6 - Administrator Digest
people:
  - Kelly O'Briant
date: '2020-12-16'
slug: rstudio-connect-1-8-6-admin-digest
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
port_status: in-progress
---

## Security & Authentication

### LDAP / Active Directory Changes

Group handling within RStudio Connect has significantly improved for LDAP / Active Directory within this release. Groups will now be synchronized via a background process on a scheduled interval. The group membership for a user is determined on login rather than at the time of content access, and permission checks will use synced data from the RStudio Connect database rather than making LDAP requests. 

LDAP Groups can be automatically populated upon user login if the `LDAP.GroupsAutoProvision` configuration option is enabled. This option is disabled by default to prevent an unexpectedly large number of groups from being pulled in unexpectedly. If the number of groups is not a concern, enabling this option is recommended for the optimal user experience.

As a result of these changes, RStudio Connect will support `session$groups` (via the HTTP header `Shiny-Server-Credentials`) in Shiny apps when using LDAP or Active Directory. Groups are listed by name according to the setting `LDAP.GroupNameAttribute`. LDAP groups are also available to other content types via the HTTP header `RStudio-Connect-Credentials`.

### Groups Page Update

The Groups page will now be available in the RStudio Connect dashboard under the "People" tab for all authentication types except those that return Unique IDs instead of group names. Using the Groups page, authorized users can add, remove, and rename groups when necessary. The Groups page can also be used to inspect groups for their user membership lists and perform group searches. 

## Deprecations & Breaking Changes

- **Breaking Change** The `Applications.TempMounting` configuration flag has been removed. Previously, disabling the flag would permit R processes to inspect the temporary data of other R processes.
- **Breaking Change** When using Postgres, RStudio Connect verifies that a minimum version of 9.5 is used.
- **Breaking Change** `GroupsByUniqueId` and `GroupsAutoProvision` cannot be enabled at the same time. IDs received from the authentication provider are not immediately useful for users when group auto provisioning is enabled. Please see this section of the Admin Guide for more information.
- **Deprecation** The `Server.SourcePackageDir`setting is deprecated and will be removed in a future release. Administrators should consider migrating to RStudio Package Manager or set up a private package repository. Please review this section of the Admin Guide for [instructions](https://docs.rstudio.com/connect/1.8.6/admin/r/package-management/#private-packages). 
- **Deprecation** The following Groups management settings have been deprecated and will be removed in a future release:

    - `LDAP.GroupsAutoRemoval`
    - `OAuth2.GroupsAutoRemoval`
    - `Proxy.GroupsAutoRemoval`
    - `SAML.GroupsAutoRemoval`

Please review the [full release notes](https://docs.rstudio.com/connect/news/#rstudio-connect-186).

## Upgrade Planning

### Upgrade Notes for LDAP / Active Directory Authentication

In RStudio Connect 1.8.6, LDAP user groups are determined on login, and group information is synced from the LDAP server to the Connect database in configured intervals.

**What to expect when upgrading to the new LDAP Sync process:**

- RStudio Connect enters "upgrade mode"
- All LDAP users start without any group memberships
- Users are divided into batches sized according to the total number of users
- RStudio Connect will attempt to obtain group memberships for all batches within the configured update interval (default 4 hours), making the best effort to not disrupt users’ normal usage of the system
- Once all users are synced, RStudio Connect enters regular operation where users are updated throughout a configured interval (default 4 hours)

In some cases, administrators may need to increase the update interval to be longer than 4 hours so that updates can be more spread out throughout the day.

**Learn more about the changes and upgrades in the [updated Admin Guide](https://docs.rstudio.com/connect/admin/authentication/).**

### Upgrade RStudio Connect

To perform an upgrade, download and run the installation script. The script installs a new version of RStudio Connect on top of the earlier one. Existing configuration settings are respected. Additional documentation can be [found here](https://docs.rstudio.com/rsc/upgrade/).

```
# Download the installation script
curl -Lo rsc-installer.sh https://cdn.rstudio.com/connect/installer/installer-v1.5.1.sh

# Run the installation script
sudo bash ./rsc-installer.sh 1.8.6
```

---

To receive email notifications for RStudio professional product releases, patches, security information, and general product support updates, subscribe to the **Product Information** list by visiting the RStudio subscription management portal linked below.  

<h3 align="center"><a href="https://rstudio.com/about/subscription-management/">Subscribe to RStudio Product Information Updates</a></h3>
