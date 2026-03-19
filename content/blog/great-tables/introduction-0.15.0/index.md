---
title: 'Great Tables `v0.15.0`: Flags, Icons, and Other Formatting Goodies'
people:
  - Rich Iannone
date: 2024-12-19T00:00:00.000Z
ported_from: great_tables
port_status: in-progress
software: ["great-tables"]
languages: ["Python"]
categories:
  - Visualization
---


<script src="https://cdn.jsdelivr.net/npm/requirejs@2.3.6/require.min.js" integrity="sha384-c9c+LnTbwQ3aujuU7ULEPVvgLs+Fn6fJUvIGTsuu1ZcCf11fiEubah0ttpca4ntM sha384-6V1/AdqZRWk1KAlWbKBlGhN7VG4iE/yAZcO6NZPMF8od0vukrvr0tg4qY6NSrItx" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js" integrity="sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/6Z/hRTt8+pR6L4N2" crossorigin="anonymous" data-relocate-top="true"></script>
<script type="application/javascript">define('jquery', [],function() {return window.jQuery;})</script>


The development of Great Tables is really moving along these days. We just released version `0.15.0` and it adds quite a few nice things to the package. The features we'll highlight in this post are:

- adding flag icons with the new `fmt_flag()` method
- peppering your table cells with Font Awesome icons via `fmt_icon()`
- support for displaying accounting notation with four number-based formatting methods

Let's look at each of these in turn!

### Using `fmt_flag()` to incorporate country flag icons

When tables contain country-level data, having a more visual representation for a country can help the reader more quickly parse the table contents. The new `fmt_flag()` method makes this easy to accomplish. You just need to have either [two-letter country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) or [three-letter country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) in a column.

Here's an example where country flags, shown as simplified circular icons, can be added to a table with `fmt_flag()`:

``` python
from great_tables import GT
from great_tables.data import peeps
import polars as pl

peeps_mini = (
    pl.from_pandas(peeps)
    .filter(pl.col("dob").str.slice(offset=0, length=4) == "1988")
    .with_columns(name=pl.col("name_given") + " " + pl.col("name_family"))
    .fill_null(value="")
    .select(["country", "name", "address", "city", "state_prov", "postcode"])
)

(
    GT(peeps_mini)
    .tab_header(title="Our Contacts (Born in 1988)")
    .fmt_flag(columns="country")
    .opt_vertical_padding(scale=0.5)
    .cols_label(
        country="",
        name="Name",
        address="Address",
        city="City",
        state_prov="State/Prov.",
        postcode="Zip/Postcode",
    )
)
```

<div id="qsceyxxmoo" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#qsceyxxmoo table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qsceyxxmoo thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qsceyxxmoo p { margin: 0; padding: 0; }
 #qsceyxxmoo .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qsceyxxmoo .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qsceyxxmoo .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qsceyxxmoo .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 1px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qsceyxxmoo .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qsceyxxmoo .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qsceyxxmoo .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qsceyxxmoo .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 3px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #qsceyxxmoo .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qsceyxxmoo .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qsceyxxmoo .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qsceyxxmoo .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 2px; padding-bottom: 2px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qsceyxxmoo .gt_spanner_row { border-bottom-style: hidden; }
 #qsceyxxmoo .gt_group_heading { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qsceyxxmoo .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #qsceyxxmoo .gt_from_md> :first-child { margin-top: 0; }
 #qsceyxxmoo .gt_from_md> :last-child { margin-bottom: 0; }
 #qsceyxxmoo .gt_row { padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #qsceyxxmoo .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #qsceyxxmoo .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #qsceyxxmoo .gt_row_group_first td { border-top-width: 2px; }
 #qsceyxxmoo .gt_row_group_first th { border-top-width: 2px; }
 #qsceyxxmoo .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qsceyxxmoo .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #qsceyxxmoo .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qsceyxxmoo .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qsceyxxmoo .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qsceyxxmoo .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qsceyxxmoo .gt_sourcenote { font-size: 90%; padding-top: 2px; padding-bottom: 2px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #qsceyxxmoo .gt_left { text-align: left; }
 #qsceyxxmoo .gt_center { text-align: center; }
 #qsceyxxmoo .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qsceyxxmoo .gt_font_normal { font-weight: normal; }
 #qsceyxxmoo .gt_font_bold { font-weight: bold; }
 #qsceyxxmoo .gt_font_italic { font-style: italic; }
 #qsceyxxmoo .gt_super { font-size: 65%; }
 #qsceyxxmoo .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qsceyxxmoo .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" style="width:100%;" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="gt_heading">
<th colspan="6" class="gt_heading gt_title gt_font_normal">Our Contacts (Born in 1988)</th>
</tr>
<tr class="gt_col_headings">
<th id="country" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th id="name" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">Name</th>
<th id="address" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">Address</th>
<th id="city" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">City</th>
<th id="state_prov" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">State/Prov.</th>
<th id="postcode" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col">Zip/Postcode</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left"><span style="white-space:nowrap;">
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
United States
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#eee" d="M256 0h256v64l-32 32 32 32v64l-32 32 32 32v64l-32 32 32 32v64l-256 32L0 448v-64l32-32-32-32v-64z"></path><path fill="#d80027" d="M224 64h288v64H224Zm0 128h288v64H256ZM0 320h512v64H0Zm0 128h512v64H0Z"></path><path fill="#0052b4" d="M0 0h256v256H0Z"></path><path fill="#eee" d="m187 243 57-41h-70l57 41-22-67zm-81 0 57-41H93l57 41-22-67zm-81 0 57-41H12l57 41-22-67zm162-81 57-41h-70l57 41-22-67zm-81 0 57-41H93l57 41-22-67zm-81 0 57-41H12l57 41-22-67Zm162-82 57-41h-70l57 41-22-67Zm-81 0 57-41H93l57 41-22-67zm-81 0 57-41H12l57 41-22-67Z"></path></g>
</svg>
</span></td>
<td class="gt_row gt_left">Martin Bartůněk</td>
<td class="gt_row gt_left">1850 Valley Lane</td>
<td class="gt_row gt_left">Austin</td>
<td class="gt_row gt_left">TX</td>
<td class="gt_row gt_left">78744</td>
</tr>
<tr>
<td class="gt_row gt_left"><span style="white-space:nowrap;">
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Slovenia
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#0052b4" d="m0 167 253.8-19.3L512 167v178l-254.9 32.3L0 345z"></path><path fill="#eee" d="M0 0h512v167H0z"></path><path fill="#d80027" d="M0 345h512v167H0z"></path><path fill="#0052b4" d="M222.7 167v-66.8H89V167l67 82.6z"></path><path fill="#eee" d="M89 167v22.2c0 51.1 66.8 66.8 66.8 66.8s66.8-15.7 66.8-66.8V167l-22.3 22.2-44.5-33.4-44.5 33.4z"></path></g>
</svg>
</span></td>
<td class="gt_row gt_left">Feride Šijan</td>
<td class="gt_row gt_left">Tavcarjeva 58</td>
<td class="gt_row gt_left">Sodražica</td>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_left">1317</td>
</tr>
<tr>
<td class="gt_row gt_left"><span style="white-space:nowrap;">
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Slovenia
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#0052b4" d="m0 167 253.8-19.3L512 167v178l-254.9 32.3L0 345z"></path><path fill="#eee" d="M0 0h512v167H0z"></path><path fill="#d80027" d="M0 345h512v167H0z"></path><path fill="#0052b4" d="M222.7 167v-66.8H89V167l67 82.6z"></path><path fill="#eee" d="M89 167v22.2c0 51.1 66.8 66.8 66.8 66.8s66.8-15.7 66.8-66.8V167l-22.3 22.2-44.5-33.4-44.5 33.4z"></path></g>
</svg>
</span></td>
<td class="gt_row gt_left">Vejsil Crevar</td>
<td class="gt_row gt_left">Gosposka ulica 60</td>
<td class="gt_row gt_left">Novo mesto</td>
<td class="gt_row gt_left"></td>
<td class="gt_row gt_left">8501</td>
</tr>
<tr>
<td class="gt_row gt_left"><span style="white-space:nowrap;">
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Canada
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#d80027" d="M0 0v512h144l112-64 112 64h144V0H368L256 64 144 0Z"></path><path fill="#eee" d="M144 0h224v512H144Z"></path><path fill="#d80027" d="m301 289 44-22-22-11v-22l-45 22 23-44h-23l-22-34-22 33h-23l23 45-45-22v22l-22 11 45 22-12 23h45v33h22v-33h45z"></path></g>
</svg>
</span></td>
<td class="gt_row gt_left">Matilda Bates</td>
<td class="gt_row gt_left">582 Islington Ave</td>
<td class="gt_row gt_left">Toronto</td>
<td class="gt_row gt_left">ON</td>
<td class="gt_row gt_left">M8V 3B6</td>
</tr>
</tbody>
</table>

</div>

This slice of the `peeps` dataset has country codes in their 3-letter form (i.e., `"USA"`, `"SVN"`, and `"CAN"`) within the `country` column. So long as they are correct, `fmt_flag()` will perform the conversion to flag icons. Also, there's a little bit of interactivity here: when hovering over a flag, the country name will appear as a tooltip!

We have the power to display multiple flag icons within a single cell. To make this happen, the country codes need to be combined in a single string where each code is separated by a comma (e.g., `"US,DE,GB"`). Here's an example that uses a portion of the `films` dataset:

``` python
from great_tables import GT, google_font
from great_tables.data import films
import polars as pl

films_mini = (
    pl.from_pandas(films)
    .filter(pl.col("director") == "Michael Haneke")
    .with_columns(title=pl.col("title") + " (" + pl.col("year").cast(pl.String) + ")")
    .select(["title", "run_time", "countries_of_origin"])
)

(
    GT(films_mini)
    .fmt_flag(columns="countries_of_origin")
    .tab_header(title="In Competition Films by Michael Haneke")
    .opt_stylize()
    .tab_options(column_labels_hidden=True)
    .opt_table_font(font=google_font("PT Sans"))
)
```

<div id="viobmltklf" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=PT+Sans&display=swap');
#viobmltklf table {
          font-family: 'PT Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#viobmltklf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#viobmltklf p { margin: 0; padding: 0; }
 #viobmltklf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #004D80; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #004D80; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #viobmltklf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #viobmltklf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #viobmltklf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #viobmltklf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #viobmltklf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #viobmltklf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #viobmltklf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #viobmltklf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #viobmltklf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #viobmltklf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #viobmltklf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #viobmltklf .gt_spanner_row { border-bottom-style: hidden; }
 #viobmltklf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #viobmltklf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; vertical-align: middle; }
 #viobmltklf .gt_from_md> :first-child { margin-top: 0; }
 #viobmltklf .gt_from_md> :last-child { margin-bottom: 0; }
 #viobmltklf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #89D3FE; border-left-style: none; border-left-width: 1px; border-left-color: #89D3FE; border-right-style: none; border-right-width: 1px; border-right-color: #89D3FE; vertical-align: middle; overflow-x: hidden; }
 #viobmltklf .gt_stub { color: #FFFFFF; background-color: #0076BA; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #0076BA; padding-left: 5px; padding-right: 5px; }
 #viobmltklf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #viobmltklf .gt_row_group_first td { border-top-width: 2px; }
 #viobmltklf .gt_row_group_first th { border-top-width: 2px; }
 #viobmltklf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #viobmltklf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #0076BA; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #0076BA; }
 #viobmltklf .gt_grand_summary_row { color: #333333; background-color: #89D3FE; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #viobmltklf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #viobmltklf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #viobmltklf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #viobmltklf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #viobmltklf .gt_left { text-align: left; }
 #viobmltklf .gt_center { text-align: center; }
 #viobmltklf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #viobmltklf .gt_font_normal { font-weight: normal; }
 #viobmltklf .gt_font_bold { font-weight: bold; }
 #viobmltklf .gt_font_italic { font-style: italic; }
 #viobmltklf .gt_super { font-size: 65%; }
 #viobmltklf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #viobmltklf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">In Competition Films by Michael Haneke</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Funny Games (1997)</td>
<td class="gt_row gt_left">1h 48m</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;">
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Austria
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#d80027" d="M0 0h512v167l-23.2 89.7L512 345v167H0V345l29.4-89L0 167z"></path><path fill="#eee" d="M0 167h512v178H0z"></path></g>
</svg>
</span></td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Code Unknown (2000)</td>
<td class="gt_row gt_left gt_striped">1h 58m</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;">
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
France
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#eee" d="M167 0h178l25.9 252.3L345 512H167l-29.8-253.4z"></path><path fill="#0052b4" d="M0 0h167v512H0z"></path><path fill="#d80027" d="M345 0h167v512H345z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Austria
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#d80027" d="M0 0h512v167l-23.2 89.7L512 345v167H0V345l29.4-89L0 167z"></path><path fill="#eee" d="M0 167h512v178H0z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Romania
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#ffda44" d="M167 0h178l25.9 252.3L345 512H167l-29.8-253.4z"></path><path fill="#0052b4" d="M0 0h167v512H0z"></path><path fill="#d80027" d="M345 0h167v512H345z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Germany
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#ffda44" d="m0 345 256.7-25.5L512 345v167H0z"></path><path fill="#d80027" d="m0 167 255-23 257 23v178H0z"></path><path fill="#333" d="M0 0h512v167H0z"></path></g>
</svg>
</span></td>
</tr>
<tr>
<td class="gt_row gt_left">The Piano Teacher (2001)</td>
<td class="gt_row gt_left">2h 11m</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;">
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
France
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#eee" d="M167 0h178l25.9 252.3L345 512H167l-29.8-253.4z"></path><path fill="#0052b4" d="M0 0h167v512H0z"></path><path fill="#d80027" d="M345 0h167v512H345z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Austria
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#d80027" d="M0 0h512v167l-23.2 89.7L512 345v167H0V345l29.4-89L0 167z"></path><path fill="#eee" d="M0 167h512v178H0z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Germany
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#ffda44" d="m0 345 256.7-25.5L512 345v167H0z"></path><path fill="#d80027" d="m0 167 255-23 257 23v178H0z"></path><path fill="#333" d="M0 0h512v167H0z"></path></g>
</svg>
</span></td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Caché (2005)</td>
<td class="gt_row gt_left gt_striped">1h 57m</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;">
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
France
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#eee" d="M167 0h178l25.9 252.3L345 512H167l-29.8-253.4z"></path><path fill="#0052b4" d="M0 0h167v512H0z"></path><path fill="#d80027" d="M345 0h167v512H345z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Austria
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#d80027" d="M0 0h512v167l-23.2 89.7L512 345v167H0V345l29.4-89L0 167z"></path><path fill="#eee" d="M0 167h512v178H0z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Germany
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#ffda44" d="m0 345 256.7-25.5L512 345v167H0z"></path><path fill="#d80027" d="m0 167 255-23 257 23v178H0z"></path><path fill="#333" d="M0 0h512v167H0z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Italy
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#eee" d="M167 0h178l25.9 252.3L345 512H167l-29.8-253.4z"></path><path fill="#6da544" d="M0 0h167v512H0z"></path><path fill="#d80027" d="M345 0h167v512H345z"></path></g>
</svg>
</span></td>
</tr>
<tr>
<td class="gt_row gt_left">The White Ribbon (2009)</td>
<td class="gt_row gt_left">2h 24m</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;">
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Germany
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#ffda44" d="m0 345 256.7-25.5L512 345v167H0z"></path><path fill="#d80027" d="m0 167 255-23 257 23v178H0z"></path><path fill="#333" d="M0 0h512v167H0z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Austria
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#d80027" d="M0 0h512v167l-23.2 89.7L512 345v167H0V345l29.4-89L0 167z"></path><path fill="#eee" d="M0 167h512v178H0z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
France
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#eee" d="M167 0h178l25.9 252.3L345 512H167l-29.8-253.4z"></path><path fill="#0052b4" d="M0 0h167v512H0z"></path><path fill="#d80027" d="M345 0h167v512H345z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Italy
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#eee" d="M167 0h178l25.9 252.3L345 512H167l-29.8-253.4z"></path><path fill="#6da544" d="M0 0h167v512H0z"></path><path fill="#d80027" d="M345 0h167v512H345z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Canada
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#d80027" d="M0 0v512h144l112-64 112 64h144V0H368L256 64 144 0Z"></path><path fill="#eee" d="M144 0h224v512H144Z"></path><path fill="#d80027" d="m301 289 44-22-22-11v-22l-45 22 23-44h-23l-22-34-22 33h-23l23 45-45-22v22l-22 11 45 22-12 23h45v33h22v-33h45z"></path></g>
</svg>
</span></td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Amour (2012)</td>
<td class="gt_row gt_left gt_striped">2h 7m</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;">
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Austria
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#d80027" d="M0 0h512v167l-23.2 89.7L512 345v167H0V345l29.4-89L0 167z"></path><path fill="#eee" d="M0 167h512v178H0z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
France
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#eee" d="M167 0h178l25.9 252.3L345 512H167l-29.8-253.4z"></path><path fill="#0052b4" d="M0 0h167v512H0z"></path><path fill="#d80027" d="M345 0h167v512H345z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Germany
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#ffda44" d="m0 345 256.7-25.5L512 345v167H0z"></path><path fill="#d80027" d="m0 167 255-23 257 23v178H0z"></path><path fill="#333" d="M0 0h512v167H0z"></path></g>
</svg>
</span></td>
</tr>
<tr>
<td class="gt_row gt_left">Happy End (2017)</td>
<td class="gt_row gt_left">1h 47m</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;">
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
France
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#eee" d="M167 0h178l25.9 252.3L345 512H167l-29.8-253.4z"></path><path fill="#0052b4" d="M0 0h167v512H0z"></path><path fill="#d80027" d="M345 0h167v512H345z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Austria
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#d80027" d="M0 0h512v167l-23.2 89.7L512 345v167H0V345l29.4-89L0 167z"></path><path fill="#eee" d="M0 167h512v178H0z"></path></g>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="512" height="512" viewbox="0 0 512 512" style="vertical-align:-0.125em;image-rendering:optimizeQuality;height:1em;width:1em;">
<title>
Germany
</title>
<mask id="a"><circle cx="256" cy="256" r="256" fill="#fff"></circle></mask><g mask="url(#a)"><path fill="#ffda44" d="m0 345 256.7-25.5L512 345v167H0z"></path><path fill="#d80027" d="m0 167 255-23 257 23v178H0z"></path><path fill="#333" d="M0 0h512v167H0z"></path></g>
</svg>
</span></td>
</tr>
</tbody>
</table>

</div>

The column `countries_of_origin` has these combined strings for each of the co-production films, where countries are arranged by decreasing level of contribution (e.g., `"FR,AT,RO,DE"` in the second row). The `fmt_flag()` method parses these strings into a sequence of flag icons that are displayed in the order provided. Each of the flags is separated by a space character but you can always change that default separator with the `sep=` argument.

### Using `fmt_icon()` to include Font Awesome icons

The new `fmt_icon()` method gives you the ability to easily include Font Awesome icons in a table. It uses a similar input/output scheme as with `fmt_flag()`: provide the *short* icon name (e.g., `"table"`, `"music"`, `"globe"`, etc.) or a comma-separated list of them, and `fmt_icon()` will provide the Font Awesome icon in place. Let's see it in action with an example that uses the `metro` dataset:

``` python
from great_tables import GT
from great_tables.data import metro
import polars as pl

metro_mini = (
    pl.from_pandas(metro).tail(10)
    .with_columns(
        services = (
            pl.when(pl.col("connect_tramway").is_not_null())
            .then(pl.lit("train, train-tram"))
            .otherwise(pl.lit("train"))
        )
    )
    .select(["name", "services", "location"])
)

(
    GT(metro_mini)
    .tab_header("Services Available at Select Stations")
    .fmt_icon(columns="services", sep=" / ")
    .tab_options(column_labels_hidden=True)
    .opt_stylize(color="green")
    .opt_horizontal_padding(scale=3)
    .opt_align_table_header(align="left")
)
```

<div id="qmrkrluboa" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#qmrkrluboa table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#qmrkrluboa thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#qmrkrluboa p { margin: 0; padding: 0; }
 #qmrkrluboa .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #027101; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #027101; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #qmrkrluboa .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #qmrkrluboa .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #qmrkrluboa .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 15px; padding-right: 15px; border-top-color: #FFFFFF; border-top-width: 0; }
 #qmrkrluboa .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qmrkrluboa .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #038901; }
 #qmrkrluboa .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #038901; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #038901; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #qmrkrluboa .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 15px; padding-right: 15px; overflow-x: hidden; }
 #qmrkrluboa .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #qmrkrluboa .gt_column_spanner_outer:first-child { padding-left: 0; }
 #qmrkrluboa .gt_column_spanner_outer:last-child { padding-right: 0; }
 #qmrkrluboa .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #038901; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #qmrkrluboa .gt_spanner_row { border-bottom-style: hidden; }
 #qmrkrluboa .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 15px; padding-right: 15px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #038901; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #038901; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #qmrkrluboa .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #038901; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #038901; vertical-align: middle; }
 #qmrkrluboa .gt_from_md> :first-child { margin-top: 0; }
 #qmrkrluboa .gt_from_md> :last-child { margin-bottom: 0; }
 #qmrkrluboa .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 15px; padding-right: 15px; margin: 10px; border-top-style: none; border-top-width: 1px; border-top-color: #CAFFAF; border-left-style: none; border-left-width: 1px; border-left-color: #CAFFAF; border-right-style: none; border-right-width: 1px; border-right-color: #CAFFAF; vertical-align: middle; overflow-x: hidden; }
 #qmrkrluboa .gt_stub { color: #FFFFFF; background-color: #038901; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #038901; padding-left: 15px; padding-right: 15px; }
 #qmrkrluboa .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 15px; padding-right: 15px; vertical-align: top; }
 #qmrkrluboa .gt_row_group_first td { border-top-width: 2px; }
 #qmrkrluboa .gt_row_group_first th { border-top-width: 2px; }
 #qmrkrluboa .gt_striped { color: #333333; background-color: #F4F4F4; }
 #qmrkrluboa .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #038901; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #038901; }
 #qmrkrluboa .gt_grand_summary_row { color: #333333; background-color: #CAFFAF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #qmrkrluboa .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #qmrkrluboa .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #qmrkrluboa .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #qmrkrluboa .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 15px; padding-right: 15px; text-align: left; }
 #qmrkrluboa .gt_left { text-align: left; }
 #qmrkrluboa .gt_center { text-align: center; }
 #qmrkrluboa .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #qmrkrluboa .gt_font_normal { font-weight: normal; }
 #qmrkrluboa .gt_font_bold { font-weight: bold; }
 #qmrkrluboa .gt_font_italic { font-style: italic; }
 #qmrkrluboa .gt_super { font-size: 65%; }
 #qmrkrluboa .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #qmrkrluboa .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="gt_heading">
<th colspan="3" class="gt_heading gt_title gt_font_normal">Services Available at Select Stations</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left">Porte de Vanves</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;">
<svg viewbox="0 0 448 512" preserveaspectratio="none" aria-hidden="true" role="img" class="fa" style="fill-opacity:None;stroke-width:1px;stroke-opacity:None;height:1em;width:0.88em;position:relative;vertical-align:-0.125em;overflow:visible;">
<path d="M96 0C43 0 0 43 0 96V352c0 48 35.2 87.7 81.1 94.9l-46 46C28.1 499.9 33.1 512 43 512H82.7c8.5 0 16.6-3.4 22.6-9.4L160 448H288l54.6 54.6c6 6 14.1 9.4 22.6 9.4H405c10 0 15-12.1 7.9-19.1l-46-46c46-7.1 81.1-46.9 81.1-94.9V96c0-53-43-96-96-96H96zM64 96c0-17.7 14.3-32 32-32H352c17.7 0 32 14.3 32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V96zM224 384c-26.5 0-48-21.5-48-48s21.5-48 48-48s48 21.5 48 48s-21.5 48-48 48z"></path>
</svg>
/
<svg viewbox="0 0 448 512" preserveaspectratio="none" aria-hidden="true" role="img" class="fa" style="fill-opacity:None;stroke-width:1px;stroke-opacity:None;height:1em;width:0.88em;position:relative;vertical-align:-0.125em;overflow:visible;">
<path d="M86.8 48c-12.2 0-23.6 5.5-31.2 15L42.7 79C34.5 89.3 19.4 91 9 82.7S-3 59.4 5.3 49L18 33C34.7 12.2 60 0 86.8 0H361.2c26.7 0 52 12.2 68.7 33l12.8 16c8.3 10.4 6.6 25.5-3.7 33.7s-25.5 6.6-33.7-3.7L392.5 63c-7.6-9.5-19.1-15-31.2-15H248V96h40c53 0 96 43 96 96V352c0 30.6-14.3 57.8-36.6 75.4l65.5 65.5c7.1 7.1 2.1 19.1-7.9 19.1H365.3c-8.5 0-16.6-3.4-22.6-9.4L288 448H160l-54.6 54.6c-6 6-14.1 9.4-22.6 9.4H43c-10 0-15-12.1-7.9-19.1l65.5-65.5C78.3 409.8 64 382.6 64 352V192c0-53 43-96 96-96h40V48H86.8zM160 160c-17.7 0-32 14.3-32 32v32c0 17.7 14.3 32 32 32H288c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32H160zm32 192c0-17.7-14.3-32-32-32s-32 14.3-32 32s14.3 32 32 32s32-14.3 32-32zm96 32c17.7 0 32-14.3 32-32s-14.3-32-32-32s-32 14.3-32 32s14.3 32 32 32z"></path>
</svg>
</span></td>
<td class="gt_row gt_left">Paris 14th</td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Saint-Denis—Porte de Paris</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;">
<svg viewbox="0 0 448 512" preserveaspectratio="none" aria-hidden="true" role="img" class="fa" style="fill-opacity:None;stroke-width:1px;stroke-opacity:None;height:1em;width:0.88em;position:relative;vertical-align:-0.125em;overflow:visible;">
<path d="M96 0C43 0 0 43 0 96V352c0 48 35.2 87.7 81.1 94.9l-46 46C28.1 499.9 33.1 512 43 512H82.7c8.5 0 16.6-3.4 22.6-9.4L160 448H288l54.6 54.6c6 6 14.1 9.4 22.6 9.4H405c10 0 15-12.1 7.9-19.1l-46-46c46-7.1 81.1-46.9 81.1-94.9V96c0-53-43-96-96-96H96zM64 96c0-17.7 14.3-32 32-32H352c17.7 0 32 14.3 32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V96zM224 384c-26.5 0-48-21.5-48-48s21.5-48 48-48s48 21.5 48 48s-21.5 48-48 48z"></path>
</svg>
/
<svg viewbox="0 0 448 512" preserveaspectratio="none" aria-hidden="true" role="img" class="fa" style="fill-opacity:None;stroke-width:1px;stroke-opacity:None;height:1em;width:0.88em;position:relative;vertical-align:-0.125em;overflow:visible;">
<path d="M86.8 48c-12.2 0-23.6 5.5-31.2 15L42.7 79C34.5 89.3 19.4 91 9 82.7S-3 59.4 5.3 49L18 33C34.7 12.2 60 0 86.8 0H361.2c26.7 0 52 12.2 68.7 33l12.8 16c8.3 10.4 6.6 25.5-3.7 33.7s-25.5 6.6-33.7-3.7L392.5 63c-7.6-9.5-19.1-15-31.2-15H248V96h40c53 0 96 43 96 96V352c0 30.6-14.3 57.8-36.6 75.4l65.5 65.5c7.1 7.1 2.1 19.1-7.9 19.1H365.3c-8.5 0-16.6-3.4-22.6-9.4L288 448H160l-54.6 54.6c-6 6-14.1 9.4-22.6 9.4H43c-10 0-15-12.1-7.9-19.1l65.5-65.5C78.3 409.8 64 382.6 64 352V192c0-53 43-96 96-96h40V48H86.8zM160 160c-17.7 0-32 14.3-32 32v32c0 17.7 14.3 32 32 32H288c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32H160zm32 192c0-17.7-14.3-32-32-32s-32 14.3-32 32s14.3 32 32 32s32-14.3 32-32zm96 32c17.7 0 32-14.3 32-32s-14.3-32-32-32s-32 14.3-32 32s14.3 32 32 32z"></path>
</svg>
</span></td>
<td class="gt_row gt_left gt_striped">Saint-Denis</td>
</tr>
<tr>
<td class="gt_row gt_left">Saint-Denis—Université</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;">
<svg viewbox="0 0 448 512" preserveaspectratio="none" aria-hidden="true" role="img" class="fa" style="fill-opacity:None;stroke-width:1px;stroke-opacity:None;height:1em;width:0.88em;position:relative;vertical-align:-0.125em;overflow:visible;">
<path d="M96 0C43 0 0 43 0 96V352c0 48 35.2 87.7 81.1 94.9l-46 46C28.1 499.9 33.1 512 43 512H82.7c8.5 0 16.6-3.4 22.6-9.4L160 448H288l54.6 54.6c6 6 14.1 9.4 22.6 9.4H405c10 0 15-12.1 7.9-19.1l-46-46c46-7.1 81.1-46.9 81.1-94.9V96c0-53-43-96-96-96H96zM64 96c0-17.7 14.3-32 32-32H352c17.7 0 32 14.3 32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V96zM224 384c-26.5 0-48-21.5-48-48s21.5-48 48-48s48 21.5 48 48s-21.5 48-48 48z"></path>
</svg>
/
<svg viewbox="0 0 448 512" preserveaspectratio="none" aria-hidden="true" role="img" class="fa" style="fill-opacity:None;stroke-width:1px;stroke-opacity:None;height:1em;width:0.88em;position:relative;vertical-align:-0.125em;overflow:visible;">
<path d="M86.8 48c-12.2 0-23.6 5.5-31.2 15L42.7 79C34.5 89.3 19.4 91 9 82.7S-3 59.4 5.3 49L18 33C34.7 12.2 60 0 86.8 0H361.2c26.7 0 52 12.2 68.7 33l12.8 16c8.3 10.4 6.6 25.5-3.7 33.7s-25.5 6.6-33.7-3.7L392.5 63c-7.6-9.5-19.1-15-31.2-15H248V96h40c53 0 96 43 96 96V352c0 30.6-14.3 57.8-36.6 75.4l65.5 65.5c7.1 7.1 2.1 19.1-7.9 19.1H365.3c-8.5 0-16.6-3.4-22.6-9.4L288 448H160l-54.6 54.6c-6 6-14.1 9.4-22.6 9.4H43c-10 0-15-12.1-7.9-19.1l65.5-65.5C78.3 409.8 64 382.6 64 352V192c0-53 43-96 96-96h40V48H86.8zM160 160c-17.7 0-32 14.3-32 32v32c0 17.7 14.3 32 32 32H288c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32H160zm32 192c0-17.7-14.3-32-32-32s-32 14.3-32 32s14.3 32 32 32s32-14.3 32-32zm96 32c17.7 0 32-14.3 32-32s-14.3-32-32-32s-32 14.3-32 32s14.3 32 32 32z"></path>
</svg>
</span></td>
<td class="gt_row gt_left">Saint-Denis</td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Saint-François-Xavier</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;">
<svg viewbox="0 0 448 512" preserveaspectratio="none" aria-hidden="true" role="img" class="fa" style="fill-opacity:None;stroke-width:1px;stroke-opacity:None;height:1em;width:0.88em;position:relative;vertical-align:-0.125em;overflow:visible;">
<path d="M96 0C43 0 0 43 0 96V352c0 48 35.2 87.7 81.1 94.9l-46 46C28.1 499.9 33.1 512 43 512H82.7c8.5 0 16.6-3.4 22.6-9.4L160 448H288l54.6 54.6c6 6 14.1 9.4 22.6 9.4H405c10 0 15-12.1 7.9-19.1l-46-46c46-7.1 81.1-46.9 81.1-94.9V96c0-53-43-96-96-96H96zM64 96c0-17.7 14.3-32 32-32H352c17.7 0 32 14.3 32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V96zM224 384c-26.5 0-48-21.5-48-48s21.5-48 48-48s48 21.5 48 48s-21.5 48-48 48z"></path>
</svg>
</span></td>
<td class="gt_row gt_left gt_striped">Paris 7th</td>
</tr>
<tr>
<td class="gt_row gt_left">Varenne</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;">
<svg viewbox="0 0 448 512" preserveaspectratio="none" aria-hidden="true" role="img" class="fa" style="fill-opacity:None;stroke-width:1px;stroke-opacity:None;height:1em;width:0.88em;position:relative;vertical-align:-0.125em;overflow:visible;">
<path d="M96 0C43 0 0 43 0 96V352c0 48 35.2 87.7 81.1 94.9l-46 46C28.1 499.9 33.1 512 43 512H82.7c8.5 0 16.6-3.4 22.6-9.4L160 448H288l54.6 54.6c6 6 14.1 9.4 22.6 9.4H405c10 0 15-12.1 7.9-19.1l-46-46c46-7.1 81.1-46.9 81.1-94.9V96c0-53-43-96-96-96H96zM64 96c0-17.7 14.3-32 32-32H352c17.7 0 32 14.3 32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V96zM224 384c-26.5 0-48-21.5-48-48s21.5-48 48-48s48 21.5 48 48s-21.5 48-48 48z"></path>
</svg>
</span></td>
<td class="gt_row gt_left">Paris 7th</td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Bibliothèque François Mitterrand</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;">
<svg viewbox="0 0 448 512" preserveaspectratio="none" aria-hidden="true" role="img" class="fa" style="fill-opacity:None;stroke-width:1px;stroke-opacity:None;height:1em;width:0.88em;position:relative;vertical-align:-0.125em;overflow:visible;">
<path d="M96 0C43 0 0 43 0 96V352c0 48 35.2 87.7 81.1 94.9l-46 46C28.1 499.9 33.1 512 43 512H82.7c8.5 0 16.6-3.4 22.6-9.4L160 448H288l54.6 54.6c6 6 14.1 9.4 22.6 9.4H405c10 0 15-12.1 7.9-19.1l-46-46c46-7.1 81.1-46.9 81.1-94.9V96c0-53-43-96-96-96H96zM64 96c0-17.7 14.3-32 32-32H352c17.7 0 32 14.3 32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V96zM224 384c-26.5 0-48-21.5-48-48s21.5-48 48-48s48 21.5 48 48s-21.5 48-48 48z"></path>
</svg>
/
<svg viewbox="0 0 448 512" preserveaspectratio="none" aria-hidden="true" role="img" class="fa" style="fill-opacity:None;stroke-width:1px;stroke-opacity:None;height:1em;width:0.88em;position:relative;vertical-align:-0.125em;overflow:visible;">
<path d="M86.8 48c-12.2 0-23.6 5.5-31.2 15L42.7 79C34.5 89.3 19.4 91 9 82.7S-3 59.4 5.3 49L18 33C34.7 12.2 60 0 86.8 0H361.2c26.7 0 52 12.2 68.7 33l12.8 16c8.3 10.4 6.6 25.5-3.7 33.7s-25.5 6.6-33.7-3.7L392.5 63c-7.6-9.5-19.1-15-31.2-15H248V96h40c53 0 96 43 96 96V352c0 30.6-14.3 57.8-36.6 75.4l65.5 65.5c7.1 7.1 2.1 19.1-7.9 19.1H365.3c-8.5 0-16.6-3.4-22.6-9.4L288 448H160l-54.6 54.6c-6 6-14.1 9.4-22.6 9.4H43c-10 0-15-12.1-7.9-19.1l65.5-65.5C78.3 409.8 64 382.6 64 352V192c0-53 43-96 96-96h40V48H86.8zM160 160c-17.7 0-32 14.3-32 32v32c0 17.7 14.3 32 32 32H288c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32H160zm32 192c0-17.7-14.3-32-32-32s-32 14.3-32 32s14.3 32 32 32s32-14.3 32-32zm96 32c17.7 0 32-14.3 32-32s-14.3-32-32-32s-32 14.3-32 32s14.3 32 32 32z"></path>
</svg>
</span></td>
<td class="gt_row gt_left gt_striped">Paris 13th</td>
</tr>
<tr>
<td class="gt_row gt_left">Cour Saint-Émilion</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;">
<svg viewbox="0 0 448 512" preserveaspectratio="none" aria-hidden="true" role="img" class="fa" style="fill-opacity:None;stroke-width:1px;stroke-opacity:None;height:1em;width:0.88em;position:relative;vertical-align:-0.125em;overflow:visible;">
<path d="M96 0C43 0 0 43 0 96V352c0 48 35.2 87.7 81.1 94.9l-46 46C28.1 499.9 33.1 512 43 512H82.7c8.5 0 16.6-3.4 22.6-9.4L160 448H288l54.6 54.6c6 6 14.1 9.4 22.6 9.4H405c10 0 15-12.1 7.9-19.1l-46-46c46-7.1 81.1-46.9 81.1-94.9V96c0-53-43-96-96-96H96zM64 96c0-17.7 14.3-32 32-32H352c17.7 0 32 14.3 32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V96zM224 384c-26.5 0-48-21.5-48-48s21.5-48 48-48s48 21.5 48 48s-21.5 48-48 48z"></path>
</svg>
</span></td>
<td class="gt_row gt_left">Paris 12th</td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Olympiades</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;">
<svg viewbox="0 0 448 512" preserveaspectratio="none" aria-hidden="true" role="img" class="fa" style="fill-opacity:None;stroke-width:1px;stroke-opacity:None;height:1em;width:0.88em;position:relative;vertical-align:-0.125em;overflow:visible;">
<path d="M96 0C43 0 0 43 0 96V352c0 48 35.2 87.7 81.1 94.9l-46 46C28.1 499.9 33.1 512 43 512H82.7c8.5 0 16.6-3.4 22.6-9.4L160 448H288l54.6 54.6c6 6 14.1 9.4 22.6 9.4H405c10 0 15-12.1 7.9-19.1l-46-46c46-7.1 81.1-46.9 81.1-94.9V96c0-53-43-96-96-96H96zM64 96c0-17.7 14.3-32 32-32H352c17.7 0 32 14.3 32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V96zM224 384c-26.5 0-48-21.5-48-48s21.5-48 48-48s48 21.5 48 48s-21.5 48-48 48z"></path>
</svg>
</span></td>
<td class="gt_row gt_left gt_striped">Paris 13th</td>
</tr>
<tr>
<td class="gt_row gt_left">Pont Cardinet</td>
<td class="gt_row gt_left"><span style="white-space:nowrap;">
<svg viewbox="0 0 448 512" preserveaspectratio="none" aria-hidden="true" role="img" class="fa" style="fill-opacity:None;stroke-width:1px;stroke-opacity:None;height:1em;width:0.88em;position:relative;vertical-align:-0.125em;overflow:visible;">
<path d="M96 0C43 0 0 43 0 96V352c0 48 35.2 87.7 81.1 94.9l-46 46C28.1 499.9 33.1 512 43 512H82.7c8.5 0 16.6-3.4 22.6-9.4L160 448H288l54.6 54.6c6 6 14.1 9.4 22.6 9.4H405c10 0 15-12.1 7.9-19.1l-46-46c46-7.1 81.1-46.9 81.1-94.9V96c0-53-43-96-96-96H96zM64 96c0-17.7 14.3-32 32-32H352c17.7 0 32 14.3 32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V96zM224 384c-26.5 0-48-21.5-48-48s21.5-48 48-48s48 21.5 48 48s-21.5 48-48 48z"></path>
</svg>
</span></td>
<td class="gt_row gt_left">Paris 17th</td>
</tr>
<tr>
<td class="gt_row gt_left gt_striped">Saint-Ouen</td>
<td class="gt_row gt_left gt_striped"><span style="white-space:nowrap;">
<svg viewbox="0 0 448 512" preserveaspectratio="none" aria-hidden="true" role="img" class="fa" style="fill-opacity:None;stroke-width:1px;stroke-opacity:None;height:1em;width:0.88em;position:relative;vertical-align:-0.125em;overflow:visible;">
<path d="M96 0C43 0 0 43 0 96V352c0 48 35.2 87.7 81.1 94.9l-46 46C28.1 499.9 33.1 512 43 512H82.7c8.5 0 16.6-3.4 22.6-9.4L160 448H288l54.6 54.6c6 6 14.1 9.4 22.6 9.4H405c10 0 15-12.1 7.9-19.1l-46-46c46-7.1 81.1-46.9 81.1-94.9V96c0-53-43-96-96-96H96zM64 96c0-17.7 14.3-32 32-32H352c17.7 0 32 14.3 32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V96zM224 384c-26.5 0-48-21.5-48-48s21.5-48 48-48s48 21.5 48 48s-21.5 48-48 48z"></path>
</svg>
</span></td>
<td class="gt_row gt_left gt_striped">Clichy, Saint-Ouen-sur-Seine</td>
</tr>
</tbody>
</table>

</div>

In the code, we added in the icon names `"train"` and `"train-tram"` to the `services` column, and there could either be just the train icon or the pair that includes the tramway service. We wanted a little separation between the icons in the latter case, so `sep=" / "` was used to place a slash with spacing between any pair of icons. The icons appear here with a black fill color, but that can be changed with the `fill_color=` argument (and there are several other arguments for controlling style attributes).

For a list of available icons, their names, and what they look like, check out [this listing on the Font Awesome website](https://fontawesome.com/search?m=free&o=r). The icons draw from the Font Awesome 'free' set (2000+ icons in total) but are not obtained via the web. Rather, we use the [faicons library](https://pypi.org/project/faicons/) so that this can be done entirely offline (directly using the SVG icons stored within faicons).

### Accounting notation in select numeric formatting methods

For certain types of tables, it may be preferable to use accounting notation for numerical figures. This type of notation renders negative values in parentheses while omitting the minus sign. This is often seen for monetary and percentage figures but it's also sensible for plain numbers in the right context. We've added support for accounting notation in four formatting methods:

- `fmt_number()`
- `fmt_integer()`
- `fmt_currency()`
- `fmt_percent()`

Here's a comprehensive example table that demonstrates how this type of formatting looks.

<details class="code-fold">
<summary>Show the code</summary>

``` python
from great_tables import GT
import polars as pl

df = pl.DataFrame({
    "number_type": ["negative", "positive"],
    "number": [-1.2, 23.6],
    "integer": [-2323, 23213],
    "currency": [-24334.23, 7323.253],
    "percent": [-0.0523, 0.363]
    }
).with_columns(
    number_acc = pl.col("number"),
    integer_acc = pl.col("integer"),
    currency_acc = pl.col("currency"),
    percent_acc = pl.col("percent")
)

(
    GT(df, rowname_col="number_type")
    .fmt_number(columns="number")
    .fmt_percent(columns="percent")
    .fmt_integer(columns="integer")
    .fmt_currency(columns="currency")
    .fmt_number(columns="number_acc", accounting=True)
    .fmt_percent(columns="percent_acc", accounting=True)
    .fmt_integer(columns="integer_acc", accounting=True)
    .fmt_currency(columns="currency_acc", accounting=True)
    .tab_spanner(label="default formatting", columns=[1, 2, 3, 4])
    .tab_spanner(label="with accounting notation", columns=[5, 6, 7, 8])
    .cols_label(
        number_acc="number",
        integer_acc="integer",
        currency_acc="currency",
        percent_acc="percent"
    )
)
```

</details>
<div id="mcjjfgubcc" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#mcjjfgubcc table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#mcjjfgubcc thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#mcjjfgubcc p { margin: 0; padding: 0; }
 #mcjjfgubcc .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #mcjjfgubcc .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #mcjjfgubcc .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #mcjjfgubcc .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #mcjjfgubcc .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mcjjfgubcc .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mcjjfgubcc .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #mcjjfgubcc .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #mcjjfgubcc .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #mcjjfgubcc .gt_column_spanner_outer:first-child { padding-left: 0; }
 #mcjjfgubcc .gt_column_spanner_outer:last-child { padding-right: 0; }
 #mcjjfgubcc .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #mcjjfgubcc .gt_spanner_row { border-bottom-style: hidden; }
 #mcjjfgubcc .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #mcjjfgubcc .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #mcjjfgubcc .gt_from_md> :first-child { margin-top: 0; }
 #mcjjfgubcc .gt_from_md> :last-child { margin-bottom: 0; }
 #mcjjfgubcc .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #mcjjfgubcc .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #mcjjfgubcc .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #mcjjfgubcc .gt_row_group_first td { border-top-width: 2px; }
 #mcjjfgubcc .gt_row_group_first th { border-top-width: 2px; }
 #mcjjfgubcc .gt_striped { color: #333333; background-color: #F4F4F4; }
 #mcjjfgubcc .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #mcjjfgubcc .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #mcjjfgubcc .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #mcjjfgubcc .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #mcjjfgubcc .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #mcjjfgubcc .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #mcjjfgubcc .gt_left { text-align: left; }
 #mcjjfgubcc .gt_center { text-align: center; }
 #mcjjfgubcc .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #mcjjfgubcc .gt_font_normal { font-weight: normal; }
 #mcjjfgubcc .gt_font_bold { font-weight: bold; }
 #mcjjfgubcc .gt_font_italic { font-style: italic; }
 #mcjjfgubcc .gt_super { font-size: 65%; }
 #mcjjfgubcc .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #mcjjfgubcc .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th colspan="4" id="default-formatting" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" scope="colgroup"><span class="gt_column_spanner">default formatting</span></th>
<th colspan="4" id="with-accounting-notation" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" scope="colgroup"><span class="gt_column_spanner">with accounting notation</span></th>
</tr>
<tr class="gt_col_headings">
<th id="number" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">number</th>
<th id="integer" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">integer</th>
<th id="currency" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">currency</th>
<th id="percent" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">percent</th>
<th id="number_acc" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">number</th>
<th id="integer_acc" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">integer</th>
<th id="currency_acc" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">currency</th>
<th id="percent_acc" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">percent</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">negative</td>
<td class="gt_row gt_right">−1.20</td>
<td class="gt_row gt_right">−2,323</td>
<td class="gt_row gt_right">−$24,334.23</td>
<td class="gt_row gt_right">−5.23%</td>
<td class="gt_row gt_right">(1.20)</td>
<td class="gt_row gt_right">(2,323)</td>
<td class="gt_row gt_right">($24,334.23)</td>
<td class="gt_row gt_right">(5.23%)</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th">positive</td>
<td class="gt_row gt_right">23.60</td>
<td class="gt_row gt_right">23,213</td>
<td class="gt_row gt_right">$7,323.25</td>
<td class="gt_row gt_right">36.30%</td>
<td class="gt_row gt_right">23.60</td>
<td class="gt_row gt_right">23,213</td>
<td class="gt_row gt_right">$7,323.25</td>
<td class="gt_row gt_right">36.30%</td>
</tr>
</tbody>
</table>

</div>

For the formatting in the final four columns, we use `accounting=True` to get the values into accounting notation. This is only apparent for the negative values (first row) as the positive values won't change their appearance, looking the same as they do when `accounting=False` (the default).

### Acknowledgements and how to contact us

We are *very* grateful for the work that [Jerry Wu](https://github.com/jrycw) has done during this release, some of which includes:

- enhancing the `fmt_image()` to support `http`/`https` schema in the `columns=` parameter, and writing an [incredible blog post](https://posit-dev.github.io/great-tables/blog/rendering-images/) about incorporating images in your tables
- improving the `save()` method, giving it the ability to perform intermediate saves (since the method returns itself)
- adding the `pipe()` method, which operates similarly to that of the Pandas and Polars APIs
- all sorts of little QoL fixes

We extend our gratitude also to [Alessandro Molina](https://github.com/amol-) for adding experimental support for `pyarrow.Table` inputs in this release.

Finally, we thank [Luke Manley](https://github.com/lukemanley) and [Guillaume Lemaitre](https://github.com/glemaitre) for their first contributions to the project!

We're always happy to get feedback. There are three good ways to talk to us:

1.  [GitHub Issues](https://github.com/posit-dev/great-tables/issues)
2.  [GitHub Discussions](https://github.com/posit-dev/great-tables/discussions)
3.  [Discord](https://discord.com/invite/Ux7nrcXHVV)

Don't be shy. We love talking tables (and how we can make them better)!
