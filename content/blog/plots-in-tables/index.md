---
title: Adding Plots to Great Tables
people:
  - Jules Walzer-Goldfeld
  - Michael Chow
date: '2025-07-03'
description: >-
  Exploring three approaches to add small plots to Great Tables using plotnine,
  svg.py, or HTML.
ported_from: great_tables
port_status: raw
categories:
  - great tables
featured: true
image: greattables-og.png
image-alt: "Great Tables hex logo"
---


<script src="https://cdn.jsdelivr.net/npm/requirejs@2.3.6/require.min.js" integrity="sha384-c9c+LnTbwQ3aujuU7ULEPVvgLs+Fn6fJUvIGTsuu1ZcCf11fiEubah0ttpca4ntM sha384-6V1/AdqZRWk1KAlWbKBlGhN7VG4iE/yAZcO6NZPMF8od0vukrvr0tg4qY6NSrItx" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js" integrity="sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/6Z/hRTt8+pR6L4N2" crossorigin="anonymous" data-relocate-top="true"></script>
<script type="application/javascript">define('jquery', [],function() {return window.jQuery;})</script>


While working on [**gt-extras**](https://posit-dev.github.io/gt-extras/articles/intro.html), I've been exploring how to add small plots to Great Tables. These can go by many names, like spark lines, nanoplots, and so on. In this post, I'll look at three approaches I tried: adding plots with [`plotnine`](https://plotnine.org/), [`svg.py`](https://github.com/orsinium-labs/svg.py), or adding HTML directly. In the first two cases, the plots are SVGs, while the latter entails a collection of composed HTML div elements.

Here are the pieces I'll cover:

-   **svg.py**: creating your own tiny chart directly for a row.
-   **direct HTML**: adding HTML divs directly.
-   **plotnine**: adding a full, stripped-down chart to a row.

In the end, it's often simplest to use `svg.py`, since you can create basic charts with minimal overhead. Building elements with HTML has even *less* overhead, but it is also slightly less user-friendly. At the other end of the spectrum, as your charts become more complex, using existing packages like the more exhaustive `plotnine` is a good alternative.

<div id="oymgiosqhh" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#oymgiosqhh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#oymgiosqhh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#oymgiosqhh p { margin: 0; padding: 0; }
 #oymgiosqhh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #oymgiosqhh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #oymgiosqhh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #oymgiosqhh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #oymgiosqhh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oymgiosqhh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oymgiosqhh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #oymgiosqhh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #oymgiosqhh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #oymgiosqhh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #oymgiosqhh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #oymgiosqhh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #oymgiosqhh .gt_spanner_row { border-bottom-style: hidden; }
 #oymgiosqhh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #oymgiosqhh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #oymgiosqhh .gt_from_md> :first-child { margin-top: 0; }
 #oymgiosqhh .gt_from_md> :last-child { margin-bottom: 0; }
 #oymgiosqhh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #oymgiosqhh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #oymgiosqhh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #oymgiosqhh .gt_row_group_first td { border-top-width: 2px; }
 #oymgiosqhh .gt_row_group_first th { border-top-width: 2px; }
 #oymgiosqhh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #oymgiosqhh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #oymgiosqhh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #oymgiosqhh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #oymgiosqhh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #oymgiosqhh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #oymgiosqhh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #oymgiosqhh .gt_left { text-align: left; }
 #oymgiosqhh .gt_center { text-align: center; }
 #oymgiosqhh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #oymgiosqhh .gt_font_normal { font-weight: normal; }
 #oymgiosqhh .gt_font_bold { font-weight: bold; }
 #oymgiosqhh .gt_font_italic { font-style: italic; }
 #oymgiosqhh .gt_super { font-size: 65%; }
 #oymgiosqhh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #oymgiosqhh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<div id="xkjpmuhxtd" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#xkjpmuhxtd table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xkjpmuhxtd thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xkjpmuhxtd p { margin: 0; padding: 0; }
 #xkjpmuhxtd .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xkjpmuhxtd .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xkjpmuhxtd .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xkjpmuhxtd .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xkjpmuhxtd .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xkjpmuhxtd .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xkjpmuhxtd .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xkjpmuhxtd .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xkjpmuhxtd .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xkjpmuhxtd .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xkjpmuhxtd .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xkjpmuhxtd .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xkjpmuhxtd .gt_spanner_row { border-bottom-style: hidden; }
 #xkjpmuhxtd .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xkjpmuhxtd .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xkjpmuhxtd .gt_from_md> :first-child { margin-top: 0; }
 #xkjpmuhxtd .gt_from_md> :last-child { margin-bottom: 0; }
 #xkjpmuhxtd .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xkjpmuhxtd .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xkjpmuhxtd .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xkjpmuhxtd .gt_row_group_first td { border-top-width: 2px; }
 #xkjpmuhxtd .gt_row_group_first th { border-top-width: 2px; }
 #xkjpmuhxtd .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xkjpmuhxtd .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xkjpmuhxtd .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xkjpmuhxtd .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xkjpmuhxtd .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xkjpmuhxtd .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xkjpmuhxtd .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xkjpmuhxtd .gt_left { text-align: left; }
 #xkjpmuhxtd .gt_center { text-align: center; }
 #xkjpmuhxtd .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xkjpmuhxtd .gt_font_normal { font-weight: normal; }
 #xkjpmuhxtd .gt_font_bold { font-weight: bold; }
 #xkjpmuhxtd .gt_font_italic { font-style: italic; }
 #xkjpmuhxtd .gt_super { font-size: 65%; }
 #xkjpmuhxtd .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xkjpmuhxtd .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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

<div id="ncjznjisly" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#ncjznjisly table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ncjznjisly thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ncjznjisly p { margin: 0; padding: 0; }
 #ncjznjisly .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ncjznjisly .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ncjznjisly .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ncjznjisly .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ncjznjisly .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ncjznjisly .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ncjznjisly .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ncjznjisly .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ncjznjisly .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ncjznjisly .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ncjznjisly .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ncjznjisly .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ncjznjisly .gt_spanner_row { border-bottom-style: hidden; }
 #ncjznjisly .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ncjznjisly .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ncjznjisly .gt_from_md> :first-child { margin-top: 0; }
 #ncjznjisly .gt_from_md> :last-child { margin-bottom: 0; }
 #ncjznjisly .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ncjznjisly .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ncjznjisly .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ncjznjisly .gt_row_group_first td { border-top-width: 2px; }
 #ncjznjisly .gt_row_group_first th { border-top-width: 2px; }
 #ncjznjisly .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ncjznjisly .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ncjznjisly .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ncjznjisly .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ncjznjisly .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ncjznjisly .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ncjznjisly .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ncjznjisly .gt_left { text-align: left; }
 #ncjznjisly .gt_center { text-align: center; }
 #ncjznjisly .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ncjznjisly .gt_font_normal { font-weight: normal; }
 #ncjznjisly .gt_font_bold { font-weight: bold; }
 #ncjznjisly .gt_font_italic { font-style: italic; }
 #ncjznjisly .gt_super { font-size: 65%; }
 #ncjznjisly .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ncjznjisly .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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

<div id="mpijxxwpzq" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#mpijxxwpzq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mpijxxwpzq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mpijxxwpzq p { margin: 0; padding: 0; }
 #mpijxxwpzq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mpijxxwpzq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mpijxxwpzq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mpijxxwpzq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mpijxxwpzq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mpijxxwpzq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mpijxxwpzq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mpijxxwpzq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mpijxxwpzq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mpijxxwpzq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mpijxxwpzq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mpijxxwpzq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mpijxxwpzq .gt_spanner_row { border-bottom-style: hidden; }
 #mpijxxwpzq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mpijxxwpzq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mpijxxwpzq .gt_from_md> :first-child { margin-top: 0; }
 #mpijxxwpzq .gt_from_md> :last-child { margin-bottom: 0; }
 #mpijxxwpzq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mpijxxwpzq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mpijxxwpzq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mpijxxwpzq .gt_row_group_first td { border-top-width: 2px; }
 #mpijxxwpzq .gt_row_group_first th { border-top-width: 2px; }
 #mpijxxwpzq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mpijxxwpzq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mpijxxwpzq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mpijxxwpzq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mpijxxwpzq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mpijxxwpzq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mpijxxwpzq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mpijxxwpzq .gt_left { text-align: left; }
 #mpijxxwpzq .gt_center { text-align: center; }
 #mpijxxwpzq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mpijxxwpzq .gt_font_normal { font-weight: normal; }
 #mpijxxwpzq .gt_font_bold { font-weight: bold; }
 #mpijxxwpzq .gt_font_italic { font-style: italic; }
 #mpijxxwpzq .gt_super { font-size: 65%; }
 #mpijxxwpzq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mpijxxwpzq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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

<div id="ezfqshgtpg" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#ezfqshgtpg table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ezfqshgtpg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ezfqshgtpg p { margin: 0; padding: 0; }
 #ezfqshgtpg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ezfqshgtpg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ezfqshgtpg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ezfqshgtpg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ezfqshgtpg .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ezfqshgtpg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ezfqshgtpg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ezfqshgtpg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ezfqshgtpg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ezfqshgtpg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ezfqshgtpg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ezfqshgtpg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ezfqshgtpg .gt_spanner_row { border-bottom-style: hidden; }
 #ezfqshgtpg .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ezfqshgtpg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ezfqshgtpg .gt_from_md> :first-child { margin-top: 0; }
 #ezfqshgtpg .gt_from_md> :last-child { margin-bottom: 0; }
 #ezfqshgtpg .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ezfqshgtpg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ezfqshgtpg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ezfqshgtpg .gt_row_group_first td { border-top-width: 2px; }
 #ezfqshgtpg .gt_row_group_first th { border-top-width: 2px; }
 #ezfqshgtpg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ezfqshgtpg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ezfqshgtpg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ezfqshgtpg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ezfqshgtpg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ezfqshgtpg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ezfqshgtpg .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ezfqshgtpg .gt_left { text-align: left; }
 #ezfqshgtpg .gt_center { text-align: center; }
 #ezfqshgtpg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ezfqshgtpg .gt_font_normal { font-weight: normal; }
 #ezfqshgtpg .gt_font_bold { font-weight: bold; }
 #ezfqshgtpg .gt_font_italic { font-style: italic; }
 #ezfqshgtpg .gt_super { font-size: 65%; }
 #ezfqshgtpg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ezfqshgtpg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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

<div id="weqlbhpoet" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#weqlbhpoet table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#weqlbhpoet thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#weqlbhpoet p { margin: 0; padding: 0; }
 #weqlbhpoet .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #weqlbhpoet .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #weqlbhpoet .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #weqlbhpoet .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #weqlbhpoet .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #weqlbhpoet .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #weqlbhpoet .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #weqlbhpoet .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #weqlbhpoet .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #weqlbhpoet .gt_column_spanner_outer:first-child { padding-left: 0; }
 #weqlbhpoet .gt_column_spanner_outer:last-child { padding-right: 0; }
 #weqlbhpoet .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #weqlbhpoet .gt_spanner_row { border-bottom-style: hidden; }
 #weqlbhpoet .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #weqlbhpoet .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #weqlbhpoet .gt_from_md> :first-child { margin-top: 0; }
 #weqlbhpoet .gt_from_md> :last-child { margin-bottom: 0; }
 #weqlbhpoet .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #weqlbhpoet .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #weqlbhpoet .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #weqlbhpoet .gt_row_group_first td { border-top-width: 2px; }
 #weqlbhpoet .gt_row_group_first th { border-top-width: 2px; }
 #weqlbhpoet .gt_striped { color: #333333; background-color: #F4F4F4; }
 #weqlbhpoet .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #weqlbhpoet .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #weqlbhpoet .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #weqlbhpoet .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #weqlbhpoet .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #weqlbhpoet .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #weqlbhpoet .gt_left { text-align: left; }
 #weqlbhpoet .gt_center { text-align: center; }
 #weqlbhpoet .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #weqlbhpoet .gt_font_normal { font-weight: normal; }
 #weqlbhpoet .gt_font_bold { font-weight: bold; }
 #weqlbhpoet .gt_font_italic { font-style: italic; }
 #weqlbhpoet .gt_super { font-size: 65%; }
 #weqlbhpoet .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #weqlbhpoet .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
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
<date>2026-02-28T22:55:25.987028</date>
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
<style type="text/css">*{stroke-linejoin: round; stroke-linecap: butt}</style>
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
" clip-path="url(#p7ee0810cf9)" style="fill: #008000"></path>
</g>
<g id="LineCollection_1">
<path d="M 1.636364 21.6 
L 1.636364 -0 
" clip-path="url(#p7ee0810cf9)" style="fill: none; stroke: #000000; stroke-width: 0.886227"></path>
</g>
</g>
</g>
<defs>
<clippath id="p7ee0810cf9">
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
<date>2026-02-28T22:55:26.041241</date>
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
<style type="text/css">*{stroke-linejoin: round; stroke-linecap: butt}</style>
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
" clip-path="url(#p331ac61a76)" style="fill: #008000"></path>
</g>
<g id="LineCollection_1">
<path d="M 1.636364 21.6 
L 1.636364 -0 
" clip-path="url(#p331ac61a76)" style="fill: none; stroke: #000000; stroke-width: 0.886227"></path>
</g>
</g>
</g>
<defs>
<clippath id="p331ac61a76">
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
<date>2026-02-28T22:55:26.118158</date>
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
<style type="text/css">*{stroke-linejoin: round; stroke-linecap: butt}</style>
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
" clip-path="url(#p6e28bc1aa0)" style="fill: #008000"></path>
</g>
<g id="LineCollection_1">
<path d="M 1.636364 21.6 
L 1.636364 -0 
" clip-path="url(#p6e28bc1aa0)" style="fill: none; stroke: #000000; stroke-width: 0.886227"></path>
</g>
</g>
</g>
<defs>
<clippath id="p6e28bc1aa0">
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
