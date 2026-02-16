# Shiny - VS Code Extension

This is an extension to help launch [Shiny applications](https://shiny.posit.co). Shiny is a package for [Python](https://shiny.posit.co/py/) and [R](https://shiny.posit.co/r/getstarted/) that is designed to make it easy to build interactive web applications with the powerful data and scientific features of Python and R.

## Features

### Run and Debug Shiny Apps

The main features of this extension are additional options in the Run button menu when editing an `app.py` or `app.R` file to "Run Shiny App" or "Debug Shiny App" (Python only).

![Run app](https://shiny.posit.co/py/docs/assets/vscode.png)

It also provides a couple of code snippets in both Python and R:

- `shinyapp` for creating a new Shiny application
- `shinymod` for creating a new Shiny module
- `shinyexpress` for creating a new Shiny Express application (Python)

For a complete Shiny for Python experience in VS Code, please [visit our docs for more information](https://shiny.posit.co/py/docs/install-create-run.html#vs-code), including instructions for configuring the type checker and debugger for use with Shiny.

### Shinylive

You can use the extension to create shareable links to your apps using [Shinylive](https://shinylive.io), a free service for sharing Shiny apps via static hosting. Shinylive links encode the app's code and data in the URL, so you can share your app with others without needing to deploy it to a server. When the link is opened, the app runs in the user's browser using special version of Python or R that can run in the browser.

**To create a Shinylive link from your app**, you have two choices:

1. For single-file apps, e.g. `app.py` or `app.R`, run the **Create ShinyLive Link from Active File** from the command palette with the app file open and active.

2. For multi-file apps, select all of the files or directories you want to include in your Shinylive app in the Explorer pane. Then right click on the selection and choose **Create ShinyLive Link from Selected Files**.

The Shiny extension will ask you which app mode you want to use (display the _app_ or show an _editor_ next to the app) and what action to take (to _open_ or _copy_ the link).You can also configure these options in the extension settings.

For the reverse operation, use the **Save App from Shinylive Link** command in the command palette to save an app and its files from a Shinylive link. You'll be prompted to paste the Shinylive link and then to choose where the app will be saved in your workspace.

## Extension Settings

This extension contributes the following settings for Python and R.

### Python

- `shiny.python.port`: The port number to listen on when running a Shiny for Python app. (By default, 0, which will choose a random port for each workspace.)
- `shiny.python.debugJustMyCode`: When running the "Debug Shiny App" command, only step through user-written code. Disable this to allow stepping through library code. (Defaults to true.)

Note that there is no setting for Python executable path or virtual environment. This extension uses whatever Python environment the VS Code Python extension thinks is active. If you find that the "Run Shiny App" and "Debug Shiny App" commands are launching with a different version of Python or different virtual environment than you intended, use the Python extension's [Select Interpreter](https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters) command to change it.

### R

- `shiny.r.port`: The port number to listen on when running a Shiny app. (By default, 0, which will choose a random port for each workspace.)
- `shiny.r.devmode`: When `true` (default), Shiny for R apps are launched [in developer mode](https://shiny.posit.co/r/reference/shiny/latest/devmode.html).

### Shinylive

- `shiny.shinylive.appMode`: Should the Shinylive link open the app in `"app"` mode, showing only the app and an optional header, or in `"editor"` mode with the app alongside an editor and console pane. The default is `"ask"`, which prompts you each time you create Shinylive link.
- `shiny.includeHeader`: Include the "Shiny" header in the Shinylive link when opening in app mode?
- `shiny.shinylive.openAction`: What action should be taken when opening a Shinylive link? Options are `"open"` to open the link in an external browser, `"copy"` the link to the clipboard, or `"ask"`. The default is `"ask"`, which prompts you each time you create a Shinylive link.
- `shiny.shinylive.host`: The Shinylive host used when creating a Shinylive link. The default is `"https://shinylive.io"`, which uses the latest released version of Shiny in Python or R. Or `"https://posit-dev.github.io/shinylive"`, which uses the latest development version of Shiny in Python or R.

### Working Directory Configuration

By default, Shiny apps run from the workspace root directory. This works well for most projects, but you may need apps to run from a different directory—for example, when using renv in a subfolder or organizing apps in a monorepo structure.

The extension provides two settings to control the working directory:

- `shiny.runFrom`: Global default for all apps in the workspace
  - `"projectRoot"` (default): Run apps from the workspace root
  - `"appDirectory"`: Run apps from the directory containing the app file

- `shiny.runFromOverrides`: Per-app overrides for specific files
  - For specific app paths (relative to the project root), choose which root-relative path the app is run from.
  - Empty string `""` means project root
  - This is a workspace-only setting

**Example configuration** for a project with apps in subfolders using renv:

```json
{
  "shiny.runFrom": "appDirectory",
  "shiny.runFromOverrides": {
    "src/apps/main/app.py": "",
    "src/r-apps/dashboard/app.R": "src/r-apps"
  }
}
```

**Setting overrides via Command Palette:**

Instead of editing `settings.json` manually, you can use the **"Shiny: Run this app from..."** command to set the run from override for an open app file.
