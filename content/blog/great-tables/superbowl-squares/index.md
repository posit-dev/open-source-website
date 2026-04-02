---
title: Using Polars to Win at Super Bowl Squares
people:
  - Michael Chow
date: '2024-02-08'
ported_from: great_tables
port_status: in-progress
software:
  - great-tables
languages:
  - Python
categories:
  - Visualization
tags:
  - Great Tables
---


<script src="https://cdn.jsdelivr.net/npm/requirejs@2.3.6/require.min.js" integrity="sha384-c9c+LnTbwQ3aujuU7ULEPVvgLs+Fn6fJUvIGTsuu1ZcCf11fiEubah0ttpca4ntM sha384-6V1/AdqZRWk1KAlWbKBlGhN7VG4iE/yAZcO6NZPMF8od0vukrvr0tg4qY6NSrItx" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js" integrity="sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/6Z/hRTt8+pR6L4N2" crossorigin="anonymous" data-relocate-top="true"></script>
<script type="application/javascript">define('jquery', [],function() {return window.jQuery;})</script>


The Super Bowl is upon us, and with it the glittering squares of chance.
Maybe you've seen Super Bowl Squares at your work.
Maybe you've played it with your pals.
Or maybe you have no idea what it is.

Whether you're a Squares-head or not, this post will help you win with data.

## What is Super Bowl Squares?

Super Bowl Squares is a betting game, where you bet on the final digits of each team in a game.

For example, here are some scores with the final digit bolded:

- Home team score: 1**4**
- Away team score: **7**

So the final digits would be:

- Home team digit: 4
- Away team digit: 7

Let's say you choose the digits above, and write this as 4/7---meaning a final digit of 4 for home and 7 for away.
You would mark yourself on this square:

<details class="code-fold">
<summary>Code</summary>

``` python
df = (
    pl.DataFrame({"x": list(range(10))})
    .join(pl.DataFrame({"y": list(range(10)), "z": "_._"}), how="cross")
    .with_columns(
        z=pl.when((pl.col("x") == 7) & (pl.col("y") == 4)).then(pl.lit("4/7")).otherwise("z")
    )
    .pivot(index="x", values="z", on="y")
    .with_row_index()
)

(
    GT(df, rowname_col="x")
    .tab_header("Example Superbowl Square")
    .tab_spanner("Home", cs.all())
    .tab_style(style.fill("green"), loc.body(columns="4", rows=pl.col("index") == 7))
    .tab_style(style.text(color="#FFFFFF", weight="bold"), loc.body())
    .cols_hide("index")
    .tab_stubhead("Away")
)
```

</details>
<div id="qrworpzoyo" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#qrworpzoyo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qrworpzoyo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qrworpzoyo p { margin: 0; padding: 0; }
 #qrworpzoyo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qrworpzoyo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qrworpzoyo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qrworpzoyo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qrworpzoyo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qrworpzoyo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qrworpzoyo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qrworpzoyo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qrworpzoyo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qrworpzoyo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qrworpzoyo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qrworpzoyo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qrworpzoyo .gt_spanner_row { border-bottom-style: hidden; }
 #qrworpzoyo .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qrworpzoyo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qrworpzoyo .gt_from_md> :first-child { margin-top: 0; }
 #qrworpzoyo .gt_from_md> :last-child { margin-bottom: 0; }
 #qrworpzoyo .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qrworpzoyo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qrworpzoyo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qrworpzoyo .gt_row_group_first td { border-top-width: 2px; }
 #qrworpzoyo .gt_row_group_first th { border-top-width: 2px; }
 #qrworpzoyo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qrworpzoyo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qrworpzoyo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qrworpzoyo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qrworpzoyo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qrworpzoyo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qrworpzoyo .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qrworpzoyo .gt_left { text-align: left; }
 #qrworpzoyo .gt_center { text-align: center; }
 #qrworpzoyo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qrworpzoyo .gt_font_normal { font-weight: normal; }
 #qrworpzoyo .gt_font_bold { font-weight: bold; }
 #qrworpzoyo .gt_font_italic { font-style: italic; }
 #qrworpzoyo .gt_super { font-size: 65%; }
 #qrworpzoyo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qrworpzoyo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="11" class="gt_heading gt_title gt_font_normal">Example Superbowl Square</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="Away" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">Away</th>
<th colspan="10" id="Home" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" scope="colgroup"><span class="gt_column_spanner">Home</span></th>
</tr>
<tr class="gt_col_headings">
<th id="0" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">0</th>
<th id="1" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">1</th>
<th id="2" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">2</th>
<th id="3" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">3</th>
<th id="4" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">4</th>
<th id="5" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">5</th>
<th id="6" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">6</th>
<th id="7" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">7</th>
<th id="8" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">8</th>
<th id="9" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">9</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">0</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">1</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">2</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">3</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">4</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">5</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">6</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">7</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="background-color: green; color: #FFFFFF; font-weight: bold">4/7</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">8</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">9</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
<td class="gt_row gt_left" style="color: #FFFFFF; font-weight: bold">_._</td>
</tr>
</tbody>
</table>

</div>

If the final score ends up being Home 4, Away 7---ding ding ding, big winner---you win the pool,
and hopefully take home some combination of money and glory. For more details on playing, see [this WikiHow article](https://www.wikihow.com/Play-Football-Squares).

## Why analyze squares?

Not all options in a Super Bowl Squares are created equal.
This is because there are specific point values you can add to your score.
For example, touchdowns often to result in 7 points, and its common to score 3 points via a field goal.
This means that ending up with a final digit of 5 is uncommon.

Analyzing the chance of each square winning let's you pick the best ones.
(In some versions of Super Bowl Squares, the squares get randomly assigned to people.
In that case, knowing the chance of winning tells you whether you got a bum deal or not ;).

## What squares are most likely to win?

We looked back at games for the KC Chiefs (away), and games for the San Francisco 49ers (home), and calculated the proportion of the time each team ended with a specific digit. Putting this together for the two teams, here is the chance of winning on a given square:

<details class="code-fold">
<summary>Code</summary>

``` python
import polars as pl
import polars.selectors as cs
from great_tables import GT, md


# Utilities -----


def calc_n(df: pl.DataFrame, colname: str):
    """Count the number of final digits observed across games."""

    return df.select(final_digit=pl.col(colname).mod(10)).group_by("final_digit").agg(n=pl.len())


def team_final_digits(game: pl.DataFrame, team_code: str) -> pl.DataFrame:
    """Calculate a team's proportion of digits across games (both home and away)."""

    home_n = calc_n(game.filter(pl.col("home_team") == team_code), "home_score")
    away_n = calc_n(game.filter(pl.col("away_team") == team_code), "away_score")

    joined = (
        home_n.join(away_n, "final_digit")
        .select("final_digit", n=pl.col("n") + pl.col("n_right"))
        .with_columns(prop=pl.col("n") / pl.col("n").sum())
    )

    return joined


# Analysis -----

games = pl.read_csv("./games.csv").filter(
    pl.col("game_id") != "2023_22_SF_KC",
    pl.col("season") >= 2015,
)

# Individual probabilities of final digits per team
home = team_final_digits(games, "KC")
away = team_final_digits(games, "SF")

# Cross and multiply p(digit | team=KC)p(digit | team=SF) to get
# the joint probability p(digit_KC, digit_SF | KC, SF)
joint = (
    home.join(away, how="cross")
    .with_columns(joint=pl.col("prop") * pl.col("prop_right"))
    .sort("final_digit", "final_digit_right")
    .pivot(values="joint", on="final_digit_right", index="final_digit")
    .with_columns((cs.exclude("final_digit") * 100).round(1))
)

# Display -----

(
    GT(joint, rowname_col="final_digit")
    .data_color(domain=[0, 4], palette=["red", "grey", "blue"])
    .tab_header(
        "Super Bowl Squares | Final Score Probabilities",
        "Based on all NFL regular season and playoff games (2015-2023)",
    )
    .tab_stubhead("")
    .tab_spanner("San Francisco 49ers", cs.all())
    .tab_stubhead("KC Chiefs")
    .tab_source_note(
        md(
            '<span style="float: right;">Source data: [Lee Sharpe, nflverse](https://github.com/nflverse/nfldata)</span>'
        )
    )
)
```

</details>
<div id="wrhbafslog" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#wrhbafslog table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#wrhbafslog thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#wrhbafslog p { margin: 0; padding: 0; }
 #wrhbafslog .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #wrhbafslog .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #wrhbafslog .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #wrhbafslog .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #wrhbafslog .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wrhbafslog .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wrhbafslog .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #wrhbafslog .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #wrhbafslog .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #wrhbafslog .gt_column_spanner_outer:first-child { padding-left: 0; }
 #wrhbafslog .gt_column_spanner_outer:last-child { padding-right: 0; }
 #wrhbafslog .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #wrhbafslog .gt_spanner_row { border-bottom-style: hidden; }
 #wrhbafslog .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #wrhbafslog .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #wrhbafslog .gt_from_md> :first-child { margin-top: 0; }
 #wrhbafslog .gt_from_md> :last-child { margin-bottom: 0; }
 #wrhbafslog .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #wrhbafslog .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #wrhbafslog .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #wrhbafslog .gt_row_group_first td { border-top-width: 2px; }
 #wrhbafslog .gt_row_group_first th { border-top-width: 2px; }
 #wrhbafslog .gt_striped { color: #333333; background-color: #F4F4F4; }
 #wrhbafslog .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #wrhbafslog .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #wrhbafslog .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #wrhbafslog .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #wrhbafslog .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #wrhbafslog .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #wrhbafslog .gt_left { text-align: left; }
 #wrhbafslog .gt_center { text-align: center; }
 #wrhbafslog .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #wrhbafslog .gt_font_normal { font-weight: normal; }
 #wrhbafslog .gt_font_bold { font-weight: bold; }
 #wrhbafslog .gt_font_italic { font-style: italic; }
 #wrhbafslog .gt_super { font-size: 65%; }
 #wrhbafslog .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #wrhbafslog .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="11" class="gt_heading gt_title gt_font_normal">Super Bowl Squares | Final Score Probabilities</th>
</tr>
<tr class="gt_heading">
<th colspan="11" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Based on all NFL regular season and playoff games (2015-2023)</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="KC-Chiefs" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">KC Chiefs</th>
<th colspan="10" id="San-Francisco-49ers" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" scope="colgroup"><span class="gt_column_spanner">San Francisco 49ers</span></th>
</tr>
<tr class="gt_col_headings">
<th id="0" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">0</th>
<th id="1" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">1</th>
<th id="2" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">2</th>
<th id="3" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">3</th>
<th id="4" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">4</th>
<th id="5" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">5</th>
<th id="6" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">6</th>
<th id="7" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">7</th>
<th id="8" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">8</th>
<th id="9" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">9</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #ff0000">0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #a2a2c8">2.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ce8e8e">1.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #9898cb">2.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c8a2a2">1.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #4c4ce5">3.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #de5f5f">1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c4abab">1.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c1b4b4">1.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d57c7c">1.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #8585d2">2.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #bebebe">2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #cb9898">1.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #FFFFFF; background-color: #5f5fde">3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c8a2a2">1.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c4abab">1.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d57c7c">1.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #8e8ece">2.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #FFFFFF; background-color: #0000ff">4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c4abab">1.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c1b4b4">1.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d57c7c">1.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #8585d2">2.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f81313">0.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #de5f5f">1.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f81313">0.2</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #de5f5f">1.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f81313">0.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #de5f5f">1.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d28585">1.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #a2a2c8">2.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ce8e8e">1.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #9898cb">2.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c8a2a2">1.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #3939ec">3.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f81313">0.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #de5f5f">1.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ce8e8e">1.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="11" class="gt_sourcenote"><span style="float: right;">Source data: <a href="https://github.com/nflverse/nfldata">Lee Sharpe, nflverse</a></span></td>
</tr>
</tfoot>
&#10;</table>

</div>

Notice how much higher the chance of winning on any score involving 7 is. This shows up in two places on the table:

- Across the 7 row (i.e. KC Chiefs end with a 7)
- Down the 7 column (i.e. S.F. 49ers ends with a 7)

Moreover, the 7/7 square has the highest chance (3.4%).
Some other good squares are 7/0 (or 0/7), and 0/0.

## Go forth and win the respect of your coworkers

We hope this square will make you the envy of your coworkers.
Here at Great Tables, we're not just interested in the beautiful display of tables, but your success
in defeating the person in the cubicle next to you.

As a final shout out, we used the python data analysis tool Polars for all the data analysis.
Using Polars with Great Tables was a total delight. To learn more about how we analyzed the data, along with the code, see the appendix below!

<details class="callout callout-note" role="note" aria-label="Note">
<summary class="callout-header">
<span class="callout-title">Appendix: analysis and code</span>
</summary>
<div class="callout-body">

### Method

In order to calculate the probability of a given square winning, we focused on the joint probability
of observing a final digit for the home team AND a final digit for the away team.

This can be expressed as `p(home_digit, away_digit | home="SF", away="KC")`.
Note that the probability is conditioned on the teams playing in the Super Bowl. In order to estimate this,
we `p(digit | team="SF")*p(digit | team="KC")`.

This essentially makes two assumptions:

1.  That the final digit does not depend on whether a team is home or away (though it may depend on the team playing).
2.  That the final digit for a given team is independent of the team they are playing.

Another way to think about this is that digit is being modeled as if each team is drawing a ball numbered 0-9 from their own urn. We are modelling the chance of observing a pair of numbers, corresponding to a draw from each team's urns.

The code for this analysis is in [this python script on github](https://github.com/posit-dev/great-tables/blob/main/docs/blog/superbowl-squares/_code.py), and is included below:

### Code

``` python
import polars as pl
import polars.selectors as cs
from great_tables import GT, md


# Utilities -----


def calc_n(df: pl.DataFrame, colname: str):
    """Count the number of final digits observed across games."""

    return df.select(final_digit=pl.col(colname).mod(10)).group_by("final_digit").agg(n=pl.len())


def team_final_digits(game: pl.DataFrame, team_code: str) -> pl.DataFrame:
    """Calculate a team's proportion of digits across games (both home and away)."""

    home_n = calc_n(game.filter(pl.col("home_team") == team_code), "home_score")
    away_n = calc_n(game.filter(pl.col("away_team") == team_code), "away_score")

    joined = (
        home_n.join(away_n, "final_digit")
        .select("final_digit", n=pl.col("n") + pl.col("n_right"))
        .with_columns(prop=pl.col("n") / pl.col("n").sum())
    )

    return joined


# Analysis -----

games = pl.read_csv("./games.csv").filter(
    pl.col("game_id") != "2023_22_SF_KC",
    pl.col("season") >= 2015,
)

# Individual probabilities of final digits per team
home = team_final_digits(games, "KC")
away = team_final_digits(games, "SF")

# Cross and multiply p(digit | team=KC)p(digit | team=SF) to get
# the joint probability p(digit_KC, digit_SF | KC, SF)
joint = (
    home.join(away, how="cross")
    .with_columns(joint=pl.col("prop") * pl.col("prop_right"))
    .sort("final_digit", "final_digit_right")
    .pivot(values="joint", on="final_digit_right", index="final_digit")
    .with_columns((cs.exclude("final_digit") * 100).round(1))
)

# Display -----

(
    GT(joint, rowname_col="final_digit")
    .data_color(domain=[0, 4], palette=["red", "grey", "blue"])
    .tab_header(
        "Super Bowl Squares | Final Score Probabilities",
        "Based on all NFL regular season and playoff games (2015-2023)",
    )
    .tab_stubhead("")
    .tab_spanner("San Francisco 49ers", cs.all())
    .tab_stubhead("KC Chiefs")
    .tab_source_note(
        md(
            '<span style="float: right;">Source data: [Lee Sharpe, nflverse](https://github.com/nflverse/nfldata)</span>'
        )
    )
)
```

<div id="rjdycdknlw" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#rjdycdknlw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rjdycdknlw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rjdycdknlw p { margin: 0; padding: 0; }
 #rjdycdknlw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rjdycdknlw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rjdycdknlw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rjdycdknlw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rjdycdknlw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rjdycdknlw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rjdycdknlw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rjdycdknlw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rjdycdknlw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rjdycdknlw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rjdycdknlw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rjdycdknlw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rjdycdknlw .gt_spanner_row { border-bottom-style: hidden; }
 #rjdycdknlw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rjdycdknlw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rjdycdknlw .gt_from_md> :first-child { margin-top: 0; }
 #rjdycdknlw .gt_from_md> :last-child { margin-bottom: 0; }
 #rjdycdknlw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rjdycdknlw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rjdycdknlw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rjdycdknlw .gt_row_group_first td { border-top-width: 2px; }
 #rjdycdknlw .gt_row_group_first th { border-top-width: 2px; }
 #rjdycdknlw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rjdycdknlw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rjdycdknlw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rjdycdknlw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rjdycdknlw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rjdycdknlw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rjdycdknlw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rjdycdknlw .gt_left { text-align: left; }
 #rjdycdknlw .gt_center { text-align: center; }
 #rjdycdknlw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rjdycdknlw .gt_font_normal { font-weight: normal; }
 #rjdycdknlw .gt_font_bold { font-weight: bold; }
 #rjdycdknlw .gt_font_italic { font-style: italic; }
 #rjdycdknlw .gt_super { font-size: 65%; }
 #rjdycdknlw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rjdycdknlw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="11" class="gt_heading gt_title gt_font_normal">Super Bowl Squares | Final Score Probabilities</th>
</tr>
<tr class="gt_heading">
<th colspan="11" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Based on all NFL regular season and playoff games (2015-2023)</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" id="KC-Chiefs" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">KC Chiefs</th>
<th colspan="10" id="San-Francisco-49ers" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" scope="colgroup"><span class="gt_column_spanner">San Francisco 49ers</span></th>
</tr>
<tr class="gt_col_headings">
<th id="0" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">0</th>
<th id="1" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">1</th>
<th id="2" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">2</th>
<th id="3" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">3</th>
<th id="4" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">4</th>
<th id="5" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">5</th>
<th id="6" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">6</th>
<th id="7" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">7</th>
<th id="8" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">8</th>
<th id="9" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">9</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #ff0000">0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #a2a2c8">2.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ce8e8e">1.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #9898cb">2.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c8a2a2">1.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #4c4ce5">3.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #de5f5f">1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c4abab">1.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c1b4b4">1.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d57c7c">1.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #8585d2">2.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #bebebe">2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #cb9898">1.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #FFFFFF; background-color: #5f5fde">3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c8a2a2">1.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c4abab">1.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d57c7c">1.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #8e8ece">2.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #FFFFFF; background-color: #0000ff">4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c4abab">1.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c1b4b4">1.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d57c7c">1.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #8585d2">2.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f81313">0.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #de5f5f">1.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f81313">0.2</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #de5f5f">1.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f81313">0.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #de5f5f">1.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d28585">1.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #a2a2c8">2.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ce8e8e">1.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #9898cb">2.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c8a2a2">1.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e25656">0.9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d87272">1.2</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #3939ec">3.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f81313">0.2</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ec3939">0.6</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">9</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #de5f5f">1.0</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e84242">0.7</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f51c1c">0.3</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #db6969">1.1</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e54c4c">0.8</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ce8e8e">1.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #ef3030">0.5</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f22626">0.4</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="11" class="gt_sourcenote"><span style="float: right;">Source data: <a href="https://github.com/nflverse/nfldata">Lee Sharpe, nflverse</a></span></td>
</tr>
</tfoot>
&#10;</table>

</div>
</div>
</details>
