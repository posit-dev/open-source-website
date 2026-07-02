---
title: "Positron + uv: Python setup in one click"
date: 2026-07-08
people:
  - Isabel Zimmerman
description: >
  Exploring the Positron features that use `uv` to enable Python installation and management.
image: "image.png"
image-alt: "uv logo + Positron logo"
topics:
  - Best Practices
software:
  - positron
languages:
  - Python
source: positron
hidesubscription: false
---

The Python community has a long-standing joke about how hard it is to just get Python running on your machine.
Many tools have been created, and the result often looks like this:

![](https://imgs.xkcd.com/comics/python_environment.png)

We've put together a few workflows that make installing and managing Python as easy as clicking a button.
Most of it leans on [uv, created by Astral](https://docs.astral.sh/uv/)
We chose uv because it's fast, simple, and has quickly become the standard across the Python community.
uv handles the heavy lifting behind the scenes, like resolving versions, downloading interpreters, and building environments; Positron wraps that power in a lightweight UI so you never have to remember a command.

## From zero to Python in one click

Positron offers to install Python if you don't have a suitable Python available.
When you go to start a Python runtime through the `Start Session` button, there will be an option `+ Install Python via uv`.

![](select-interpreter.png)

When you choose it, Positron will ask to install uv for you if you don't already have it available.
Then it shows you the supported Python versions (currently 3.9-3.14) and installs whichever one you pick.
If you have a folder open, it offers to create a virtual environment for the project and starts a Python console session using that environment.
Once you have a Python available to use, this option disappears from the session picker.

If you're not interested in seeing the prompt to install Python, you can turn it off with the `python.allowUvPythonInstall` setting (enabled by default).
Search for it in Settings, or set it directly in your `settings.json`.

<div class="callout callout-tip" role="note" aria-label="Tip">
<div class="callout-header">
<span class="callout-title">Why do I see this when already have Python on my machine?</span>
</div>
<div class="callout-body">

If you only have system Pythons available, you'll still see the `+ Install Python via uv` option.
[Using system Python tends to cause problems down the road](https://pydevtools.com/handbook/explanation/why-should-i-avoid-system-python/), so Positron will always nudge you toward a managed Python and virtual environment instead.

</div>
</div>



## More Python versions at your fingertips

You don't have to wait for Positron to ask, either.
Open the command palette (`cmd+shift+P` on macOS, `ctrl+shift+P` on Windows and Linux) and run `Python: Install Python via uv` any time you want another version.
It's the same flow as the session-picker button above — same uv install, same version list, same optional virtual environment setup — just available whenever you want it, not only on that first run.

![](cmd-uv.png)

Since it runs on demand, it's a clean way to add another interpreter to a project you've already set up.
And because it's the same predictable flow every time, it works well for teaching, since everyone ends up in the same place, the same way.

## Virtual environment support

Setting up a virtual environment isn't limited to that first-run experience.
Whenever Positron spots a `pyproject.toml` or `requirements.txt` in a project that doesn't already have a virtual environment, it'll offer to create one with uv and install your dependencies.
It's especially handy when you've just cloned a colleague's project and want to get running without thinking about it.

![](requirements.png)

If there's a single requirements source, like a lone `requirements.txt` or `pyproject.toml`, it will prompt you to create a `.venv` and install everything right away.
And if there are several sources, say a `requirements.txt` alongside a nested `requirements/dev.txt` and `requirements/prod.txt`, you can choose what files to install.
If your `pyproject.toml` happens to be an installable package, Positron installs it in editable mode with `pip install -e .` as part of that setup.

Positron also knows when to stay out of your way.
If you already have a local virtual environment, or if you use non-uv files like `environment.yml`, `Pipfile`, or `poetry.lock`, you won't get a prompt at all.

## Try it yourself

No more juggling tools and install headaches.
Whether you're setting up a brand new machine, picking up a colleague's project, or getting a room full of students ready to code, the path to a working Python is faster than ever.

Give it a try in [Positron's July 2026 release](https://positron.posit.co/) and let us know what you think.
