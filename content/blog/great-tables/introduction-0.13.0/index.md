---
title: 'Great Tables `v0.13.0`: Applying styles to all table locations'
description: "Great Tables v0.13.0 brings styling to all table locations via expanded loc.*() methods."
auto-description: true
people:
  - Rich Iannone
  - Michael Chow
date: '2024-10-10T00:00:00.000Z'
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


We did something in Great Tables (`0.13.0`) that'll make your tables that much more customizable: super *fine-grained* ways of setting styles throughout the table. Before you were largely constrained to styling through the following strategies:

1.  use a limited set of styles (e.g., background color, font weight, etc.) to different table locations like the stub, the column labels, etc., through `tab_options()`
2.  use `tab_style()` with a larger set of styling options for the table body cells (specified by `loc.body()`)

In `v0.13.0`, we can target much more than just the table body! Here is the expanded set of `loc.*()` methods along with the locations that they can target.

![](./GT-locations-map.png)

This augmentation of the `loc` module to include all locations in the table means that there won't be a spot in the table to which you can't add styling. This is terrific because it gives you free rein to fully customize the look of your table.

Let's make a table and see how this new feature could be used.

### Starting things off with a big GT table

The table we'll make uses the `nuclides` dataset (available in the `great_tables.data` module). Through use of the `tab_*()` methods, quite a few table components (hence *locations*) will be added. We have hidden the code here because it is quite lengthy but you're encouraged to check it out to glean some interesting GT tricks.

<details class="code-fold">
<summary>Show the code</summary>

``` python
from great_tables import GT, md, style, loc, google_font
from great_tables.data import nuclides
import polars as pl
import polars.selectors as cs

nuclides_mini = (
    pl.from_pandas(nuclides)
    .filter(pl.col("element") == "C")
    .with_columns(pl.col("nuclide").str.replace(r"[0-9]+$", ""))
    .with_columns(mass_number=pl.col("z") + pl.col("n"))
    .with_columns(
        isotope=pl.concat_str(pl.col("element") + "-" + pl.col("mass_number").cast(pl.String))
    )
    .select(["isotope", "atomic_mass", "half_life", "isospin", "decay_1", "decay_2", "decay_3"])
)

gt_tbl = (
    GT(nuclides_mini, rowname_col="isotope")
    .tab_header(
        title="Isotopes of Carbon",
        subtitle="There are two stable isotopes of carbon and twelve that are unstable.",
    )
    .tab_spanner(label="Decay Mode", columns=cs.starts_with("decay"))
    .tab_source_note(md("Data obtained from the *nuclides* dataset."))
    .tab_stubhead(label="Isotope")
    .fmt_scientific(columns="half_life")
    .fmt_number(
        columns="atomic_mass",
        decimals=4,
        scale_by=1 / 1e6,
    )
    .sub_missing(columns="half_life", missing_text=md("**STABLE**"))
    .sub_missing(columns=cs.starts_with("decay"))
    .cols_label(
        atomic_mass="Atomic Mass",
        half_life="Half Life, s",
        isospin="Isospin",
        decay_1="1",
        decay_2="2",
        decay_3="3",
    )
    .cols_align(align="center", columns=[cs.starts_with("decay"), "isospin"])
    .opt_align_table_header(align="left")
    .opt_table_font(font=google_font(name="IBM Plex Sans"))
    .opt_vertical_padding(scale=0.5)
    .opt_horizontal_padding(scale=2)
)

gt_tbl
```

</details>
<div id="eesrsbynwg" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#eesrsbynwg table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eesrsbynwg thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eesrsbynwg p { margin: 0; padding: 0; }
 #eesrsbynwg .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eesrsbynwg .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eesrsbynwg .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eesrsbynwg .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eesrsbynwg .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eesrsbynwg .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eesrsbynwg .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eesrsbynwg .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #eesrsbynwg .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eesrsbynwg .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eesrsbynwg .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eesrsbynwg .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eesrsbynwg .gt_spanner_row { border-bottom-style: hidden; }
 #eesrsbynwg .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eesrsbynwg .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eesrsbynwg .gt_from_md> :first-child { margin-top: 0; }
 #eesrsbynwg .gt_from_md> :last-child { margin-bottom: 0; }
 #eesrsbynwg .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eesrsbynwg .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #eesrsbynwg .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #eesrsbynwg .gt_row_group_first td { border-top-width: 2px; }
 #eesrsbynwg .gt_row_group_first th { border-top-width: 2px; }
 #eesrsbynwg .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eesrsbynwg .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eesrsbynwg .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eesrsbynwg .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eesrsbynwg .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eesrsbynwg .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eesrsbynwg .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #eesrsbynwg .gt_left { text-align: left; }
 #eesrsbynwg .gt_center { text-align: center; }
 #eesrsbynwg .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eesrsbynwg .gt_font_normal { font-weight: normal; }
 #eesrsbynwg .gt_font_bold { font-weight: bold; }
 #eesrsbynwg .gt_font_italic { font-style: italic; }
 #eesrsbynwg .gt_super { font-size: 65%; }
 #eesrsbynwg .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eesrsbynwg .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" scope="colgroup"><span class="gt_column_spanner">Decay Mode</span></th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-8</td>
<td class="gt_row gt_right">8.0376</td>
<td class="gt_row gt_right">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-9</td>
<td class="gt_row gt_right">9.0310</td>
<td class="gt_row gt_right">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-10</td>
<td class="gt_row gt_right">10.0169</td>
<td class="gt_row gt_right">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-11</td>
<td class="gt_row gt_right">11.0114</td>
<td class="gt_row gt_right">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-12</td>
<td class="gt_row gt_right">12.0000</td>
<td class="gt_row gt_right"><strong>STABLE</strong></td>
<td class="gt_row gt_center">0</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-13</td>
<td class="gt_row gt_right">13.0034</td>
<td class="gt_row gt_right"><strong>STABLE</strong></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-14</td>
<td class="gt_row gt_right">14.0032</td>
<td class="gt_row gt_right">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-15</td>
<td class="gt_row gt_right">15.0106</td>
<td class="gt_row gt_right">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-16</td>
<td class="gt_row gt_right">16.0147</td>
<td class="gt_row gt_right">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-17</td>
<td class="gt_row gt_right">17.0226</td>
<td class="gt_row gt_right">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-18</td>
<td class="gt_row gt_right">18.0268</td>
<td class="gt_row gt_right">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-19</td>
<td class="gt_row gt_right">19.0348</td>
<td class="gt_row gt_right">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-20</td>
<td class="gt_row gt_right">20.0403</td>
<td class="gt_row gt_right">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-22</td>
<td class="gt_row gt_right">22.0576</td>
<td class="gt_row gt_right">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="7" class="gt_sourcenote">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>
&#10;</table>

</div>

This table will serve as a great starting point for demonstrating all the things you can now do with `tab_style()`. And the following checklist will serve as a rough plan for how we will style the table:

- use `loc.body()` to emphasize isotope half-life values
- employ `loc.stub()` to draw attention to isotope names (and also point out the 'STABLE' rows)
- use `style.css()` for creating custom CSS styles (e.g., to indent row labels for stable isotopes)
- work with composite locations and style the whole header and footer quite simply
- set the default table body fill with `tab_options()`

Really this'll be `tab_style()` like you've never seen it before, so let's get on with it.

### Styling the body

First, we'll use `loc.body()` to emphasize half life values in two ways:

- Make the values in the `atomic_mass` and `half_life` use a monospace font.
- fill the background of isotopes with STABLE half lives to be PaleTurquoise.

``` python
gt_tbl = (
    gt_tbl
    .tab_style(
        style=style.text(font=google_font(name="IBM Plex Mono")),
        locations=loc.body(columns=["atomic_mass", "half_life"])
    )
    .tab_style(
        style=[style.text(color="Navy"), style.fill(color="PaleTurquoise")],
        locations=loc.body(columns="half_life", rows=pl.col("half_life").is_not_null())
    )
)

gt_tbl
```

<div id="ygetgyulbv" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#ygetgyulbv table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ygetgyulbv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ygetgyulbv p { margin: 0; padding: 0; }
 #ygetgyulbv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ygetgyulbv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ygetgyulbv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ygetgyulbv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ygetgyulbv .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ygetgyulbv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ygetgyulbv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ygetgyulbv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #ygetgyulbv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ygetgyulbv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ygetgyulbv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ygetgyulbv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ygetgyulbv .gt_spanner_row { border-bottom-style: hidden; }
 #ygetgyulbv .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ygetgyulbv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ygetgyulbv .gt_from_md> :first-child { margin-top: 0; }
 #ygetgyulbv .gt_from_md> :last-child { margin-bottom: 0; }
 #ygetgyulbv .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ygetgyulbv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #ygetgyulbv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #ygetgyulbv .gt_row_group_first td { border-top-width: 2px; }
 #ygetgyulbv .gt_row_group_first th { border-top-width: 2px; }
 #ygetgyulbv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ygetgyulbv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ygetgyulbv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ygetgyulbv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ygetgyulbv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ygetgyulbv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ygetgyulbv .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #ygetgyulbv .gt_left { text-align: left; }
 #ygetgyulbv .gt_center { text-align: center; }
 #ygetgyulbv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ygetgyulbv .gt_font_normal { font-weight: normal; }
 #ygetgyulbv .gt_font_bold { font-weight: bold; }
 #ygetgyulbv .gt_font_italic { font-style: italic; }
 #ygetgyulbv .gt_super { font-size: 65%; }
 #ygetgyulbv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ygetgyulbv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" scope="colgroup"><span class="gt_column_spanner">Decay Mode</span></th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-8</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-9</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-10</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-11</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-12</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono"><strong>STABLE</strong></td>
<td class="gt_row gt_center">0</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-13</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono"><strong>STABLE</strong></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-14</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-15</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-16</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-17</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-18</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-19</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-20</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">C-22</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="7" class="gt_sourcenote">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>
&#10;</table>

</div>

Note these important pieces in the code:

- setting monospace font: we used [`google_font()`](https://posit-dev.github.io/great-tables/reference/google_font.html) (added in the previous release) to apply the monospaced font IBM Plex Mono.
- filling unstable half lives to turquoise: because the half life cells with the value STABLE are actually missing in the underlying data, and filled in using `GT.sub_missing()`, we used the polars expression `pl.col("half_life").is_not_null()` to target everything that isn't STABLE.

This is mainly a reminder that Polars expressions are quite something. And targeting cells in the body with `loc.body(rows=...)` can be powerful by extension.

### Don't forget the stub!

We mustn't forget the stub. It's a totally separate location, being off to the side and having the important responsibility of holding the row labels. Here, we are going to do two things:

1.  Change the fill color (to 'Linen') and make the text bold for the *entire stub*
2.  Highlight the rows where we have stable isotopes (the extent is both for the stub and the body cells)

``` python
gt_tbl = (
    gt_tbl
    .tab_style(
        style=[style.fill(color="Linen"), style.text(weight="bold")],
        locations=loc.stub()
    )
    .tab_style(
        style=style.fill(color="LightCyan"),
        locations=[
            loc.body(rows=pl.col("half_life").is_null()),
            loc.stub(rows=pl.col("half_life").is_null())
        ]
    )
 )

gt_tbl
```

<div id="tnrmqwhifq" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#tnrmqwhifq table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#tnrmqwhifq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#tnrmqwhifq p { margin: 0; padding: 0; }
 #tnrmqwhifq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #tnrmqwhifq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #tnrmqwhifq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #tnrmqwhifq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #tnrmqwhifq .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tnrmqwhifq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tnrmqwhifq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #tnrmqwhifq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #tnrmqwhifq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #tnrmqwhifq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #tnrmqwhifq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #tnrmqwhifq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #tnrmqwhifq .gt_spanner_row { border-bottom-style: hidden; }
 #tnrmqwhifq .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #tnrmqwhifq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #tnrmqwhifq .gt_from_md> :first-child { margin-top: 0; }
 #tnrmqwhifq .gt_from_md> :last-child { margin-bottom: 0; }
 #tnrmqwhifq .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #tnrmqwhifq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #tnrmqwhifq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #tnrmqwhifq .gt_row_group_first td { border-top-width: 2px; }
 #tnrmqwhifq .gt_row_group_first th { border-top-width: 2px; }
 #tnrmqwhifq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #tnrmqwhifq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #tnrmqwhifq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #tnrmqwhifq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #tnrmqwhifq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #tnrmqwhifq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #tnrmqwhifq .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #tnrmqwhifq .gt_left { text-align: left; }
 #tnrmqwhifq .gt_center { text-align: center; }
 #tnrmqwhifq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #tnrmqwhifq .gt_font_normal { font-weight: normal; }
 #tnrmqwhifq .gt_font_bold { font-weight: bold; }
 #tnrmqwhifq .gt_font_italic { font-style: italic; }
 #tnrmqwhifq .gt_super { font-size: 65%; }
 #tnrmqwhifq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #tnrmqwhifq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" scope="colgroup"><span class="gt_column_spanner">Decay Mode</span></th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-8</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-9</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-10</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-11</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold; background-color: LightCyan">C-12</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">0</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold; background-color: LightCyan">C-13</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">1/2</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-14</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-15</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-16</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-17</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-18</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-19</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-20</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-22</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="7" class="gt_sourcenote">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>
&#10;</table>

</div>

For task #1, a simple `.tab_style(..., locations=loc.stub())` targeted the entire stub.

Task #2 is more interesting. Like `loc.body()`, `loc.stub()` has a `rows=` argument that can target specific rows with Polars expressions. We used the same Polars expression as in the previous section to target those rows that belong to the stable isotopes.

We've dressed up the stub so that it is that much more prominent. And that linen-colored stub goes so well with the light-cyan rows, representative of carbon-12 and carbon-13!

### Using custom style rules with the new `style.css()`

Aside from decking out the `loc` module with all manner of location methods, we've added a little something to the `style` module: `style.css()`! What's it for? It lets you supply style declarations to its single `rule=` argument.

As an example, I might want to indent some text in one or more table cells. You can't really do that with the `style.text()` method since it doesn't have an `indent=` argument. So, in Great Tables `0.13.0` you can manually indent the row label text for the 'STABLE' rows using a CSS style rule:

``` python
gt_tbl = (
    gt_tbl
    .tab_style(
        style=style.css(rule="text-indent: 4px;"),
        locations=loc.stub(rows=pl.col("half_life").is_null())
    )
)

gt_tbl
```

<div id="djqlttujdh" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#djqlttujdh table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#djqlttujdh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#djqlttujdh p { margin: 0; padding: 0; }
 #djqlttujdh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #djqlttujdh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #djqlttujdh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #djqlttujdh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #djqlttujdh .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #djqlttujdh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #djqlttujdh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #djqlttujdh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #djqlttujdh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #djqlttujdh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #djqlttujdh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #djqlttujdh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #djqlttujdh .gt_spanner_row { border-bottom-style: hidden; }
 #djqlttujdh .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #djqlttujdh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #djqlttujdh .gt_from_md> :first-child { margin-top: 0; }
 #djqlttujdh .gt_from_md> :last-child { margin-bottom: 0; }
 #djqlttujdh .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #djqlttujdh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #djqlttujdh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #djqlttujdh .gt_row_group_first td { border-top-width: 2px; }
 #djqlttujdh .gt_row_group_first th { border-top-width: 2px; }
 #djqlttujdh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #djqlttujdh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #djqlttujdh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #djqlttujdh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #djqlttujdh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #djqlttujdh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #djqlttujdh .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #djqlttujdh .gt_left { text-align: left; }
 #djqlttujdh .gt_center { text-align: center; }
 #djqlttujdh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #djqlttujdh .gt_font_normal { font-weight: normal; }
 #djqlttujdh .gt_font_bold { font-weight: bold; }
 #djqlttujdh .gt_font_italic { font-style: italic; }
 #djqlttujdh .gt_super { font-size: 65%; }
 #djqlttujdh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #djqlttujdh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" scope="colgroup"><span class="gt_column_spanner">Decay Mode</span></th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-8</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-9</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-10</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-11</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-12</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">0</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-13</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">1/2</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-14</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-15</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-16</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-17</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-18</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-19</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-20</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-22</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="7" class="gt_sourcenote">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>
&#10;</table>

</div>

We targeted the cells in the stub that corresponded to the stable isotopes (carbon-12 and -13) with a Polars expression (same one as in the previous code cell) and now we have a 4px indentation of the 'C-12' and 'C-13' text! This new bonus functionality really allows almost any type of styling possible, provided you have those CSS skillz.

### The *combined* location helpers: `loc.column_header()` and `loc.footer()`

Look, I know we brought up the expression *fine-grained* before---right in the first paragraph---but sometimes you need just the opposite. There are lots of little locations in a GT table and some make for logical groupings. To that end, we have the concept of *combined* location helpers.

Let's set a grey background fill on the stubhead, column header, and footer:

``` python
gt_tbl = (
    gt_tbl
    .tab_style(
        style=[style.text(v_align="middle"), style.fill(color="#EEEEEE")],
        locations=[loc.stubhead(), loc.column_header(), loc.footer()]
    )
)

gt_tbl
```

<div id="dgixsmcplv" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#dgixsmcplv table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#dgixsmcplv thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#dgixsmcplv p { margin: 0; padding: 0; }
 #dgixsmcplv .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #dgixsmcplv .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #dgixsmcplv .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #dgixsmcplv .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #dgixsmcplv .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dgixsmcplv .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dgixsmcplv .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #dgixsmcplv .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #dgixsmcplv .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #dgixsmcplv .gt_column_spanner_outer:first-child { padding-left: 0; }
 #dgixsmcplv .gt_column_spanner_outer:last-child { padding-right: 0; }
 #dgixsmcplv .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #dgixsmcplv .gt_spanner_row { border-bottom-style: hidden; }
 #dgixsmcplv .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #dgixsmcplv .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #dgixsmcplv .gt_from_md> :first-child { margin-top: 0; }
 #dgixsmcplv .gt_from_md> :last-child { margin-bottom: 0; }
 #dgixsmcplv .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #dgixsmcplv .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #dgixsmcplv .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #dgixsmcplv .gt_row_group_first td { border-top-width: 2px; }
 #dgixsmcplv .gt_row_group_first th { border-top-width: 2px; }
 #dgixsmcplv .gt_striped { color: #333333; background-color: #F4F4F4; }
 #dgixsmcplv .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #dgixsmcplv .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #dgixsmcplv .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #dgixsmcplv .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #dgixsmcplv .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #dgixsmcplv .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #dgixsmcplv .gt_left { text-align: left; }
 #dgixsmcplv .gt_center { text-align: center; }
 #dgixsmcplv .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #dgixsmcplv .gt_font_normal { font-weight: normal; }
 #dgixsmcplv .gt_font_bold { font-weight: bold; }
 #dgixsmcplv .gt_font_italic { font-style: italic; }
 #dgixsmcplv .gt_super { font-size: 65%; }
 #dgixsmcplv .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #dgixsmcplv .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="colgroup"><span class="gt_column_spanner">Decay Mode</span></th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-8</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-9</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-10</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-11</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-12</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">0</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-13</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">1/2</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-14</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-15</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-16</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-17</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-18</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-19</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-20</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-22</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="7" class="gt_sourcenote" style="vertical-align: middle; background-color: #EEEEEE">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>
&#10;</table>

</div>

The [`loc.column_header()`](https://posit-dev.github.io/great-tables/reference/loc.column_header.html) location always targets both `loc.column_labels()` and `loc.spanner_labels()`.

A good strategy for your tables would be to style with combined location helpers first and then drill into the specific cells of those super locations with more fine-grained styles in a later `tab_style()` call.

### Styling the title and the subtitle

Although it really doesn't appear to have separate locations, the table header (produced by way of `tab_header()`) can have two of them: the title and the subtitle (the latter is optional). These can be targeted via `loc.title()` and `loc.subtitle()`. Let's focus in on the title location and set an aliceblue background fill on the title, along with some font and border adjustments.

``` python
gt_tbl = (
    gt_tbl
    .tab_style(
        style=[
            style.text(size="24px"),
            style.fill(color="aliceblue"),
            style.borders(sides="bottom", color="#BFDFF6", weight="2px")
        ],
        locations=loc.title()
    )
)

gt_tbl
```

<div id="epdokuzzpb" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#epdokuzzpb table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#epdokuzzpb thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#epdokuzzpb p { margin: 0; padding: 0; }
 #epdokuzzpb .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #epdokuzzpb .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #epdokuzzpb .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #epdokuzzpb .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #epdokuzzpb .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #epdokuzzpb .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #epdokuzzpb .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #epdokuzzpb .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #epdokuzzpb .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #epdokuzzpb .gt_column_spanner_outer:first-child { padding-left: 0; }
 #epdokuzzpb .gt_column_spanner_outer:last-child { padding-right: 0; }
 #epdokuzzpb .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #epdokuzzpb .gt_spanner_row { border-bottom-style: hidden; }
 #epdokuzzpb .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #epdokuzzpb .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #epdokuzzpb .gt_from_md> :first-child { margin-top: 0; }
 #epdokuzzpb .gt_from_md> :last-child { margin-bottom: 0; }
 #epdokuzzpb .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #epdokuzzpb .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #epdokuzzpb .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #epdokuzzpb .gt_row_group_first td { border-top-width: 2px; }
 #epdokuzzpb .gt_row_group_first th { border-top-width: 2px; }
 #epdokuzzpb .gt_striped { color: #333333; background-color: #F4F4F4; }
 #epdokuzzpb .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #epdokuzzpb .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #epdokuzzpb .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #epdokuzzpb .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #epdokuzzpb .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #epdokuzzpb .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #epdokuzzpb .gt_left { text-align: left; }
 #epdokuzzpb .gt_center { text-align: center; }
 #epdokuzzpb .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #epdokuzzpb .gt_font_normal { font-weight: normal; }
 #epdokuzzpb .gt_font_bold { font-weight: bold; }
 #epdokuzzpb .gt_font_italic { font-style: italic; }
 #epdokuzzpb .gt_super { font-size: 65%; }
 #epdokuzzpb .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #epdokuzzpb .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal" style="font-size: 24px; background-color: aliceblue; border-bottom: 2px solid #BFDFF6">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="colgroup"><span class="gt_column_spanner">Decay Mode</span></th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-8</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-9</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-10</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-11</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-12</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">0</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-13</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">1/2</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-14</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-15</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-16</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-17</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-18</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-19</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-20</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-22</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="7" class="gt_sourcenote" style="vertical-align: middle; background-color: #EEEEEE">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>
&#10;</table>

</div>

Looks good. Notice that the title location is separate from the subtitle one, the background fill reveals the extent of its area.

A subtitle is an optional part of the header. We do have one in our table example, so let's style that as well. The `style.css()` method will be used to give the subtitle text some additional top and bottom padding, and, we'll put in a fancy background involving a linear gradient.

``` python
gt_tbl = (
    gt_tbl
    .tab_style(
        style=style.css(rule="padding-top: 5px;"
            "padding-bottom: 5px;"
            "background-image: linear-gradient(120deg, #d4fc79 0%, #96f6a1 100%);"
        ),
        locations=loc.subtitle()
    )
)

gt_tbl
```

<div id="qdreuqjuhy" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#qdreuqjuhy table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qdreuqjuhy thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qdreuqjuhy p { margin: 0; padding: 0; }
 #qdreuqjuhy .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qdreuqjuhy .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qdreuqjuhy .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qdreuqjuhy .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qdreuqjuhy .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qdreuqjuhy .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qdreuqjuhy .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qdreuqjuhy .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #qdreuqjuhy .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qdreuqjuhy .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qdreuqjuhy .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qdreuqjuhy .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qdreuqjuhy .gt_spanner_row { border-bottom-style: hidden; }
 #qdreuqjuhy .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qdreuqjuhy .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qdreuqjuhy .gt_from_md> :first-child { margin-top: 0; }
 #qdreuqjuhy .gt_from_md> :last-child { margin-bottom: 0; }
 #qdreuqjuhy .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qdreuqjuhy .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #qdreuqjuhy .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #qdreuqjuhy .gt_row_group_first td { border-top-width: 2px; }
 #qdreuqjuhy .gt_row_group_first th { border-top-width: 2px; }
 #qdreuqjuhy .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qdreuqjuhy .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qdreuqjuhy .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qdreuqjuhy .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qdreuqjuhy .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qdreuqjuhy .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qdreuqjuhy .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #qdreuqjuhy .gt_left { text-align: left; }
 #qdreuqjuhy .gt_center { text-align: center; }
 #qdreuqjuhy .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qdreuqjuhy .gt_font_normal { font-weight: normal; }
 #qdreuqjuhy .gt_font_bold { font-weight: bold; }
 #qdreuqjuhy .gt_font_italic { font-style: italic; }
 #qdreuqjuhy .gt_super { font-size: 65%; }
 #qdreuqjuhy .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qdreuqjuhy .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal" style="font-size: 24px; background-color: aliceblue; border-bottom: 2px solid #BFDFF6">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="padding-top: 5px; padding-bottom: 5px; background-image: linear-gradient(120deg, #d4fc79 0%, #96f6a1 100%)">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="colgroup"><span class="gt_column_spanner">Decay Mode</span></th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-8</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-9</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-10</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-11</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-12</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">0</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-13</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">1/2</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-14</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-15</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-16</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-17</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-18</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-19</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-20</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-22</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="7" class="gt_sourcenote" style="vertical-align: middle; background-color: #EEEEEE">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>
&#10;</table>

</div>

None of what was done above could be done prior to `v0.13.0`. The `style.css()` method makes this all possible.

The combined location helper for the title and the subtitle locations is `loc.header()`. As mentioned before, it can be used as a shorthand for `locations=[loc.title(), loc_subtitle()]` and it's useful here where we want to change the font for the title and subtitle text.

``` python
gt_tbl = (
    gt_tbl
    .tab_style(
        style=style.text(font=google_font("IBM Plex Serif")),
        locations=loc.header()
    )
)

gt_tbl
```

<div id="ukzjaozmxn" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Serif&display=swap');
#ukzjaozmxn table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ukzjaozmxn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ukzjaozmxn p { margin: 0; padding: 0; }
 #ukzjaozmxn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ukzjaozmxn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ukzjaozmxn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ukzjaozmxn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ukzjaozmxn .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ukzjaozmxn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ukzjaozmxn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ukzjaozmxn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #ukzjaozmxn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ukzjaozmxn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ukzjaozmxn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ukzjaozmxn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ukzjaozmxn .gt_spanner_row { border-bottom-style: hidden; }
 #ukzjaozmxn .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ukzjaozmxn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ukzjaozmxn .gt_from_md> :first-child { margin-top: 0; }
 #ukzjaozmxn .gt_from_md> :last-child { margin-bottom: 0; }
 #ukzjaozmxn .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ukzjaozmxn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #ukzjaozmxn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #ukzjaozmxn .gt_row_group_first td { border-top-width: 2px; }
 #ukzjaozmxn .gt_row_group_first th { border-top-width: 2px; }
 #ukzjaozmxn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ukzjaozmxn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ukzjaozmxn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ukzjaozmxn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ukzjaozmxn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ukzjaozmxn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ukzjaozmxn .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #ukzjaozmxn .gt_left { text-align: left; }
 #ukzjaozmxn .gt_center { text-align: center; }
 #ukzjaozmxn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ukzjaozmxn .gt_font_normal { font-weight: normal; }
 #ukzjaozmxn .gt_font_bold { font-weight: bold; }
 #ukzjaozmxn .gt_font_italic { font-style: italic; }
 #ukzjaozmxn .gt_super { font-size: 65%; }
 #ukzjaozmxn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ukzjaozmxn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal" style="font-family: IBM Plex Serif; font-size: 24px; background-color: aliceblue; border-bottom: 2px solid #BFDFF6">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="font-family: IBM Plex Serif; padding-top: 5px; padding-bottom: 5px; background-image: linear-gradient(120deg, #d4fc79 0%, #96f6a1 100%)">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="colgroup"><span class="gt_column_spanner">Decay Mode</span></th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-8</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-9</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-10</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-11</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-12</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">0</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-13</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">1/2</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-14</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-15</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-16</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-17</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-18</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-19</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-20</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-22</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="7" class="gt_sourcenote" style="vertical-align: middle; background-color: #EEEEEE">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>
&#10;</table>

</div>

Though the order of things matters when setting styles via `tab_style()`, it's not a problem here to set a style for the combined 'header' location after doing so for the 'title' and 'subtitle' locations because the 'font' attribute *wasn't* set by `tab_style()` for those smaller locations.

### How `tab_style()` fits in with `tab_options()`

When it comes to styling, you can use `tab_options()` for some of the basics and use `tab_style()` for the more demanding styling tasks. And you could combine the usage of both in your table. Let's set a default honeydew background fill on the body values:

``` python
gt_tbl = gt_tbl.tab_options(table_background_color="HoneyDew")

gt_tbl
```

<div id="vidwnzshpq" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Serif&display=swap');
#vidwnzshpq table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vidwnzshpq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vidwnzshpq p { margin: 0; padding: 0; }
 #vidwnzshpq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: HoneyDew; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vidwnzshpq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vidwnzshpq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; border-bottom-color: HoneyDew; border-bottom-width: 0; }
 #vidwnzshpq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; border-top-color: HoneyDew; border-top-width: 0; }
 #vidwnzshpq .gt_heading { background-color: HoneyDew; text-align: left; border-bottom-color: HoneyDew; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vidwnzshpq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vidwnzshpq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vidwnzshpq .gt_col_heading { color: #333333; background-color: HoneyDew; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #vidwnzshpq .gt_column_spanner_outer { color: #333333; background-color: HoneyDew; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vidwnzshpq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vidwnzshpq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vidwnzshpq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vidwnzshpq .gt_spanner_row { border-bottom-style: hidden; }
 #vidwnzshpq .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: HoneyDew; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vidwnzshpq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: HoneyDew; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vidwnzshpq .gt_from_md> :first-child { margin-top: 0; }
 #vidwnzshpq .gt_from_md> :last-child { margin-bottom: 0; }
 #vidwnzshpq .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vidwnzshpq .gt_stub { color: #333333; background-color: HoneyDew; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #vidwnzshpq .gt_stub_row_group { color: #333333; background-color: HoneyDew; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #vidwnzshpq .gt_row_group_first td { border-top-width: 2px; }
 #vidwnzshpq .gt_row_group_first th { border-top-width: 2px; }
 #vidwnzshpq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vidwnzshpq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vidwnzshpq .gt_grand_summary_row { color: #333333; background-color: HoneyDew; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vidwnzshpq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vidwnzshpq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vidwnzshpq .gt_sourcenotes { color: #333333; background-color: HoneyDew; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vidwnzshpq .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #vidwnzshpq .gt_left { text-align: left; }
 #vidwnzshpq .gt_center { text-align: center; }
 #vidwnzshpq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vidwnzshpq .gt_font_normal { font-weight: normal; }
 #vidwnzshpq .gt_font_bold { font-weight: bold; }
 #vidwnzshpq .gt_font_italic { font-style: italic; }
 #vidwnzshpq .gt_super { font-size: 65%; }
 #vidwnzshpq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vidwnzshpq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_title gt_font_normal" style="font-family: IBM Plex Serif; font-size: 24px; background-color: aliceblue; border-bottom: 2px solid #BFDFF6">Isotopes of Carbon</th>
</tr>
<tr class="gt_heading">
<th colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="font-family: IBM Plex Serif; padding-top: 5px; padding-bottom: 5px; background-image: linear-gradient(120deg, #d4fc79 0%, #96f6a1 100%)">There are two stable isotopes of carbon and twelve that are unstable.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Isotope" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isotope</th>
<th rowspan="2" id="atomic_mass" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Atomic Mass</th>
<th rowspan="2" id="half_life" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Half Life, s</th>
<th rowspan="2" id="isospin" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">Isospin</th>
<th colspan="3" id="Decay-Mode" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="colgroup"><span class="gt_column_spanner">Decay Mode</span></th>
</tr>
<tr class="gt_col_headings">
<th id="decay_1" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">1</th>
<th id="decay_2" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">2</th>
<th id="decay_3" class="gt_col_heading gt_columns_bottom_border gt_center" data-quarto-table-cell-role="th" style="vertical-align: middle; background-color: #EEEEEE" scope="col">3</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-8</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">8.0376</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">3.51 × 10<sup>−21</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">2P</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-9</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">9.0310</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.26 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">B+P</td>
<td class="gt_row gt_center">B+A</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-10</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">10.0169</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>1</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-11</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">11.0114</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.22 × 10<sup>3</sup></td>
<td class="gt_row gt_center">1/2</td>
<td class="gt_row gt_center">EC+B+</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-12</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">12.0000</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">0</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold; background-color: LightCyan; text-indent: 4px">C-13</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan">13.0034</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; background-color: LightCyan"><strong>STABLE</strong></td>
<td class="gt_row gt_center" style="background-color: LightCyan">1/2</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
<td class="gt_row gt_center" style="background-color: LightCyan">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-14</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">14.0032</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.80 × 10<sup>11</sup></td>
<td class="gt_row gt_center">1</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-15</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">15.0106</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">2.45</td>
<td class="gt_row gt_center">3/2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">—</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-16</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">16.0147</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">7.47 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">2</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-17</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.0226</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.93 × 10<sup>−1</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-18</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">18.0268</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">9.20 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">3</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">—</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-19</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">19.0348</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">4.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-20</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">20.0403</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">1.63 × 10<sup>−2</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="background-color: Linen; font-weight: bold">C-22</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">22.0576</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono; color: Navy; background-color: PaleTurquoise">6.10 × 10<sup>−3</sup></td>
<td class="gt_row gt_center">None</td>
<td class="gt_row gt_center">B-</td>
<td class="gt_row gt_center">B-N</td>
<td class="gt_row gt_center">B-2N</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="7" class="gt_sourcenote" style="vertical-align: middle; background-color: #EEEEEE">Data obtained from the <em>nuclides</em> dataset.</td>
</tr>
</tfoot>
&#10;</table>

</div>

In the example, we asked for the HoneyDew background fill on the entire table with `tab_options()`. However, even though `tab_options()` was used after those `tab_style()` invocations, the 'HoneyDew' background color was only applied to the locations that didn't have a background color set through `tab_style(). The important takeaway here is that the precedence (or priority) is *always* given to`tab_style()\`, regardless of the order of invocation.

### Wrapping up

We'd like to thank [Tim Paine](https://github.com/timkpaine) for getting the expanded `loc` work off the ground. Additionally, we are grateful to [Jerry Wu](https://github.com/jrycw) for his contributions to the `v0.13.0` release of the package.

We'd be very pleased to receive comments or suggestions on the new functionality. [GitHub Issues](https://github.com/posit-dev/great-tables/issues) or [GitHub Discussions](https://github.com/posit-dev/great-tables/discussions) are both fine venues for getting in touch with us. Finally, if ever you want to talk about tables with us, you're always welcome to jump into our [Discord Server](https://discord.com/invite/Ux7nrcXHVV).
