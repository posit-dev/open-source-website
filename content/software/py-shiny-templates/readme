# Shiny for Python Templates

This repository hosts source files behind [Shiny for Python templates](https://shiny.posit.co/py/templates).

## Installation

To install dependencies for _every_ template, run:

```bash
make install
```

To install dependencies for a specific template, use the `requirements.txt` file in the template's directory. For example:

```bash
pip install -r basic-app-plot/requirements.txt
```

## Running a template

From the terminal, you can then run a template like so:

```bash
shiny run basic-app-plot/app-core.py
```

Alternatively, open the app file of interest in VSCode and [run it from there](https://shiny.posit.co/py/docs/install-create-run.html#run).

# Deployment

Apps are automatically deployed to shinyapps.io.
This should just work for applications that have been previously deployed, but you need to follow a few steps to
deploy a new application.
Each deployment retries three times to avoid spurious failures, and caches the result so as not to redeploy applications which have not changed since the last successful deployment.

# Contributing

1. Create a new folder for the application, the folder should contain at least an `app-core.py` file and a `requirements.txt` file. Optionally add an `app-express.py` file if you want to give people the option to use Shiny Express.
  * Make sure also to add this `requirements.txt` file to the root `./requirements.txt` file.

2. Deploy the app to shinyapps.io in the `gallery` account, if you don't have access to this account mention it in the PR and a member of the Shiny team will do this and the following step for you.

3. Add your application to `deployments.json`, you will need to login to shinyapps.io to get the guid.
  - Note that this `guid` is the same as the `app_id` left in the `rsconnect-python/` manifest created by `rsconnect deploy shiny`.

4. Raise a PR with your changes
