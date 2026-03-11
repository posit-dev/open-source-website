---
title: Time Travel with RStudio Package Manager 1.0.4
people:
  - Sean Lopp
date: '2019-01-30'
slug: time-travel-with-rstudio-package-manager-1-0-4
categories:
- RStudio Package Manager
tags:
- RSPM
- packages
- RStudio Package Manager
blogcategories:
- Products and Technology
events: blog
ported_from: rstudio
port_status: raw
---


We all love packages. We don't love when broken package environments prevent us
from reproducing our work. In version 1.0.4 of RStudio Package Manager,
individuals and teams can navigate through repository checkpoints,
making it easy to recreate environments and reproduce work. The new release also
adds important security updates, improvements for Git sources, further access to
retired packages, and beta support for Amazon S3 storage.

#### New to RStudio Package Manager? 

[Download](https://rstudio.com/products/package-manager/) the 45-day evaluation
today to see how RStudio Package Manager can help you, your team, and your
entire organization access and organize R packages. Learn more with our [online
demo server](https://demo.rstudiopm.com) or [latest webinar](https://resources.rstudio.com/webinars/introduction-to-the-rstudio-package-manager-sean-lopp).

{{< figure src="/blog-images/rspm-104-calendar.png" caption="Easily navigate historical repositories" alt= "Easily navigate historical repositories">}}

## Updates

### Time Travel

RStudio Package Manager automatically tracks every change to your repositories,
whether you're adding new packages to a curated source, syncing the latest data
from CRAN, or building a new commit of your internal package. These changes are
efficiently stored as checkpoints. By default, R users installing packages will
get the latest and greatest, but they can also install packages from any point
in the past.

A [new calendar](https://demo.rstudiopm.com/client/#/repos/3/overview) on a
repository's setup page can be used to travel backwards in time. If you last
used a project in November, you can install packages as they existed **in your
repository** from that moment, making it much easier to guarantee your work is
reproducible.

{{< figure src="/blog-images/rspm-104-calendar.gif" caption="Time travel with a repository calendar" alt= "Time travel with a repository calendar">}}

Alternatively, it is also possible to preemptively pin a project to a frozen
checkpoint. This can be really useful in cases where you know you'll always want
the same set of packages. For example, you can include a reference to a
checkpoint inside of a Dockerfile to ensure anytime the Docker image is rebuilt,
you'll get the same packages and versions.

```
RUN Rscript -e 'install.packages(...,
  repos = "https://rpkgs.example.com/cran/128")'
```

### New Storage Options

Version 1.0.4 adds beta support for storing packages on Amazon S3 instead of
local or shared storage. In addition, we've expanded the [configuration
options](https://docs.rstudio.com/rspm/admin/appendix-configuration.html#appendix-configuration-filestorage) for administrators to control exactly where and how Package Manager stores packages, data, and metrics.


### Retired Packages

You may be familiar with archived packages - they are older versions of packages
that are listed at the bottom of a package's information page.

{{< figure src="/blog-images/rspm-104-archive.png" caption="Access archived versions" alt= "Access archived versions">}}

Did you know that CRAN packages can be retired? "Retirement" occurs when every
version of a package is placed in the archive and no version remains current.
Packages can be retired for a variety of reasons: perhaps the maintainer is no
longer fixing breaking changes, or the functionality has been replaced
by a new package. While retired packages are typically not used by new projects,
it can be useful to see if a package you're searching for is retired. Library
management tools like `packrat` also make use of retired packages to recreate
older environments. In 1.0.4, retired packages show up in a repository with a
special page indicating their status.

{{< figure src="/blog-images/rspm-104-retire.png" caption="View retired packages" alt= "View retired packages">}}

### Git Source Improvements

RStudio Package Manager makes it easy to share R packages that live inside of
Git, either internal packages or packages from GitHub. This release includes a
number of quality of life improvements:

- **Subdirectories** In verison 1.0.4, we've added support to build packages that live in
sub-directories of a Git file system.

- **SSH keys** We've added support for SSH keys that use a passphrase, and
we've significantly improved how SSH keys are used to access Git repos.

- **Description Files** Packages built from Git now have the commit SHA included
in their DESCRIPTION file for reference.

## Deprecations, Breaking Changes, and Security Updates

- **Breaking Change** Version 1.0.4 introduces an important security enhancement that
helps isolate package builds from the rest of Package Manager. If you are using
packages from Git **and** running on RedHat/CentOS or inside of a Docker
container, you may need to update your configuration. Follow [these
instructions](https://docs.rstudio.com/rspm/1.0.4/admin/process-management.html)
for more information.

- The use of SSH keys for accessing Git repositories has been improved by adding
support for passphrases and isolated SSH agents.

Please review the [full release notes](https://docs.rstudio.com/rspm/news).

> #### Upgrade Planning
> Please note the breaking changes and deprecations above. Upgrading to 1.0.4
> from 1.0.0 will take less than five minutes. If you are upgrading from an
> earlier beta version, be sure to consult the release notes for the
> intermediate releases, as well.

Don't see that perfect feature? Wondering why you should be worried about
package management? Want to talk about other package management strategies?
[Email us](mailto:sales@rstudio.com), our product team is happy to help!

- [Admin Guide](https://docs.rstudio.com/rspm/admin)
- [Overview PDF](https://www.rstudio.com/wp-content/uploads/2018/07/RStudio-Package-Manager-Overview.pdf)
- [Introductory Webinar](https://resources.rstudio.com/webinars/introduction-to-the-rstudio-package-manager-sean-lopp)
- [Online Demo](https://demo.rstudiopm.com)

