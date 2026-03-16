---
title: 'Great Tables `v0.2.0`: Easy Data Coloring'
people:
  - Rich Iannone
date: 2024-01-24T00:00:00.000Z
ported_from: great_tables
port_status: in-progress
---


<script src="https://cdn.jsdelivr.net/npm/requirejs@2.3.6/require.min.js" integrity="sha384-c9c+LnTbwQ3aujuU7ULEPVvgLs+Fn6fJUvIGTsuu1ZcCf11fiEubah0ttpca4ntM sha384-6V1/AdqZRWk1KAlWbKBlGhN7VG4iE/yAZcO6NZPMF8od0vukrvr0tg4qY6NSrItx" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js" integrity="sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/6Z/hRTt8+pR6L4N2" crossorigin="anonymous" data-relocate-top="true"></script>
<script type="application/javascript">define('jquery', [],function() {return window.jQuery;})</script>


We enjoy working on **Great Tables** because we want everybody to easily make beautiful tables. Tables don't have to be boring, they really could be captivating and insightful. With every release we get closer and closer to realizing our mission and, as such, we're happy to announce the `v0.2.0` release that's now on PyPI.

The really big feature that's available with this release is the `data_color()` method. It gives you several options for colorizing data cells based on the underlying data. The method automatically scales color values according to the data in order to emphasize differences or reveal trends. The example below emphasizes large currency values with a `"darkgreen"` fill color.

``` python
from great_tables import GT, exibble

(
    GT(exibble[["currency", "date", "row"]].head(4), rowname_col="row")
    .data_color(
        columns="currency",
        palette=["lightblue", "darkgreen"]
    )
)
```

<div id="vlzluwutbf" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#vlzluwutbf table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vlzluwutbf thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vlzluwutbf p { margin: 0; padding: 0; }
 #vlzluwutbf .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vlzluwutbf .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vlzluwutbf .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vlzluwutbf .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vlzluwutbf .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vlzluwutbf .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vlzluwutbf .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vlzluwutbf .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #vlzluwutbf .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vlzluwutbf .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vlzluwutbf .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vlzluwutbf .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vlzluwutbf .gt_spanner_row { border-bottom-style: hidden; }
 #vlzluwutbf .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vlzluwutbf .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vlzluwutbf .gt_from_md> :first-child { margin-top: 0; }
 #vlzluwutbf .gt_from_md> :last-child { margin-bottom: 0; }
 #vlzluwutbf .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vlzluwutbf .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #vlzluwutbf .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #vlzluwutbf .gt_row_group_first td { border-top-width: 2px; }
 #vlzluwutbf .gt_row_group_first th { border-top-width: 2px; }
 #vlzluwutbf .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vlzluwutbf .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vlzluwutbf .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vlzluwutbf .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vlzluwutbf .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vlzluwutbf .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vlzluwutbf .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #vlzluwutbf .gt_left { text-align: left; }
 #vlzluwutbf .gt_center { text-align: center; }
 #vlzluwutbf .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vlzluwutbf .gt_font_normal { font-weight: normal; }
 #vlzluwutbf .gt_font_bold { font-weight: bold; }
 #vlzluwutbf .gt_font_italic { font-style: italic; }
 #vlzluwutbf .gt_super { font-size: 65%; }
 #vlzluwutbf .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vlzluwutbf .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|       | currency | date       |
|-------|----------|------------|
| row_1 | 49.95    | 2015-01-15 |
| row_2 | 17.95    | 2015-02-15 |
| row_3 | 1.39     | 2015-03-15 |
| row_4 | 65100.0  | 2015-04-15 |

</div>

Note that we use `columns=` to specify which columns get the colorizing treatment (just `currency` here) and the `palette=` is given as a list of color values. From this we can see that the `65100.0` value polarizes the data coloring process; it is `"darkgreen"` while all other values are `"lightblue"` (with no interpolated colors in between). Also, isn't it nice that the text adapts to the background color?

The above example is suitable for emphasizing large values, but, maybe you consider the extreme value to be something that's out of bounds? For that, we can use the `domain=` and `na_value=` arguments to gray-out the extreme values. We'll also nicely format the `currency` column in this next example.

``` python
(
    GT(exibble[["currency", "date", "row"]].head(4), rowname_col="row")
    .data_color(
        columns="currency",
        palette=["lightblue", "darkgreen"],
        domain=[0, 50],
        na_color="lightgray"
    )
    .fmt_currency(
        columns="currency",
        currency="GBP",
        use_subunits=False
    )
)
```

<div id="pktdbjupvi" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#pktdbjupvi table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pktdbjupvi thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pktdbjupvi p { margin: 0; padding: 0; }
 #pktdbjupvi .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pktdbjupvi .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pktdbjupvi .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pktdbjupvi .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pktdbjupvi .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pktdbjupvi .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pktdbjupvi .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pktdbjupvi .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pktdbjupvi .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pktdbjupvi .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pktdbjupvi .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pktdbjupvi .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pktdbjupvi .gt_spanner_row { border-bottom-style: hidden; }
 #pktdbjupvi .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pktdbjupvi .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pktdbjupvi .gt_from_md> :first-child { margin-top: 0; }
 #pktdbjupvi .gt_from_md> :last-child { margin-bottom: 0; }
 #pktdbjupvi .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pktdbjupvi .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pktdbjupvi .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pktdbjupvi .gt_row_group_first td { border-top-width: 2px; }
 #pktdbjupvi .gt_row_group_first th { border-top-width: 2px; }
 #pktdbjupvi .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pktdbjupvi .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pktdbjupvi .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pktdbjupvi .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pktdbjupvi .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #pktdbjupvi .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pktdbjupvi .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pktdbjupvi .gt_left { text-align: left; }
 #pktdbjupvi .gt_center { text-align: center; }
 #pktdbjupvi .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pktdbjupvi .gt_font_normal { font-weight: normal; }
 #pktdbjupvi .gt_font_bold { font-weight: bold; }
 #pktdbjupvi .gt_font_italic { font-style: italic; }
 #pktdbjupvi .gt_super { font-size: 65%; }
 #pktdbjupvi .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pktdbjupvi .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

|       | currency | date       |
|-------|----------|------------|
| row_1 | £50      | 2015-01-15 |
| row_2 | £18      | 2015-02-15 |
| row_3 | £1       | 2015-03-15 |
| row_4 | £65,100  | 2015-04-15 |

</div>

Now the very large value is in `"lightgray"`, making all other values easier to compare. We did setting `domain=[0, 50]` and specifying `na_color="lightgray"`. This caused the out-of-bounds value of `65100` to have a light gray background. Notice that the values are also formatted as currencies, and this is thanks to `fmt_currency()` which never interferes with styling.

Here's a more inspirational example that uses a heavily-manipulated version of the `countrypops` dataset (thanks again, **Polars**!) along with a color treatment that's mediated by `data_color()`. Here, the population values can be easily compared by the amount of `"purple"` within them.

``` python
from great_tables.data import countrypops
import polars as pl
import polars.selectors as cs

wide_pops = (
    pl.from_pandas(countrypops)
    .filter(
        pl.col("country_code_2").is_in(["FM", "GU", "KI", "MH", "MP", "NR", "PW"])
        & pl.col("year").is_in([2000, 2010, 2020])
    )
    .pivot(index="country_name", on="year", values="population")
    .sort("2020", descending=True)
)

(
    GT(wide_pops, rowname_col="country_name")
    .tab_header(
        title="Populations of Select Countries in Oceania",
        subtitle="Population values are from 2000, 2010, and 2020.",
    )
    .tab_spanner(label="Total Population", columns=cs.all())
    .fmt_integer(columns=["2000", "2010", "2020"])
    .data_color(palette=["white", "purple"], domain=[0, 1.7e5])
)
```

<div id="xsjsldoicj" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#xsjsldoicj table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#xsjsldoicj thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#xsjsldoicj p { margin: 0; padding: 0; }
 #xsjsldoicj .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #xsjsldoicj .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #xsjsldoicj .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #xsjsldoicj .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #xsjsldoicj .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xsjsldoicj .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xsjsldoicj .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #xsjsldoicj .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #xsjsldoicj .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #xsjsldoicj .gt_column_spanner_outer:first-child { padding-left: 0; }
 #xsjsldoicj .gt_column_spanner_outer:last-child { padding-right: 0; }
 #xsjsldoicj .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #xsjsldoicj .gt_spanner_row { border-bottom-style: hidden; }
 #xsjsldoicj .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #xsjsldoicj .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #xsjsldoicj .gt_from_md> :first-child { margin-top: 0; }
 #xsjsldoicj .gt_from_md> :last-child { margin-bottom: 0; }
 #xsjsldoicj .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #xsjsldoicj .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #xsjsldoicj .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #xsjsldoicj .gt_row_group_first td { border-top-width: 2px; }
 #xsjsldoicj .gt_row_group_first th { border-top-width: 2px; }
 #xsjsldoicj .gt_striped { color: #333333; background-color: #F4F4F4; }
 #xsjsldoicj .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #xsjsldoicj .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #xsjsldoicj .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #xsjsldoicj .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #xsjsldoicj .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #xsjsldoicj .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #xsjsldoicj .gt_left { text-align: left; }
 #xsjsldoicj .gt_center { text-align: center; }
 #xsjsldoicj .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #xsjsldoicj .gt_font_normal { font-weight: normal; }
 #xsjsldoicj .gt_font_bold { font-weight: bold; }
 #xsjsldoicj .gt_font_italic { font-style: italic; }
 #xsjsldoicj .gt_super { font-size: 65%; }
 #xsjsldoicj .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #xsjsldoicj .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

<table class="gt_table" data-quarto-postprocess="true" data-quarto-disable-processing="false" data-quarto-bootstrap="false">
<thead>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_title gt_font_normal">Populations of Select Countries in Oceania</th>
</tr>
<tr class="gt_heading">
<th colspan="4" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border">Population values are from 2000, 2010, and 2020.</th>
</tr>
<tr class="gt_col_headings gt_spanner_row">
<th rowspan="2" class="gt_col_heading gt_columns_bottom_border gt_left" data-quarto-table-cell-role="th" scope="col"></th>
<th colspan="3" id="Total-Population" class="gt_center gt_columns_top_border gt_column_spanner_outer" data-quarto-table-cell-role="th" scope="colgroup"><span class="gt_column_spanner">Total Population</span></th>
</tr>
<tr class="gt_col_headings">
<th id="2000" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">2000</th>
<th id="2010" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">2010</th>
<th id="2020" class="gt_col_heading gt_columns_bottom_border gt_right" data-quarto-table-cell-role="th" scope="col">2020</th>
</tr>
</thead>
<tbody class="gt_table_body">
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">Guam</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a52df1">160,188</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a327f0">164,905</td>
<td class="gt_row gt_right" style="color: #FFFFFF; background-color: #a021f0">169,231</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">Kiribati</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #cd8af7">88,826</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c371f5">107,995</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #b859f4">126,463</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">Micronesia (Federated States)</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c16cf5">111,709</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c372f6">107,588</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #c06cf5">112,106</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">Northern Mariana Islands</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #d296f8">80,338</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e1b8fa">54,087</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e3befb">49,587</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">Marshall Islands</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e1b8fa">54,224</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e1b9fa">53,416</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #e7c6fb">43,413</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">Palau</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f4e5fd">19,726</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f5e7fd">18,540</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f5e7fd">17,972</td>
</tr>
<tr>
<td class="gt_row gt_left gt_stub" data-quarto-table-cell-role="th" style="color: #000000; background-color: #808080">Nauru</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f9f1fe">10,377</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f9f2fe">10,241</td>
<td class="gt_row gt_right" style="color: #000000; background-color: #f8effe">12,315</td>
</tr>
</tbody>
</table>

</div>

This was just a sampler of what you can do with the all-new `data_color()` method. Take a look at these pages for more information:

- The [*Colorizing with Data*](https://posit-dev.github.io/great-tables/get-started/colorizing-with-data.html) page in the *Get Started* Guide, which provides more details on how to use `data_color()`
- The guide on [Basic Styling](https://posit-dev.github.io/great-tables/get-started/basic-styling.html) covers general styling (e.g., bold text, underlines, etc.) with `tab_style()`
- The reference pages for [`data_color()`](https://posit-dev.github.io/great-tables/reference/GT.data_color.html) and [`tab_style()`](https://posit-dev.github.io/great-tables/reference/GT.tab_style.html)

To conclude, we're happy that this new functionality is now in the **Great Tables** package! We hope you find it useful for your table-generation work. And we'll keep improving upon it so that you'll have more possibilities to make beautiful, and colorful, tables for presentation.
