---
title: 'Great Tables `v0.12.0`: Google Fonts and zebra stripes'
description: "New in Great Tables v0.12.0: Google Fonts via google_font() and zebra striping with opt_row_striping()."
auto-description: true
people:
  - Rich Iannone
date: '2024-09-30T00:00:00.000Z'
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


In Great Tables `0.12.0` we focused on adding options for customizing the appearance of a table. In this post, we'll present two new features:

- using typefaces from Google Fonts via `tab_style()` and `opt_table_font()`
- adding table striping via `tab_options()` and `opt_row_striping()`

Let's have a look at how these new features can be used!

### Using fonts from Google Fonts

Google Fonts is a free service that allows use of hosted typefaces in your own websites. In Great Tables, we added the `google_font()` helper function to easily incorporate such fonts in your tables. There are two ways to go about this:

1.  use `google_font()` with `opt_table_font()` to set a Google Font for the entire table
2.  invoke `google_font()` within `tab_style(styles=style.text(font=...))` to set the font within a location

Let's start with this small table that uses the default set of fonts for the entire table.

<details class="code-fold">
<summary>Show the code</summary>

``` python
from great_tables import GT, exibble, style, loc

gt_tbl = (
    GT(exibble.head(), rowname_col="row", groupname_col="group")
    .cols_hide(columns=["char", "fctr", "date", "time"])
    .tab_header(
        title="A small piece of the exibble dataset",
        subtitle="Displaying the first five rows (of eight)",
    )
    .tab_source_note(
        source_note="This dataset is included in Great Tables."
    )
)

gt_tbl
```

</details>
<div id="qwmdcpmegn" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#qwmdcpmegn table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qwmdcpmegn thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qwmdcpmegn p { margin: 0; padding: 0; }
 #qwmdcpmegn .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qwmdcpmegn .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qwmdcpmegn .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qwmdcpmegn .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qwmdcpmegn .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qwmdcpmegn .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qwmdcpmegn .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qwmdcpmegn .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qwmdcpmegn .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qwmdcpmegn .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qwmdcpmegn .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qwmdcpmegn .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qwmdcpmegn .gt_spanner_row { border-bottom-style: hidden; }
 #qwmdcpmegn .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qwmdcpmegn .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qwmdcpmegn .gt_from_md> :first-child { margin-top: 0; }
 #qwmdcpmegn .gt_from_md> :last-child { margin-bottom: 0; }
 #qwmdcpmegn .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qwmdcpmegn .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qwmdcpmegn .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qwmdcpmegn .gt_row_group_first td { border-top-width: 2px; }
 #qwmdcpmegn .gt_row_group_first th { border-top-width: 2px; }
 #qwmdcpmegn .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qwmdcpmegn .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qwmdcpmegn .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qwmdcpmegn .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qwmdcpmegn .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qwmdcpmegn .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qwmdcpmegn .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qwmdcpmegn .gt_left { text-align: left; }
 #qwmdcpmegn .gt_center { text-align: center; }
 #qwmdcpmegn .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qwmdcpmegn .gt_font_normal { font-weight: normal; }
 #qwmdcpmegn .gt_font_bold { font-weight: bold; }
 #qwmdcpmegn .gt_font_italic { font-style: italic; }
 #qwmdcpmegn .gt_super { font-size: 65%; }
 #qwmdcpmegn .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qwmdcpmegn .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" data-quarto-table-cell-role="th">grp_a</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" data-quarto-table-cell-role="th">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>
&#10;</table>

</div>

Now, with `opt_table_font()` + `google_font()`, we'll change the table's font to one from Google Fonts. I like [`Noto Serif`](https://fonts.google.com/noto/specimen/Noto+Serif) so let's use that here!

``` python
from great_tables import GT, exibble, style, loc, google_font

(
    gt_tbl
    .opt_table_font(font=google_font(name="Noto Serif"))
)
```

<div id="opnlnkumof" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif&display=swap');
#opnlnkumof table {
          font-family: 'Noto Serif', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#opnlnkumof thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#opnlnkumof p { margin: 0; padding: 0; }
 #opnlnkumof .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #opnlnkumof .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #opnlnkumof .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #opnlnkumof .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #opnlnkumof .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #opnlnkumof .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #opnlnkumof .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #opnlnkumof .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #opnlnkumof .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #opnlnkumof .gt_column_spanner_outer:first-child { padding-left: 0; }
 #opnlnkumof .gt_column_spanner_outer:last-child { padding-right: 0; }
 #opnlnkumof .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #opnlnkumof .gt_spanner_row { border-bottom-style: hidden; }
 #opnlnkumof .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #opnlnkumof .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #opnlnkumof .gt_from_md> :first-child { margin-top: 0; }
 #opnlnkumof .gt_from_md> :last-child { margin-bottom: 0; }
 #opnlnkumof .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #opnlnkumof .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #opnlnkumof .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #opnlnkumof .gt_row_group_first td { border-top-width: 2px; }
 #opnlnkumof .gt_row_group_first th { border-top-width: 2px; }
 #opnlnkumof .gt_striped { color: #333333; background-color: #F4F4F4; }
 #opnlnkumof .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #opnlnkumof .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #opnlnkumof .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #opnlnkumof .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #opnlnkumof .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #opnlnkumof .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #opnlnkumof .gt_left { text-align: left; }
 #opnlnkumof .gt_center { text-align: center; }
 #opnlnkumof .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #opnlnkumof .gt_font_normal { font-weight: normal; }
 #opnlnkumof .gt_font_bold { font-weight: bold; }
 #opnlnkumof .gt_font_italic { font-style: italic; }
 #opnlnkumof .gt_super { font-size: 65%; }
 #opnlnkumof .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #opnlnkumof .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" data-quarto-table-cell-role="th">grp_a</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_2</td>
<td class="gt_row gt_right">2.222</td>
<td class="gt_row gt_right">2018-02-02 14:33</td>
<td class="gt_row gt_right">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_4</td>
<td class="gt_row gt_right">444.4</td>
<td class="gt_row gt_right">2018-04-04 15:55</td>
<td class="gt_row gt_right">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" data-quarto-table-cell-role="th">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>
&#10;</table>

</div>

Looking good! And we don't have to apply the font to the entire table. We might just wanted to use a Google Font in the table body. For that use case, `tab_style()` is the preferred method. Here's an example that uses the [`IBM Plex Mono`](https://fonts.google.com/specimen/IBM+Plex+Mono) typeface.

``` python
(
    gt_tbl
    .tab_style(
        style=style.text(font=google_font(name="IBM Plex Mono")),
        locations=loc.body()
    )
)
```

<div id="iyvfcbcbmw" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
#iyvfcbcbmw table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#iyvfcbcbmw thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#iyvfcbcbmw p { margin: 0; padding: 0; }
 #iyvfcbcbmw .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #iyvfcbcbmw .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #iyvfcbcbmw .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #iyvfcbcbmw .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #iyvfcbcbmw .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iyvfcbcbmw .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iyvfcbcbmw .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #iyvfcbcbmw .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #iyvfcbcbmw .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #iyvfcbcbmw .gt_column_spanner_outer:first-child { padding-left: 0; }
 #iyvfcbcbmw .gt_column_spanner_outer:last-child { padding-right: 0; }
 #iyvfcbcbmw .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #iyvfcbcbmw .gt_spanner_row { border-bottom-style: hidden; }
 #iyvfcbcbmw .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #iyvfcbcbmw .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #iyvfcbcbmw .gt_from_md> :first-child { margin-top: 0; }
 #iyvfcbcbmw .gt_from_md> :last-child { margin-bottom: 0; }
 #iyvfcbcbmw .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #iyvfcbcbmw .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #iyvfcbcbmw .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #iyvfcbcbmw .gt_row_group_first td { border-top-width: 2px; }
 #iyvfcbcbmw .gt_row_group_first th { border-top-width: 2px; }
 #iyvfcbcbmw .gt_striped { color: #333333; background-color: #F4F4F4; }
 #iyvfcbcbmw .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #iyvfcbcbmw .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #iyvfcbcbmw .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #iyvfcbcbmw .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #iyvfcbcbmw .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #iyvfcbcbmw .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #iyvfcbcbmw .gt_left { text-align: left; }
 #iyvfcbcbmw .gt_center { text-align: center; }
 #iyvfcbcbmw .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #iyvfcbcbmw .gt_font_normal { font-weight: normal; }
 #iyvfcbcbmw .gt_font_bold { font-weight: bold; }
 #iyvfcbcbmw .gt_font_italic { font-style: italic; }
 #iyvfcbcbmw .gt_super { font-size: 65%; }
 #iyvfcbcbmw .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #iyvfcbcbmw .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" data-quarto-table-cell-role="th">grp_a</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_1</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">0.1111</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-01-01 02:22</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_2</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2.222</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-02-02 14:33</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_3</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">33.33</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-03-03 03:44</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_4</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">444.4</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-04-04 15:55</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" data-quarto-table-cell-role="th">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_5</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">5550.0</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">2018-05-05 04:00</td>
<td class="gt_row gt_right" style="font-family: IBM Plex Mono">1325.81</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>
&#10;</table>

</div>

Nice! And it's refreshing to see tables with fonts different from default set, as good as it might be. We kept the `google_font()` helper function as simple as possible, requiring only the font name in its `name=` argument. There are hundreds of fonts hosted on [Google Fonts](https://fonts.google.com) so look through the site, experiment, and find the fonts that you think look best in your tables!

### Striping rows in your table

Some people like having row striping (a.k.a. zebra stripes) in their display tables. We also know that some [advise against the practice](https://www.darkhorseanalytics.com/blog/clear-off-the-table/). We understand it's a controversial table issue, however, we also want to give you the creative freedom to just include the stripes. To that end, we now have that option in the package. There are two ways to enable this look:

1.  invoking `opt_row_striping()` to quickly set row stripes in the table body
2.  using some combination of three `row_striping_*` arguments in `tab_options()`

Let's use that example table with `opt_row_striping()`.

``` python
gt_tbl.opt_row_striping()
```

<div id="adsisobill" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#adsisobill table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#adsisobill thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#adsisobill p { margin: 0; padding: 0; }
 #adsisobill .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #adsisobill .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #adsisobill .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #adsisobill .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #adsisobill .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #adsisobill .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #adsisobill .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #adsisobill .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #adsisobill .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #adsisobill .gt_column_spanner_outer:first-child { padding-left: 0; }
 #adsisobill .gt_column_spanner_outer:last-child { padding-right: 0; }
 #adsisobill .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #adsisobill .gt_spanner_row { border-bottom-style: hidden; }
 #adsisobill .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #adsisobill .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #adsisobill .gt_from_md> :first-child { margin-top: 0; }
 #adsisobill .gt_from_md> :last-child { margin-bottom: 0; }
 #adsisobill .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #adsisobill .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #adsisobill .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #adsisobill .gt_row_group_first td { border-top-width: 2px; }
 #adsisobill .gt_row_group_first th { border-top-width: 2px; }
 #adsisobill .gt_striped { color: #333333; background-color: #F4F4F4; }
 #adsisobill .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #adsisobill .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #adsisobill .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #adsisobill .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #adsisobill .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #adsisobill .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #adsisobill .gt_left { text-align: left; }
 #adsisobill .gt_center { text-align: center; }
 #adsisobill .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #adsisobill .gt_font_normal { font-weight: normal; }
 #adsisobill .gt_font_bold { font-weight: bold; }
 #adsisobill .gt_font_italic { font-style: italic; }
 #adsisobill .gt_super { font-size: 65%; }
 #adsisobill .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #adsisobill .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" data-quarto-table-cell-role="th">grp_a</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_2</td>
<td class="gt_row gt_right gt_striped">2.222</td>
<td class="gt_row gt_right gt_striped">2018-02-02 14:33</td>
<td class="gt_row gt_right gt_striped">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_4</td>
<td class="gt_row gt_right gt_striped">444.4</td>
<td class="gt_row gt_right gt_striped">2018-04-04 15:55</td>
<td class="gt_row gt_right gt_striped">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" data-quarto-table-cell-role="th">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>
&#10;</table>

</div>

It's somewhat subtle but there is an alternating, slightly gray background (starting on the `"row_2"` row). The color is `#808080` but with an alpha (transparency) value of `0.05`.

If this is not exactly what you want, there is an alternative to this. The `tab_options()` method has three new arguments:

- `row_striping_background_color`: color to use for row striping
- `row_striping_include_stub`: should striping include cells in the stub?
- `row_striping_include_table_body`: should striping include cells in the body?

With these new options, we can choose to stripe the *entire* row (stub cells + body cells) and use a darker color like `"lightblue"`.

``` python
(
    gt_tbl
    .tab_options(
        row_striping_background_color="lightblue",
        row_striping_include_stub=True,
        row_striping_include_table_body=True,
    )
)
```

<div id="zogjwuunac" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#zogjwuunac table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#zogjwuunac thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#zogjwuunac p { margin: 0; padding: 0; }
 #zogjwuunac .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #zogjwuunac .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #zogjwuunac .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #zogjwuunac .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #zogjwuunac .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zogjwuunac .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zogjwuunac .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #zogjwuunac .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #zogjwuunac .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #zogjwuunac .gt_column_spanner_outer:first-child { padding-left: 0; }
 #zogjwuunac .gt_column_spanner_outer:last-child { padding-right: 0; }
 #zogjwuunac .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #zogjwuunac .gt_spanner_row { border-bottom-style: hidden; }
 #zogjwuunac .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #zogjwuunac .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #zogjwuunac .gt_from_md> :first-child { margin-top: 0; }
 #zogjwuunac .gt_from_md> :last-child { margin-bottom: 0; }
 #zogjwuunac .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #zogjwuunac .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #zogjwuunac .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #zogjwuunac .gt_row_group_first td { border-top-width: 2px; }
 #zogjwuunac .gt_row_group_first th { border-top-width: 2px; }
 #zogjwuunac .gt_striped { color: #333333; background-color: lightblue; }
 #zogjwuunac .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #zogjwuunac .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #zogjwuunac .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #zogjwuunac .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #zogjwuunac .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #zogjwuunac .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #zogjwuunac .gt_left { text-align: left; }
 #zogjwuunac .gt_center { text-align: center; }
 #zogjwuunac .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #zogjwuunac .gt_font_normal { font-weight: normal; }
 #zogjwuunac .gt_font_bold { font-weight: bold; }
 #zogjwuunac .gt_font_italic { font-style: italic; }
 #zogjwuunac .gt_super { font-size: 65%; }
 #zogjwuunac .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #zogjwuunac .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">A small piece of the exibble dataset</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Displaying the first five rows (of eight)</th>
</tr>
<tr class="gt_col_headings">
<th class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="num" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">num</th>
<th id="datetime" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">datetime</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">currency</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" data-quarto-table-cell-role="th">grp_a</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_1</td>
<td class="gt_row gt_right">0.1111</td>
<td class="gt_row gt_right">2018-01-01 02:22</td>
<td class="gt_row gt_right">49.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_striped" data-quarto-table-cell-role="th">row_2</td>
<td class="gt_row gt_right gt_striped">2.222</td>
<td class="gt_row gt_right gt_striped">2018-02-02 14:33</td>
<td class="gt_row gt_right gt_striped">17.95</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_3</td>
<td class="gt_row gt_right">33.33</td>
<td class="gt_row gt_right">2018-03-03 03:44</td>
<td class="gt_row gt_right">1.39</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub gt_striped" data-quarto-table-cell-role="th">row_4</td>
<td class="gt_row gt_right gt_striped">444.4</td>
<td class="gt_row gt_right gt_striped">2018-04-04 15:55</td>
<td class="gt_row gt_right gt_striped">65100.0</td>
</tr>
<tr class="gt_group_heading_row">
<td colspan="4" class="gt_group_heading" data-quarto-table-cell-role="th">grp_b</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">row_5</td>
<td class="gt_row gt_right">5550.0</td>
<td class="gt_row gt_right">2018-05-05 04:00</td>
<td class="gt_row gt_right">1325.81</td>
</tr>
</tbody><tfoot class="gt_sourcenotes">
<tr>
<td colspan="4" class="gt_sourcenote">This dataset is included in Great Tables.</td>
</tr>
</tfoot>
&#10;</table>

</div>

These alternating fills can be a good idea in some table display circumstances. Now, you can make that call and the functionality is there to support your decision.

### Wrapping up

We are excited that this new functionality is now available in Great Tables. As ever, please let us know through [GitHub Issues](https://github.com/posit-dev/great-tables/issues) whether you ran into problems with any feature (new or old), or, if you have suggestions for further improvement!
