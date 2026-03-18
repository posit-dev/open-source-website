---
title: 'DT 0.4: Editing Tables, Smart Filtering, and More'
people:
  - Yihui Xie
date: '2018-03-29'
categories:
- Packages
tags:
- DT
- DataTables
- shiny
- Packages
slug: dt-0-4
blogcategories:
- Products and Technology
- Open Source
ported_from: rstudio
port_status: in-progress
---


It has been [more than two years](/2015/06/24/dt-an-r-interface-to-the-datatables-library/) since we announced the initial version of the **DT** package. Today we want to highlight a few significant changes and new features in the recent releases v0.3 and v0.4. The full changes can be found in the [release notes](https://github.com/rstudio/DT/releases).

## Editable tables

Now you can make a table editable through the new argument `datatable(..., editable = TRUE)`. Then you will be able to edit a cell by double-clicking on it. This feature works in both client-side and server-side (Shiny) processing modes. See [here for examples](https://github.com/rstudio/DT/pull/480).

![An editable tables](https://user-images.githubusercontent.com/163582/38057156-1c0cce84-32a4-11e8-84ac-1c93ec60684e.png)

## Smart filtering in the server-side processing mode

Searching in the server-side processing mode has enabled [the "smart" mode](https://datatables.net/reference/option/search.smart) by default. Previously, this mode only works in the client-side processing mode. If you want to disable the smart filtering, you can set the initialization option in `datatable()` (e.g., `options = list(search = list(smart = FALSE))`). The smart filtering means spaces in the global search keyword for the table will have a special meaning: each returned record in the table should match _all_ of the words separated by spaces. For example, a keyword "1234 abc" will match every record in the table that contain both "1234" and "abc" (in previous versions, this is just treated as a single keyword).

![Smart filters in DataTables](https://user-images.githubusercontent.com/163582/38057956-bedfad96-32a6-11e8-815c-73abce2d74bc.png)

## Shift + Clicking for row selection

After you have enabled [row selection](https://rstudio.github.io/DT/shiny.html), you can hold the `Shift` key and click to select multiple consecutive rows.

## DTOutput() and renderDT() for Shiny apps

We have added functions `DTOutput()` and `renderDT()` as aliases of `dataTableOutput()` and `renderDataTable()`, respectively. This is because the latter two often collide with functions of the same names in **shiny**. You are recommended to use `DTOutput()` and `renderDT()` in Shiny apps, so that you don't have to worry about forgetting the `DT::` qualifier (e.g., `DT::renderDataTable`). Naming is hard, and this was perhaps my biggest mistake in the initial version of **DT**. I was too optimistic that `DT::renderDataTable()` could quickly and easily replace `shiny::renderDataTable()` so we could drop the latter. It turned out that the two were not completely compatible initially, and had got more and more differences later (**DT** has many more features).

Versions 0.3 and 0.4 also include several bug fixes, and we appreciate all the bug reports and pull requests from **DT** users. In particular, we want to thank Xianying Tan ([@shrektan](https://github.com/shrektan)) for his many helpful pull requests to implement new features and fix bugs.

Again, the full documentation is at <https://rstudio.github.io/DT/>. Please use [Github issues](https://github.com/rstudio/DT/issues) if you want to file bug reports or feature requests, and use [StackOverflow](https://stackoverflow.com/questions/tagged/dt) or [RStudio Community](https://community.rstudio.com) if you have questions.

