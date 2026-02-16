Shinylive Python package
========================

[![Build and test](https://github.com/posit-dev/py-shinylive/actions/workflows/build.yml/badge.svg)](https://github.com/posit-dev/py-shinylive/actions/)
[![PyPI Latest Release](https://img.shields.io/pypi/v/shinylive.svg)](https://pypi.org/project/shinylive/)

[Documentation site](https://github.com/posit-dev/py-shinylive)

The goal of the shinylive Python package is to help you create Shinylive applications from your [Shiny for Python](https://shiny.posit.co/py) applications.
Shinylive runs Shiny entirely in the browser, without any need for a hosted server, using WebAssembly via [pyodide](https://pyodide.org/en/stable/).

## About Shinylive

The Shinylive project consists of four interdependent components that work together in several different contexts.

1. Shinylive ([posit-dev/shinylive](https://github.com/posit-dev/shinylive)) is a web assets library that runs Shiny applications in the browser. You can try it out online at [shinylive.io/r](https://shinylive.io/r) or [shinylive.io/py](https://shinylive.io/py).

2. The [shinylive Python package](https://shiny.posit.co/py/get-started/shinylive.html) ([posit-dev/py-shinylive](https://github.com/posit-dev/py-shinylive)) helps you export your Shiny applications from local files to a directory that can be hosted on a static web server.

   The Python package also downloads the Shinylive web assets mentioned above and manages them in a local cache. These assets are included in the exported Shinylive applications and are used to run your Shiny app in the browser.

3. The shinylive R package ([posit-dev/r-shinylive](https://github.com/posit-dev/r-shinylive)) serves the same role as the shinylive Python package but for Shiny for R apps.

4. The [shinylive Quarto extension](https://quarto-ext.github.io/shinylive/) ([quarto-ext/shinylive](https://github.com/quarto-ext/shinylive)) lets you write Shiny applications in [Quarto web documents and slides](https://quarto.org) and uses the Python or R package (or both) to translate `shinylive-py` or `shinylive-r` code blocks into Shinylive applications.

## Installation

```
pip install shinylive
```


## Usage

(Optional) Create a basic shiny application in a new directory `myapp/`:

```
shiny create myapp
```

Once you have a Shiny application in `myapp/` and would like turn it into a Shinylive app in `site/`:

```
shinylive export myapp site
```

Then you can preview the application by running a web server and visiting it in a browser:

```
python3 -m http.server --directory site --bind localhost 8008
```

At this point, you can deploy the `site/` directory to any static web hosting service.


### Multiple applications

If you have multiple applications that you want to put on the same site, you can export them to subdirectories of the site, so that they can all share the same Shinylive assets. You can do this with the `--subdir` option:

```bash
shinylive export myapp1 site --subdir app1
shinylive export myapp2 site --subdir app2
```


## Shinylive asset management

Each version of the Shinylive Python package is associated with a particular version of the Shinylive web assets. ([See the releases here](https://github.com/posit-dev/shinylive/releases).)

To see which version of this Python package you have, and which version of the web assets it is associated with, simply run `shinylive` at the command prompt:

```
$ shinylive
Usage: shinylive [OPTIONS] COMMAND [ARGS]...

  shinylive Python package version: 0.1.0
  shinylive web assets version:     0.2.1
...
```

The web assets will be downloaded and cached the first time you run `shinylive export`. Or, you can run `shinylive assets download` to fetch them.

```
$ shinylive assets download
Downloading https://github.com/posit-dev/shinylive/releases/download/v0.2.1/shinylive-0.2.1.tar.gz...
Unzipping to /Users/username/Library/Caches/shinylive/
```

To see what versions you have installed, run `shinylive assets info`:

```
$ shinylive assets info
    Local cached shinylive asset dir:
    /Users/username/Library/Caches/shinylive

    Installed versions:
    /Users/username/Library/Caches/shinylive/shinylive-0.2.1
    /Users/username/Library/Caches/shinylive/shinylive-0.0.6
```

You can remove old versions with `shinylive assets cleanup`. This will remove all versions except the one that the Python package wants to use:

```
$ shinylive assets cleanup
Keeping version 0.2.1
Removing /Users/username/Library/Caches/shinylive/shinylive-0.0.6
```

If you want to force it to remove a specific version, use the `shinylive assets remove xxx`:

```
$ shinylive assets remove 0.2.1
Removing /Users/username/Library/Caches/shinylive/shinylive-0.2.1
```
