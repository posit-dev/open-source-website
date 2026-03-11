---
title: Shiny Server (Pro) 1.5.8
people:
  - Joe Cheng
date: '2018-09-04'
slug: shiny-server-pro-1-5-8
categories:
- Shiny
tags:
- shiny server pro
- shiny
- Shiny
blogcategories:
- Products and Technology
events: blog
ported_from: rstudio
port_status: raw
---


[Shiny Server 1.5.8.921 and Shiny Server Pro 1.5.8.985 are now available.](https://www.rstudio.com/products/shiny/shiny-server/)

This release includes support for listening on IPv6 addresses. It also fixes issues with servers that have home directories mounted over NFS with `root_squash`, and with networks that use double-bind LDAP with restrictive permissions on user accounts.

Finally, this release changes the default SSL/TLS configuration in Shiny Server Pro to remove support for the obsolete and insecure TLSv1 protocol.

### Shiny Server 1.5.8.921

* Upgrade to Node v8.11.3.

* Added support for listening on IPv6 addresses.

* X-Powered-By response header now reports "Shiny Server" instead of "Express".

* Resolve permissions issues when log directory is on an NFS mount with root
  squash. The `log_as_user` directive was intended to work for these situations,
  but would fail in common configurations. It should now work.

* `log_file_mode` no longer respects the process umask, and the default has been
  changed from `0660` to `0640`.

* Exit code of shiny-server process was always 0, regardless of the reason the
  process exited. Now a non-zero exit code is used if the process was terminated
  by a signal, or an unhandled error crashed the process, or loading of the
  shiny-server.conf config file failed during startup.

### Shiny Server Pro 1.5.8.985

The above changes, plus:

* For LDAP double-bind authentication, use the base_bind account to iterate the
  user's groups (rather than the user's own LDAP account, which sometimes does
  not have permissions to see its own groups).

* Added `auth_ignore_case` directive, which can be used to treat `required_user`
  and `required_group` directives as case-insensitive. Disabled by default, as
  it's only safe to use on systems that prevent the creation of users/groups
  whose names vary from existing users/groups only by case.

* For SSL/TLS configurations, remove support for TLSv1 by default (SSLv2 and v3
  were already not supported). If a stricter or looser policy is desired, this
  can be achieved by adding `ssl_min_version` as a child directive of `ssl`;
  valid values for `ssl_min_version` are `tlsv1`, `tlsv11`, and `tlsv12`.

