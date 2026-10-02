---
jupyter: python3
html-table-processing: none
title: Introducing Great Tables
description: >-
  A tour of the new Great Tables Python package — building structured tables,
  formatting cell values, applying targeted styles, and using Polars expressions
  for column selection.
people:
  - Rich Iannone
date: '2024-01-04'
freeze: true
ported_from: great_tables
source: great_tables
port_status: in-progress
software:
  - great-tables
languages:
  - Python
topics:
  - Visualization
tags:
  - Great Tables
---


<script src="https://cdn.jsdelivr.net/npm/requirejs@2.3.6/require.min.js" integrity="sha384-c9c+LnTbwQ3aujuU7ULEPVvgLs+Fn6fJUvIGTsuu1ZcCf11fiEubah0ttpca4ntM sha384-6V1/AdqZRWk1KAlWbKBlGhN7VG4iE/yAZcO6NZPMF8od0vukrvr0tg4qY6NSrItx" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js" integrity="sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/6Z/hRTt8+pR6L4N2" crossorigin="anonymous" data-relocate-top="true"></script>
<script type="application/javascript">define('jquery', [],function() {return window.jQuery;})</script>


We are really excited about developing the **Great Tables** package because we believe it'll make great-looking display tables possible in Python. Though it's still early days for the project/package, you can do good things with it today! The most recent version of **Great Tables** is in [`PyPI`](https://pypi.org/project/great-tables/). You can install it by using:

``` bash
pip install great_tables
```

In this short post, we'll take a look at a few examples that focus on the more common table-making use cases. We'll show you how to:

- configure the structure of the table
- format table-cell values
- integrate source notes
- add styling to targeted table cells
- use features from **Polars** to make it all better/nicer

Alright! Let's get right into it.

## A Basic Table

Let's get right to making a display table with **Great Tables**. The package has quite a few datasets and so we'll start by making use of the very small, but useful, `exibble` dataset. After importing the `GT` class and that dataset, we'll introduce that Pandas table to `GT()`.

``` python
from great_tables import GT, exibble

# Create a display table with the `exibble` dataset
gt_tbl = GT(exibble)

# Now, show the gt table
gt_tbl
```

<div id="thnfailrsn" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#thnfailrsn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#thnfailrsn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#thnfailrsn p { margin: 0; padding: 0; }
 #thnfailrsn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #thnfailrsn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #thnfailrsn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #thnfailrsn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #thnfailrsn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #thnfailrsn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #thnfailrsn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #thnfailrsn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #thnfailrsn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #thnfailrsn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #thnfailrsn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #thnfailrsn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #thnfailrsn .gt_spanner_row { border-bottom-style: hidden; }
 #thnfailrsn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #thnfailrsn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #thnfailrsn .gt_from_md> :first-child { margin-top: 0; }
 #thnfailrsn .gt_from_md> :last-child { margin-bottom: 0; }
 #thnfailrsn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #thnfailrsn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #thnfailrsn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #thnfailrsn .gt_row_group_first td { border-top-width: 2px; }
 #thnfailrsn .gt_row_group_first th { border-top-width: 2px; }
 #thnfailrsn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #thnfailrsn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #thnfailrsn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #thnfailrsn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #thnfailrsn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #thnfailrsn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #thnfailrsn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #thnfailrsn .gt_left { text-align: left; }
 #thnfailrsn .gt_center { text-align: center; }
 #thnfailrsn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #thnfailrsn .gt_font_normal { font-weight: normal; }
 #thnfailrsn .gt_font_bold { font-weight: bold; }
 #thnfailrsn .gt_font_italic { font-style: italic; }
 #thnfailrsn .gt_super { font-size: 65%; }
 #thnfailrsn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #thnfailrsn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>
<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>

<tr class="gt_col_headings">
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="num">num</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="char">char</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="fctr">fctr</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="date">date</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="time">time</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="datetime">datetime</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="currency">currency</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="row">row</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="group">group</th>
</tr>
</thead>
<tbody class="gt_table_body">
  <tr>
    <td class="gt_row gt_right">0.1111</td>
    <td class="gt_row gt_left">apricot</td>
    <td class="gt_row gt_left">one</td>
    <td class="gt_row gt_right">2015-01-15</td>
    <td class="gt_row gt_right">13:35</td>
    <td class="gt_row gt_right">2018-01-01 02:22</td>
    <td class="gt_row gt_right">49.95</td>
    <td class="gt_row gt_left">row_1</td>
    <td class="gt_row gt_left">grp_a</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">2.222</td>
    <td class="gt_row gt_left">banana</td>
    <td class="gt_row gt_left">two</td>
    <td class="gt_row gt_right">2015-02-15</td>
    <td class="gt_row gt_right">14:40</td>
    <td class="gt_row gt_right">2018-02-02 14:33</td>
    <td class="gt_row gt_right">17.95</td>
    <td class="gt_row gt_left">row_2</td>
    <td class="gt_row gt_left">grp_a</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">33.33</td>
    <td class="gt_row gt_left">coconut</td>
    <td class="gt_row gt_left">three</td>
    <td class="gt_row gt_right">2015-03-15</td>
    <td class="gt_row gt_right">15:45</td>
    <td class="gt_row gt_right">2018-03-03 03:44</td>
    <td class="gt_row gt_right">1.39</td>
    <td class="gt_row gt_left">row_3</td>
    <td class="gt_row gt_left">grp_a</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">444.4</td>
    <td class="gt_row gt_left">durian</td>
    <td class="gt_row gt_left">four</td>
    <td class="gt_row gt_right">2015-04-15</td>
    <td class="gt_row gt_right">16:50</td>
    <td class="gt_row gt_right">2018-04-04 15:55</td>
    <td class="gt_row gt_right">65100.0</td>
    <td class="gt_row gt_left">row_4</td>
    <td class="gt_row gt_left">grp_a</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">5550.0</td>
    <td class="gt_row gt_left"><NA></td>
    <td class="gt_row gt_left">five</td>
    <td class="gt_row gt_right">2015-05-15</td>
    <td class="gt_row gt_right">17:55</td>
    <td class="gt_row gt_right">2018-05-05 04:00</td>
    <td class="gt_row gt_right">1325.81</td>
    <td class="gt_row gt_left">row_5</td>
    <td class="gt_row gt_left">grp_b</td>
  </tr>
  <tr>
    <td class="gt_row gt_right"><NA></td>
    <td class="gt_row gt_left">fig</td>
    <td class="gt_row gt_left">six</td>
    <td class="gt_row gt_right">2015-06-15</td>
    <td class="gt_row gt_right"><NA></td>
    <td class="gt_row gt_right">2018-06-06 16:11</td>
    <td class="gt_row gt_right">13.255</td>
    <td class="gt_row gt_left">row_6</td>
    <td class="gt_row gt_left">grp_b</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">777000.0</td>
    <td class="gt_row gt_left">grapefruit</td>
    <td class="gt_row gt_left">seven</td>
    <td class="gt_row gt_right"><NA></td>
    <td class="gt_row gt_right">19:10</td>
    <td class="gt_row gt_right">2018-07-07 05:22</td>
    <td class="gt_row gt_right"><NA></td>
    <td class="gt_row gt_left">row_7</td>
    <td class="gt_row gt_left">grp_b</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">8880000.0</td>
    <td class="gt_row gt_left">honeydew</td>
    <td class="gt_row gt_left">eight</td>
    <td class="gt_row gt_right">2015-08-15</td>
    <td class="gt_row gt_right">20:20</td>
    <td class="gt_row gt_right"><NA></td>
    <td class="gt_row gt_right">0.44</td>
    <td class="gt_row gt_left">row_8</td>
    <td class="gt_row gt_left">grp_b</td>
  </tr>
</tbody>


</table>

</div>
        

That looks pretty good! Indeed, it is a basic table but we really didn't really ask for much either. What we did get was an HTML table containing column labels and all of the body cells. You'll probably be wanting a bit more, so, let's look at how we can incorporate more table components and perform cell data formatting in the upcoming examples.

## More Complex Tables

Let's take things a bit further and create a table with the included `gtcars` dataset. **Great Tables** provides a large selection of methods and they let you refine the table display. They were designed so that you can easily create a really presentable and *beautiful* table visualization.

For this next table, we'll incorporate a *Stub* component and this provides a place for the row labels. Groupings of rows will be generated through categorical values in a particular column (we just have to cite the column name for that to work). We'll add a table title and subtitle with `tab_header()`. The numerical values will be formatted with the `fmt_integer()` and `fmt_currency()` methods. Column labels will be enhanced via `cols_label()` and a source note will be included through use of the `tab_source_note()` method. Here is the table code, followed by the table itself.

``` python
from great_tables import GT, md, html
from great_tables.data import gtcars

gtcars_mini = gtcars[["mfr", "model", "year", "hp", "trq", "msrp"]].tail(10)

(
    GT(gtcars_mini, rowname_col="model", groupname_col="mfr")
    .tab_spanner(label=md("*Performance*"), columns=["hp", "trq"])
    .tab_header(
        title=html("Data listing from <strong>gtcars</strong>"),
        subtitle=html("A <span style='font-size:12px;'>small selection</span> of great cars."),
    )
    .cols_label(year="Year Produced", hp="HP", trq="Torque", msrp="Price (USD)")
    .fmt_integer(columns=["year", "hp", "trq"], use_seps=False)
    .fmt_currency(columns="msrp")
    .tab_source_note(source_note="Source: the gtcars dataset within the Great Tables package.")
)
```

<div id="lcybcuwnlj" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#lcybcuwnlj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#lcybcuwnlj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#lcybcuwnlj p { margin: 0; padding: 0; }
 #lcybcuwnlj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #lcybcuwnlj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #lcybcuwnlj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #lcybcuwnlj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #lcybcuwnlj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lcybcuwnlj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lcybcuwnlj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #lcybcuwnlj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #lcybcuwnlj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #lcybcuwnlj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #lcybcuwnlj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #lcybcuwnlj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #lcybcuwnlj .gt_spanner_row { border-bottom-style: hidden; }
 #lcybcuwnlj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #lcybcuwnlj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #lcybcuwnlj .gt_from_md> :first-child { margin-top: 0; }
 #lcybcuwnlj .gt_from_md> :last-child { margin-bottom: 0; }
 #lcybcuwnlj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #lcybcuwnlj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #lcybcuwnlj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #lcybcuwnlj .gt_row_group_first td { border-top-width: 2px; }
 #lcybcuwnlj .gt_row_group_first th { border-top-width: 2px; }
 #lcybcuwnlj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #lcybcuwnlj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #lcybcuwnlj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #lcybcuwnlj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #lcybcuwnlj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #lcybcuwnlj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #lcybcuwnlj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #lcybcuwnlj .gt_left { text-align: left; }
 #lcybcuwnlj .gt_center { text-align: center; }
 #lcybcuwnlj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #lcybcuwnlj .gt_font_normal { font-weight: normal; }
 #lcybcuwnlj .gt_font_bold { font-weight: bold; }
 #lcybcuwnlj .gt_font_italic { font-style: italic; }
 #lcybcuwnlj .gt_super { font-size: 65%; }
 #lcybcuwnlj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #lcybcuwnlj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>
<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>

  <tr class="gt_heading">
    <td colspan="5" class="gt_heading gt_title gt_font_normal">Data listing from <strong>gtcars</strong></td>
  </tr>
  <tr class="gt_heading">
    <td colspan="5" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">A <span style='font-size:12px;'>small selection</span> of great cars.</td>
  </tr>
<tr class="gt_col_headings gt_spanner_row">
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="2" colspan="1" scope="col" id=""></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="2" colspan="1" scope="col" id="year">Year Produced</th>
  <th class="gt_center gt_columns_top_border gt_column_spanner_outer" rowspan="1" colspan="2" scope="colgroup" id="&lt;em&gt;Performance&lt;/em&gt;">
    <span class="gt_column_spanner"><em>Performance</em></span>
  </th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="2" colspan="1" scope="col" id="msrp">Price (USD)</th>
</tr>
<tr class="gt_col_headings">
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="hp">HP</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="trq">Torque</th>
</tr>
</thead>
<tbody class="gt_table_body">
  <tr class="gt_group_heading_row">
    <th class="gt_group_heading" colspan="5">Mercedes-Benz</th>
  </tr>
  <tr>
    <th class="gt_row gt_left gt_stub">AMG GT</th>
    <td class="gt_row gt_right">2016</td>
    <td class="gt_row gt_right">503</td>
    <td class="gt_row gt_right">479</td>
    <td class="gt_row gt_right">$129,900.00</td>
  </tr>
  <tr>
    <th class="gt_row gt_left gt_stub">SL-Class</th>
    <td class="gt_row gt_right">2016</td>
    <td class="gt_row gt_right">329</td>
    <td class="gt_row gt_right">354</td>
    <td class="gt_row gt_right">$85,050.00</td>
  </tr>
  <tr class="gt_group_heading_row">
    <th class="gt_group_heading" colspan="5">Tesla</th>
  </tr>
  <tr>
    <th class="gt_row gt_left gt_stub">Model S</th>
    <td class="gt_row gt_right">2017</td>
    <td class="gt_row gt_right">259</td>
    <td class="gt_row gt_right">243</td>
    <td class="gt_row gt_right">$74,500.00</td>
  </tr>
  <tr class="gt_group_heading_row">
    <th class="gt_group_heading" colspan="5">Porsche</th>
  </tr>
  <tr>
    <th class="gt_row gt_left gt_stub">718 Boxster</th>
    <td class="gt_row gt_right">2017</td>
    <td class="gt_row gt_right">300</td>
    <td class="gt_row gt_right">280</td>
    <td class="gt_row gt_right">$56,000.00</td>
  </tr>
  <tr>
    <th class="gt_row gt_left gt_stub">718 Cayman</th>
    <td class="gt_row gt_right">2017</td>
    <td class="gt_row gt_right">300</td>
    <td class="gt_row gt_right">280</td>
    <td class="gt_row gt_right">$53,900.00</td>
  </tr>
  <tr>
    <th class="gt_row gt_left gt_stub">911</th>
    <td class="gt_row gt_right">2016</td>
    <td class="gt_row gt_right">350</td>
    <td class="gt_row gt_right">287</td>
    <td class="gt_row gt_right">$84,300.00</td>
  </tr>
  <tr>
    <th class="gt_row gt_left gt_stub">Panamera</th>
    <td class="gt_row gt_right">2016</td>
    <td class="gt_row gt_right">310</td>
    <td class="gt_row gt_right">295</td>
    <td class="gt_row gt_right">$78,100.00</td>
  </tr>
  <tr class="gt_group_heading_row">
    <th class="gt_group_heading" colspan="5">McLaren</th>
  </tr>
  <tr>
    <th class="gt_row gt_left gt_stub">570</th>
    <td class="gt_row gt_right">2016</td>
    <td class="gt_row gt_right">570</td>
    <td class="gt_row gt_right">443</td>
    <td class="gt_row gt_right">$184,900.00</td>
  </tr>
  <tr class="gt_group_heading_row">
    <th class="gt_group_heading" colspan="5">Rolls-Royce</th>
  </tr>
  <tr>
    <th class="gt_row gt_left gt_stub">Dawn</th>
    <td class="gt_row gt_right">2016</td>
    <td class="gt_row gt_right">563</td>
    <td class="gt_row gt_right">575</td>
    <td class="gt_row gt_right">$335,000.00</td>
  </tr>
  <tr>
    <th class="gt_row gt_left gt_stub">Wraith</th>
    <td class="gt_row gt_right">2016</td>
    <td class="gt_row gt_right">624</td>
    <td class="gt_row gt_right">590</td>
    <td class="gt_row gt_right">$304,350.00</td>
  </tr>
</tbody>
  <tfoot class="gt_sourcenotes">
  
  <tr>
    <td class="gt_sourcenote" colspan="5">Source: the gtcars dataset within the Great Tables package.</td>
  </tr>

</tfoot>

</table>

</div>
        

With the six different methods applied, the table looks highly presentable! The rendering you're seeing here has been done through [**Quarto**](https://quarto.org) (this entire site has been generated with [**quartodoc**](https://machow.github.io/quartodoc/get-started/overview.html)). If you haven't yet tried out **Quarto**, we highly recommend it!

For this next example we'll use the `airquality` dataset (also included in the package; it's inside the `data` submodule). With this table, two spanners will be added with the `tab_spanner()` method. This method is meant to be easy to use, you only need to provide the text for the spanner label and the columns associated with the spanner. We also make it easy to move columns around. You can use `cols_move_to_start()` (example of that below) and there are also the `cols_move_to_end()` and `cols_move()` methods.

``` python
from great_tables.data import airquality

airquality_mini = airquality.head(10).assign(Year=1973)

(
    GT(airquality_mini)
    .tab_header(
        title="New York Air Quality Measurements",
        subtitle="Daily measurements in New York City (May 1-10, 1973)",
    )
    .cols_label(
        Ozone=html("Ozone,<br>ppbV"),
        Solar_R=html("Solar R.,<br>cal/m<sup>2</sup>"),
        Wind=html("Wind,<br>mph"),
        Temp=html("Temp,<br>&deg;F"),
    )
    .tab_spanner(label="Date", columns=["Year", "Month", "Day"])
    .tab_spanner(label="Measurement", columns=["Ozone", "Solar.R", "Wind", "Temp"])
    .cols_move_to_start(columns=["Year", "Month", "Day"])
)
```

<div id="ukvopkeije" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#ukvopkeije table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#ukvopkeije thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#ukvopkeije p { margin: 0; padding: 0; }
 #ukvopkeije .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #ukvopkeije .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #ukvopkeije .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #ukvopkeije .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #ukvopkeije .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ukvopkeije .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ukvopkeije .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #ukvopkeije .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #ukvopkeije .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #ukvopkeije .gt_column_spanner_outer:first-child { padding-left: 0; }
 #ukvopkeije .gt_column_spanner_outer:last-child { padding-right: 0; }
 #ukvopkeije .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #ukvopkeije .gt_spanner_row { border-bottom-style: hidden; }
 #ukvopkeije .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #ukvopkeije .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #ukvopkeije .gt_from_md> :first-child { margin-top: 0; }
 #ukvopkeije .gt_from_md> :last-child { margin-bottom: 0; }
 #ukvopkeije .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #ukvopkeije .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #ukvopkeije .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #ukvopkeije .gt_row_group_first td { border-top-width: 2px; }
 #ukvopkeije .gt_row_group_first th { border-top-width: 2px; }
 #ukvopkeije .gt_striped { color: #333333; background-color: #F4F4F4; }
 #ukvopkeije .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #ukvopkeije .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #ukvopkeije .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #ukvopkeije .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #ukvopkeije .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #ukvopkeije .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #ukvopkeije .gt_left { text-align: left; }
 #ukvopkeije .gt_center { text-align: center; }
 #ukvopkeije .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #ukvopkeije .gt_font_normal { font-weight: normal; }
 #ukvopkeije .gt_font_bold { font-weight: bold; }
 #ukvopkeije .gt_font_italic { font-style: italic; }
 #ukvopkeije .gt_super { font-size: 65%; }
 #ukvopkeije .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #ukvopkeije .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>
<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>

  <tr class="gt_heading">
    <td colspan="7" class="gt_heading gt_title gt_font_normal">New York Air Quality Measurements</td>
  </tr>
  <tr class="gt_heading">
    <td colspan="7" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Daily measurements in New York City (May 1-10, 1973)</td>
  </tr>
<tr class="gt_col_headings gt_spanner_row">
  <th class="gt_center gt_columns_top_border gt_column_spanner_outer" rowspan="1" colspan="3" scope="colgroup" id="Date">
    <span class="gt_column_spanner">Date</span>
  </th>
  <th class="gt_center gt_columns_top_border gt_column_spanner_outer" rowspan="1" colspan="3" scope="colgroup" id="Measurement">
    <span class="gt_column_spanner">Measurement</span>
  </th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="2" colspan="1" scope="col" id="Solar_R">Solar R.,<br>cal/m<sup>2</sup></th>
</tr>
<tr class="gt_col_headings">
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Year">Year</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Month">Month</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Day">Day</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Ozone">Ozone,<br>ppbV</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Wind">Wind,<br>mph</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Temp">Temp,<br>&deg;F</th>
</tr>
</thead>
<tbody class="gt_table_body">
  <tr>
    <td class="gt_row gt_right">1973</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">1</td>
    <td class="gt_row gt_right">41.0</td>
    <td class="gt_row gt_right">7.4</td>
    <td class="gt_row gt_right">67</td>
    <td class="gt_row gt_right">190.0</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">1973</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">2</td>
    <td class="gt_row gt_right">36.0</td>
    <td class="gt_row gt_right">8.0</td>
    <td class="gt_row gt_right">72</td>
    <td class="gt_row gt_right">118.0</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">1973</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">3</td>
    <td class="gt_row gt_right">12.0</td>
    <td class="gt_row gt_right">12.6</td>
    <td class="gt_row gt_right">74</td>
    <td class="gt_row gt_right">149.0</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">1973</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">4</td>
    <td class="gt_row gt_right">18.0</td>
    <td class="gt_row gt_right">11.5</td>
    <td class="gt_row gt_right">62</td>
    <td class="gt_row gt_right">313.0</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">1973</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right"><NA></td>
    <td class="gt_row gt_right">14.3</td>
    <td class="gt_row gt_right">56</td>
    <td class="gt_row gt_right"><NA></td>
  </tr>
  <tr>
    <td class="gt_row gt_right">1973</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">6</td>
    <td class="gt_row gt_right">28.0</td>
    <td class="gt_row gt_right">14.9</td>
    <td class="gt_row gt_right">66</td>
    <td class="gt_row gt_right"><NA></td>
  </tr>
  <tr>
    <td class="gt_row gt_right">1973</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">7</td>
    <td class="gt_row gt_right">23.0</td>
    <td class="gt_row gt_right">8.6</td>
    <td class="gt_row gt_right">65</td>
    <td class="gt_row gt_right">299.0</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">1973</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">8</td>
    <td class="gt_row gt_right">19.0</td>
    <td class="gt_row gt_right">13.8</td>
    <td class="gt_row gt_right">59</td>
    <td class="gt_row gt_right">99.0</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">1973</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">9</td>
    <td class="gt_row gt_right">8.0</td>
    <td class="gt_row gt_right">20.1</td>
    <td class="gt_row gt_right">61</td>
    <td class="gt_row gt_right">19.0</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">1973</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">10</td>
    <td class="gt_row gt_right"><NA></td>
    <td class="gt_row gt_right">8.6</td>
    <td class="gt_row gt_right">69</td>
    <td class="gt_row gt_right">194.0</td>
  </tr>
</tbody>


</table>

</div>
        

That table looks really good, and the nice thing about all these methods is that they can be used in virtually any order.

## Formatting Table Cells

We didn't want to skimp on formatting methods for table cells with this early release. There are 12 `fmt_*()` methods available right now:

- `fmt_number()`: format numeric values
- `fmt_integer()`: format values as integers
- `fmt_percent()`: format values as percentages
- `fmt_scientific()`: format values to scientific notation
- `fmt_currency()`: format values as currencies
- `fmt_bytes()`: format values as bytes
- `fmt_roman()`: format values as Roman numerals
- `fmt_date()`: format values as dates
- `fmt_time()`: format values as times
- `fmt_datetime()`: format values as datetimes
- `fmt_markdown()`: format Markdown text
- `fmt()`: set a column format with a formatting function

We strive to make formatting a simple task but we also want to provide the user a lot of power through advanced options and we ensure that varied combinations of options works well. For example, most of the formatting methods have a `locale=` argument. We want as many users as possible to be able to format numbers, dates, and times in ways that are familiar to them and are adapted to their own regional specifications. Now let's take a look at an example of this with a smaller version of the `exibble` dataset:

``` python
exibble_smaller = exibble[["date", "time"]].head(4)

(
    GT(exibble_smaller)
    .fmt_date(columns="date", date_style="wday_month_day_year")
    .fmt_date(columns="date", rows=[2, 3], date_style="day_month_year", locale="de-CH")
    .fmt_time(columns="time", time_style="h_m_s_p")
)
```

<div id="zqixdtfpbe" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#zqixdtfpbe table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zqixdtfpbe thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zqixdtfpbe p { margin: 0; padding: 0; }
 #zqixdtfpbe .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zqixdtfpbe .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zqixdtfpbe .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zqixdtfpbe .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zqixdtfpbe .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zqixdtfpbe .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zqixdtfpbe .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zqixdtfpbe .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zqixdtfpbe .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zqixdtfpbe .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zqixdtfpbe .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zqixdtfpbe .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zqixdtfpbe .gt_spanner_row { border-bottom-style: hidden; }
 #zqixdtfpbe .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zqixdtfpbe .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zqixdtfpbe .gt_from_md> :first-child { margin-top: 0; }
 #zqixdtfpbe .gt_from_md> :last-child { margin-bottom: 0; }
 #zqixdtfpbe .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zqixdtfpbe .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zqixdtfpbe .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zqixdtfpbe .gt_row_group_first td { border-top-width: 2px; }
 #zqixdtfpbe .gt_row_group_first th { border-top-width: 2px; }
 #zqixdtfpbe .gt_striped { color: #333333; background-color: #F4F4F4; }
 #zqixdtfpbe .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zqixdtfpbe .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zqixdtfpbe .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zqixdtfpbe .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zqixdtfpbe .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zqixdtfpbe .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zqixdtfpbe .gt_left { text-align: left; }
 #zqixdtfpbe .gt_center { text-align: center; }
 #zqixdtfpbe .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zqixdtfpbe .gt_font_normal { font-weight: normal; }
 #zqixdtfpbe .gt_font_bold { font-weight: bold; }
 #zqixdtfpbe .gt_font_italic { font-style: italic; }
 #zqixdtfpbe .gt_super { font-size: 65%; }
 #zqixdtfpbe .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zqixdtfpbe .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>
<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>

<tr class="gt_col_headings">
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="date">date</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="time">time</th>
</tr>
</thead>
<tbody class="gt_table_body">
  <tr>
    <td class="gt_row gt_right">Thursday, January 15, 2015</td>
    <td class="gt_row gt_right">1:35:00 PM</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">Sunday, February 15, 2015</td>
    <td class="gt_row gt_right">2:40:00 PM</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">15 März 2015</td>
    <td class="gt_row gt_right">3:45:00 PM</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">15 April 2015</td>
    <td class="gt_row gt_right">4:50:00 PM</td>
  </tr>
</tbody>


</table>

</div>
        

We support hundreds of locales, from `af` to `zu`! While there are more formatting methods yet to be added, the ones that are available all work exceedingly well.

## Using Styles within a Table

We can use the `tab_style()` method in combination with `loc.body()` and various `style.*()` functions to set styles on cells of data within the table body. For example, the table-making code below applies a yellow background color to the targeted cells.

``` python
from great_tables import GT, style, loc
from great_tables.data import airquality

airquality_mini = airquality.head()

(
    GT(airquality_mini)
    .tab_style(
        style=style.fill(color="yellow"),
        locations=loc.body(columns="Temp", rows=[1, 2])
    )
)
```

<div id="cnhxvieuez" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#cnhxvieuez table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#cnhxvieuez thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#cnhxvieuez p { margin: 0; padding: 0; }
 #cnhxvieuez .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #cnhxvieuez .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #cnhxvieuez .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #cnhxvieuez .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #cnhxvieuez .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cnhxvieuez .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cnhxvieuez .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #cnhxvieuez .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #cnhxvieuez .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #cnhxvieuez .gt_column_spanner_outer:first-child { padding-left: 0; }
 #cnhxvieuez .gt_column_spanner_outer:last-child { padding-right: 0; }
 #cnhxvieuez .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #cnhxvieuez .gt_spanner_row { border-bottom-style: hidden; }
 #cnhxvieuez .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #cnhxvieuez .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #cnhxvieuez .gt_from_md> :first-child { margin-top: 0; }
 #cnhxvieuez .gt_from_md> :last-child { margin-bottom: 0; }
 #cnhxvieuez .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #cnhxvieuez .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #cnhxvieuez .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #cnhxvieuez .gt_row_group_first td { border-top-width: 2px; }
 #cnhxvieuez .gt_row_group_first th { border-top-width: 2px; }
 #cnhxvieuez .gt_striped { color: #333333; background-color: #F4F4F4; }
 #cnhxvieuez .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #cnhxvieuez .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #cnhxvieuez .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #cnhxvieuez .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #cnhxvieuez .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #cnhxvieuez .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #cnhxvieuez .gt_left { text-align: left; }
 #cnhxvieuez .gt_center { text-align: center; }
 #cnhxvieuez .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #cnhxvieuez .gt_font_normal { font-weight: normal; }
 #cnhxvieuez .gt_font_bold { font-weight: bold; }
 #cnhxvieuez .gt_font_italic { font-style: italic; }
 #cnhxvieuez .gt_super { font-size: 65%; }
 #cnhxvieuez .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #cnhxvieuez .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>
<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>

<tr class="gt_col_headings">
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Ozone">Ozone</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Solar_R">Solar_R</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Wind">Wind</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Temp">Temp</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Month">Month</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Day">Day</th>
</tr>
</thead>
<tbody class="gt_table_body">
  <tr>
    <td class="gt_row gt_right">41.0</td>
    <td class="gt_row gt_right">190.0</td>
    <td class="gt_row gt_right">7.4</td>
    <td class="gt_row gt_right">67</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">1</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">36.0</td>
    <td class="gt_row gt_right">118.0</td>
    <td class="gt_row gt_right">8.0</td>
    <td style="background-color: yellow;" class="gt_row gt_right">72</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">2</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">12.0</td>
    <td class="gt_row gt_right">149.0</td>
    <td class="gt_row gt_right">12.6</td>
    <td style="background-color: yellow;" class="gt_row gt_right">74</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">3</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">18.0</td>
    <td class="gt_row gt_right">313.0</td>
    <td class="gt_row gt_right">11.5</td>
    <td class="gt_row gt_right">62</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">4</td>
  </tr>
  <tr>
    <td class="gt_row gt_right"><NA></td>
    <td class="gt_row gt_right"><NA></td>
    <td class="gt_row gt_right">14.3</td>
    <td class="gt_row gt_right">56</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">5</td>
  </tr>
</tbody>


</table>

</div>
        

Aside from `style.fill()` we can also use `style.text()` and `style.borders()` to focus the styling on cell text and borders. Here's an example where we perform several types of styling on targeted cells (the key is to put the `style.*()` calls in a list).

``` python
from great_tables import GT, style, exibble

(
    GT(exibble[["num", "currency"]])
    .fmt_number(columns = "num", decimals=1)
    .fmt_currency(columns = "currency")
    .tab_style(
        style=[
            style.fill(color="lightcyan"),
            style.text(weight="bold")
        ],
        locations=loc.body(columns="num")
    )
    .tab_style(
        style=[
            style.fill(color = "#F9E3D6"),
            style.text(style = "italic")
        ],
        locations=loc.body(columns="currency")
    )
)
```

<div id="eycpxyjlfr" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#eycpxyjlfr table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#eycpxyjlfr thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#eycpxyjlfr p { margin: 0; padding: 0; }
 #eycpxyjlfr .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #eycpxyjlfr .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #eycpxyjlfr .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #eycpxyjlfr .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #eycpxyjlfr .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eycpxyjlfr .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eycpxyjlfr .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #eycpxyjlfr .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #eycpxyjlfr .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #eycpxyjlfr .gt_column_spanner_outer:first-child { padding-left: 0; }
 #eycpxyjlfr .gt_column_spanner_outer:last-child { padding-right: 0; }
 #eycpxyjlfr .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #eycpxyjlfr .gt_spanner_row { border-bottom-style: hidden; }
 #eycpxyjlfr .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #eycpxyjlfr .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #eycpxyjlfr .gt_from_md> :first-child { margin-top: 0; }
 #eycpxyjlfr .gt_from_md> :last-child { margin-bottom: 0; }
 #eycpxyjlfr .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #eycpxyjlfr .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #eycpxyjlfr .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #eycpxyjlfr .gt_row_group_first td { border-top-width: 2px; }
 #eycpxyjlfr .gt_row_group_first th { border-top-width: 2px; }
 #eycpxyjlfr .gt_striped { color: #333333; background-color: #F4F4F4; }
 #eycpxyjlfr .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #eycpxyjlfr .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #eycpxyjlfr .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #eycpxyjlfr .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #eycpxyjlfr .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #eycpxyjlfr .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #eycpxyjlfr .gt_left { text-align: left; }
 #eycpxyjlfr .gt_center { text-align: center; }
 #eycpxyjlfr .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #eycpxyjlfr .gt_font_normal { font-weight: normal; }
 #eycpxyjlfr .gt_font_bold { font-weight: bold; }
 #eycpxyjlfr .gt_font_italic { font-style: italic; }
 #eycpxyjlfr .gt_super { font-size: 65%; }
 #eycpxyjlfr .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #eycpxyjlfr .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>
<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>

<tr class="gt_col_headings">
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="num">num</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="currency">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
  <tr>
    <td style="background-color: lightcyan; font-weight: bold;" class="gt_row gt_right">0.1</td>
    <td style="background-color: #F9E3D6; font-style: italic;" class="gt_row gt_right">$49.95</td>
  </tr>
  <tr>
    <td style="background-color: lightcyan; font-weight: bold;" class="gt_row gt_right">2.2</td>
    <td style="background-color: #F9E3D6; font-style: italic;" class="gt_row gt_right">$17.95</td>
  </tr>
  <tr>
    <td style="background-color: lightcyan; font-weight: bold;" class="gt_row gt_right">33.3</td>
    <td style="background-color: #F9E3D6; font-style: italic;" class="gt_row gt_right">$1.39</td>
  </tr>
  <tr>
    <td style="background-color: lightcyan; font-weight: bold;" class="gt_row gt_right">444.4</td>
    <td style="background-color: #F9E3D6; font-style: italic;" class="gt_row gt_right">$65,100.00</td>
  </tr>
  <tr>
    <td style="background-color: lightcyan; font-weight: bold;" class="gt_row gt_right">5,550.0</td>
    <td style="background-color: #F9E3D6; font-style: italic;" class="gt_row gt_right">$1,325.81</td>
  </tr>
  <tr>
    <td style="background-color: lightcyan; font-weight: bold;" class="gt_row gt_right"><NA></td>
    <td style="background-color: #F9E3D6; font-style: italic;" class="gt_row gt_right">$13.26</td>
  </tr>
  <tr>
    <td style="background-color: lightcyan; font-weight: bold;" class="gt_row gt_right">777,000.0</td>
    <td style="background-color: #F9E3D6; font-style: italic;" class="gt_row gt_right"><NA></td>
  </tr>
  <tr>
    <td style="background-color: lightcyan; font-weight: bold;" class="gt_row gt_right">8,880,000.0</td>
    <td style="background-color: #F9E3D6; font-style: italic;" class="gt_row gt_right">$0.44</td>
  </tr>
</tbody>


</table>

</div>
        

## Column Selection with Polars (and How It Helps with Styling)

Styles can also be specified using **Polars** expressions. For example, the code below uses the `Temp` column to set color to `"lightyellow"` or `"lightblue"`.

``` python
import polars as pl

from great_tables import GT, from_column, style, loc
from great_tables.data import airquality

airquality_mini = pl.from_pandas(airquality.head())

# A Polars expression defines color based on values in `Temp`
fill_color_temp = (
    pl.when(pl.col("Temp") > 70)
    .then(pl.lit("lightyellow"))
    .otherwise(pl.lit("lightblue"))
)

# Pass `fill_color_temp` to the `color=` arg of `style.fill()`
(
    GT(airquality_mini)
    .tab_style(
        style=style.fill(color=fill_color_temp),
        locations=loc.body("Temp")
    )
)
```

<div id="akjhuxzpol" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#akjhuxzpol table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#akjhuxzpol thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#akjhuxzpol p { margin: 0; padding: 0; }
 #akjhuxzpol .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #akjhuxzpol .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #akjhuxzpol .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #akjhuxzpol .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #akjhuxzpol .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #akjhuxzpol .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #akjhuxzpol .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #akjhuxzpol .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #akjhuxzpol .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #akjhuxzpol .gt_column_spanner_outer:first-child { padding-left: 0; }
 #akjhuxzpol .gt_column_spanner_outer:last-child { padding-right: 0; }
 #akjhuxzpol .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #akjhuxzpol .gt_spanner_row { border-bottom-style: hidden; }
 #akjhuxzpol .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #akjhuxzpol .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #akjhuxzpol .gt_from_md> :first-child { margin-top: 0; }
 #akjhuxzpol .gt_from_md> :last-child { margin-bottom: 0; }
 #akjhuxzpol .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #akjhuxzpol .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #akjhuxzpol .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #akjhuxzpol .gt_row_group_first td { border-top-width: 2px; }
 #akjhuxzpol .gt_row_group_first th { border-top-width: 2px; }
 #akjhuxzpol .gt_striped { color: #333333; background-color: #F4F4F4; }
 #akjhuxzpol .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #akjhuxzpol .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #akjhuxzpol .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #akjhuxzpol .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #akjhuxzpol .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #akjhuxzpol .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #akjhuxzpol .gt_left { text-align: left; }
 #akjhuxzpol .gt_center { text-align: center; }
 #akjhuxzpol .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #akjhuxzpol .gt_font_normal { font-weight: normal; }
 #akjhuxzpol .gt_font_bold { font-weight: bold; }
 #akjhuxzpol .gt_font_italic { font-style: italic; }
 #akjhuxzpol .gt_super { font-size: 65%; }
 #akjhuxzpol .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #akjhuxzpol .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>
<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>

<tr class="gt_col_headings">
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Ozone">Ozone</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Solar_R">Solar_R</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Wind">Wind</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Temp">Temp</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Month">Month</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Day">Day</th>
</tr>
</thead>
<tbody class="gt_table_body">
  <tr>
    <td class="gt_row gt_right">41.0</td>
    <td class="gt_row gt_right">190.0</td>
    <td class="gt_row gt_right">7.4</td>
    <td style="background-color: lightblue;" class="gt_row gt_right">67</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">1</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">36.0</td>
    <td class="gt_row gt_right">118.0</td>
    <td class="gt_row gt_right">8.0</td>
    <td style="background-color: lightyellow;" class="gt_row gt_right">72</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">2</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">12.0</td>
    <td class="gt_row gt_right">149.0</td>
    <td class="gt_row gt_right">12.6</td>
    <td style="background-color: lightyellow;" class="gt_row gt_right">74</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">3</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">18.0</td>
    <td class="gt_row gt_right">313.0</td>
    <td class="gt_row gt_right">11.5</td>
    <td style="background-color: lightblue;" class="gt_row gt_right">62</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">4</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">None</td>
    <td class="gt_row gt_right">None</td>
    <td class="gt_row gt_right">14.3</td>
    <td style="background-color: lightblue;" class="gt_row gt_right">56</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">5</td>
  </tr>
</tbody>


</table>

</div>
        

We can deftly mix and match **Polars** column selectors and expressions. This gives us great flexibility in selecting specific columns and rows. Here's an example of doing that again with `tab_style()`:

``` python
import polars.selectors as cs

(
    GT(airquality_mini)
    .tab_style(
        style=style.fill(color="yellow"),
        locations=loc.body(
            columns=cs.starts_with("Te"),
            rows=pl.col("Temp") > 70
        )
    )
)
```

<div id="rqdopthwde" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#rqdopthwde table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#rqdopthwde thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#rqdopthwde p { margin: 0; padding: 0; }
 #rqdopthwde .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #rqdopthwde .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #rqdopthwde .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #rqdopthwde .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #rqdopthwde .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rqdopthwde .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rqdopthwde .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #rqdopthwde .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #rqdopthwde .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #rqdopthwde .gt_column_spanner_outer:first-child { padding-left: 0; }
 #rqdopthwde .gt_column_spanner_outer:last-child { padding-right: 0; }
 #rqdopthwde .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #rqdopthwde .gt_spanner_row { border-bottom-style: hidden; }
 #rqdopthwde .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #rqdopthwde .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #rqdopthwde .gt_from_md> :first-child { margin-top: 0; }
 #rqdopthwde .gt_from_md> :last-child { margin-bottom: 0; }
 #rqdopthwde .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #rqdopthwde .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #rqdopthwde .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #rqdopthwde .gt_row_group_first td { border-top-width: 2px; }
 #rqdopthwde .gt_row_group_first th { border-top-width: 2px; }
 #rqdopthwde .gt_striped { color: #333333; background-color: #F4F4F4; }
 #rqdopthwde .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #rqdopthwde .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #rqdopthwde .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #rqdopthwde .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #rqdopthwde .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #rqdopthwde .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #rqdopthwde .gt_left { text-align: left; }
 #rqdopthwde .gt_center { text-align: center; }
 #rqdopthwde .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #rqdopthwde .gt_font_normal { font-weight: normal; }
 #rqdopthwde .gt_font_bold { font-weight: bold; }
 #rqdopthwde .gt_font_italic { font-style: italic; }
 #rqdopthwde .gt_super { font-size: 65%; }
 #rqdopthwde .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #rqdopthwde .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>
<table class="gt_table" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>

<tr class="gt_col_headings">
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Ozone">Ozone</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Solar_R">Solar_R</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Wind">Wind</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Temp">Temp</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Month">Month</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="Day">Day</th>
</tr>
</thead>
<tbody class="gt_table_body">
  <tr>
    <td class="gt_row gt_right">41.0</td>
    <td class="gt_row gt_right">190.0</td>
    <td class="gt_row gt_right">7.4</td>
    <td class="gt_row gt_right">67</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">1</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">36.0</td>
    <td class="gt_row gt_right">118.0</td>
    <td class="gt_row gt_right">8.0</td>
    <td style="background-color: yellow;" class="gt_row gt_right">72</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">2</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">12.0</td>
    <td class="gt_row gt_right">149.0</td>
    <td class="gt_row gt_right">12.6</td>
    <td style="background-color: yellow;" class="gt_row gt_right">74</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">3</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">18.0</td>
    <td class="gt_row gt_right">313.0</td>
    <td class="gt_row gt_right">11.5</td>
    <td class="gt_row gt_right">62</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">4</td>
  </tr>
  <tr>
    <td class="gt_row gt_right">None</td>
    <td class="gt_row gt_right">None</td>
    <td class="gt_row gt_right">14.3</td>
    <td class="gt_row gt_right">56</td>
    <td class="gt_row gt_right">5</td>
    <td class="gt_row gt_right">5</td>
  </tr>
</tbody>


</table>

</div>
        

It feels great to use the conveniences offered by **Polars** and we're excited about how far we can take this!

## Where We're Going with **Great Tables**

We're obviously pretty encouraged about how **Great Tables** is turning out and so we'll continue to get useful table-making niceties into the package. We welcome any and all feedback, so get in touch with us:

- you can file a GitHub [issue](https://github.com/posit-dev/great-tables/issues) or get a discussion going in [GitHub Discussions](https://github.com/posit-dev/great-tables/discussions)
- there's an [X/Twitter account at @gt_package](https://twitter.com/gt_package), so check it out for package news and announcements
- there's a fun [Discord server](https://discord.gg/Ux7nrcXHVV) that lets you more casually ask questions and generally just talk about table things

Stay tuned for more on **Great Tables** in this blog or elsewhere in the Internet!
