---
title: Style Table Body with `mask=` in `loc.body()`
people:
  - Jerry Wu
date: 2025-01-24T00:00:00.000Z
format:
  html:
    code-summary: Show the Code
ported_from: great-tables
port_status: in-progress
---


<script src="https://cdn.jsdelivr.net/npm/requirejs@2.3.6/require.min.js" integrity="sha384-c9c+LnTbwQ3aujuU7ULEPVvgLs+Fn6fJUvIGTsuu1ZcCf11fiEubah0ttpca4ntM sha384-6V1/AdqZRWk1KAlWbKBlGhN7VG4iE/yAZcO6NZPMF8od0vukrvr0tg4qY6NSrItx" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js" integrity="sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/6Z/hRTt8+pR6L4N2" crossorigin="anonymous" data-relocate-top="true"></script>
<script type="application/javascript">define('jquery', [],function() {return window.jQuery;})</script>


In Great Tables `0.16.0`, we introduced the `mask=` parameter in `loc.body()`, enabling users to apply conditional styling to rows on a per-column basis more efficiently when working with a Polars DataFrame. This post will demonstrate how it works and compare it with the "old-fashioned" approach:

- **Leveraging the `mask=` parameter in `loc.body()`:** Use Polars expressions for streamlined styling.
- **Utilizing the `locations=` parameter in `GT.tab_style()`:** Pass a list of `loc.body()` objects.

Let's dive in.

### Preparations

We'll use the built-in dataset `gtcars` to create a Polars DataFrame. Next, we'll select the columns `mfr`, `drivetrain`, `year`, and `hp` to create a small pivoted table named `df_mini`. Finally, we'll pass `df_mini` to the `GT` object to create a table named `gt`, using `drivetrain` as the `rowname_col=` and `mfr` as the `groupname_col=`, as shown below:

<details class="code-fold">
<summary>Code</summary>

``` python
import polars as pl
from great_tables import GT, loc, style
from great_tables.data import gtcars
from polars import selectors as cs

year_cols = ["2014", "2015", "2016", "2017"]
df_mini = (
    pl.from_pandas(gtcars)
    .filter(pl.col("mfr").is_in(["Ferrari", "Lamborghini", "BMW"]))
    .sort("drivetrain")
    .pivot(on="year", index=["mfr", "drivetrain"], values="hp", aggregate_function="mean")
    .select(["mfr", "drivetrain", *year_cols])
)

gt = GT(df_mini).tab_stub(rowname_col="drivetrain", groupname_col="mfr").opt_stylize(color="cyan")
gt
```

</details>
<div id="edkkayhgmo" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#edkkayhgmo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#edkkayhgmo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#edkkayhgmo p { margin: 0; padding: 0; }
 #edkkayhgmo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #016763; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #016763; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #edkkayhgmo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #edkkayhgmo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #edkkayhgmo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #edkkayhgmo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #edkkayhgmo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; }
 #edkkayhgmo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #edkkayhgmo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #edkkayhgmo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #edkkayhgmo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #edkkayhgmo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #edkkayhgmo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #edkkayhgmo .gt_spanner_row { border-bottom-style: hidden; }
 #edkkayhgmo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #edkkayhgmo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; vertical-align: middle; }
 #edkkayhgmo .gt_from_md> :first-child { margin-top: 0; }
 #edkkayhgmo .gt_from_md> :last-child { margin-bottom: 0; }
 #edkkayhgmo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #A5FEF2; border-left-style: none; border-left-width: 1px; border-left-color: #A5FEF2; border-right-style: none; border-right-width: 1px; border-right-color: #A5FEF2; vertical-align: middle; overflow-x: hidden; }
 #edkkayhgmo .gt_stub { color: #FFFFFF; background-color: #01837B; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #01837B; padding-left: 5px; padding-right: 5px; }
 #edkkayhgmo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #edkkayhgmo .gt_row_group_first td { border-top-width: 2px; }
 #edkkayhgmo .gt_row_group_first th { border-top-width: 2px; }
 #edkkayhgmo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #edkkayhgmo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; }
 #edkkayhgmo .gt_grand_summary_row { color: #333333; background-color: #A5FEF2; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #edkkayhgmo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #edkkayhgmo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #edkkayhgmo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #edkkayhgmo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #edkkayhgmo .gt_left { text-align: left; }
 #edkkayhgmo .gt_center { text-align: center; }
 #edkkayhgmo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #edkkayhgmo .gt_font_normal { font-weight: normal; }
 #edkkayhgmo .gt_font_bold { font-weight: bold; }
 #edkkayhgmo .gt_font_italic { font-style: italic; }
 #edkkayhgmo .gt_super { font-size: 65%; }
 #edkkayhgmo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #edkkayhgmo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="2014" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">2014</th>
<th id="2015" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">2015</th>
<th id="2016" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">2016</th>
<th id="2017" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">2017</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading" data-quarto-table-cell-role="th">Ferrari</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">652.0</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">680.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">rwd</td>
<td class="gt_row gt_right gt_striped">562.0</td>
<td class="gt_row gt_right gt_striped">678.4</td>
<td class="gt_row gt_right gt_striped">661.0</td>
<td class="gt_row gt_right gt_striped">None</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading" data-quarto-table-cell-role="th">Lamborghini</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">700.0</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">rwd</td>
<td class="gt_row gt_right gt_striped">550.0</td>
<td class="gt_row gt_right gt_striped">610.0</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">None</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading" data-quarto-table-cell-role="th">BMW</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">357.0</td>
<td class="gt_row gt_right">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">rwd</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">465.0</td>
<td class="gt_row gt_right gt_striped">None</td>
</tr>
</tbody>
</table>

</div>

The numbers in the cells represent the average horsepower for each combination of `mfr` and `drivetrain` for a specific year.

### Leveraging the `mask=` parameter in `loc.body()`

The `mask=` parameter in `loc.body()` accepts a Polars expression that evaluates to a boolean result for each cell.

Here's how we can use it to achieve the two goals:

- Highlight the cell text in red if the column datatype is numerical and the cell value exceeds 650.
- Fill the background color as lightgrey if the cell value is missing in the last two columns (`2016` and `2017`).

``` python
(
    gt.tab_style(
        style=style.text(color="red"),
        locations=loc.body(mask=cs.numeric().gt(650))
    ).tab_style(
        style=style.fill(color="lightgrey"),
        locations=loc.body(mask=pl.nth(-2, -1).is_null()),
    )
)
```

<div id="karukhsjwx" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#karukhsjwx table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#karukhsjwx thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#karukhsjwx p { margin: 0; padding: 0; }
 #karukhsjwx .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #016763; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #016763; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #karukhsjwx .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #karukhsjwx .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #karukhsjwx .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #karukhsjwx .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #karukhsjwx .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; }
 #karukhsjwx .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #karukhsjwx .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #karukhsjwx .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #karukhsjwx .gt_column_spanner_outer:first-child { padding-left: 0; }
 #karukhsjwx .gt_column_spanner_outer:last-child { padding-right: 0; }
 #karukhsjwx .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #karukhsjwx .gt_spanner_row { border-bottom-style: hidden; }
 #karukhsjwx .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #karukhsjwx .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; vertical-align: middle; }
 #karukhsjwx .gt_from_md> :first-child { margin-top: 0; }
 #karukhsjwx .gt_from_md> :last-child { margin-bottom: 0; }
 #karukhsjwx .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #A5FEF2; border-left-style: none; border-left-width: 1px; border-left-color: #A5FEF2; border-right-style: none; border-right-width: 1px; border-right-color: #A5FEF2; vertical-align: middle; overflow-x: hidden; }
 #karukhsjwx .gt_stub { color: #FFFFFF; background-color: #01837B; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #01837B; padding-left: 5px; padding-right: 5px; }
 #karukhsjwx .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #karukhsjwx .gt_row_group_first td { border-top-width: 2px; }
 #karukhsjwx .gt_row_group_first th { border-top-width: 2px; }
 #karukhsjwx .gt_striped { color: #333333; background-color: #F4F4F4; }
 #karukhsjwx .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #01837B; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #01837B; }
 #karukhsjwx .gt_grand_summary_row { color: #333333; background-color: #A5FEF2; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #karukhsjwx .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #karukhsjwx .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #karukhsjwx .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #karukhsjwx .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #karukhsjwx .gt_left { text-align: left; }
 #karukhsjwx .gt_center { text-align: center; }
 #karukhsjwx .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #karukhsjwx .gt_font_normal { font-weight: normal; }
 #karukhsjwx .gt_font_bold { font-weight: bold; }
 #karukhsjwx .gt_font_italic { font-style: italic; }
 #karukhsjwx .gt_super { font-size: 65%; }
 #karukhsjwx .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #karukhsjwx .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="2014" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">2014</th>
<th id="2015" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">2015</th>
<th id="2016" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">2016</th>
<th id="2017" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">2017</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading" data-quarto-table-cell-role="th">Ferrari</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right" style="color: red">652.0</td>
<td class="gt_row gt_right" style="background-color: lightgrey">None</td>
<td class="gt_row gt_right" style="color: red">680.0</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">rwd</td>
<td class="gt_row gt_right gt_striped">562.0</td>
<td class="gt_row gt_right gt_striped" style="color: red">678.4</td>
<td class="gt_row gt_right gt_striped" style="color: red">661.0</td>
<td class="gt_row gt_right gt_striped" style="background-color: lightgrey">None</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading" data-quarto-table-cell-role="th">Lamborghini</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right" style="color: red">700.0</td>
<td class="gt_row gt_right" style="background-color: lightgrey">None</td>
<td class="gt_row gt_right" style="background-color: lightgrey">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">rwd</td>
<td class="gt_row gt_right gt_striped">550.0</td>
<td class="gt_row gt_right gt_striped">610.0</td>
<td class="gt_row gt_right gt_striped" style="background-color: lightgrey">None</td>
<td class="gt_row gt_right gt_striped" style="background-color: lightgrey">None</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="5" class="gt_group_heading" data-quarto-table-cell-role="th">BMW</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">awd</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">None</td>
<td class="gt_row gt_right">357.0</td>
<td class="gt_row gt_right" style="background-color: lightgrey">None</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">rwd</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">None</td>
<td class="gt_row gt_right gt_striped">465.0</td>
<td class="gt_row gt_right gt_striped" style="background-color: lightgrey">None</td>
</tr>
</tbody>
</table>

</div>

In this example:

- `cs.numeric()` targets numerical columns, and `.gt(650)` checks if the cell value is greater than 650.
- `pl.nth(-2, -1)` targets the last two columns, and `.is_null()` identifies missing values.

Did you notice that we can use Polars selectors and expressions to dynamically identify columns at runtime? This is definitely a killer feature when working with pivoted operations.

The `mask=` parameter acts as a syntactic sugar, streamlining the process and removing the need to loop through columns manually.

> **Using `mask=` Independently**
>
> `mask=` should not be used in combination with the `columns` or `rows` arguments. Attempting to do so will raise a `ValueError`.

### Utilizing the `locations=` parameter in `GT.tab_style()`

A more "old-fashioned" approach involves passing a list of `loc.body()` objects to the `locations=` parameter in `GT.tab_style()`:

``` python
(
    gt.tab_style(
        style=style.text(color="red"),
        locations=[loc.body(columns=col, rows=pl.col(col).gt(650))
                   for col in year_cols],
    ).tab_style(
        style=style.fill(color="lightgrey"),
        locations=[loc.body(columns=col, rows=pl.col(col).is_null())
                   for col in year_cols[-2:]],
    )
)
```

This approach, though functional, demands additional effort:

- Explicitly preparing the column names in advance.
- Specifying the `columns=` and `rows=` arguments for each `loc.body()` in the loop.

While effective, it is less efficient and more verbose compared to the first approach.

### Wrapping up

With the introduction of the `mask=` parameter in `loc.body()`, users can now style the table body in a more vectorized-like manner, akin to using `df.apply()` in Pandas, enhancing the overall user experience.

We extend our gratitude to [@igorcalabria](https://github.com/igorcalabria) for suggesting this feature in [#389](https://github.com/posit-dev/great-tables/issues/389) and providing an insightful explanation of its utility. A special thanks to [@henryharbeck](https://github.com/henryharbeck) for providing the second approach.

We hope you enjoy this new functionality as much as we do! Have ideas to make Great Tables even better? Share them with us via [GitHub Issues](https://github.com/posit-dev/great-tables/issues). We're always amazed by the creativity of our users! See you, until the next great table.
