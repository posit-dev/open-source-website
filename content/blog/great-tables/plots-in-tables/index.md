---
title: Adding Plots to Great Tables
people:
  - Jules Walzer-Goldfeld
  - Michael Chow
date: '2025-07-03T00:00:00.000Z'
ported_from: great_tables
port_status: in-progress
software: ["great-tables"]
languages: ["Python"]
categories:
  - Visualization
tags:
  - Great Tables
---


<script src="https://cdn.jsdelivr.net/npm/requirejs@2.3.6/require.min.js" integrity="sha384-c9c+LnTbwQ3aujuU7ULEPVvgLs+Fn6fJUvIGTsuu1ZcCf11fiEubah0ttpca4ntM sha384-6V1/AdqZRWk1KAlWbKBlGhN7VG4iE/yAZcO6NZPMF8od0vukrvr0tg4qY6NSrItx" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js" integrity="sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/6Z/hRTt8+pR6L4N2" crossorigin="anonymous" data-relocate-top="true"></script>
<script type="application/javascript">define('jquery', [],function() {return window.jQuery;})</script>


While working on [**gt-extras**](https://posit-dev.github.io/gt-extras/articles/intro.html), I've been exploring how to add small plots to Great Tables. These can go by many names, like spark lines, nanoplots, and so on. In this post, I'll look at three approaches I tried: adding plots with [`plotnine`](https://plotnine.org/), [`svg.py`](https://github.com/orsinium-labs/svg.py), or adding HTML directly. In the first two cases, the plots are SVGs, while the latter entails a collection of composed HTML div elements.

Here are the pieces I'll cover:

- **svg.py**: creating your own tiny chart directly for a row.
- **direct HTML**: adding HTML divs directly.
- **plotnine**: adding a full, stripped-down chart to a row.

In the end, it's often simplest to use `svg.py`, since you can create basic charts with minimal overhead. Building elements with HTML has even *less* overhead, but it is also slightly less user-friendly. At the other end of the spectrum, as your charts become more complex, using existing packages like the more exhaustive `plotnine` is a good alternative.

<div id="fpuvtcetir" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#fpuvtcetir table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#fpuvtcetir thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#fpuvtcetir p { margin: 0; padding: 0; }
 #fpuvtcetir .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #fpuvtcetir .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #fpuvtcetir .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #fpuvtcetir .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #fpuvtcetir .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fpuvtcetir .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fpuvtcetir .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #fpuvtcetir .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #fpuvtcetir .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #fpuvtcetir .gt_column_spanner_outer:first-child { padding-left: 0; }
 #fpuvtcetir .gt_column_spanner_outer:last-child { padding-right: 0; }
 #fpuvtcetir .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #fpuvtcetir .gt_spanner_row { border-bottom-style: hidden; }
 #fpuvtcetir .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #fpuvtcetir .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #fpuvtcetir .gt_from_md> :first-child { margin-top: 0; }
 #fpuvtcetir .gt_from_md> :last-child { margin-bottom: 0; }
 #fpuvtcetir .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #fpuvtcetir .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #fpuvtcetir .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #fpuvtcetir .gt_row_group_first td { border-top-width: 2px; }
 #fpuvtcetir .gt_row_group_first th { border-top-width: 2px; }
 #fpuvtcetir .gt_striped { color: #333333; background-color: #F4F4F4; }
 #fpuvtcetir .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #fpuvtcetir .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #fpuvtcetir .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #fpuvtcetir .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #fpuvtcetir .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #fpuvtcetir .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #fpuvtcetir .gt_left { text-align: left; }
 #fpuvtcetir .gt_center { text-align: center; }
 #fpuvtcetir .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #fpuvtcetir .gt_font_normal { font-weight: normal; }
 #fpuvtcetir .gt_font_bold { font-weight: bold; }
 #fpuvtcetir .gt_font_italic { font-style: italic; }
 #fpuvtcetir .gt_super { font-size: 65%; }
 #fpuvtcetir .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #fpuvtcetir .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Animal  | Legs | Plot |
|---------|------|------|
| Ostrich | 2    | 2    |
| Spider  | 8    | 8    |
| Lion    | 4    | 4    |

</div>

Here is the final result:

<details class="code-fold">
<summary>Code</summary>

``` python
import polars as pl
from great_tables import GT
from svg import SVG, Rect, Line

df = pl.DataFrame({"Animal": ["Ostrich", "Spider", "Lion"], "Legs": [2, 8, 4], "Plot": [2, 8, 4]})

width = 50
height = 30
max_legs_value = df["Legs"].max()


def create_plot_svg_py(val: int) -> str:
    canvas = SVG(
        width=width,
        height=height,
        elements=[
            Rect(
                x=0,
                y=height / 4,
                width=width * (val / max_legs_value),
                height=height / 2,
                fill="blue",
            ),
            Line(x1=0, x2=0, y1=0, y2=height, stroke="black"),
        ],
    )

    html = f"<div>{canvas}</div>"
    return html


GT(df).fmt(fns=create_plot_svg_py, columns=["Plot"])
```

</details>
<div id="pftjpqlkkc" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#pftjpqlkkc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pftjpqlkkc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pftjpqlkkc p { margin: 0; padding: 0; }
 #pftjpqlkkc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pftjpqlkkc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pftjpqlkkc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pftjpqlkkc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pftjpqlkkc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pftjpqlkkc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pftjpqlkkc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pftjpqlkkc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pftjpqlkkc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pftjpqlkkc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pftjpqlkkc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pftjpqlkkc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pftjpqlkkc .gt_spanner_row { border-bottom-style: hidden; }
 #pftjpqlkkc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pftjpqlkkc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pftjpqlkkc .gt_from_md> :first-child { margin-top: 0; }
 #pftjpqlkkc .gt_from_md> :last-child { margin-bottom: 0; }
 #pftjpqlkkc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pftjpqlkkc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pftjpqlkkc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pftjpqlkkc .gt_row_group_first td { border-top-width: 2px; }
 #pftjpqlkkc .gt_row_group_first th { border-top-width: 2px; }
 #pftjpqlkkc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pftjpqlkkc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pftjpqlkkc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pftjpqlkkc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pftjpqlkkc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pftjpqlkkc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pftjpqlkkc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pftjpqlkkc .gt_left { text-align: left; }
 #pftjpqlkkc .gt_center { text-align: center; }
 #pftjpqlkkc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pftjpqlkkc .gt_font_normal { font-weight: normal; }
 #pftjpqlkkc .gt_font_bold { font-weight: bold; }
 #pftjpqlkkc .gt_font_italic { font-style: italic; }
 #pftjpqlkkc .gt_super { font-size: 65%; }
 #pftjpqlkkc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pftjpqlkkc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="gt_col_headings">
<th id="Animal" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">Animal</th>
<th id="Legs" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Legs</th>
<th id="Plot" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Plot</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ostrich</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right"><div>
<svg xmlns="http://www.w3.org/2000/svg" width="50" height="30">
<rect x="0" y="7.5" width="12.5" height="15.0" fill="blue"></rect><line stroke="black" x1="0" y1="0" x2="0" y2="30"></line>
</svg>
</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Spider</td>
<td class="gt_row gt_right">8</td>
<td class="gt_row gt_right"><div>
<svg xmlns="http://www.w3.org/2000/svg" width="50" height="30">
<rect x="0" y="7.5" width="50.0" height="15.0" fill="blue"></rect><line stroke="black" x1="0" y1="0" x2="0" y2="30"></line>
</svg>
</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Lion</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right"><div>
<svg xmlns="http://www.w3.org/2000/svg" width="50" height="30">
<rect x="0" y="7.5" width="25.0" height="15.0" fill="blue"></rect><line stroke="black" x1="0" y1="0" x2="0" y2="30"></line>
</svg>
</div></td>
</tr>
</tbody>
</table>

</div>

## Setup

Here is the code to start:

``` python
import polars as pl
from great_tables import GT

df = pl.DataFrame(
    {
        "Animal": ["Ostrich", "Spider", "Lion"],
        "Legs": [2, 8, 4],
        "Plot": [2, 8, 4],
    }
)

gt = GT(df)
```

## The Binding Component: GT.fmt()

Let's take advantage of the [`fmt()`](https://posit-dev.github.io/great-tables/reference/GT.fmt.html#great_tables.GT.fmt) method to apply a plotting function that formats our row values into plots. To see how we might use `fmt()`, we first need to define a formatting function to apply to each cell in a column. It will take as input the value in the cell, and should return whatever you want in that cell. Before plotting, let's imagine we wanted to replace the number with a tally of the number of legs:

``` python
def create_leg_tally(value: int) -> str:
    return "|" * value


gt.fmt(fns=create_leg_tally, columns="Plot")
```

<div id="stpyfgvtjj" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#stpyfgvtjj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#stpyfgvtjj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#stpyfgvtjj p { margin: 0; padding: 0; }
 #stpyfgvtjj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #stpyfgvtjj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #stpyfgvtjj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #stpyfgvtjj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #stpyfgvtjj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #stpyfgvtjj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #stpyfgvtjj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #stpyfgvtjj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #stpyfgvtjj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #stpyfgvtjj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #stpyfgvtjj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #stpyfgvtjj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #stpyfgvtjj .gt_spanner_row { border-bottom-style: hidden; }
 #stpyfgvtjj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #stpyfgvtjj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #stpyfgvtjj .gt_from_md> :first-child { margin-top: 0; }
 #stpyfgvtjj .gt_from_md> :last-child { margin-bottom: 0; }
 #stpyfgvtjj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #stpyfgvtjj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #stpyfgvtjj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #stpyfgvtjj .gt_row_group_first td { border-top-width: 2px; }
 #stpyfgvtjj .gt_row_group_first th { border-top-width: 2px; }
 #stpyfgvtjj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #stpyfgvtjj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #stpyfgvtjj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #stpyfgvtjj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #stpyfgvtjj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #stpyfgvtjj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #stpyfgvtjj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #stpyfgvtjj .gt_left { text-align: left; }
 #stpyfgvtjj .gt_center { text-align: center; }
 #stpyfgvtjj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #stpyfgvtjj .gt_font_normal { font-weight: normal; }
 #stpyfgvtjj .gt_font_bold { font-weight: bold; }
 #stpyfgvtjj .gt_font_italic { font-style: italic; }
 #stpyfgvtjj .gt_super { font-size: 65%; }
 #stpyfgvtjj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #stpyfgvtjj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Animal  | Legs | Plot             |
|---------|------|------------------|
| Ostrich | 2    | \|\|             |
| Spider  | 8    | \|\|\|\|\|\|\|\| |
| Lion    | 4    | \|\|\|\|         |

</div>

## A Lightweight Approach: Svg.py

Now we can apply that same logic to making our plots. Let's start with the function that will eventually be passed into `fmt()`:

``` python
from svg import SVG, Rect, Line

height = 30
width = 50


def create_plot_svg_py(val: int) -> str:
    canvas = SVG(
        width=width,
        height=height,
        elements=[
            Rect(
                x=0,
                y=height / 4,
                width=width * (val / max_legs_value),
                height=height / 2,
                fill="blue",
            ),
            Line(x1=0, x2=0, y1=0, y2=height, stroke="black"),
        ],
    )

    html = f"<div>{canvas}</div>"
    return html
```

Here you get to call `fmt()` to modify the column you want to apply the plotting function to.

``` python
gt.fmt(fns=create_plot_svg_py, columns="Plot")
```

<div id="lqzcgvvbzu" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#lqzcgvvbzu table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lqzcgvvbzu thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lqzcgvvbzu p { margin: 0; padding: 0; }
 #lqzcgvvbzu .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lqzcgvvbzu .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lqzcgvvbzu .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lqzcgvvbzu .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lqzcgvvbzu .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lqzcgvvbzu .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lqzcgvvbzu .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lqzcgvvbzu .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lqzcgvvbzu .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lqzcgvvbzu .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lqzcgvvbzu .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lqzcgvvbzu .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lqzcgvvbzu .gt_spanner_row { border-bottom-style: hidden; }
 #lqzcgvvbzu .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lqzcgvvbzu .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lqzcgvvbzu .gt_from_md> :first-child { margin-top: 0; }
 #lqzcgvvbzu .gt_from_md> :last-child { margin-bottom: 0; }
 #lqzcgvvbzu .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lqzcgvvbzu .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lqzcgvvbzu .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lqzcgvvbzu .gt_row_group_first td { border-top-width: 2px; }
 #lqzcgvvbzu .gt_row_group_first th { border-top-width: 2px; }
 #lqzcgvvbzu .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lqzcgvvbzu .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lqzcgvvbzu .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lqzcgvvbzu .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lqzcgvvbzu .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lqzcgvvbzu .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lqzcgvvbzu .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lqzcgvvbzu .gt_left { text-align: left; }
 #lqzcgvvbzu .gt_center { text-align: center; }
 #lqzcgvvbzu .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lqzcgvvbzu .gt_font_normal { font-weight: normal; }
 #lqzcgvvbzu .gt_font_bold { font-weight: bold; }
 #lqzcgvvbzu .gt_font_italic { font-style: italic; }
 #lqzcgvvbzu .gt_super { font-size: 65%; }
 #lqzcgvvbzu .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lqzcgvvbzu .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="gt_col_headings">
<th id="Animal" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">Animal</th>
<th id="Legs" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Legs</th>
<th id="Plot" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Plot</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ostrich</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right"><div>
<svg xmlns="http://www.w3.org/2000/svg" width="50" height="30">
<rect x="0" y="7.5" width="12.5" height="15.0" fill="blue"></rect><line stroke="black" x1="0" y1="0" x2="0" y2="30"></line>
</svg>
</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Spider</td>
<td class="gt_row gt_right">8</td>
<td class="gt_row gt_right"><div>
<svg xmlns="http://www.w3.org/2000/svg" width="50" height="30">
<rect x="0" y="7.5" width="50.0" height="15.0" fill="blue"></rect><line stroke="black" x1="0" y1="0" x2="0" y2="30"></line>
</svg>
</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Lion</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right"><div>
<svg xmlns="http://www.w3.org/2000/svg" width="50" height="30">
<rect x="0" y="7.5" width="25.0" height="15.0" fill="blue"></rect><line stroke="black" x1="0" y1="0" x2="0" y2="30"></line>
</svg>
</div></td>
</tr>
</tbody>
</table>

</div>

This was very direct, we didn't have save to a buffer or import heavy duty plotting functions. We built the string with the help of `svg.py` and were able to insert into the table. See the string below:

<!-- I would really like to wrap the output here, but nothing I've tried has worked -->
<!-- https://github.com/quarto-dev/quarto-cli/discussions/6017 -->

    '<div><svg xmlns="http://www.w3.org/2000/svg" width="50" height="30"><rect x="0" y="7.5" width="25.0" height="15.0" fill="blue"/><line stroke="black" x1="0" y1="0" x2="0" y2="30"/></svg></div>'

Even in its outputted form the string is still easily readable, which is another upside of using an SVG generation package.

## Extreme Minimalism: Adding HTML directly

In the previous section, note that `svg.py` simply generated a string of HTML. You can do the same thing directly.

``` python
def create_plot_html(val: int) -> str:
    bar_element = f"""
    <div style="position: absolute;
                width: {width * val / max_legs_value}px;
                height: {height / 2}px;
                background-color: purple;
                margin-top: {height / 4}px;
    "></div>"""

    line_element = """
    <div style="position: absolute;
                top: 0;
                bottom: 0;
                width: 1px;
                background-color: black;
    "></div>"""

    html = f"""
    <div style="position: relative; width: {width}px; height: {height}px;">
        {bar_element}
        {line_element}
    </div>
    """

    return html
```

Now that we've defined our `create_plot_*` formatting function, the call to `fmt()` is identical to the one above.

``` python
gt.fmt(fns=create_plot_html, columns="Plot")
```

<div id="kauzxggwba" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#kauzxggwba table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kauzxggwba thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kauzxggwba p { margin: 0; padding: 0; }
 #kauzxggwba .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kauzxggwba .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kauzxggwba .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kauzxggwba .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kauzxggwba .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kauzxggwba .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kauzxggwba .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kauzxggwba .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kauzxggwba .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kauzxggwba .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kauzxggwba .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kauzxggwba .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kauzxggwba .gt_spanner_row { border-bottom-style: hidden; }
 #kauzxggwba .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kauzxggwba .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kauzxggwba .gt_from_md> :first-child { margin-top: 0; }
 #kauzxggwba .gt_from_md> :last-child { margin-bottom: 0; }
 #kauzxggwba .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kauzxggwba .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kauzxggwba .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kauzxggwba .gt_row_group_first td { border-top-width: 2px; }
 #kauzxggwba .gt_row_group_first th { border-top-width: 2px; }
 #kauzxggwba .gt_striped { color: #333333; background-color: #F4F4F4; }
 #kauzxggwba .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kauzxggwba .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #kauzxggwba .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #kauzxggwba .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #kauzxggwba .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kauzxggwba .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kauzxggwba .gt_left { text-align: left; }
 #kauzxggwba .gt_center { text-align: center; }
 #kauzxggwba .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kauzxggwba .gt_font_normal { font-weight: normal; }
 #kauzxggwba .gt_font_bold { font-weight: bold; }
 #kauzxggwba .gt_font_italic { font-style: italic; }
 #kauzxggwba .gt_super { font-size: 65%; }
 #kauzxggwba .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kauzxggwba .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="gt_col_headings">
<th id="Animal" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">Animal</th>
<th id="Legs" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Legs</th>
<th id="Plot" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Plot</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ostrich</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right"><div style="position: relative; width: 50px; height: 30px;">
<div style="position: absolute;
                width: 12.5px;
                height: 15.0px;
                background-color: purple;
                margin-top: 7.5px;
    ">
&#10;</div>
<div style="position: absolute;
                top: 0;
                bottom: 0;
                width: 1px;
                background-color: black;
    ">
&#10;</div>
</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Spider</td>
<td class="gt_row gt_right">8</td>
<td class="gt_row gt_right"><div style="position: relative; width: 50px; height: 30px;">
<div style="position: absolute;
                width: 50.0px;
                height: 15.0px;
                background-color: purple;
                margin-top: 7.5px;
    ">
&#10;</div>
<div style="position: absolute;
                top: 0;
                bottom: 0;
                width: 1px;
                background-color: black;
    ">
&#10;</div>
</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Lion</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right"><div style="position: relative; width: 50px; height: 30px;">
<div style="position: absolute;
                width: 25.0px;
                height: 15.0px;
                background-color: purple;
                margin-top: 7.5px;
    ">
&#10;</div>
<div style="position: absolute;
                top: 0;
                bottom: 0;
                width: 1px;
                background-color: black;
    ">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

At first glance, encoding HTML in multi-line strings may not be aesthetically pleasing, nor is it particularly more lightweight than `svg.py`. Still, it provides a good alternative if you are like me and insist on being as close to the output as possible. Separately, I have found the inclusion of text to be simpler with HTML on account of the default text handling behavior that comes along with it.

## A Comprehensive Package: Plotnine

``` python
from io import StringIO
from plotnine import (
    ggplot,
    aes,
    coord_flip,
    geom_col,
    scale_y_continuous,
    scale_x_continuous,
    theme_void,
    geom_hline,
)

max_legs_value = df["Legs"].max()


def create_plot_plotnine(val: int) -> str:
    plot = (
        ggplot()
        + aes(x=1, y=val)
        + geom_col(width=0.5, fill="green", show_legend=False)
        + scale_y_continuous(limits=(0, max_legs_value))
        + scale_x_continuous(limits=(0.5, 1.5))
        + coord_flip()
        + theme_void()
        + geom_hline(yintercept=0)
    )

    buf = StringIO()
    plot.save(buf, format="svg", width=0.5, height=0.3, verbose=False)
    svg_content = buf.getvalue()
    buf.close()

    html = f"<div>{svg_content}</div>"
    return html


# This might be familiar by now
gt.fmt(fns=create_plot_plotnine, columns="Plot")
```

<div id="hbekmneezk" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#hbekmneezk table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#hbekmneezk thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#hbekmneezk p { margin: 0; padding: 0; }
 #hbekmneezk .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #hbekmneezk .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #hbekmneezk .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #hbekmneezk .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #hbekmneezk .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hbekmneezk .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hbekmneezk .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #hbekmneezk .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #hbekmneezk .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #hbekmneezk .gt_column_spanner_outer:first-child { padding-left: 0; }
 #hbekmneezk .gt_column_spanner_outer:last-child { padding-right: 0; }
 #hbekmneezk .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #hbekmneezk .gt_spanner_row { border-bottom-style: hidden; }
 #hbekmneezk .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #hbekmneezk .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #hbekmneezk .gt_from_md> :first-child { margin-top: 0; }
 #hbekmneezk .gt_from_md> :last-child { margin-bottom: 0; }
 #hbekmneezk .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #hbekmneezk .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #hbekmneezk .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #hbekmneezk .gt_row_group_first td { border-top-width: 2px; }
 #hbekmneezk .gt_row_group_first th { border-top-width: 2px; }
 #hbekmneezk .gt_striped { color: #333333; background-color: #F4F4F4; }
 #hbekmneezk .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #hbekmneezk .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #hbekmneezk .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #hbekmneezk .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #hbekmneezk .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #hbekmneezk .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #hbekmneezk .gt_left { text-align: left; }
 #hbekmneezk .gt_center { text-align: center; }
 #hbekmneezk .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #hbekmneezk .gt_font_normal { font-weight: normal; }
 #hbekmneezk .gt_font_bold { font-weight: bold; }
 #hbekmneezk .gt_font_italic { font-style: italic; }
 #hbekmneezk .gt_super { font-size: 65%; }
 #hbekmneezk .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #hbekmneezk .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="gt_col_headings">
<th id="Animal" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">Animal</th>
<th id="Legs" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Legs</th>
<th id="Plot" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Plot</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Ostrich</td>
<td class="gt_row gt_right">2</td>
<td class="gt_row gt_right"><div>
<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="36pt" height="21.6pt" viewbox="0 0 36 21.6" xmlns="http://www.w3.org/2000/svg" version="1.1">
<metadata>
<rdf xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<work>
<type rdf:resource="http://purl.org/dc/dcmitype/StillImage"></type>
<date>2026-03-13T11:58:39.602794</date>
<format>image/svg+xml</format>
<creator>
<agent>
<title>
Matplotlib v3.10.8, https://matplotlib.org/
</title>
</agent>
</creator>
</work>
</rdf>
</metadata>
<defs>
</defs>
<g id="figure_1">
<g id="patch_1">
<path d="M 0 21.6 
L 36 21.6 
L 36 0 
L 0 0 
z
" style="fill: #ffffff"></path>
</g>
<g id="axes_1">
<g id="matplotlib.axis_1">
<g id="xtick_1"></g>
<g id="xtick_2"></g>
<g id="xtick_3"></g>
<g id="xtick_4"></g>
<g id="xtick_5"></g>
<g id="xtick_6"></g>
<g id="xtick_7"></g>
<g id="xtick_8"></g>
<g id="xtick_9"></g>
</g>
<g id="matplotlib.axis_2">
<g id="ytick_1"></g>
<g id="ytick_2"></g>
<g id="ytick_3"></g>
<g id="ytick_4"></g>
<g id="ytick_5"></g>
<g id="ytick_6"></g>
<g id="ytick_7"></g>
<g id="ytick_8"></g>
<g id="ytick_9"></g>
</g>
<g id="PolyCollection_1">
<path d="M 1.636364 15.709091 
L 1.636364 5.890909 
L 9.818182 5.890909 
L 9.818182 15.709091 
z
" clip-path="url(#pb77253c51c)" style="fill: #008000"></path>
</g>
<g id="LineCollection_1">
<path d="M 1.636364 21.6 
L 1.636364 -0 
" clip-path="url(#pb77253c51c)" style="fill: none; stroke: #000000; stroke-width: 0.886227"></path>
</g>
</g>
</g>
<defs>
<clippath id="pb77253c51c">
<rect x="0" y="0" width="36" height="21.6"></rect>
</clippath>
</defs>
</svg>
</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Spider</td>
<td class="gt_row gt_right">8</td>
<td class="gt_row gt_right"><div>
<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="36pt" height="21.6pt" viewbox="0 0 36 21.6" xmlns="http://www.w3.org/2000/svg" version="1.1">
<metadata>
<rdf xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<work>
<type rdf:resource="http://purl.org/dc/dcmitype/StillImage"></type>
<date>2026-03-13T11:58:39.641571</date>
<format>image/svg+xml</format>
<creator>
<agent>
<title>
Matplotlib v3.10.8, https://matplotlib.org/
</title>
</agent>
</creator>
</work>
</rdf>
</metadata>
<defs>
</defs>
<g id="figure_1">
<g id="patch_1">
<path d="M 0 21.6 
L 36 21.6 
L 36 0 
L 0 0 
z
" style="fill: #ffffff"></path>
</g>
<g id="axes_1">
<g id="matplotlib.axis_1">
<g id="xtick_1"></g>
<g id="xtick_2"></g>
<g id="xtick_3"></g>
<g id="xtick_4"></g>
<g id="xtick_5"></g>
<g id="xtick_6"></g>
<g id="xtick_7"></g>
<g id="xtick_8"></g>
<g id="xtick_9"></g>
</g>
<g id="matplotlib.axis_2">
<g id="ytick_1"></g>
<g id="ytick_2"></g>
<g id="ytick_3"></g>
<g id="ytick_4"></g>
<g id="ytick_5"></g>
<g id="ytick_6"></g>
<g id="ytick_7"></g>
<g id="ytick_8"></g>
<g id="ytick_9"></g>
</g>
<g id="PolyCollection_1">
<path d="M 1.636364 15.709091 
L 1.636364 5.890909 
L 34.363636 5.890909 
L 34.363636 15.709091 
z
" clip-path="url(#p7dab6c5e74)" style="fill: #008000"></path>
</g>
<g id="LineCollection_1">
<path d="M 1.636364 21.6 
L 1.636364 -0 
" clip-path="url(#p7dab6c5e74)" style="fill: none; stroke: #000000; stroke-width: 0.886227"></path>
</g>
</g>
</g>
<defs>
<clippath id="p7dab6c5e74">
<rect x="0" y="0" width="36" height="21.6"></rect>
</clippath>
</defs>
</svg>
</div></td>
</tr>
<tr>
<td class="gt_row gt_left">Lion</td>
<td class="gt_row gt_right">4</td>
<td class="gt_row gt_right"><div>
<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="36pt" height="21.6pt" viewbox="0 0 36 21.6" xmlns="http://www.w3.org/2000/svg" version="1.1">
<metadata>
<rdf xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<work>
<type rdf:resource="http://purl.org/dc/dcmitype/StillImage"></type>
<date>2026-03-13T11:58:39.678418</date>
<format>image/svg+xml</format>
<creator>
<agent>
<title>
Matplotlib v3.10.8, https://matplotlib.org/
</title>
</agent>
</creator>
</work>
</rdf>
</metadata>
<defs>
</defs>
<g id="figure_1">
<g id="patch_1">
<path d="M 0 21.6 
L 36 21.6 
L 36 0 
L 0 0 
z
" style="fill: #ffffff"></path>
</g>
<g id="axes_1">
<g id="matplotlib.axis_1">
<g id="xtick_1"></g>
<g id="xtick_2"></g>
<g id="xtick_3"></g>
<g id="xtick_4"></g>
<g id="xtick_5"></g>
<g id="xtick_6"></g>
<g id="xtick_7"></g>
<g id="xtick_8"></g>
<g id="xtick_9"></g>
</g>
<g id="matplotlib.axis_2">
<g id="ytick_1"></g>
<g id="ytick_2"></g>
<g id="ytick_3"></g>
<g id="ytick_4"></g>
<g id="ytick_5"></g>
<g id="ytick_6"></g>
<g id="ytick_7"></g>
<g id="ytick_8"></g>
<g id="ytick_9"></g>
</g>
<g id="PolyCollection_1">
<path d="M 1.636364 15.709091 
L 1.636364 5.890909 
L 18 5.890909 
L 18 15.709091 
z
" clip-path="url(#p83128198cc)" style="fill: #008000"></path>
</g>
<g id="LineCollection_1">
<path d="M 1.636364 21.6 
L 1.636364 -0 
" clip-path="url(#p83128198cc)" style="fill: none; stroke: #000000; stroke-width: 0.886227"></path>
</g>
</g>
</g>
<defs>
<clippath id="p83128198cc">
<rect x="0" y="0" width="36" height="21.6"></rect>
</clippath>
</defs>
</svg>
</div></td>
</tr>
</tbody>
</table>

</div>

Nice! But that was a sizable chunk of code just to create plots comprised of one bar each. If you're like me, you'll find it's not at all trivial to do, especially without experience using the plotting package.

However, this isn't the only graphic you might want to have on display -- when you come across a use case that necessitates more detailed plots, a comprehensive plotting package like `plotnine` could very well be your best bet. Imagine we are passing in a list of tuples and want to generate a scatterplot, writing all of those as `svg.py` elements or direct HTML would be quite cumbersome.

## Conclusion

How you choose to add plots to Great Tables is up to you. In writing graphical plotting functions for [**gt-extras**](https://posit-dev.github.io/gt-extras/articles/intro.html), I've personally turned towards an HTML-only approach that I've felt comfortable with in other settings. With that said, I do believe converting table values to graphic output is a task best done with a little bit of help (whether it be `svg-py` or another plotting package will depend on how detailed your plots are).

The choice ultimately depends on your specific needs: simplicity and directness, versus abstraction and power. By understanding the trade-offs, you will be able to tailor your approach to the needs of your project.
