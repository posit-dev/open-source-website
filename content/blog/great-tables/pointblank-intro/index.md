---
title: How We Used Great Tables to Supercharge Reporting in Pointblank
people:
  - Rich Iannone
date: 2025-02-11T00:00:00.000Z
ported_from: great_tables
port_status: in-progress
---


<script src="https://cdn.jsdelivr.net/npm/requirejs@2.3.6/require.min.js" integrity="sha384-c9c+LnTbwQ3aujuU7ULEPVvgLs+Fn6fJUvIGTsuu1ZcCf11fiEubah0ttpca4ntM sha384-6V1/AdqZRWk1KAlWbKBlGhN7VG4iE/yAZcO6NZPMF8od0vukrvr0tg4qY6NSrItx" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js" integrity="sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/6Z/hRTt8+pR6L4N2" crossorigin="anonymous" data-relocate-top="true"></script>
<script type="application/javascript">define('jquery', [],function() {return window.jQuery;})</script>


The Great Tables package allows you to make tables, and they're really great when part of a report, a book, or a web page. The API is meant to be easy to work with so DataFrames could be made into publication-quality tables without a lot of hassle. And having nice-looking tables in the mix elevates the quality of the medium you're working in.

We were inspired by this and decided to explore what it could mean to introduce a package where reporting is largely in the form of beautiful tables. To this end, we started work on a new Python package that generates tables (c/o Great Tables) as reporting objects. This package is called [Pointblank](https://github.com/posit-dev/pointblank), its focus is that of data validation, and the reporting tables it can produce informs users on the results of a data validation workflow. In this post we'll go through how Pointblank:

- enables you to validate many types of DataFrames and SQL databases
- provides easy-to-understand validation result tables and thorough drilldowns
- gives you nice previews of data tables across a range of backends

### Validating data with Pointblank

Just like Great Tables, Pointblank's primary input is a table and the goal of that library is to perform checks of the tabular data. Other libraries in this domain include [Great Expectations](https://github.com/great-expectations/great_expectations), [pandera](https://github.com/unionai-oss/pandera), [Soda](https://github.com/sodadata/soda-core?tab=readme-ov-file), and [PyDeequ](https://github.com/awslabs/python-deequ).

Below is the main validation report table that users are likely to see quite often. Each row is a validation step, with columns reporting details about each step and their results.

<details class="code-fold">
<summary>Show the code</summary>

``` python
import pointblank as pb

validation = (
    pb.Validate(
        data=pb.load_dataset(dataset="small_table", tbl_type="polars"),
        label="An example validation",
        thresholds=(0.1, 0.2, 0.5),
    )
    .col_vals_gt(columns="d", value=1000)
    .col_vals_le(columns="c", value=5)
    .col_exists(columns=["date", "date_time"])
    .interrogate()
)

validation
```

</details>

    /Users/charlottewickham/Documents/posit/open-source-website/content/blog/great-tables/pointblank-intro/.venv/lib/python3.13/site-packages/pointblank/column.py:990: SyntaxWarning: invalid escape sequence '\d'
      """
    /Users/charlottewickham/Documents/posit/open-source-website/content/blog/great-tables/pointblank-intro/.venv/lib/python3.13/site-packages/pointblank/thresholds.py:295: SyntaxWarning: invalid escape sequence '\d'
      """
    /Users/charlottewickham/Documents/posit/open-source-website/content/blog/great-tables/pointblank-intro/.venv/lib/python3.13/site-packages/pointblank/validate.py:112: SyntaxWarning: invalid escape sequence '\d'
      """Access step-level metadata when authoring custom actions.
    /Users/charlottewickham/Documents/posit/open-source-website/content/blog/great-tables/pointblank-intro/.venv/lib/python3.13/site-packages/pointblank/validate.py:8866: SyntaxWarning: invalid escape sequence '\d'
      """

<div id="pb_tbl" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
#pb_tbl table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pb_tbl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pb_tbl p { margin: 0; padding: 0; }
 #pb_tbl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 90%; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pb_tbl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pb_tbl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pb_tbl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pb_tbl .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pb_tbl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pb_tbl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pb_tbl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pb_tbl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pb_tbl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pb_tbl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pb_tbl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pb_tbl .gt_spanner_row { border-bottom-style: hidden; }
 #pb_tbl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pb_tbl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pb_tbl .gt_from_md> :first-child { margin-top: 0; }
 #pb_tbl .gt_from_md> :last-child { margin-bottom: 0; }
 #pb_tbl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #pb_tbl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pb_tbl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pb_tbl .gt_row_group_first td { border-top-width: 2px; }
 #pb_tbl .gt_row_group_first th { border-top-width: 2px; }
 #pb_tbl .gt_striped { background-color: rgba(128,128,128,0.05); }
 #pb_tbl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pb_tbl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pb_tbl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pb_tbl .gt_left { text-align: left; }
 #pb_tbl .gt_center { text-align: center; }
 #pb_tbl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pb_tbl .gt_font_normal { font-weight: normal; }
 #pb_tbl .gt_font_bold { font-weight: bold; }
 #pb_tbl .gt_font_italic { font-style: italic; }
 #pb_tbl .gt_super { font-size: 65%; }
 #pb_tbl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pb_tbl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>
<table style="table-layout: fixed;; width: 0px" class="gt_table" data-quarto-disable-processing="true" data-quarto-bootstrap="false">
<colgroup>
  <col style="width:4px;"/>
  <col style="width:35px;"/>
  <col style="width:190px;"/>
  <col style="width:120px;"/>
  <col style="width:120px;"/>
  <col style="width:50px;"/>
  <col style="width:50px;"/>
  <col style="width:60px;"/>
  <col style="width:60px;"/>
  <col style="width:60px;"/>
  <col style="width:30px;"/>
  <col style="width:30px;"/>
  <col style="width:30px;"/>
  <col style="width:65px;"/>
</colgroup>

<thead>

  <tr class="gt_heading">
    <td colspan="14" class="gt_heading gt_title gt_font_normal" style="color: #444444;font-size: 28px;text-align: left;font-weight: bold;">Pointblank Validation</td>
  </tr>
  <tr class="gt_heading">
    <td colspan="14" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border"><div><span style='text-decoration-style: solid; text-decoration-color: #ADD8E6; text-decoration-line: underline; text-underline-position: under; color: #333333; font-variant-numeric: tabular-nums; padding-left: 4px; margin-right: 5px; padding-right: 2px;'>An example validation</span><div style="padding-top: 10px; padding-bottom: 5px;"><span style='background-color: #0075FF; color: #FFFFFF; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin: 5px 10px 5px 0px; border: solid 1px #0075FF; font-weight: bold; padding: 2px 10px 2px 10px; font-size: 10px;'>Polars</span><span><span style="background-color: #AAAAAA; color: white; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin: 5px 0px 5px 5px; border: solid 1px #AAAAAA; font-weight: bold; padding: 2px 15px 2px 15px; font-size: smaller;">WARNING</span><span style="background-color: none; color: #333333; padding: 0.5em 0.5em; position: inherit; margin: 5px 0px 5px -4px; font-weight: bold; border: solid 1px #AAAAAA; padding: 2px 15px 2px 15px; font-size: smaller; margin-right: 5px;">0.1</span><span style="background-color: #EBBC14; color: white; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin: 5px 0px 5px 1px; border: solid 1px #EBBC14; font-weight: bold; padding: 2px 15px 2px 15px; font-size: smaller;">ERROR</span><span style="background-color: none; color: #333333; padding: 0.5em 0.5em; position: inherit; margin: 5px 0px 5px -4px; font-weight: bold; border: solid 1px #EBBC14; padding: 2px 15px 2px 15px; font-size: smaller; margin-right: 5px;">0.2</span><span style="background-color: #FF3300; color: white; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin: 5px 0px 5px 1px; border: solid 1px #FF3300; font-weight: bold; padding: 2px 15px 2px 15px; font-size: smaller;">CRITICAL</span><span style="background-color: none; color: #333333; padding: 0.5em 0.5em; position: inherit; margin: 5px 0px 5px -4px; font-weight: bold; border: solid 1px #FF3300; padding: 2px 15px 2px 15px; font-size: smaller;">0.5</span></span></div></div></td>
  </tr>
<tr class="gt_col_headings">
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" style="color: #666666;font-weight: bold;" scope="col" id="pb_tbl-status_color"></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: #666666;font-weight: bold;" scope="col" id="pb_tbl-i"></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" style="color: #666666;font-weight: bold;" scope="col" id="pb_tbl-type_upd">STEP</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" style="color: #666666;font-weight: bold;" scope="col" id="pb_tbl-columns_upd">COLUMNS</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" style="color: #666666;font-weight: bold;" scope="col" id="pb_tbl-values_upd">VALUES</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_center" rowspan="1" colspan="1" style="color: #666666;font-weight: bold;" scope="col" id="pb_tbl-tbl">TBL</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_center" rowspan="1" colspan="1" style="color: #666666;font-weight: bold;" scope="col" id="pb_tbl-eval">EVAL</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: #666666;font-weight: bold;" scope="col" id="pb_tbl-test_units">UNITS</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: #666666;font-weight: bold;" scope="col" id="pb_tbl-pass">PASS</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: #666666;font-weight: bold;" scope="col" id="pb_tbl-fail">FAIL</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_center" rowspan="1" colspan="1" style="color: #666666;font-weight: bold;" scope="col" id="pb_tbl-w_upd">W</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_center" rowspan="1" colspan="1" style="color: #666666;font-weight: bold;" scope="col" id="pb_tbl-e_upd">E</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_center" rowspan="1" colspan="1" style="color: #666666;font-weight: bold;" scope="col" id="pb_tbl-c_upd">C</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_center" rowspan="1" colspan="1" style="color: #666666;font-weight: bold;" scope="col" id="pb_tbl-extract_upd">EXT</th>
</tr>
</thead>
<tbody class="gt_table_body">
  <tr>
    <td style="height: 40px; background-color: #EBBC14; color: transparent;font-size: 0px;" class="gt_row gt_left">#EBBC14</td>
    <td style="height: 40px; color: #666666;font-size: 13px;font-weight: bold;" class="gt_row gt_right">1</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_left">
        <div style="margin: 0; padding: 0; display: inline-block; height: 30px; vertical-align: middle; width: 16%;">
            <!--?xml version="1.0" encoding="UTF-8"?--><?xml version="1.0" encoding="UTF-8"?>
<svg width="30px" height="30px" viewBox="0 0 67 67" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <title>col_vals_gt</title>
    <g id="All-Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="col_vals_gt" transform="translate(0.000000, 0.724138)">
            <path d="M56.712234,1 C59.1975153,1 61.4475153,2.00735931 63.076195,3.63603897 C64.7048747,5.26471863 65.712234,7.51471863 65.712234,10 L65.712234,10 L65.712234,65 L10.712234,65 C8.22695259,65 5.97695259,63.9926407 4.34827294,62.363961 C2.71959328,60.7352814 1.71223397,58.4852814 1.71223397,56 L1.71223397,56 L1.71223397,10 C1.71223397,7.51471863 2.71959328,5.26471863 4.34827294,3.63603897 C5.97695259,2.00735931 8.22695259,1 10.712234,1 L10.712234,1 Z" id="rectangle" stroke="#000000" stroke-width="2" fill="#FFFFFF"></path>
            <path d="M49.7099609,12 L17.7099609,12 C14.9499609,12 12.7099609,14.24 12.7099609,17 L12.7099609,49 C12.7099609,51.76 14.9499609,54 17.7099609,54 L49.7099609,54 C52.4699609,54 54.7099609,51.76 54.7099609,49 L54.7099609,17 C54.7099609,14.24 52.4699609,12 49.7099609,12 Z M27.2799609,44.82 L26.1399609,43.18 L40.9499609,33 L26.1399609,22.82 L27.2799609,21.18 L44.4799609,33 L27.2799609,44.82 Z" id="greater_than" fill="#000000" fill-rule="nonzero"></path>
        </g>
    </g>
</svg>
        </div>
        <div style="font-family: 'IBM Plex Mono', monospace, courier; color: black; font-size: 11px; display: inline-block; vertical-align: middle;">
            <div>col_vals_gt()</div>
        </div>
        
        </td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">d</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">1000</td>
    <td style="height: 40px; background-color: #FCFCFC; border-left: 1px solid #D3D3D3;" class="gt_row gt_center"><svg width="25px" height="25px" viewBox="0 0 25 25" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="vertical-align: middle;">
    <g id="unchanged" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="unchanged" transform="translate(0.500000, 0.570147)">
            <rect id="Rectangle" x="0.125132506" y="0" width="23.749735" height="23.7894737"></rect>
            <path d="M5.80375046,8.18194736 C3.77191832,8.18194736 2.11875046,9.83495328 2.11875046,11.8669474 C2.11875046,13.8989414 3.77191832,15.5519474 5.80375046,15.5519474 C7.8355826,15.5519474 9.48875046,13.8989414 9.48875046,11.8669474 C9.48875046,9.83495328 7.83552863,8.18194736 5.80375046,8.18194736 Z M5.80375046,14.814915 C4.17821997,14.814915 2.85578285,13.4924778 2.85578285,11.8669474 C2.85578285,10.2414169 4.17821997,8.91897975 5.80375046,8.91897975 C7.42928095,8.91897975 8.75171807,10.2414169 8.75171807,11.8669474 C8.75171807,13.4924778 7.42928095,14.814915 5.80375046,14.814915 Z" id="Shape" fill="#000000" fill-rule="nonzero"></path>
            <path d="M13.9638189,8.699335 C13.9364621,8.70430925 13.9091059,8.71176968 13.8842359,8.71923074 C13.7822704,8.73663967 13.6877654,8.77643115 13.6056956,8.83860518 L10.2433156,11.3852598 C10.0766886,11.5046343 9.97720993,11.6986181 9.97720993,11.9025491 C9.97720993,12.1064807 10.0766886,12.3004639 10.2433156,12.4198383 L13.6056956,14.966493 C13.891697,15.1803725 14.2970729,15.1231721 14.5109517,14.8371707 C14.7248313,14.5511692 14.6676309,14.145794 14.3816294,13.9319145 L12.5313257,12.5392127 L21.8812495,12.5392127 L21.8812495,11.2658854 L12.5313257,11.2658854 L14.3816294,9.87318364 C14.6377872,9.71650453 14.7497006,9.40066014 14.6477351,9.11714553 C14.5482564,8.83363156 14.262255,8.65954352 13.9638189,8.699335 Z" id="arrow" fill="#000000" transform="translate(15.929230, 11.894737) rotate(-180.000000) translate(-15.929230, -11.894737) "></path>
        </g>
    </g>
</svg></td>
    <td style="height: 40px; background-color: #FCFCFC; border-right: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color:#4CA64C;">&check;</span></td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_right">13</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">7<br />0.54</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">6<br />0.46</td>
    <td style="height: 40px; background-color: #FCFCFC; border-left: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #AAAAAA;">&#9679;</span></td>
    <td style="height: 40px; background-color: #FCFCFC;" class="gt_row gt_center"><span style="color: #EBBC14;">&#9679;</span></td>
    <td style="height: 40px; background-color: #FCFCFC; border-right: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #FF3300;">&cir;</span></td>
    <td style="height: 40px;" class="gt_row gt_center"><a href="data:text/csv;base64,X3Jvd19udW1fLGRhdGVfdGltZSxkYXRlLGEsYixjLGQsZSxmCjUsMjAxNi0wMS0wOVQxMjozNjowMC4wMDAwMDAsMjAxNi0wMS0wOSw4LDMtbGRtLTAzOCw3LDI4My45NCx0cnVlLGxvdwo3LDIwMTYtMDEtMTVUMTg6NDY6MDAuMDAwMDAwLDIwMTYtMDEtMTUsNywxLWtudy0wOTMsMyw4NDMuMzQsdHJ1ZSxoaWdoCjksMjAxNi0wMS0yMFQwNDozMDowMC4wMDAwMDAsMjAxNi0wMS0yMCwzLDUtYmNlLTY0Miw5LDgzNy45MyxmYWxzZSxoaWdoCjEwLDIwMTYtMDEtMjBUMDQ6MzA6MDAuMDAwMDAwLDIwMTYtMDEtMjAsMyw1LWJjZS02NDIsOSw4MzcuOTMsZmFsc2UsaGlnaAoxMSwyMDE2LTAxLTI2VDIwOjA3OjAwLjAwMDAwMCwyMDE2LTAxLTI2LDQsMi1kbXgtMDEwLDcsODMzLjk4LHRydWUsbG93CjEyLDIwMTYtMDEtMjhUMDI6NTE6MDAuMDAwMDAwLDIwMTYtMDEtMjgsMiw3LWRteC0wMTAsOCwxMDguMzQsZmFsc2UsbG93Cg==" download="extract_0001.csv"><button style="background-color: #67C2DC; color: #FFFFFF; border: none; padding: 5px; font-weight: bold; cursor: pointer; border-radius: 4px;">CSV</button></a></td>
  </tr>
  <tr>
    <td style="height: 40px; background-color: #FF3300; color: transparent;font-size: 0px;" class="gt_row gt_left">#FF3300</td>
    <td style="height: 40px; color: #666666;font-size: 13px;font-weight: bold;" class="gt_row gt_right">2</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_left">
        <div style="margin: 0; padding: 0; display: inline-block; height: 30px; vertical-align: middle; width: 16%;">
            <!--?xml version="1.0" encoding="UTF-8"?--><?xml version="1.0" encoding="UTF-8"?>
<svg width="30px" height="30px" viewBox="0 0 67 67" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <title>col_vals_lte</title>
    <g id="All-Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="col_vals_lte" transform="translate(0.000000, 0.793103)">
            <path d="M56.712234,1 C59.1975153,1 61.4475153,2.00735931 63.076195,3.63603897 C64.7048747,5.26471863 65.712234,7.51471863 65.712234,10 L65.712234,10 L65.712234,65 L10.712234,65 C8.22695259,65 5.97695259,63.9926407 4.34827294,62.363961 C2.71959328,60.7352814 1.71223397,58.4852814 1.71223397,56 L1.71223397,56 L1.71223397,10 C1.71223397,7.51471863 2.71959328,5.26471863 4.34827294,3.63603897 C5.97695259,2.00735931 8.22695259,1 10.712234,1 L10.712234,1 Z" id="rectangle" stroke="#000000" stroke-width="2" fill="#FFFFFF"></path>
            <path d="M53.712234,12 L13.712234,12 C13.157547,12 12.712234,12.449219 12.712234,13 L12.712234,53 C12.712234,53.550781 13.157547,54 13.712234,54 L53.712234,54 C54.266922,54 54.712234,53.550781 54.712234,53 L54.712234,13 C54.712234,12.449219 54.266922,12 53.712234,12 Z M42.227859,19.125 L43.196609,20.875 L26.770828,30 L43.196609,39.125 L42.227859,40.875 L22.65364,30 L42.227859,19.125 Z M44.712234,47 L22.712234,47 L22.712234,45 L44.712234,45 L44.712234,47 Z" id="less_than_equal" fill="#000000" fill-rule="nonzero"></path>
        </g>
    </g>
</svg>
        </div>
        <div style="font-family: 'IBM Plex Mono', monospace, courier; color: black; font-size: 11px; display: inline-block; vertical-align: middle;">
            <div>col_vals_le()</div>
        </div>
        
        </td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">c</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">5</td>
    <td style="height: 40px; background-color: #FCFCFC; border-left: 1px solid #D3D3D3;" class="gt_row gt_center"><svg width="25px" height="25px" viewBox="0 0 25 25" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="vertical-align: middle;">
    <g id="unchanged" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="unchanged" transform="translate(0.500000, 0.570147)">
            <rect id="Rectangle" x="0.125132506" y="0" width="23.749735" height="23.7894737"></rect>
            <path d="M5.80375046,8.18194736 C3.77191832,8.18194736 2.11875046,9.83495328 2.11875046,11.8669474 C2.11875046,13.8989414 3.77191832,15.5519474 5.80375046,15.5519474 C7.8355826,15.5519474 9.48875046,13.8989414 9.48875046,11.8669474 C9.48875046,9.83495328 7.83552863,8.18194736 5.80375046,8.18194736 Z M5.80375046,14.814915 C4.17821997,14.814915 2.85578285,13.4924778 2.85578285,11.8669474 C2.85578285,10.2414169 4.17821997,8.91897975 5.80375046,8.91897975 C7.42928095,8.91897975 8.75171807,10.2414169 8.75171807,11.8669474 C8.75171807,13.4924778 7.42928095,14.814915 5.80375046,14.814915 Z" id="Shape" fill="#000000" fill-rule="nonzero"></path>
            <path d="M13.9638189,8.699335 C13.9364621,8.70430925 13.9091059,8.71176968 13.8842359,8.71923074 C13.7822704,8.73663967 13.6877654,8.77643115 13.6056956,8.83860518 L10.2433156,11.3852598 C10.0766886,11.5046343 9.97720993,11.6986181 9.97720993,11.9025491 C9.97720993,12.1064807 10.0766886,12.3004639 10.2433156,12.4198383 L13.6056956,14.966493 C13.891697,15.1803725 14.2970729,15.1231721 14.5109517,14.8371707 C14.7248313,14.5511692 14.6676309,14.145794 14.3816294,13.9319145 L12.5313257,12.5392127 L21.8812495,12.5392127 L21.8812495,11.2658854 L12.5313257,11.2658854 L14.3816294,9.87318364 C14.6377872,9.71650453 14.7497006,9.40066014 14.6477351,9.11714553 C14.5482564,8.83363156 14.262255,8.65954352 13.9638189,8.699335 Z" id="arrow" fill="#000000" transform="translate(15.929230, 11.894737) rotate(-180.000000) translate(-15.929230, -11.894737) "></path>
        </g>
    </g>
</svg></td>
    <td style="height: 40px; background-color: #FCFCFC; border-right: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color:#4CA64C;">&check;</span></td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_right">13</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">5<br />0.38</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">8<br />0.62</td>
    <td style="height: 40px; background-color: #FCFCFC; border-left: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #AAAAAA;">&#9679;</span></td>
    <td style="height: 40px; background-color: #FCFCFC;" class="gt_row gt_center"><span style="color: #EBBC14;">&#9679;</span></td>
    <td style="height: 40px; background-color: #FCFCFC; border-right: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #FF3300;">&#9679;</span></td>
    <td style="height: 40px;" class="gt_row gt_center"><a href="data:text/csv;base64,X3Jvd19udW1fLGRhdGVfdGltZSxkYXRlLGEsYixjLGQsZSxmCjIsMjAxNi0wMS0wNFQwMDozMjowMC4wMDAwMDAsMjAxNi0wMS0wNCwzLDUtZWdoLTE2Myw4LDk5OTkuOTksdHJ1ZSxsb3cKNCwyMDE2LTAxLTA2VDE3OjIzOjAwLjAwMDAwMCwyMDE2LTAxLTA2LDIsNS1qZG8tOTAzLCwzODkyLjQsZmFsc2UsbWlkCjUsMjAxNi0wMS0wOVQxMjozNjowMC4wMDAwMDAsMjAxNi0wMS0wOSw4LDMtbGRtLTAzOCw3LDI4My45NCx0cnVlLGxvdwo5LDIwMTYtMDEtMjBUMDQ6MzA6MDAuMDAwMDAwLDIwMTYtMDEtMjAsMyw1LWJjZS02NDIsOSw4MzcuOTMsZmFsc2UsaGlnaAoxMCwyMDE2LTAxLTIwVDA0OjMwOjAwLjAwMDAwMCwyMDE2LTAxLTIwLDMsNS1iY2UtNjQyLDksODM3LjkzLGZhbHNlLGhpZ2gKMTEsMjAxNi0wMS0yNlQyMDowNzowMC4wMDAwMDAsMjAxNi0wMS0yNiw0LDItZG14LTAxMCw3LDgzMy45OCx0cnVlLGxvdwoxMiwyMDE2LTAxLTI4VDAyOjUxOjAwLjAwMDAwMCwyMDE2LTAxLTI4LDIsNy1kbXgtMDEwLDgsMTA4LjM0LGZhbHNlLGxvdwoxMywyMDE2LTAxLTMwVDExOjIzOjAwLjAwMDAwMCwyMDE2LTAxLTMwLDEsMy1ka2EtMzAzLCwyMjMwLjA5LHRydWUsaGlnaAo=" download="extract_0002.csv"><button style="background-color: #67C2DC; color: #FFFFFF; border: none; padding: 5px; font-weight: bold; cursor: pointer; border-radius: 4px;">CSV</button></a></td>
  </tr>
  <tr>
    <td style="height: 40px; background-color: #4CA64C; color: transparent;font-size: 0px;" class="gt_row gt_left">#4CA64C</td>
    <td style="height: 40px; color: #666666;font-size: 13px;font-weight: bold;" class="gt_row gt_right">3</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_left">
        <div style="margin: 0; padding: 0; display: inline-block; height: 30px; vertical-align: middle; width: 16%;">
            <!--?xml version="1.0" encoding="UTF-8"?--><?xml version="1.0" encoding="UTF-8"?>
<svg width="30px" height="30px" viewBox="0 0 67 67" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <title>col_exists</title>
    <g id="All-Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="col_exists" transform="translate(0.000000, 0.827586)">
            <path d="M56.712234,1.01466935 C59.1975153,1.01466935 61.4475153,2.02202867 63.076195,3.65070832 C64.7048747,5.27938798 65.712234,7.52938798 65.712234,10.0146694 L65.712234,10.0146694 L65.712234,65.0146694 L10.712234,65.0146694 C8.22695259,65.0146694 5.97695259,64.00731 4.34827294,62.3786304 C2.71959328,60.7499507 1.71223397,58.4999507 1.71223397,56.0146694 L1.71223397,56.0146694 L1.71223397,10.0146694 C1.71223397,7.52938798 2.71959328,5.27938798 4.34827294,3.65070832 C5.97695259,2.02202867 8.22695259,1.01466935 10.712234,1.01466935 L10.712234,1.01466935 Z" id="rectangle" stroke="#000000" stroke-width="2" fill="#FFFFFF"></path>
            <rect id="column" fill="#000000" x="12.2117153" y="12.0146694" width="20" height="42" rx="1"></rect>
            <path d="M44.3177114,43.0146694 L44.3177114,40.5136928 L46.818688,40.5136928 L46.818688,43.0146694 L44.3177114,43.0146694 Z M44.3177114,38.0000209 L44.3177114,37.314474 C44.3177114,35.6979295 44.9397755,34.178739 46.1839224,32.7568569 L46.9837271,31.830099 C48.3125097,30.3066539 48.9768911,29.058294 48.9768911,28.0849819 C48.9768911,27.3317229 48.6849019,26.7350492 48.1009146,26.2949428 C47.5169273,25.8548364 46.7298258,25.6347865 45.7395864,25.6347865 C44.4446581,25.6347865 43.0693463,25.9479345 41.6136099,26.5742397 L41.6136099,24.4541225 C43.1793729,23.9801618 44.643551,23.743185 46.006188,23.743185 C47.7327591,23.743185 49.1038392,24.1303881 50.1194692,24.9048061 C51.1350993,25.679224 51.6429067,26.7265768 51.6429067,28.0468959 C51.6429067,28.7916913 51.4969121,29.4327982 51.2049185,29.9702358 C50.9129248,30.5076733 50.3522208,31.1699389 49.5227896,31.9570522 L48.7356802,32.6933803 C47.9485669,33.4381757 47.432296,34.0623556 47.1868521,34.5659389 C46.9414081,35.0695221 46.818688,35.7487146 46.818688,36.6035365 L46.818688,38.0000209 L44.3177114,38.0000209 Z" id="?" fill="#000000"></path>
        </g>
    </g>
</svg>
        </div>
        <div style="font-family: 'IBM Plex Mono', monospace, courier; color: black; font-size: 11px; display: inline-block; vertical-align: middle;">
            <div>col_exists()</div>
        </div>
        
        </td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">date</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">&mdash;</td>
    <td style="height: 40px; background-color: #FCFCFC; border-left: 1px solid #D3D3D3;" class="gt_row gt_center"><svg width="25px" height="25px" viewBox="0 0 25 25" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="vertical-align: middle;">
    <g id="unchanged" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="unchanged" transform="translate(0.500000, 0.570147)">
            <rect id="Rectangle" x="0.125132506" y="0" width="23.749735" height="23.7894737"></rect>
            <path d="M5.80375046,8.18194736 C3.77191832,8.18194736 2.11875046,9.83495328 2.11875046,11.8669474 C2.11875046,13.8989414 3.77191832,15.5519474 5.80375046,15.5519474 C7.8355826,15.5519474 9.48875046,13.8989414 9.48875046,11.8669474 C9.48875046,9.83495328 7.83552863,8.18194736 5.80375046,8.18194736 Z M5.80375046,14.814915 C4.17821997,14.814915 2.85578285,13.4924778 2.85578285,11.8669474 C2.85578285,10.2414169 4.17821997,8.91897975 5.80375046,8.91897975 C7.42928095,8.91897975 8.75171807,10.2414169 8.75171807,11.8669474 C8.75171807,13.4924778 7.42928095,14.814915 5.80375046,14.814915 Z" id="Shape" fill="#000000" fill-rule="nonzero"></path>
            <path d="M13.9638189,8.699335 C13.9364621,8.70430925 13.9091059,8.71176968 13.8842359,8.71923074 C13.7822704,8.73663967 13.6877654,8.77643115 13.6056956,8.83860518 L10.2433156,11.3852598 C10.0766886,11.5046343 9.97720993,11.6986181 9.97720993,11.9025491 C9.97720993,12.1064807 10.0766886,12.3004639 10.2433156,12.4198383 L13.6056956,14.966493 C13.891697,15.1803725 14.2970729,15.1231721 14.5109517,14.8371707 C14.7248313,14.5511692 14.6676309,14.145794 14.3816294,13.9319145 L12.5313257,12.5392127 L21.8812495,12.5392127 L21.8812495,11.2658854 L12.5313257,11.2658854 L14.3816294,9.87318364 C14.6377872,9.71650453 14.7497006,9.40066014 14.6477351,9.11714553 C14.5482564,8.83363156 14.262255,8.65954352 13.9638189,8.699335 Z" id="arrow" fill="#000000" transform="translate(15.929230, 11.894737) rotate(-180.000000) translate(-15.929230, -11.894737) "></path>
        </g>
    </g>
</svg></td>
    <td style="height: 40px; background-color: #FCFCFC; border-right: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color:#4CA64C;">&check;</span></td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_right">1</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">1<br />1.00</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">0<br />0.00</td>
    <td style="height: 40px; background-color: #FCFCFC; border-left: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #AAAAAA;">&cir;</span></td>
    <td style="height: 40px; background-color: #FCFCFC;" class="gt_row gt_center"><span style="color: #EBBC14;">&cir;</span></td>
    <td style="height: 40px; background-color: #FCFCFC; border-right: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #FF3300;">&cir;</span></td>
    <td style="height: 40px;" class="gt_row gt_center">—</td>
  </tr>
  <tr>
    <td style="height: 40px; background-color: #4CA64C; color: transparent;font-size: 0px;" class="gt_row gt_left">#4CA64C</td>
    <td style="height: 40px; color: #666666;font-size: 13px;font-weight: bold;" class="gt_row gt_right">4</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_left">
        <div style="margin: 0; padding: 0; display: inline-block; height: 30px; vertical-align: middle; width: 16%;">
            <!--?xml version="1.0" encoding="UTF-8"?--><?xml version="1.0" encoding="UTF-8"?>
<svg width="30px" height="30px" viewBox="0 0 67 67" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <title>col_exists</title>
    <g id="All-Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="col_exists" transform="translate(0.000000, 0.827586)">
            <path d="M56.712234,1.01466935 C59.1975153,1.01466935 61.4475153,2.02202867 63.076195,3.65070832 C64.7048747,5.27938798 65.712234,7.52938798 65.712234,10.0146694 L65.712234,10.0146694 L65.712234,65.0146694 L10.712234,65.0146694 C8.22695259,65.0146694 5.97695259,64.00731 4.34827294,62.3786304 C2.71959328,60.7499507 1.71223397,58.4999507 1.71223397,56.0146694 L1.71223397,56.0146694 L1.71223397,10.0146694 C1.71223397,7.52938798 2.71959328,5.27938798 4.34827294,3.65070832 C5.97695259,2.02202867 8.22695259,1.01466935 10.712234,1.01466935 L10.712234,1.01466935 Z" id="rectangle" stroke="#000000" stroke-width="2" fill="#FFFFFF"></path>
            <rect id="column" fill="#000000" x="12.2117153" y="12.0146694" width="20" height="42" rx="1"></rect>
            <path d="M44.3177114,43.0146694 L44.3177114,40.5136928 L46.818688,40.5136928 L46.818688,43.0146694 L44.3177114,43.0146694 Z M44.3177114,38.0000209 L44.3177114,37.314474 C44.3177114,35.6979295 44.9397755,34.178739 46.1839224,32.7568569 L46.9837271,31.830099 C48.3125097,30.3066539 48.9768911,29.058294 48.9768911,28.0849819 C48.9768911,27.3317229 48.6849019,26.7350492 48.1009146,26.2949428 C47.5169273,25.8548364 46.7298258,25.6347865 45.7395864,25.6347865 C44.4446581,25.6347865 43.0693463,25.9479345 41.6136099,26.5742397 L41.6136099,24.4541225 C43.1793729,23.9801618 44.643551,23.743185 46.006188,23.743185 C47.7327591,23.743185 49.1038392,24.1303881 50.1194692,24.9048061 C51.1350993,25.679224 51.6429067,26.7265768 51.6429067,28.0468959 C51.6429067,28.7916913 51.4969121,29.4327982 51.2049185,29.9702358 C50.9129248,30.5076733 50.3522208,31.1699389 49.5227896,31.9570522 L48.7356802,32.6933803 C47.9485669,33.4381757 47.432296,34.0623556 47.1868521,34.5659389 C46.9414081,35.0695221 46.818688,35.7487146 46.818688,36.6035365 L46.818688,38.0000209 L44.3177114,38.0000209 Z" id="?" fill="#000000"></path>
        </g>
    </g>
</svg>
        </div>
        <div style="font-family: 'IBM Plex Mono', monospace, courier; color: black; font-size: 11px; display: inline-block; vertical-align: middle;">
            <div>col_exists()</div>
        </div>
        
        </td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">date_time</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">&mdash;</td>
    <td style="height: 40px; background-color: #FCFCFC; border-left: 1px solid #D3D3D3;" class="gt_row gt_center"><svg width="25px" height="25px" viewBox="0 0 25 25" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="vertical-align: middle;">
    <g id="unchanged" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="unchanged" transform="translate(0.500000, 0.570147)">
            <rect id="Rectangle" x="0.125132506" y="0" width="23.749735" height="23.7894737"></rect>
            <path d="M5.80375046,8.18194736 C3.77191832,8.18194736 2.11875046,9.83495328 2.11875046,11.8669474 C2.11875046,13.8989414 3.77191832,15.5519474 5.80375046,15.5519474 C7.8355826,15.5519474 9.48875046,13.8989414 9.48875046,11.8669474 C9.48875046,9.83495328 7.83552863,8.18194736 5.80375046,8.18194736 Z M5.80375046,14.814915 C4.17821997,14.814915 2.85578285,13.4924778 2.85578285,11.8669474 C2.85578285,10.2414169 4.17821997,8.91897975 5.80375046,8.91897975 C7.42928095,8.91897975 8.75171807,10.2414169 8.75171807,11.8669474 C8.75171807,13.4924778 7.42928095,14.814915 5.80375046,14.814915 Z" id="Shape" fill="#000000" fill-rule="nonzero"></path>
            <path d="M13.9638189,8.699335 C13.9364621,8.70430925 13.9091059,8.71176968 13.8842359,8.71923074 C13.7822704,8.73663967 13.6877654,8.77643115 13.6056956,8.83860518 L10.2433156,11.3852598 C10.0766886,11.5046343 9.97720993,11.6986181 9.97720993,11.9025491 C9.97720993,12.1064807 10.0766886,12.3004639 10.2433156,12.4198383 L13.6056956,14.966493 C13.891697,15.1803725 14.2970729,15.1231721 14.5109517,14.8371707 C14.7248313,14.5511692 14.6676309,14.145794 14.3816294,13.9319145 L12.5313257,12.5392127 L21.8812495,12.5392127 L21.8812495,11.2658854 L12.5313257,11.2658854 L14.3816294,9.87318364 C14.6377872,9.71650453 14.7497006,9.40066014 14.6477351,9.11714553 C14.5482564,8.83363156 14.262255,8.65954352 13.9638189,8.699335 Z" id="arrow" fill="#000000" transform="translate(15.929230, 11.894737) rotate(-180.000000) translate(-15.929230, -11.894737) "></path>
        </g>
    </g>
</svg></td>
    <td style="height: 40px; background-color: #FCFCFC; border-right: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color:#4CA64C;">&check;</span></td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_right">1</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">1<br />1.00</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">0<br />0.00</td>
    <td style="height: 40px; background-color: #FCFCFC; border-left: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #AAAAAA;">&cir;</span></td>
    <td style="height: 40px; background-color: #FCFCFC;" class="gt_row gt_center"><span style="color: #EBBC14;">&cir;</span></td>
    <td style="height: 40px; background-color: #FCFCFC; border-right: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #FF3300;">&cir;</span></td>
    <td style="height: 40px;" class="gt_row gt_center">—</td>
  </tr>
</tbody>
  <tfoot class="gt_sourcenotes">
  
  <tr>
    <td class="gt_sourcenote" colspan="14"><div style='margin-top: 5px; margin-bottom: 5px;'><span style='background-color: #FFF; color: #444; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin-left: 10px; margin-right: 5px; border: solid 1px #999999; font-variant-numeric: tabular-nums; border-radius: 0; padding: 2px 10px 2px 10px;'>2026-03-13 19:07:32 UTC</span><span style='background-color: #FFF; color: #444; padding: 0.5em 0.5em; position: inherit; margin-right: 5px; border: solid 1px #999999; font-variant-numeric: tabular-nums; border-radius: 0; padding: 2px 10px 2px 10px;'>< 1 s</span><span style='background-color: #FFF; color: #444; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin: 5px 1px 5px -1px; border: solid 1px #999999; font-variant-numeric: tabular-nums; border-radius: 0; padding: 2px 10px 2px 10px;'>2026-03-13 19:07:32 UTC</span></div></td>
  </tr>

</tfoot>

</table>

</div>

The first validation step (`cols_val_gt()`) checks the `d` column in the data, to ensure each value is greater than `1000`. Notice that the red bar on the left indicates it failed, and the `FAIL` column says it has 6 failing values out of 13 `UNITS`.

The table is chock full of the information you need when doing data validation tasks. And it's also easy on the eyes. Some cool features include:

1.  a header with information on the type of input table plus important validation options
2.  vertical color strips on the left side to indicate overall status of the rows
3.  icons in several columns (space saving and they let you know what's up)
4.  'CSV' buttons that, when clicked, provide you with a CSV file
5.  a footer with timing information for the analysis

It's a nice table and it scales nicely to the large variety of validation types and options available in the Pointblank library. Viewing this table is a central part of using that library and the great thing about the reporting being a table like this is that it can be shared by placing it in a publication environment of your choosing (for example, it could be put in a Quarto document).

Here is the code that was used to generate the data validation above:

``` python
import pointblank as pb

validation = (
    pb.Validate(
        data=pb.load_dataset(dataset="small_table", tbl_type="polars"),
        label="An example validation",
        thresholds=(0.1, 0.2, 0.5),
    )
    .col_vals_gt(columns="d", value=1000)
    .col_vals_le(columns="c", value=5)
    .col_exists(columns=["date", "date_time"])
    .interrogate()
)

validation
```

Pointblank makes it easy to get started by giving you a simple entry point (`Validate()`), allowing you to define as many validation steps as needed. Each validation step is specified by calling methods like `.cols_vals_gt()`, which is short for checking that "column values are greater than" some specified value.

Pointblank enables you to validate many types of DataFrames and SQL databases. Pointblank supports Pandas and Polars through Narwhals, and numerous backends (like DuckDB and MySQL) are also supported though our Ibis integration.

### Exploring data validation failures

Note that the above validation report table showed 6 failures in the first validation step. You might want to know exactly *what* failed, giving you a chance to fix the underlying data quality issues. To do that, you can use the `get_step_report()` method:

``` python
validation.get_step_report(i=1)
```

<div id="pb_preview_tbl" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
#pb_preview_tbl table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pb_preview_tbl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pb_preview_tbl p { margin: 0; padding: 0; }
 #pb_preview_tbl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pb_preview_tbl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pb_preview_tbl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pb_preview_tbl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pb_preview_tbl .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pb_preview_tbl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pb_preview_tbl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pb_preview_tbl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: solid; border-left-width: 1px; border-left-color: #F2F2F2; border-right-style: solid; border-right-width: 1px; border-right-color: #F2F2F2; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pb_preview_tbl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pb_preview_tbl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pb_preview_tbl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pb_preview_tbl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pb_preview_tbl .gt_spanner_row { border-bottom-style: hidden; }
 #pb_preview_tbl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pb_preview_tbl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pb_preview_tbl .gt_from_md> :first-child { margin-top: 0; }
 #pb_preview_tbl .gt_from_md> :last-child { margin-bottom: 0; }
 #pb_preview_tbl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: solid; border-left-width: 1px; border-left-color: #E9E9E9; border-right-style: solid; border-right-width: 1px; border-right-color: #E9E9E9; vertical-align: middle; overflow-x: hidden; }
 #pb_preview_tbl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pb_preview_tbl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pb_preview_tbl .gt_row_group_first td { border-top-width: 2px; }
 #pb_preview_tbl .gt_row_group_first th { border-top-width: 2px; }
 #pb_preview_tbl .gt_striped { background-color: rgba(128,128,128,0.05); }
 #pb_preview_tbl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pb_preview_tbl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pb_preview_tbl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pb_preview_tbl .gt_left { text-align: left; }
 #pb_preview_tbl .gt_center { text-align: center; }
 #pb_preview_tbl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pb_preview_tbl .gt_font_normal { font-weight: normal; }
 #pb_preview_tbl .gt_font_bold { font-weight: bold; }
 #pb_preview_tbl .gt_font_italic { font-style: italic; }
 #pb_preview_tbl .gt_super { font-size: 65%; }
 #pb_preview_tbl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pb_preview_tbl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>
<table style="table-layout: fixed;; width: 0px" class="gt_table" data-quarto-disable-processing="true" data-quarto-bootstrap="false">
<colgroup>
  <col style="width:25.6px;"/>
  <col style="width:158px;"/>
  <col style="width:88px;"/>
  <col style="width:49px;"/>
  <col style="width:80px;"/>
  <col style="width:49px;"/>
  <col style="width:65px;"/>
  <col style="width:65px;"/>
  <col style="width:57px;"/>
</colgroup>

<thead>

  <tr class="gt_heading">
    <td colspan="9" class="gt_heading gt_title gt_font_normal">Report for Validation Step 1<div style='font-size: 13.6px;'><div style='padding-top: 7px;'>ASSERTION <span style='border-style: solid; border-width: thin; border-color: lightblue; padding-left: 2px; padding-right: 2px;'><code style='color: #303030; background-color: transparent; position: relative; bottom: 1px;'><code style='color: #303030; font-family: monospace; font-size: smaller;'>d > 1000</code></code></span></div><div style='padding-top: 7px;'><strong>6</strong> / <strong>13</strong> TEST UNIT FAILURES IN COLUMN <strong>6</strong></div><div>EXTRACT OF ALL <strong>6</strong> ROWS WITH <span style='color: #B22222;'>TEST UNIT FAILURES IN RED</span>:</div></div></td>
  </tr>
<tr class="gt_col_headings">
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-_row_num_"></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-date_time"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>date_time</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>Datetime</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-date"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>date</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>Date</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-a"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>a</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>Int64</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-b"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>b</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>String</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-c"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>c</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>Int64</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px; border-left: 2px solid black;border-right: 2px solid black;" scope="col" id="pb_preview_tbl-d"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>d</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>Float64</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_center" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-e"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>e</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>Boolean</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-f"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>f</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>String</em></div></div></th>
</tr>
</thead>
<tbody class="gt_table_body">
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">5</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2016-01-09 12:36:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2016-01-09</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">8</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">3-ldm-038</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">7</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: #B22222; background-color: #FFC1C159; border-left: 2px solid black;border-right: 2px solid black;" class="gt_row gt_right">283.94</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_center">True</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">low</td>
  </tr>
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">7</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2016-01-15 18:46:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2016-01-15</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">7</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">1-knw-093</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">3</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: #B22222; background-color: #FFC1C159; border-left: 2px solid black;border-right: 2px solid black;" class="gt_row gt_right">843.34</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_center">True</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">high</td>
  </tr>
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">9</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2016-01-20 04:30:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2016-01-20</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">3</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">5-bce-642</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">9</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: #B22222; background-color: #FFC1C159; border-left: 2px solid black;border-right: 2px solid black;" class="gt_row gt_right">837.93</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_center">False</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">high</td>
  </tr>
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">10</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2016-01-20 04:30:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2016-01-20</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">3</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">5-bce-642</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">9</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: #B22222; background-color: #FFC1C159; border-left: 2px solid black;border-right: 2px solid black;" class="gt_row gt_right">837.93</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_center">False</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">high</td>
  </tr>
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">11</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2016-01-26 20:07:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2016-01-26</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">4</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">2-dmx-010</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">7</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: #B22222; background-color: #FFC1C159; border-left: 2px solid black;border-right: 2px solid black;" class="gt_row gt_right">833.98</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_center">True</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">low</td>
  </tr>
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">12</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2016-01-28 02:51:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2016-01-28</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">7-dmx-010</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">8</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: #B22222; background-color: #FFC1C159; border-left: 2px solid black;border-right: 2px solid black;" class="gt_row gt_right">108.34</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_center">False</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">low</td>
  </tr>
</tbody>


</table>

</div>

The use of a table for reporting is ideal here! The main features of this step report table include:

1.  a header with summarized information
2.  the selected rows that contain the failures
3.  a highlighted column of interest

Different types of validation methods will have step report tables that organize the pertinent information in a way that makes sense for the validation performed.

### Previewing datasets across backends

Because many of the backends Pointblank supports have varying ways to view the underlying data, we provide a unified `preview()` function. It gives you a beautiful and consistent view of any data table. Here is how it looks against a 2,000 row DuckDB table that's included in the package (`game_revenue`):

<details class="code-fold">
<summary>Show the code</summary>

``` python
pb.preview(pb.load_dataset(dataset="game_revenue", tbl_type="duckdb"))
```

</details>
<div id="pb_preview_tbl" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
#pb_preview_tbl table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#pb_preview_tbl thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#pb_preview_tbl p { margin: 0; padding: 0; }
 #pb_preview_tbl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #pb_preview_tbl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #pb_preview_tbl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #pb_preview_tbl .gt_subtitle { color: #333333; font-size: 12px; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #pb_preview_tbl .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pb_preview_tbl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pb_preview_tbl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #pb_preview_tbl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: solid; border-left-width: 1px; border-left-color: #F2F2F2; border-right-style: solid; border-right-width: 1px; border-right-color: #F2F2F2; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #pb_preview_tbl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #pb_preview_tbl .gt_column_spanner_outer:first-child { padding-left: 0; }
 #pb_preview_tbl .gt_column_spanner_outer:last-child { padding-right: 0; }
 #pb_preview_tbl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #pb_preview_tbl .gt_spanner_row { border-bottom-style: hidden; }
 #pb_preview_tbl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #pb_preview_tbl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #pb_preview_tbl .gt_from_md> :first-child { margin-top: 0; }
 #pb_preview_tbl .gt_from_md> :last-child { margin-bottom: 0; }
 #pb_preview_tbl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: solid; border-left-width: 1px; border-left-color: #E9E9E9; border-right-style: solid; border-right-width: 1px; border-right-color: #E9E9E9; vertical-align: middle; overflow-x: hidden; }
 #pb_preview_tbl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #pb_preview_tbl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #pb_preview_tbl .gt_row_group_first td { border-top-width: 2px; }
 #pb_preview_tbl .gt_row_group_first th { border-top-width: 2px; }
 #pb_preview_tbl .gt_striped { background-color: rgba(128,128,128,0.05); }
 #pb_preview_tbl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pb_preview_tbl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #pb_preview_tbl .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #pb_preview_tbl .gt_left { text-align: left; }
 #pb_preview_tbl .gt_center { text-align: center; }
 #pb_preview_tbl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #pb_preview_tbl .gt_font_normal { font-weight: normal; }
 #pb_preview_tbl .gt_font_bold { font-weight: bold; }
 #pb_preview_tbl .gt_font_italic { font-style: italic; }
 #pb_preview_tbl .gt_super { font-size: 65%; }
 #pb_preview_tbl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #pb_preview_tbl .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>
<table style="table-layout: fixed;; width: 0px" class="gt_table" data-quarto-disable-processing="true" data-quarto-bootstrap="false">
<colgroup>
  <col style="width:41.2px;"/>
  <col style="width:127px;"/>
  <col style="width:197px;"/>
  <col style="width:205px;"/>
  <col style="width:205px;"/>
  <col style="width:80px;"/>
  <col style="width:80px;"/>
  <col style="width:104px;"/>
  <col style="width:135px;"/>
  <col style="width:88px;"/>
  <col style="width:119px;"/>
  <col style="width:111px;"/>
</colgroup>

<thead>

  <tr class="gt_heading">
    <td colspan="12" class="gt_heading gt_title gt_font_normal"><div><div style="padding-top: 0; padding-bottom: 7px;"><span style='background-color: #000000; color: #FFFFFF; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin: 5px 10px 5px 0px; border: solid 1px #000000; font-weight: bold; padding: 2px 10px 2px 10px; font-size: 10px;'>DuckDB</span><span style='background-color: #eecbff; color: #333333; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin: 5px 0px 5px 5px; font-weight: bold; border: solid 1px #eecbff; padding: 2px 15px 2px 15px; font-size: 10px;'>Rows</span><span style='background-color: none; color: #333333; padding: 0.5em 0.5em; position: inherit; margin: 5px 0px 5px -4px; font-weight: bold; border: solid 1px #eecbff; padding: 2px 15px 2px 15px; font-size: 10px;'>2,000</span><span style='background-color: #BDE7B4; color: #333333; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin: 5px 0px 5px 3px; font-weight: bold; border: solid 1px #BDE7B4; padding: 2px 15px 2px 15px; font-size: 10px;'>Columns</span><span style='background-color: none; color: #333333; padding: 0.5em 0.5em; position: inherit; margin: 5px 0px 5px -4px; font-weight: bold; border: solid 1px #BDE7B4; padding: 2px 15px 2px 15px; font-size: 10px;'>11</span></div></div></td>
  </tr>
<tr class="gt_col_headings">
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-_row_num_"></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-player_id"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>player_id</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>string</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-session_id"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>session_id</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>string</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-session_start"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>session_start</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>timestamp</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-time"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>time</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>timestamp</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-item_type"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>item_type</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>string</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-item_name"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>item_name</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>string</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-item_revenue"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>item_revenue</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>float64</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-session_duration"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>session_duration</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>float64</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-start_day"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>start_day</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>date</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-acquisition"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>acquisition</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>string</em></div></div></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" style="color: gray20;font-family: IBM Plex Mono;font-size: 12px;" scope="col" id="pb_preview_tbl-country"><div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-bottom: 2px; margin-bottom: 2px;'>country</div><div style='white-space: nowrap; text-overflow: ellipsis; overflow: hidden; padding-top: 2px; margin-top: 2px;'><em>string</em></div></div></th>
</tr>
</thead>
<tbody class="gt_table_body">
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">1</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ECPANOIXLZHF896</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ECPANOIXLZHF896-eol2j8bs</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-01 01:31:03+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-01 01:31:27+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">iap</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">offer2</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">8.99</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">16.3</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-01</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">google</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">Germany</td>
  </tr>
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">2</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ECPANOIXLZHF896</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ECPANOIXLZHF896-eol2j8bs</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-01 01:31:03+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-01 01:36:57+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">iap</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">gems3</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">22.49</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">16.3</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-01</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">google</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">Germany</td>
  </tr>
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">3</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ECPANOIXLZHF896</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ECPANOIXLZHF896-eol2j8bs</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-01 01:31:03+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-01 01:37:45+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">iap</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">gold7</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">107.99</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">16.3</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-01</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">google</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">Germany</td>
  </tr>
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">4</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ECPANOIXLZHF896</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ECPANOIXLZHF896-eol2j8bs</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-01 01:31:03+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-01 01:42:33+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ad</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ad_20sec</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">0.76</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">16.3</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-01</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">google</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">Germany</td>
  </tr>
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; border-bottom: 2px solid #6699CC80; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">5</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; border-bottom: 2px solid #6699CC80;" class="gt_row gt_left">ECPANOIXLZHF896</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; border-bottom: 2px solid #6699CC80;" class="gt_row gt_left">ECPANOIXLZHF896-hdu9jkls</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; border-bottom: 2px solid #6699CC80;" class="gt_row gt_right">2015-01-01 11:50:02+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; border-bottom: 2px solid #6699CC80;" class="gt_row gt_right">2015-01-01 11:55:20+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; border-bottom: 2px solid #6699CC80;" class="gt_row gt_left">ad</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; border-bottom: 2px solid #6699CC80;" class="gt_row gt_left">ad_5sec</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; border-bottom: 2px solid #6699CC80;" class="gt_row gt_right">0.03</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; border-bottom: 2px solid #6699CC80;" class="gt_row gt_right">35.2</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; border-bottom: 2px solid #6699CC80;" class="gt_row gt_right">2015-01-01</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; border-bottom: 2px solid #6699CC80;" class="gt_row gt_left">google</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; border-bottom: 2px solid #6699CC80;" class="gt_row gt_left">Germany</td>
  </tr>
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">1996</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">NAOJRDMCSEBI281</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">NAOJRDMCSEBI281-j2vs9ilp</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-21 01:57:50+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-21 02:02:50+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ad</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ad_survey</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">1.332</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">25.8</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-11</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">organic</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">Norway</td>
  </tr>
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">1997</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">NAOJRDMCSEBI281</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">NAOJRDMCSEBI281-j2vs9ilp</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-21 01:57:50+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-21 02:22:14+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ad</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ad_survey</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">1.35</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">25.8</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-11</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">organic</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">Norway</td>
  </tr>
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">1998</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">RMOSWHJGELCI675</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">RMOSWHJGELCI675-vbhcsmtr</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-21 02:39:48+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-21 02:40:00+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ad</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ad_5sec</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">0.03</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">8.4</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-10</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">other_campaign</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">France</td>
  </tr>
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">1999</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">RMOSWHJGELCI675</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">RMOSWHJGELCI675-vbhcsmtr</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-21 02:39:48+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-21 02:47:12+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">iap</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">offer5</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">26.09</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">8.4</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-10</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">other_campaign</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">France</td>
  </tr>
  <tr>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E; color: gray;font-family: IBM Plex Mono;font-size: 10px; border-right: 2px solid #6699CC80;" class="gt_row gt_right">2000</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">GJCXNTWEBIPQ369</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">GJCXNTWEBIPQ369-9elq67md</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-21 03:59:23+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-21 04:06:29+00:00</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ad</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">ad_5sec</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">0.12</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">18.5</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_right">2015-01-14</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">organic</td>
    <td style="height: 14px; padding: 4px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: black;font-family: IBM Plex Mono;font-size: 12px; border-top: 1px solid #E9E9E;border-bottom: 1px solid #E9E9E;" class="gt_row gt_left">United States</td>
  </tr>
</tbody>


</table>

</div>

Notice that the table displays only 10 rows by default, 5 from the top and 5 from the bottom. The grey text on the left of the table indicates the row number, and a blue line helps demarcate the top and bottom rows.

The `preview()` function had a few design goals in mind:

- get the dimensions of the table and display them prominently in the header
- provide the column names and the column types
- have a consistent line height along with a sensible limit to the column width
- use a monospaced typeface having high legibility
- should work for all sorts of tables!

This is a nice drop-in replacement for looking at DataFrames or Ibis tables (the types of tables that Pointblank can work with). If you were to inspect the DuckDB table materialized by `pb.load_dataset(dataset="game_revenue", tbl_type="duckdb")` without `preview()` you'd get this:

<details class="code-fold">
<summary>Show the code</summary>

``` python
pb.load_dataset(dataset="game_revenue", tbl_type="duckdb")
```

</details>
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">DatabaseTable: game_revenue
  player_id        string
  session_id       string
  session_start    timestamp('UTC', 6)
  time             timestamp('UTC', 6)
  item_type        string
  item_name        string
  item_revenue     float64
  session_duration float64
  start_day        date
  acquisition      string
  country          string
</pre>

Which is not nearly as good.

### In closing

We hope this post is a good introduction to Pointblank and that it provides some insight on how Great Tables makes sense for reporting in a different library. If you'd like to learn more about Pointblank, please visit the [project website](https://posit-dev.github.io/pointblank/) and check out the many [examples](https://posit-dev.github.io/pointblank/demos/).
