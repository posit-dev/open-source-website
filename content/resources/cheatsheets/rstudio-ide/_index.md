---
title: RStudio IDE
image: page-1.png
resource_type: cheatsheet
by: posit
date: '2026-08-01'
description: Navigate the RStudio IDE's source editor, pane layout, Git integration, debugging tools, code diagnostics, and keyboard shortcuts.
download_url: rstudio-ide.pdf
people:
- Garrett Grolemund
- Mine Çetinkaya-Rundel
- Averi Perny
- Curtis Kephart
- Andy Teucher
- David Díaz Rodríguez
thumbnails:
- page-1.png
- page-2.png
software:
- rstudio
languages:
- R
translations:
- language: French
  lang: fr
  file: rstudio-ide_fr.pdf
  added: 2017-01
  people:
  - Diane Beldame
- language: Greek
  lang: el
  file: rstudio-ide_el.pdf
  updated: 2017-09
  people:
  - Kleanthis Koupidis
- language: Italian
  lang: it
  file: rstudio-ide_it.pdf
  updated: 2016-01
  people:
  - Angelo Salatino
- language: Japanese
  lang: ja
  file: rstudio-ide_ja.pdf
  updated: 2017-09
  people:
  - Masato Takahashi
- language: Portuguese
  lang: pt
  file: rstudio-ide_pt.pdf
  updated: 2016-03
  people:
  - Augusto Queiroz de Macedo
- language: Spanish
  lang: es
  file: rstudio-ide_es.pdf
  updated: 2024-05
  people:
  - Monica Alonso
  - David Díaz Rodríguez
- language: Vietnamese
  lang: vi
  file: rstudio-ide_vi.pdf
  edition: Awesome 5.15.3
  updated: 2021-07
  people:
  - Le-Huynh Truc-Ly
---

## Documents and Apps

Open Shiny, Quarto, R Markdown, knitr, Sweave, LaTeX, .Rd files and more in Source Pane.

![RStudio Source Pane view](images/document-and-apps-rstudio-ide.png)

<details>
<summary>Expand to read about the features in the RStudio Source Pane</summary>

### Features within the RStudio Source Pane

-   Check spelling
-   Render output
-   Choose output format
-   Configure render options
-   Insert code chunk
-   Publish to server
-   Jump to previous chunk
-   Jump to next chunk
-   Run code
-   Show file outline
-   Visual Editor (reverse side)
-   Jump to section or chunk
-   Run this and all previous code chunks
-   Run this code chunk
-   Set knitr chunk options

</details>

Access markdown guide at **Help \> Markdown Quick Reference**.

See below for more on [Visual Editor](#visual-editor).

## Source Editor

![RStudio Source Editor view](images/source-editor-rstudio-ide.png)

<details>
<summary>Expand to read about the features in the Source Editor</summary>

### Features within the Source Editor

-   Navigate backwards/forwards
-   Open in new window
-   Save
-   Find and replace
-   Compile as notebook
-   Run selected code
-   Re-run previous code
-   Source with or without Echo or as a Local Job
-   Show file outline
-   Multiple cursors/column selection with Alt + mouse drag.
-   Code diagnostics that appear in the margin. Hover over diagnostic symbols for details.
-   Syntax highlighting based on your file's extension
-   Tab completion to finish function names, file paths, arguments, and more.
-   Multi-language code snippets to quickly use common blocks of code.
-   Jump to function in file
-   Change file type
-   Working Directory
-   Run scripts in separate sessions
-   Maximize, minimize panes
-   <kbd>Ctrl/Cmd + ↑</kbd> to see history
-   R Markdown Build Log
-   Drag pane boundaries

</details>

## Tab Panes

![RStudio Tab Panes view](images/tab-panes.png)

<details>
<summary>Expand to read about the features in the Tab Panes</summary>

### Features within the Tab Panes

-   **Import data** with wizard
-   History of past commands to run/copy
-   Manage external databases
-   View memory usage
-   R tutorials
-   Load workspace
-   Save workspace
-   Clear R workspace
-   Search inside environment
-   Choose environment to display from list of parent environments
-   Display objects as list or grid
-   Displays saved objects by type with short description
-   View in data viewer
-   View function source code
-   Create folder
-   Path to displayed directory
-   Delete file
-   Rename file
-   More file options
-   Change directory
-   A File browser keyed to your working directory. Click on file or directory name to open.

</details>

## Version Control

Turn on at **Tools \> Project Options \> Git/SVN**

<ul class="inline">

<li>A - Added</li>

<li>D - Deleted</li>

<li>M - Modified</li>

<li>R - Renamed</li>

<li>?
- Untracked</li>

</ul>

![Version Control view](images/version-control.png)

<details>
<summary>Expand to read about the features in the version control view</summary>

### Features within the version control view

-   Stage files
-   Commit staged files
-   Push/Pull to remote
-   View History
-   Current branch
-   Show file diff to view file differences

</details>

## Package Development

Create a new package with **File \> New Project \> New Directory \> R Package**

Enable roxygen documentation with **Tools \> Project Options \> Build Tools**

Roxygen guide at **Help \> Roxygen Quick Reference**

See package information in the **Build Tab**

![Package build view](images/pd-build-tab.png)

<details>
<summary>Expand to read about the features in the Build Tab</summary>

### Features within the Build Tab

-   Install package and restart R
-   Run devtools::load_all() and reload changes
-   Run R CMD check
-   Clear output and rebuild
-   Customize package build options
-   Run package tests

</details>

RStudio opens plots in a dedicated **Plots** pane

![Plots view](images/pd-plots-pane.png)

<details>
<summary>Expand to read about the features in the Plots</summary>

### Features within the Plots pane

-   Navigate recent plots
-   Open in window
-   Export plot
-   Delete plot
-   Delete all plots

</details>

GUI **Package** manager lists every installed package

![Package manager view](images/pd-package-manager.png)

<details>
<summary>Expand to read about the features in the Package manager</summary>

### Features within the Package manager

-   Install Packages
-   Update Packages
-   Browse package site
-   Click to load package with `library()`. Unclick to detach package with `detach()`.
-   Package version installed
-   Delete from library

</details>

RStudio opens documentation in a dedicated **Help** pane

![Help pane view](images/pd-help-pane.png)

<details>
<summary>Expand to read about the features in the Help pane</summary>

### Features within the Help pane

-   Home page of helpful links
-   Search within help file
-   Search for help file

</details>

**Viewer** pane displays HTML content, such as Shiny apps, R Markdown reports, and interactive visualizations

![Viewer pane view](images/pd-viewer-pane.png)

<details>
<summary>Expand to read about the features in the Viewer pane</summary>

### Features within the Viewer pane

-   Stop Shiny apps
-   Publish to shinyapps.io, Posit Connect, Posit Cloud, ...
-   Refresh

</details>

`View(<data>)` opens spreadsheet like view of data set

![Spreadsheet pane view](images/pd-view-data.png)

<details>
<summary>Expand to read about the features in the data set spreadsheet</summary>

### Features within the data set spreadsheet

-   Filter rows by value or value range
-   Sort by values
-   Search for value

</details>

## Debug Mode

Use `debug()`, `browser()`, or a breakpoint and execute your code to open the debugger mode.

![Debug console view](images/dm-console.png)

<details>
<summary>Expand to read about the features in the debug console</summary>

### Features within the debug console

-   Launch debugger mode from origin of error
-   Open traceback to examine the functions that R called before the error occurred
-   Click next to line number to add/remove a breakpoint.
-   Highlighted line shows where execution has paused
-   Run commands in environment where execution has paused
-   Examine variables in executing environment
-   Select function in traceback to debug
-   Step through code one line at a time
-   Step into and out of functions to run
-   Resume execution
-   Quit debug mode

</details>

## Keyboard Shortcuts

View the Keyboard Shortcut Quick Reference with **Tools \> Keyboard Shortcuts** or <kbd>Alt/Option + Shift + K</kbd>

![Keyboard Shortcut Quick Reference view](images/tools-keyboard-shortcuts.png)

Search for keyboard shortcuts with **Tools \> Show Command Palette** or <kbd>Ctrl/Cmd + Shift + P</kbd>.

![Show Command Palette view](images/tools-show-command-palette.png)

## Visual Editor

![Visual Editor view](images/ide-visual-editor.png)

<details>
<summary>Expand to read about the features in the Visual Editor</summary>

### Features within the Visual Editor

-   Check spelling
-   Render output
-   Choose output format
-   Choose output location
-   Insert code chunk
-   Jump to previous chunk
-   Jump to next chunk
-   Run selected lines
-   Publish to server
-   Show file outline
-   Block format
-   Back to Source Editor (front page)
-   Insert verbatim code
-   Clear formatting
-   Lists and block quotes
-   Links
-   Citations
-   Images
-   More formatting
-   Insert blocks, citations, equations, and special characters
-   Insert and edit tables
-   File outline
-   Add/Edit attributes
-   Jump to chunk or header
-   Set knitr chunk options
-   Run this and all previous code chunks
-   Run this code chunk

</details>

## Posit Workbench

### Why Posit Workbench?

Extend the open source server with a commercial license, support, and more:

-   open and run multiple R sessions at once
-   tune your resources to improve performance
-   administrative tools for managing user sessions
-   collaborate real-time with others in shared projects
-   switch easily from one version of R to a different version
-   integrate with your authentication, authorization, and audit practices
-   work in the RStudio IDE, JupyterLab, Jupyter Notebooks, or VS Code

Download a free [45 day evaluation](https://posit.co/products/enterprise/workbench/).

## Share Projects

**File \> New Project**

RStudio saves the call history, workspace, and working directory associated with a project.
It reloads each when you re-open a project.

![Share Project view](images/share-projects.png)

<details>
<summary>Expand to read about the features in the Share Project</summary>

### Features within the Share Project

-   Start **new R Session** in current project
-   Close R Session in project
-   Active shared collaborators
-   Name of current project
-   **Share Project** with Collaborators
-   **Select R Version**

</details>

## Run Remote Jobs

Run R on remote clusters (Kubernetes/Slurm) via the Job Launcher

![Launcher view](images/run-remote-job.png)

<details>
<summary>Expand to read about the features in the Job Launcher</summary>

### Features within the Job Launcher

-   Launch a job
-   Monitor launcher jobs
-   Run launcher jobs remotely

</details>

------------------------------------------------------------------------

CC BY SA Posit Software, PBC • [info\@posit.co](mailto:info@posit.co) • [posit.co](https://posit.co)

Learn more at [docs.posit.co/ide/user](https://docs.posit.co/ide/user/).

Updated: 2026-08.

RStudio IDE 2024.04.1+748.

------------------------------------------------------------------------
