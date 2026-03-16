---
title: 'renv: Project Environments for R'
people:
  - Kevin Ushey
date: '2019-11-06'
slug: renv-project-environments-for-r
categories:
- Packages
tags:
- Packages
- Packages
blogcategories:
- Products and Technology
- Open Source
events: blog
ported_from: rstudio
port_status: in-progress
---


We're excited to announce that [`renv`](https://rstudio.github.io/renv/) is now available on CRAN! You can install `renv` with:

```r install-renv, eval=FALSE
install.packages("renv")
```

`renv` is an R dependency manager. Use `renv` to make your projects more:

- **Isolated**: Each project gets its own library of R packages, so you can feel free to upgrade and change package versions in one project without worrying about breaking your other projects.

- **Portable**: Because `renv` captures the state of your R packages within a lockfile, you can more easily share and collaborate on projects with others, and ensure that everyone is working from a common base.

- **Reproducible**: Use `renv::snapshot()` to save the state of your R library to the lockfile `renv.lock`. You can later use `renv::restore()` to restore your R library exactly as specified in the lockfile.

If you've used [Packrat](http://rstudio.github.io/packrat) before, this may all feel familiar. User feedback has made it clear that a number of the decisions we made during Packrat's development ultimately made it frustrating to use, and led to a sub-optimal user experience. The goal then is for `renv` to be a robust, stable replacement for the Packrat package, with fewer surprises and better default behaviors. While we will continue maintaining Packrat, all new development will focus on `renv`.

In addition, we've built `renv` to work well with R projects using Python through [`reticulate`](https://rstudio.github.io/reticulate/). Using `renv`, you can also create project-local Python environments, and instruct `reticulate` to automatically bind to, manage, and use these environments.


## Getting Started

The core essence of the `renv` workflow is fairly simple:

1. Use `renv::init()` to initialize a project. `renv` will discover the R packages used in your project, and install those packages into a private project library.

2. Work in your project as usual, installing and upgrading R packages as required as your project evolves.

3. Use `renv::snapshot()` to save the state of your project library. The project state will be serialized into a file called `renv.lock`.

4. Use `renv::restore()` to restore your project library from the state of your previously-created lockfile `renv.lock`.

In short: use `renv::init()` to initialize your project library, and use `renv::snapshot()` / `renv::restore()` to save and load the state of your library.

After your project has been initialized, you can work within the project as before, but without fear that installing or upgrading packages could affect other projects on your system.


## Collaborating

When you want to share a project with other collaborators, you may want to ensure everyone is working with the same environment -- otherwise, code in the project may unexpectedly fail to run because of changes in behavior between different versions of the packages in use. You can use `renv` to help make this possible.

When using `renv`, the packages used in your project will be recorded into a lockfile, `renv.lock`. Because `renv.lock` records the exact versions of R packages used within a project, if you share that file with your collaborators, they will be able to use `renv::restore()` to install exactly those packages into their own library. This implies the following workflow for collaboration:

1. Select a way to share your project sources. The most common way nowadays is to use a version control system with a hosted repository; e.g. [Git](https://git-scm.com/) with [GitHub](https://github.com/), but many other options are available.

1. Make sure your project is initialized with `renv` by calling `renv::init()`.

1. Call `renv::snapshot()` as needed, to generate and update `renv.lock`.

1. Share your project sources, alongside the generated lockfile `renv.lock`.

After your collaborators have received your `renv.lock` lockfile -- for example, by cloning the project repository -- they can then also execute `renv::init()` to automatically install the packages declared in that lockfile into their own private project library. By doing this, they will now be able to work within your project using the exact same R packages that you were when `renv.lock` was generated.


## Time Travel

On some occasions, you might find that you've made a change to `renv.lock` that you'd like to roll back. If you're using [Git](https://git-scm.com/) for version control with your project (and we strongly encourage you to!), `renv` has a couple helper functions that make it easy to find and use previously-committed versions of the lockfile.

- Use `renv::history()` to view past versions of `renv.lock` that have been committed to your repository, and find the commit hash associated with that particular revision of `renv.lock`.

- Use `renv::revert()` to pull out an old version of `renv.lock` based on the previously-discovered commit, and then use `renv::restore()` to restore your library from that state.

If you have an alternate version control system you'd like to see us support, please [let us know](https://github.com/rstudio/renv/issues)!


## Integration with Python

`renv` also makes it easy to set up a project-local Python environment to use with your R projects. This can be especially useful if you're using the [`reticulate`](https://rstudio.github.io/reticulate/) package, or other packages depending on reticulate such as [`tensorflow`](https://tensorflow.rstudio.com/) or [`keras`](https://keras.rstudio.com/). Just call:

```r use-python, eval=FALSE
renv::use_python()
```

and a project-local Python environment will be set up and used by `reticulate`. When `renv`'s Python integration is active, a couple extra features will activate:

1. `renv` will instruct `reticulate` to load your project-local version of Python by default, avoiding some of the challenges with finding and selecting an appropriate version of Python on the system.

2. Calling `reticulate::py_install()` will install packages into the project's Python environment by default.

3. When `renv::snapshot()` is called, your project's Python library will also be captured into `requirements.txt` (for virtual environments) / `environment.yml` (for [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) environments).

4. Similarly, `renv::restore()` will also attempt to restore your Python environment, as encoded in `requirements.txt` / `environment.yml` from a previous snapshot.


## Packrat

If you've used Packrat before, you're likely interested to learn what's changed in `renv`. We'll try to summarize the most poignant changes:


### Project Initialization

`packrat::init()` would, by default, attempt to retrieve package sources from CRAN under the assumption that you might want to rebuild packages from sources in the future (e.g. in an offline environment). This assumption was rarely true, and still often was unhelpful as many packages are difficult to build from sources.

To alleviate this, `renv::init()` no longer downloads package sources, and also attempts to copy and reuse packages already installed in your R libraries. This makes initializing new projects a breeze -- you no longer have to sit around and wait as your project's multitude of dependencies get reinstalled; instead, the copies already available on your system will be copied and re-used.


### Snapshots and Dependencies

`packrat::snapshot()` would, in addition to capturing the state of your project library, also attempt to discover the R packages used in your project by crawling your `.R` and `.Rmd` files for dependencies. Unfortunately, this system was fairly unreliable and caused a number of issues, especially when the machinery itself emitted warnings or errors that could not be easily diagnosed.

The dependency discovery machinery in `renv` has been rewritten from the ground up, and should now be much more reliable. However, if you discover that this still causes issues for you, you can disable this altogether by changing the type of snapshot performed in your project. Use `renv::settings$snapshot.type("simple")` to use "simple" snapshots in your project, where the state of your library is captured as-is without any extra filtering to limit which of your installed packages enter the lockfile.


## Extra Tools

In addition, `renv` comes with a couple extra tools out-of-the-box to help with common development workflows:

- Install packages from a wide variety of sources with `renv::install()`. `renv::install()` understands a subset of the [remotes specification](https://cran.r-project.org/web/packages/remotes/vignettes/dependencies.html), and so can be used for simple, dependency-free package installation in your projects. Currently, you can install packages from CRAN, GitHub, Gitlab, and Bitbucket. In addition, `renv` is also compatible with other tools commonly used to install packages, such as [`remotes`](https://remotes.r-lib.org/) and [`pak`](https://pak.r-lib.org/).

- Use `renv::dependencies()` to enumerate the R dependencies in your project. If necessary, use `.renvignore` files to tell `renv` which files and folders should not be scanned during dependency discovery.

Finally, if you have a Packrat project that you'd like to try porting to `renv`, you can use `renv::migrate()` to migrate the project infrastructure over to `renv`.


## Learning More

Please check out the `renv` [Getting started guide](https://rstudio.github.io/renv/articles/renv.html) to learn more. If you are looking for strategies to manage reproducible environments, or don't know if `renv` is the right fit, check out <https://environments.rstudio.com>. If you have questions or comments, please get in touch with us on the [RStudio community forums](https://community.rstudio.com/).

