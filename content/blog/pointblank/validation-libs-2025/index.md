---
title: Data Validation Libraries for Polars (2025 Edition)
people:
  - Rich Iannone
date: 2025-06-04T00:00:00.000Z
ported_from: pointblank
port_status: in-progress
---


<script src="https://cdn.jsdelivr.net/npm/requirejs@2.3.6/require.min.js" integrity="sha384-c9c+LnTbwQ3aujuU7ULEPVvgLs+Fn6fJUvIGTsuu1ZcCf11fiEubah0ttpca4ntM sha384-6V1/AdqZRWk1KAlWbKBlGhN7VG4iE/yAZcO6NZPMF8od0vukrvr0tg4qY6NSrItx" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js" integrity="sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/6Z/hRTt8+pR6L4N2" crossorigin="anonymous" data-relocate-top="true"></script>
<script type="application/javascript">define('jquery', [],function() {return window.jQuery;})</script>


Data validation is a very important part of any data pipeline. And with Polars gaining popularity as
a superfast and feature-packed DataFrame library, developers need validation tools that work
seamlessly with it. But here's the thing: not all validation libraries are created equal, and
choosing the wrong one can lead to frustration, technical debt, or validation gaps that could bite
you later.

In this survey (conducted halfway through 2025) we'll explore five Python validation libraries that
support Polars DataFrames, each bringing distinct strengths to different validation challenges.

> **Note**
>
> Great Expectations, while being one of the most established data validation frameworks in the Python
> ecosystem, is not included in this survey as it doesn't yet offer native Polars support. See [this
> issue](https://github.com/great-expectations/great_expectations/issues/10702) and
> [this discussion](https://github.com/great-expectations/great_expectations/discussions/10144) for
> the inside baseball.

## Recommendations

Here are the unique strengths for each library:

<div id="vacnurfmpq" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#vacnurfmpq table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#vacnurfmpq thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#vacnurfmpq p { margin: 0; padding: 0; }
 #vacnurfmpq .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #vacnurfmpq .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #vacnurfmpq .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #vacnurfmpq .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #vacnurfmpq .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vacnurfmpq .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vacnurfmpq .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #vacnurfmpq .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #vacnurfmpq .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #vacnurfmpq .gt_column_spanner_outer:first-child { padding-left: 0; }
 #vacnurfmpq .gt_column_spanner_outer:last-child { padding-right: 0; }
 #vacnurfmpq .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #vacnurfmpq .gt_spanner_row { border-bottom-style: hidden; }
 #vacnurfmpq .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #vacnurfmpq .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #vacnurfmpq .gt_from_md> :first-child { margin-top: 0; }
 #vacnurfmpq .gt_from_md> :last-child { margin-bottom: 0; }
 #vacnurfmpq .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #vacnurfmpq .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #vacnurfmpq .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #vacnurfmpq .gt_row_group_first td { border-top-width: 2px; }
 #vacnurfmpq .gt_row_group_first th { border-top-width: 2px; }
 #vacnurfmpq .gt_striped { color: #333333; background-color: #F4F4F4; }
 #vacnurfmpq .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #vacnurfmpq .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #vacnurfmpq .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #vacnurfmpq .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #vacnurfmpq .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #vacnurfmpq .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #vacnurfmpq .gt_left { text-align: left; }
 #vacnurfmpq .gt_center { text-align: center; }
 #vacnurfmpq .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #vacnurfmpq .gt_font_normal { font-weight: normal; }
 #vacnurfmpq .gt_font_bold { font-weight: bold; }
 #vacnurfmpq .gt_font_italic { font-style: italic; }
 #vacnurfmpq .gt_super { font-size: 65%; }
 #vacnurfmpq .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #vacnurfmpq .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Library | ⭐ | Best Features |
|----|----|----|
| <a href="https://github.com/unionai-oss/pandera" style="color: #333333; text-underline-offset: 3px;">Pandera</a> | 3,838 | Statistical testing, schema-centric validation, mypy integration |
| <a href="https://github.com/JakobGM/patito" style="color: #333333; text-underline-offset: 3px;">Patito</a> | 468 | Pydantic integration, model-based validation, row-level objects |
| <a href="https://github.com/posit-dev/pointblank" style="color: #333333; text-underline-offset: 3px;">Pointblank</a> | 173 | Interactive reports, threshold management, stakeholder communication |
| <a href="https://github.com/akmalsoliev/Validoopsie" style="color: #333333; text-underline-offset: 3px;">Validoopsie</a> | 63 | Built-in logging, composable validation, impact levels, lightweight Great Expectations alternative |
| <a href="https://github.com/Quantco/dataframely" style="color: #333333; text-underline-offset: 3px;">Dataframely</a> | 319 | Collection validation, advanced type safety, failure analysis |

</div>

Based on these strengths, here are my recommendations for which libraries to use according to use case:

<div id="nncbugwwxh" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#nncbugwwxh table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#nncbugwwxh thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#nncbugwwxh p { margin: 0; padding: 0; }
 #nncbugwwxh .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #nncbugwwxh .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #nncbugwwxh .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #nncbugwwxh .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 10px; padding-right: 10px; border-top-color: #FFFFFF; border-top-width: 0; }
 #nncbugwwxh .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nncbugwwxh .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nncbugwwxh .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #nncbugwwxh .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 10px; padding-right: 10px; overflow-x: hidden; }
 #nncbugwwxh .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #nncbugwwxh .gt_column_spanner_outer:first-child { padding-left: 0; }
 #nncbugwwxh .gt_column_spanner_outer:last-child { padding-right: 0; }
 #nncbugwwxh .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #nncbugwwxh .gt_spanner_row { border-bottom-style: hidden; }
 #nncbugwwxh .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 10px; padding-right: 10px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #nncbugwwxh .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #nncbugwwxh .gt_from_md> :first-child { margin-top: 0; }
 #nncbugwwxh .gt_from_md> :last-child { margin-bottom: 0; }
 #nncbugwwxh .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 10px; padding-right: 10px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #nncbugwwxh .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; }
 #nncbugwwxh .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 10px; padding-right: 10px; vertical-align: top; }
 #nncbugwwxh .gt_row_group_first td { border-top-width: 2px; }
 #nncbugwwxh .gt_row_group_first th { border-top-width: 2px; }
 #nncbugwwxh .gt_striped { color: #333333; background-color: #F4F4F4; }
 #nncbugwwxh .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #nncbugwwxh .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #nncbugwwxh .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #nncbugwwxh .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
 #nncbugwwxh .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #nncbugwwxh .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 10px; padding-right: 10px; text-align: left; }
 #nncbugwwxh .gt_left { text-align: left; }
 #nncbugwwxh .gt_center { text-align: center; }
 #nncbugwwxh .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #nncbugwwxh .gt_font_normal { font-weight: normal; }
 #nncbugwwxh .gt_font_bold { font-weight: bold; }
 #nncbugwwxh .gt_font_italic { font-style: italic; }
 #nncbugwwxh .gt_super { font-size: 65%; }
 #nncbugwwxh .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #nncbugwwxh .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

| Use Case | Best Libraries | Description |
|----|----|----|
| Type-safe pipelines | Pandera, Dataframely, Patito | Static type checking and compile-time validation |
| Stakeholder reporting | Pointblank | Sharing validation results with non-technical teams |
| Row-level object modeling | Patito | Converting DataFrame rows to Python objects with business logic |
| Statistical validation | Pandera | Testing data distributions and statistical properties |
| Data quality improvement | Pointblank, Validoopsie | Gradual quality improvement with threshold tracking |

</div>

## Setup

We are going to run through examples with **Pandera**, **Patito**, **Pointblank**, **Validoopsie**,
and **Dataframely**, using this Polars DataFrame as our test case:

``` python
import polars as pl

# Standard dataset for all validation examples
user_data = pl.DataFrame({
    "user_id": [1, 2, 3, 4, 5],
    "age": [25, 30, 22, 45, 95],  # <- includes a very high age
    "email": [
        "user1@example.com", "user2@example.com", "invalid-email",  # <- has an invalid email
        "user4@example.com", "user5@example.com"
    ],
    "score": [85.5, 92.0, 78.3, 88.7, 95.2]
})
```

We'll try to run the same data validation across the surveyed libraries, so we'll check:

- schema validation (correct column types)
- `user_id` values greater than `0`
- `age` values between `18` and `80` (inclusive)
- `email` strings matching a basic email regex pattern
- `score` values between `0` and `100` (inclusive)

Now let's dive into each library, starting with the statistically-focused Pandera.

## 1. Pandera: Schema-First Validation with Statistical Checks

Pandera is a statistical data validation toolkit designed to provide a flexible and expressive API
for performing data validation on dataframe-like objects. The library centers on schema-centric
validation, where you define the expected structure and constraints of your data upfront. You can
enable both runtime validation and static type checking integration. Pandera added Polars support in
version `0.19.0` (early 2024).

### Example

``` python
import pandera.polars as pa

# Define schema using our standard dataset
schema = pa.DataFrameSchema({
    "user_id": pa.Column(pl.Int64, checks=pa.Check.gt(0)),
    "age": pa.Column(pl.Int64, checks=[pa.Check.ge(18), pa.Check.le(80)]),
    "email": pa.Column(pl.Utf8, checks=pa.Check.str_matches(r"^[^@]+@[^@]+\.[^@]+$")),
    "score": pa.Column(pl.Float64, checks=pa.Check.in_range(0, 100))
})

# Validate the schema
try:
    validated_data = schema.validate(user_data)
    print("Validation successful!")
except pa.errors.SchemaError as e:
    print(f"Validation failed: {e}")
```

    Validation failed: Column 'age' failed validator number 1: <Check less_than_or_equal_to: less_than_or_equal_to(80)> failure case examples: [{'age': 95}]

This example demonstrates Pandera's declarative approach, where you define what your data should
look like rather than writing imperative validation logic. The schema acts as both documentation and
as a validation contract. Notice how multiple checks can be applied to a single column (here, the
`age` column receives two checks), and the validation either succeeds completely or provides
error information about what failed.

### Comparisons

Both Pandera and Patito use declarative, schema-centric approaches, but differ in their design
philosophies:

- Pandera uses a dictionary-like schema structure with Column objects for defining validation rules
- Patito uses Pydantic model classes with familiar Field syntax for validation constraints
- Pandera focuses heavily on statistical validation capabilities like hypothesis testing
- Patito emphasizes integration with existing Pydantic workflows and object modeling
- a key behavioral difference: Patito reports all validation errors in a single pass, while Pandera
  stops at the first failure

The choice between them often comes down to whether you prefer Pandera's statistical focus or
Patito's Pydantic integration.

Unlike Pointblank's step-by-step validation reporting, Pandera validates the entire schema at once.
Compared to Patito's model-based approach, Pandera focuses more on statistical validation
capabilities. Unlike Validoopsie's and Pointblank's method chaining style, Pandera uses a more
declarative, schema-centric approach.

### Unique Strengths and When to Use

Here are some of stand-out features that Pandera has:

- type-safe schema definitions with `mypy` integration
- statistical hypothesis testing for data distributions: perform t-tests, chi-square tests, and
  custom statistical tests directly in your validation schema
- excellent integration with Pandas, Polars, and Arrow support
- declarative schema syntax that serves as documentation
- built-in support for data coercion and transformation

This statistical validation capability goes beyond basic type and range checking to test actual data
relationships and distributional assumptions. For example, you can validate that the mean height of
group `"M"` is significantly greater than group `"F"` using a two-sample t-test, or test whether a
column follows a normal distribution. This makes Pandera uniquely powerful for data science
workflows where the statistical properties of your data are as important as individual data points
meeting basic constraints.

Data practitioners should choose Pandera when building type-safe data pipelines where schema
validation is critical, especially in data science workflows that require statistical validation.
It's ideal for users that value static type checking, need to validate statistical properties of
their data, or want schemas that double as documentation.

Pandera also excels in environments where data contracts between teams are important and where the
statistical properties of data matter as much as basic type checking.

## 2. Patito: Pydantic-Style Data Models for DataFrames

Patito brings Pydantic's well-received model-based validation approach to DataFrame validation,
creating a bridge between Pydantic-style data validation and DataFrame processing. The library's
primary goal is to provide a familiar, Pydantic-style interface for defining and validating
DataFrame schemas, making it particularly appealing to developers already using Pydantic in their
applications.

Patito launched with Polars support from the beginning (in late 2022). Native Polars integration is
touted as one of its core features, reflecting the growing adoption of Polars in the Python
ecosystem.

### Example

``` python
import patito as pt
from typing import Annotated

class UserModel(pt.Model):
    user_id: int = pt.Field(gt=0)
    age: Annotated[int, pt.Field(ge=18, le=80)]
    email: str = pt.Field(pattern=r"^[^@]+@[^@]+\.[^@]+$")
    score: float = pt.Field(ge=0.0, le=100.0)

# Validate using the model
try:
    UserModel.validate(user_data)
    print("Validation successful!")
except pt.exceptions.DataFrameValidationError as e:
    print(f"Validation failed: {e}")
```

    Validation failed: 2 validation errors for UserModel
    age
      1 row with out of bound values. (type=value_error.rowvalue)
    email
      1 row with out of bound values. (type=value_error.rowvalue)

This example showcases Patito's model-centric approach where validation rules are embedded in class
definitions. The use of Python's type hints and Pydantic's Field syntax makes the validation rules
self-documenting. Notably, Patito reports all validation errors at once, providing a fairly
comprehensive view of data quality issues, whereas other libraries (e.g., Pandera) stop at the first
failure.

### Column Validation Approaches: Pandera vs Patito

**Pandera offers a much more extensive and flexible system for column validation** compared to
Patito's field-based approach. While Patito provides a solid set of built-in field constraints
(like `gt`, `le`, `regex`, `unique`, etc.) that cover common validation scenarios, Pandera's Check
system is designed for both simple and highly sophisticated validation logic.

The key architectural difference seems to lie in extensibility and complexity. Pandera's `Check`
objects accept arbitrary functions, allowing you to write custom validation logic that can be as
simple as `lambda s: s > 0` or as complex as statistical hypothesis tests using scipy. You can
create vectorized checks that operate on entire Series objects for performance, element-wise checks
for atomic validation, and even grouped checks that validate subsets of data based on other columns.
Patito's `Field` constraints, while clean and declarative, are more limited to the predefined
validation types that Pydantic and Patito provide.

Pandera also supports advanced validation patterns that Patito doesn't directly offer, such as
wide-form data checks (validating relationships across multiple columns), grouped validation (where
checks are applied to subsets of data based on grouping columns), and the ability to raise warnings
instead of errors for non-critical validation failures. While Patito does support custom constraints
through Polars expressions via the `constraints` parameter, this requires knowledge of Polars
expression syntax and, depending on where you're coming from, could be less intuitive than Pandera's
function-based approach.

For most common validation scenarios, Patito's field-based validation is simpler and more readable,
especially for teams already familiar with Pydantic. However, for complex data validation
requirements, statistical validation, or when you need maximum flexibility in defining validation
logic, Pandera's Check system provides significantly more power and extensibility.

### Unique Strengths and When to Use

- Pydantic-style model definitions with familiar syntax for Pydantic users
- rich type system integration with Python's typing system
- model inheritance and composition for complex data structures
- seamless integration with existing Pydantic-based applications
- row-level object modeling for converting DataFrame rows to Python objects with methods
- mock data generation for testing with `.examples()` method

People should choose Patito when they're already using Pydantic in their applications and want
consistent validation patterns across data processing and application logic. It's great when you
need to validate DataFrames and then work with individual rows as rich Python objects with embedded
business logic and methods (e.g., a `Product` row that has a `.url` property or
`.calculate_discount()` method). Patito is also good when you need to generate realistic test data
and want object-oriented interfaces for their data models.

## 3. Pointblank: Comprehensive Validation with Beautiful Reports

Pointblank is a comprehensive data validation framework designed to make data quality assessment
both thorough and accessible to stakeholders. Originally inspired by the R package of the same name,
Pointblank's primary mission is to provide validation workflows that generate beautiful, interactive
reports that can be shared with both technical and non-technical team members.

Pointblank launched with Polars support as a core feature from its initial Python release in late
2024, built on top of the Narwhals and Ibis compatibility layers to provide consistent DataFrame
operations across multiple backends including Polars, Pandas, and database connections.

### Example

``` python
import pointblank as pb

schema = pb.Schema(
    columns=[("user_id", "Int64"), ("age", "Int64"), ("email", "String"), ("score", "Float64")]
)

validation = (
    pb.Validate(data=user_data, label="An example.", tbl_name="users", thresholds=(0.1, 0.2, 0.3))
    .col_vals_gt(columns="user_id", value=0)
    .col_vals_between(columns="age", left=18, right=80)
    .col_vals_regex(columns="email", pattern=r"^[^@]+@[^@]+\.[^@]+$")
    .col_vals_between(columns="score", left=0, right=100)
    .col_schema_match(schema=schema)
    .interrogate()
)

validation
```

<div id="pb_tbl" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
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
 #pb_tbl .gt_striped { color: #333333; background-color: #F4F4F4; }
 #pb_tbl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #pb_tbl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
 #pb_tbl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
 #pb_tbl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
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
    <td colspan="14" class="gt_heading gt_title gt_font_normal" style="color: #444444;font-size: 28px;text-align: left;font-weight: bold; text-align: left;">Pointblank Validation</td>
  </tr>
  <tr class="gt_heading">
    <td colspan="14" class="gt_heading gt_subtitle gt_font_normal gt_bottom_border" style="text-align: left;"><div><span style='text-decoration-style: solid; text-decoration-color: #ADD8E6; text-decoration-line: underline; text-underline-position: under; color: #333333; font-variant-numeric: tabular-nums; padding-left: 4px; margin-right: 5px; padding-right: 2px;'>An example.</span><div style="padding-top: 10px; padding-bottom: 5px;"><span style='background-color: #0075FF; color: #FFFFFF; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin: 5px 0px 5px 0px; border: solid 1px #0075FF; font-weight: bold; padding: 2px 15px 2px 15px; font-size: 10px;'>Polars</span><span style='background-color: none; color: #222222; padding: 0.5em 0.5em; position: inherit; margin: 5px 10px 5px -4px; border: solid 1px #0075FF; font-weight: bold; padding: 2px 15px 2px 15px; font-size: 10px;'>users</span><span><span style="background-color: #AAAAAA; color: white; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin: 5px 0px 5px 5px; border: solid 1px #AAAAAA; font-weight: bold; padding: 2px 15px 2px 15px; font-size: smaller;">WARNING</span><span style="background-color: none; color: #333333; padding: 0.5em 0.5em; position: inherit; margin: 5px 0px 5px -4px; font-weight: bold; border: solid 1px #AAAAAA; padding: 2px 15px 2px 15px; font-size: smaller; margin-right: 5px;">0.1</span><span style="background-color: #EBBC14; color: white; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin: 5px 0px 5px 1px; border: solid 1px #EBBC14; font-weight: bold; padding: 2px 15px 2px 15px; font-size: smaller;">ERROR</span><span style="background-color: none; color: #333333; padding: 0.5em 0.5em; position: inherit; margin: 5px 0px 5px -4px; font-weight: bold; border: solid 1px #EBBC14; padding: 2px 15px 2px 15px; font-size: smaller; margin-right: 5px;">0.2</span><span style="background-color: #FF3300; color: white; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin: 5px 0px 5px 1px; border: solid 1px #FF3300; font-weight: bold; padding: 2px 15px 2px 15px; font-size: smaller;">CRITICAL</span><span style="background-color: none; color: #333333; padding: 0.5em 0.5em; position: inherit; margin: 5px 0px 5px -4px; font-weight: bold; border: solid 1px #FF3300; padding: 2px 15px 2px 15px; font-size: smaller;">0.3</span></span></div></div></td>
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
    <td style="height: 40px; background-color: #4CA64C; color: transparent;font-size: 0px;" class="gt_row gt_left">#4CA64C</td>
    <td style="height: 40px; color: #666666;font-size: 13px;font-weight: bold;" class="gt_row gt_right">1</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_left">
        <div style="margin: 0; padding: 0; display: inline-block; height: 30px; vertical-align: middle; width: 16%;">
            <!--?xml version="1.0" encoding="UTF-8"?--><?xml version="1.0" encoding="UTF-8"?>
<svg width="30px" height="30px" viewBox="0 0 67 67" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="background: #FFFFFF;">
    <title>col_vals_gt</title>
    <g id="Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="col_vals_gt" transform="translate(1.500000, 1.500000)" fill-rule="nonzero">
            <path d="M55,0 C57.4852813,0 59.7352813,1.00735931 61.363961,2.63603897 C62.9926407,4.26471863 64,6.51471863 64,9 L64,9 L64,64 L9,64 C6.51471862,64 4.26471862,62.9926407 2.63603897,61.363961 C1.00735931,59.7352814 0,57.4852814 0,55 L0,55 L0,9 C0,6.51471863 1.00735931,4.26471863 2.63603897,2.63603897 C4.26471862,1.00735931 6.51471862,0 9,0 L9,0 L55,0 Z" id="rectangle" stroke="#000000" stroke-width="2" fill="#FFFFFF"></path>
            <path d="M48.7619048,10 L15.2380953,10 C12.3466667,10 10,12.3466667 10,15.2380952 L10,48.7619048 C10,51.6533333 12.3466667,54 15.2380953,54 L48.7619048,54 C51.6533333,54 54,51.6533333 54,48.7619048 L54,15.2380952 C54,12.3466667 51.6533333,10 48.7619048,10 Z M25.2638095,44.3828571 L24.0695238,42.6647619 L39.5847619,32 L24.0695238,21.3352381 L25.2638095,19.6171429 L43.2828572,32 L25.2638095,44.3828571 Z" id="greater_than" fill="#000000"></path>
        </g>
    </g>
</svg>
        </div>
        <div style="font-family: 'IBM Plex Mono', monospace, courier; color: black; font-size: 11px; display: inline-block; vertical-align: middle;">
            <div>col_vals_gt()</div>
        </div>
        
        </td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">user_id</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">0</td>
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
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_right">5</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">5<br />1.00</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">0<br />0.00</td>
    <td style="height: 40px; background-color: #FCFCFC; border-left: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #AAAAAA;">&cir;</span></td>
    <td style="height: 40px; background-color: #FCFCFC;" class="gt_row gt_center"><span style="color: #EBBC14;">&cir;</span></td>
    <td style="height: 40px; background-color: #FCFCFC; border-right: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #FF3300;">&cir;</span></td>
    <td style="height: 40px;" class="gt_row gt_center">—</td>
  </tr>
  <tr>
    <td style="height: 40px; background-color: #EBBC14; color: transparent;font-size: 0px;" class="gt_row gt_left">#EBBC14</td>
    <td style="height: 40px; color: #666666;font-size: 13px;font-weight: bold;" class="gt_row gt_right">2</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_left">
        <div style="margin: 0; padding: 0; display: inline-block; height: 30px; vertical-align: middle; width: 16%;">
            <!--?xml version="1.0" encoding="UTF-8"?--><?xml version="1.0" encoding="UTF-8"?>
<svg width="30px" height="30px" viewBox="0 0 67 67" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <title>col_vals_between</title>
    <g id="Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="col_vals_between" transform="translate(0.000000, 0.206897)">
            <path d="M56.712234,1 C59.1975153,1 61.4475153,2.00735931 63.076195,3.63603897 C64.7048747,5.26471863 65.712234,7.51471863 65.712234,10 L65.712234,10 L65.712234,65 L10.712234,65 C8.22695259,65 5.97695259,63.9926407 4.34827294,62.363961 C2.71959328,60.7352814 1.71223397,58.4852814 1.71223397,56 L1.71223397,56 L1.71223397,10 C1.71223397,7.51471863 2.71959328,5.26471863 4.34827294,3.63603897 C5.97695259,2.00735931 8.22695259,1 10.712234,1 L10.712234,1 Z" id="rectangle" stroke="#000000" stroke-width="2" fill="#FFFFFF"></path>
            <path d="M11.993484,21.96875 C10.962234,22.082031 10.188797,22.964844 10.212234,24 L10.212234,42 C10.200515,42.722656 10.579422,43.390625 11.204422,43.753906 C11.825515,44.121094 12.598953,44.121094 13.220047,43.753906 C13.845047,43.390625 14.223953,42.722656 14.212234,42 L14.212234,24 C14.220047,23.457031 14.009109,22.9375 13.626297,22.554688 C13.243484,22.171875 12.723953,21.960938 12.180984,21.96875 C12.118484,21.964844 12.055984,21.964844 11.993484,21.96875 Z M55.993484,21.96875 C54.962234,22.082031 54.188797,22.964844 54.212234,24 L54.212234,42 C54.200515,42.722656 54.579422,43.390625 55.204422,43.753906 C55.825515,44.121094 56.598953,44.121094 57.220047,43.753906 C57.845047,43.390625 58.223953,42.722656 58.212234,42 L58.212234,24 C58.220047,23.457031 58.009109,22.9375 57.626297,22.554688 C57.243484,22.171875 56.723953,21.960938 56.180984,21.96875 C56.118484,21.964844 56.055984,21.964844 55.993484,21.96875 Z M16.212234,22 C15.661453,22 15.212234,22.449219 15.212234,23 C15.212234,23.550781 15.661453,24 16.212234,24 C16.763015,24 17.212234,23.550781 17.212234,23 C17.212234,22.449219 16.763015,22 16.212234,22 Z M20.212234,22 C19.661453,22 19.212234,22.449219 19.212234,23 C19.212234,23.550781 19.661453,24 20.212234,24 C20.763015,24 21.212234,23.550781 21.212234,23 C21.212234,22.449219 20.763015,22 20.212234,22 Z M24.212234,22 C23.661453,22 23.212234,22.449219 23.212234,23 C23.212234,23.550781 23.661453,24 24.212234,24 C24.763015,24 25.212234,23.550781 25.212234,23 C25.212234,22.449219 24.763015,22 24.212234,22 Z M28.212234,22 C27.661453,22 27.212234,22.449219 27.212234,23 C27.212234,23.550781 27.661453,24 28.212234,24 C28.763015,24 29.212234,23.550781 29.212234,23 C29.212234,22.449219 28.763015,22 28.212234,22 Z M32.212234,22 C31.661453,22 31.212234,22.449219 31.212234,23 C31.212234,23.550781 31.661453,24 32.212234,24 C32.763015,24 33.212234,23.550781 33.212234,23 C33.212234,22.449219 32.763015,22 32.212234,22 Z M36.212234,22 C35.661453,22 35.212234,22.449219 35.212234,23 C35.212234,23.550781 35.661453,24 36.212234,24 C36.763015,24 37.212234,23.550781 37.212234,23 C37.212234,22.449219 36.763015,22 36.212234,22 Z M40.212234,22 C39.661453,22 39.212234,22.449219 39.212234,23 C39.212234,23.550781 39.661453,24 40.212234,24 C40.763015,24 41.212234,23.550781 41.212234,23 C41.212234,22.449219 40.763015,22 40.212234,22 Z M44.212234,22 C43.661453,22 43.212234,22.449219 43.212234,23 C43.212234,23.550781 43.661453,24 44.212234,24 C44.763015,24 45.212234,23.550781 45.212234,23 C45.212234,22.449219 44.763015,22 44.212234,22 Z M48.212234,22 C47.661453,22 47.212234,22.449219 47.212234,23 C47.212234,23.550781 47.661453,24 48.212234,24 C48.763015,24 49.212234,23.550781 49.212234,23 C49.212234,22.449219 48.763015,22 48.212234,22 Z M52.212234,22 C51.661453,22 51.212234,22.449219 51.212234,23 C51.212234,23.550781 51.661453,24 52.212234,24 C52.763015,24 53.212234,23.550781 53.212234,23 C53.212234,22.449219 52.763015,22 52.212234,22 Z M21.462234,27.96875 C21.419265,27.976563 21.376297,27.988281 21.337234,28 C21.177078,28.027344 21.02864,28.089844 20.899734,28.1875 L15.618484,32.1875 C15.356765,32.375 15.200515,32.679688 15.200515,33 C15.200515,33.320313 15.356765,33.625 15.618484,33.8125 L20.899734,37.8125 C21.348953,38.148438 21.985672,38.058594 22.321609,37.609375 C22.657547,37.160156 22.567703,36.523438 22.118484,36.1875 L19.212234,34 L49.212234,34 L46.305984,36.1875 C45.856765,36.523438 45.766922,37.160156 46.102859,37.609375 C46.438797,38.058594 47.075515,38.148438 47.524734,37.8125 L52.805984,33.8125 C53.067703,33.625 53.223953,33.320313 53.223953,33 C53.223953,32.679688 53.067703,32.375 52.805984,32.1875 L47.524734,28.1875 C47.30989,28.027344 47.040359,27.960938 46.774734,28 C46.743484,28 46.712234,28 46.680984,28 C46.282547,28.074219 45.96614,28.382813 45.884109,28.78125 C45.802078,29.179688 45.970047,29.585938 46.305984,29.8125 L49.212234,32 L19.212234,32 L22.118484,29.8125 C22.520828,29.566406 22.696609,29.070313 22.536453,28.625 C22.380203,28.179688 21.930984,27.90625 21.462234,27.96875 Z M16.212234,42 C15.661453,42 15.212234,42.449219 15.212234,43 C15.212234,43.550781 15.661453,44 16.212234,44 C16.763015,44 17.212234,43.550781 17.212234,43 C17.212234,42.449219 16.763015,42 16.212234,42 Z M20.212234,42 C19.661453,42 19.212234,42.449219 19.212234,43 C19.212234,43.550781 19.661453,44 20.212234,44 C20.763015,44 21.212234,43.550781 21.212234,43 C21.212234,42.449219 20.763015,42 20.212234,42 Z M24.212234,42 C23.661453,42 23.212234,42.449219 23.212234,43 C23.212234,43.550781 23.661453,44 24.212234,44 C24.763015,44 25.212234,43.550781 25.212234,43 C25.212234,42.449219 24.763015,42 24.212234,42 Z M28.212234,42 C27.661453,42 27.212234,42.449219 27.212234,43 C27.212234,43.550781 27.661453,44 28.212234,44 C28.763015,44 29.212234,43.550781 29.212234,43 C29.212234,42.449219 28.763015,42 28.212234,42 Z M32.212234,42 C31.661453,42 31.212234,42.449219 31.212234,43 C31.212234,43.550781 31.661453,44 32.212234,44 C32.763015,44 33.212234,43.550781 33.212234,43 C33.212234,42.449219 32.763015,42 32.212234,42 Z M36.212234,42 C35.661453,42 35.212234,42.449219 35.212234,43 C35.212234,43.550781 35.661453,44 36.212234,44 C36.763015,44 37.212234,43.550781 37.212234,43 C37.212234,42.449219 36.763015,42 36.212234,42 Z M40.212234,42 C39.661453,42 39.212234,42.449219 39.212234,43 C39.212234,43.550781 39.661453,44 40.212234,44 C40.763015,44 41.212234,43.550781 41.212234,43 C41.212234,42.449219 40.763015,42 40.212234,42 Z M44.212234,42 C43.661453,42 43.212234,42.449219 43.212234,43 C43.212234,43.550781 43.661453,44 44.212234,44 C44.763015,44 45.212234,43.550781 45.212234,43 C45.212234,42.449219 44.763015,42 44.212234,42 Z M48.212234,42 C47.661453,42 47.212234,42.449219 47.212234,43 C47.212234,43.550781 47.661453,44 48.212234,44 C48.763015,44 49.212234,43.550781 49.212234,43 C49.212234,42.449219 48.763015,42 48.212234,42 Z M52.212234,42 C51.661453,42 51.212234,42.449219 51.212234,43 C51.212234,43.550781 51.661453,44 52.212234,44 C52.763015,44 53.212234,43.550781 53.212234,43 C53.212234,42.449219 52.763015,42 52.212234,42 Z" id="inside_range" fill="#000000" fill-rule="nonzero"></path>
        </g>
    </g>
</svg>
        </div>
        <div style="font-family: 'IBM Plex Mono', monospace, courier; color: black; font-size: 10px; display: inline-block; vertical-align: middle;">
            <div>col_vals_between()</div>
        </div>
        
        </td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">age</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">[18, 80]</td>
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
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_right">5</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">4<br />0.80</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">1<br />0.20</td>
    <td style="height: 40px; background-color: #FCFCFC; border-left: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #AAAAAA;">&#9679;</span></td>
    <td style="height: 40px; background-color: #FCFCFC;" class="gt_row gt_center"><span style="color: #EBBC14;">&#9679;</span></td>
    <td style="height: 40px; background-color: #FCFCFC; border-right: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #FF3300;">&cir;</span></td>
    <td style="height: 40px;" class="gt_row gt_center"><a href="data:text/csv;base64,X3Jvd19udW1fLHVzZXJfaWQsYWdlLGVtYWlsLHNjb3JlCjUsNSw5NSx1c2VyNUBleGFtcGxlLmNvbSw5NS4yCg==" download="extract_0002.csv"><button style="background-color: #67C2DC; color: #FFFFFF; border: none; padding: 5px; font-weight: bold; cursor: pointer; border-radius: 4px;">CSV</button></a></td>
  </tr>
  <tr>
    <td style="height: 40px; background-color: #EBBC14; color: transparent;font-size: 0px;" class="gt_row gt_left">#EBBC14</td>
    <td style="height: 40px; color: #666666;font-size: 13px;font-weight: bold;" class="gt_row gt_right">3</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_left">
        <div style="margin: 0; padding: 0; display: inline-block; height: 30px; vertical-align: middle; width: 16%;">
            <!--?xml version="1.0" encoding="UTF-8"?--><?xml version="1.0" encoding="UTF-8"?>
<svg width="30px" height="30px" viewBox="0 0 67 67" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <title>col_vals_regex</title>
    <g id="Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="col_vals_regex" transform="translate(0.000000, 0.034483)">
            <path d="M56.712234,1 C59.1975153,1 61.4475153,2.00735931 63.076195,3.63603897 C64.7048747,5.26471863 65.712234,7.51471863 65.712234,10 L65.712234,10 L65.712234,65 L10.712234,65 C8.22695259,65 5.97695259,63.9926407 4.34827294,62.363961 C2.71959328,60.7352814 1.71223397,58.4852814 1.71223397,56 L1.71223397,56 L1.71223397,10 C1.71223397,7.51471863 2.71959328,5.26471863 4.34827294,3.63603897 C5.97695259,2.00735931 8.22695259,1 10.712234,1 L10.712234,1 Z" id="rectangle" stroke="#000000" stroke-width="2" fill="#FFFFFF"></path>
            <g id="regex_symbols" transform="translate(18.000000, 12.000000)" fill="#000000" fill-rule="nonzero">
                <path d="M4.17434508,33.013582 C1.94895328,33.013582 0.138006923,34.8245284 0.138006923,37.0499202 C0.138006923,39.275312 1.94895328,41.0862583 4.17434508,41.0862583 C6.39973688,41.0862583 8.21068324,39.275312 8.21068324,37.0499202 C8.21068324,34.8245284 6.39973688,33.013582 4.17434508,33.013582 Z" id="full_stop"></path>
                <path d="M23.9479718,23.3175402 L21.5628264,23.3175402 C21.2344032,23.3175402 20.9665401,23.0520067 20.9665401,22.7212538 L20.9665401,15.1022979 L14.3445004,18.8873192 C14.0626621,19.050366 13.7016292,18.952538 13.5362533,18.6706991 L12.3436806,16.6442575 C12.262157,16.506832 12.2388642,16.3437852 12.2807909,16.1900549 C12.3203879,16.0363251 12.4205455,15.9058874 12.557971,15.8266929 L19.1800101,11.9880994 L12.557971,8.15183511 C12.4205455,8.07264112 12.3203879,7.93987439 12.2807909,7.78614401 C12.2388642,7.63241423 12.262157,7.46936689 12.3413509,7.33194137 L13.5339237,5.30549975 C13.6993001,5.02366143 14.0626621,4.92816199 14.3445004,5.09120934 L20.9665401,8.87390091 L20.9665401,1.25494501 C20.9665401,0.926521818 21.2344032,0.658658658 21.5628264,0.658658658 L23.9479718,0.658658658 C24.2787247,0.658658658 24.5442582,0.926521818 24.5442582,1.25494501 L24.5442582,8.87390091 L31.1662979,5.09120934 C31.4481362,4.92816199 31.8091691,5.02366143 31.9745455,5.30549975 L33.1671182,7.33194137 C33.2486413,7.46936689 33.2719341,7.63241423 33.2300074,7.78614401 C33.1904104,7.93987439 33.0902528,8.07264112 32.9528278,8.15183511 L26.3307882,11.9880994 L32.9528278,15.8243638 C33.0879237,15.9058874 33.1880813,16.0363251 33.2300074,16.1900549 C33.269605,16.3437852 33.2486413,16.506832 33.1671182,16.6442575 L31.9745455,18.6706991 C31.8091691,18.952538 31.4481362,19.050366 31.1662979,18.8849895 L24.5442582,15.1022979 L24.5442582,22.7212538 C24.5442582,23.0520067 24.2787247,23.3175402 23.9479718,23.3175402 Z" id="asterisk"></path>
            </g>
        </g>
    </g>
</svg>
        </div>
        <div style="font-family: 'IBM Plex Mono', monospace, courier; color: black; font-size: 11px; display: inline-block; vertical-align: middle;">
            <div>col_vals_regex()</div>
        </div>
        
        </td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">email</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">^[^@]+@[^@]+\.[^@]+$</td>
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
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_right">5</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">4<br />0.80</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">1<br />0.20</td>
    <td style="height: 40px; background-color: #FCFCFC; border-left: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #AAAAAA;">&#9679;</span></td>
    <td style="height: 40px; background-color: #FCFCFC;" class="gt_row gt_center"><span style="color: #EBBC14;">&#9679;</span></td>
    <td style="height: 40px; background-color: #FCFCFC; border-right: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #FF3300;">&cir;</span></td>
    <td style="height: 40px;" class="gt_row gt_center"><a href="data:text/csv;base64,X3Jvd19udW1fLHVzZXJfaWQsYWdlLGVtYWlsLHNjb3JlCjMsMywyMixpbnZhbGlkLWVtYWlsLDc4LjMK" download="extract_0003.csv"><button style="background-color: #67C2DC; color: #FFFFFF; border: none; padding: 5px; font-weight: bold; cursor: pointer; border-radius: 4px;">CSV</button></a></td>
  </tr>
  <tr>
    <td style="height: 40px; background-color: #4CA64C; color: transparent;font-size: 0px;" class="gt_row gt_left">#4CA64C</td>
    <td style="height: 40px; color: #666666;font-size: 13px;font-weight: bold;" class="gt_row gt_right">4</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_left">
        <div style="margin: 0; padding: 0; display: inline-block; height: 30px; vertical-align: middle; width: 16%;">
            <!--?xml version="1.0" encoding="UTF-8"?--><?xml version="1.0" encoding="UTF-8"?>
<svg width="30px" height="30px" viewBox="0 0 67 67" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <title>col_vals_between</title>
    <g id="Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="col_vals_between" transform="translate(0.000000, 0.206897)">
            <path d="M56.712234,1 C59.1975153,1 61.4475153,2.00735931 63.076195,3.63603897 C64.7048747,5.26471863 65.712234,7.51471863 65.712234,10 L65.712234,10 L65.712234,65 L10.712234,65 C8.22695259,65 5.97695259,63.9926407 4.34827294,62.363961 C2.71959328,60.7352814 1.71223397,58.4852814 1.71223397,56 L1.71223397,56 L1.71223397,10 C1.71223397,7.51471863 2.71959328,5.26471863 4.34827294,3.63603897 C5.97695259,2.00735931 8.22695259,1 10.712234,1 L10.712234,1 Z" id="rectangle" stroke="#000000" stroke-width="2" fill="#FFFFFF"></path>
            <path d="M11.993484,21.96875 C10.962234,22.082031 10.188797,22.964844 10.212234,24 L10.212234,42 C10.200515,42.722656 10.579422,43.390625 11.204422,43.753906 C11.825515,44.121094 12.598953,44.121094 13.220047,43.753906 C13.845047,43.390625 14.223953,42.722656 14.212234,42 L14.212234,24 C14.220047,23.457031 14.009109,22.9375 13.626297,22.554688 C13.243484,22.171875 12.723953,21.960938 12.180984,21.96875 C12.118484,21.964844 12.055984,21.964844 11.993484,21.96875 Z M55.993484,21.96875 C54.962234,22.082031 54.188797,22.964844 54.212234,24 L54.212234,42 C54.200515,42.722656 54.579422,43.390625 55.204422,43.753906 C55.825515,44.121094 56.598953,44.121094 57.220047,43.753906 C57.845047,43.390625 58.223953,42.722656 58.212234,42 L58.212234,24 C58.220047,23.457031 58.009109,22.9375 57.626297,22.554688 C57.243484,22.171875 56.723953,21.960938 56.180984,21.96875 C56.118484,21.964844 56.055984,21.964844 55.993484,21.96875 Z M16.212234,22 C15.661453,22 15.212234,22.449219 15.212234,23 C15.212234,23.550781 15.661453,24 16.212234,24 C16.763015,24 17.212234,23.550781 17.212234,23 C17.212234,22.449219 16.763015,22 16.212234,22 Z M20.212234,22 C19.661453,22 19.212234,22.449219 19.212234,23 C19.212234,23.550781 19.661453,24 20.212234,24 C20.763015,24 21.212234,23.550781 21.212234,23 C21.212234,22.449219 20.763015,22 20.212234,22 Z M24.212234,22 C23.661453,22 23.212234,22.449219 23.212234,23 C23.212234,23.550781 23.661453,24 24.212234,24 C24.763015,24 25.212234,23.550781 25.212234,23 C25.212234,22.449219 24.763015,22 24.212234,22 Z M28.212234,22 C27.661453,22 27.212234,22.449219 27.212234,23 C27.212234,23.550781 27.661453,24 28.212234,24 C28.763015,24 29.212234,23.550781 29.212234,23 C29.212234,22.449219 28.763015,22 28.212234,22 Z M32.212234,22 C31.661453,22 31.212234,22.449219 31.212234,23 C31.212234,23.550781 31.661453,24 32.212234,24 C32.763015,24 33.212234,23.550781 33.212234,23 C33.212234,22.449219 32.763015,22 32.212234,22 Z M36.212234,22 C35.661453,22 35.212234,22.449219 35.212234,23 C35.212234,23.550781 35.661453,24 36.212234,24 C36.763015,24 37.212234,23.550781 37.212234,23 C37.212234,22.449219 36.763015,22 36.212234,22 Z M40.212234,22 C39.661453,22 39.212234,22.449219 39.212234,23 C39.212234,23.550781 39.661453,24 40.212234,24 C40.763015,24 41.212234,23.550781 41.212234,23 C41.212234,22.449219 40.763015,22 40.212234,22 Z M44.212234,22 C43.661453,22 43.212234,22.449219 43.212234,23 C43.212234,23.550781 43.661453,24 44.212234,24 C44.763015,24 45.212234,23.550781 45.212234,23 C45.212234,22.449219 44.763015,22 44.212234,22 Z M48.212234,22 C47.661453,22 47.212234,22.449219 47.212234,23 C47.212234,23.550781 47.661453,24 48.212234,24 C48.763015,24 49.212234,23.550781 49.212234,23 C49.212234,22.449219 48.763015,22 48.212234,22 Z M52.212234,22 C51.661453,22 51.212234,22.449219 51.212234,23 C51.212234,23.550781 51.661453,24 52.212234,24 C52.763015,24 53.212234,23.550781 53.212234,23 C53.212234,22.449219 52.763015,22 52.212234,22 Z M21.462234,27.96875 C21.419265,27.976563 21.376297,27.988281 21.337234,28 C21.177078,28.027344 21.02864,28.089844 20.899734,28.1875 L15.618484,32.1875 C15.356765,32.375 15.200515,32.679688 15.200515,33 C15.200515,33.320313 15.356765,33.625 15.618484,33.8125 L20.899734,37.8125 C21.348953,38.148438 21.985672,38.058594 22.321609,37.609375 C22.657547,37.160156 22.567703,36.523438 22.118484,36.1875 L19.212234,34 L49.212234,34 L46.305984,36.1875 C45.856765,36.523438 45.766922,37.160156 46.102859,37.609375 C46.438797,38.058594 47.075515,38.148438 47.524734,37.8125 L52.805984,33.8125 C53.067703,33.625 53.223953,33.320313 53.223953,33 C53.223953,32.679688 53.067703,32.375 52.805984,32.1875 L47.524734,28.1875 C47.30989,28.027344 47.040359,27.960938 46.774734,28 C46.743484,28 46.712234,28 46.680984,28 C46.282547,28.074219 45.96614,28.382813 45.884109,28.78125 C45.802078,29.179688 45.970047,29.585938 46.305984,29.8125 L49.212234,32 L19.212234,32 L22.118484,29.8125 C22.520828,29.566406 22.696609,29.070313 22.536453,28.625 C22.380203,28.179688 21.930984,27.90625 21.462234,27.96875 Z M16.212234,42 C15.661453,42 15.212234,42.449219 15.212234,43 C15.212234,43.550781 15.661453,44 16.212234,44 C16.763015,44 17.212234,43.550781 17.212234,43 C17.212234,42.449219 16.763015,42 16.212234,42 Z M20.212234,42 C19.661453,42 19.212234,42.449219 19.212234,43 C19.212234,43.550781 19.661453,44 20.212234,44 C20.763015,44 21.212234,43.550781 21.212234,43 C21.212234,42.449219 20.763015,42 20.212234,42 Z M24.212234,42 C23.661453,42 23.212234,42.449219 23.212234,43 C23.212234,43.550781 23.661453,44 24.212234,44 C24.763015,44 25.212234,43.550781 25.212234,43 C25.212234,42.449219 24.763015,42 24.212234,42 Z M28.212234,42 C27.661453,42 27.212234,42.449219 27.212234,43 C27.212234,43.550781 27.661453,44 28.212234,44 C28.763015,44 29.212234,43.550781 29.212234,43 C29.212234,42.449219 28.763015,42 28.212234,42 Z M32.212234,42 C31.661453,42 31.212234,42.449219 31.212234,43 C31.212234,43.550781 31.661453,44 32.212234,44 C32.763015,44 33.212234,43.550781 33.212234,43 C33.212234,42.449219 32.763015,42 32.212234,42 Z M36.212234,42 C35.661453,42 35.212234,42.449219 35.212234,43 C35.212234,43.550781 35.661453,44 36.212234,44 C36.763015,44 37.212234,43.550781 37.212234,43 C37.212234,42.449219 36.763015,42 36.212234,42 Z M40.212234,42 C39.661453,42 39.212234,42.449219 39.212234,43 C39.212234,43.550781 39.661453,44 40.212234,44 C40.763015,44 41.212234,43.550781 41.212234,43 C41.212234,42.449219 40.763015,42 40.212234,42 Z M44.212234,42 C43.661453,42 43.212234,42.449219 43.212234,43 C43.212234,43.550781 43.661453,44 44.212234,44 C44.763015,44 45.212234,43.550781 45.212234,43 C45.212234,42.449219 44.763015,42 44.212234,42 Z M48.212234,42 C47.661453,42 47.212234,42.449219 47.212234,43 C47.212234,43.550781 47.661453,44 48.212234,44 C48.763015,44 49.212234,43.550781 49.212234,43 C49.212234,42.449219 48.763015,42 48.212234,42 Z M52.212234,42 C51.661453,42 51.212234,42.449219 51.212234,43 C51.212234,43.550781 51.661453,44 52.212234,44 C52.763015,44 53.212234,43.550781 53.212234,43 C53.212234,42.449219 52.763015,42 52.212234,42 Z" id="inside_range" fill="#000000" fill-rule="nonzero"></path>
        </g>
    </g>
</svg>
        </div>
        <div style="font-family: 'IBM Plex Mono', monospace, courier; color: black; font-size: 10px; display: inline-block; vertical-align: middle;">
            <div>col_vals_between()</div>
        </div>
        
        </td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">score</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">[0, 100]</td>
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
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_right">5</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">5<br />1.00</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5;" class="gt_row gt_right">0<br />0.00</td>
    <td style="height: 40px; background-color: #FCFCFC; border-left: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #AAAAAA;">&cir;</span></td>
    <td style="height: 40px; background-color: #FCFCFC;" class="gt_row gt_center"><span style="color: #EBBC14;">&cir;</span></td>
    <td style="height: 40px; background-color: #FCFCFC; border-right: 1px solid #D3D3D3;" class="gt_row gt_center"><span style="color: #FF3300;">&cir;</span></td>
    <td style="height: 40px;" class="gt_row gt_center">—</td>
  </tr>
  <tr>
    <td style="height: 40px; background-color: #4CA64C; color: transparent;font-size: 0px;" class="gt_row gt_left">#4CA64C</td>
    <td style="height: 40px; color: #666666;font-size: 13px;font-weight: bold;" class="gt_row gt_right">5</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px;" class="gt_row gt_left">
        <div style="margin: 0; padding: 0; display: inline-block; height: 30px; vertical-align: middle; width: 16%;">
            <!--?xml version="1.0" encoding="UTF-8"?--><?xml version="1.0" encoding="UTF-8"?>
<svg width="30px" height="30px" viewBox="0 0 67 67" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <title>col_schema_match</title>
    <g id="Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g id="col_schema_match" transform="translate(0.000000, 0.310345)">
            <path d="M56.712234,1.01466935 C59.1975153,1.01466935 61.4475153,2.02202867 63.076195,3.65070832 C64.7048747,5.27938798 65.712234,7.52938798 65.712234,10.0146694 L65.712234,10.0146694 L65.712234,65.0146694 L10.712234,65.0146694 C8.22695259,65.0146694 5.97695259,64.00731 4.34827294,62.3786304 C2.71959328,60.7499507 1.71223397,58.4999507 1.71223397,56.0146694 L1.71223397,56.0146694 L1.71223397,10.0146694 C1.71223397,7.52938798 2.71959328,5.27938798 4.34827294,3.65070832 C5.97695259,2.02202867 8.22695259,1.01466935 10.712234,1.01466935 L10.712234,1.01466935 Z" id="rectangle" stroke="#000000" stroke-width="2" fill="#FFFFFF"></path>
            <path d="M53.712234,39.7885268 L54.212234,56.2885268 L42.212234,56.7885268 L42.212234,39.7885268 L53.712234,39.7885268 Z M39.712234,39.7885268 L39.712234,56.7885268 L27.712234,56.7885268 L27.712234,39.7885268 L39.712234,39.7885268 Z M25.212234,39.7885268 L25.212234,56.7885268 L13.712234,56.7885268 L13.212234,40.2885268 L25.212234,39.7885268 Z" id="columns_schema" stroke="#000000" fill-rule="nonzero"></path>
            <g id="vertical_equal" transform="translate(30.000000, 29.000000)" stroke="#000000" stroke-linecap="square">
                <line x1="2.21223397" y1="0.514669353" x2="2.21223397" y2="7.58573716" id="Line"></line>
                <line x1="5.21223397" y1="0.514669353" x2="5.21223397" y2="7.58573716" id="Line-Copy"></line>
            </g>
            <path d="M41.712234,9.01466935 L41.712234,27.0146694 L53.712234,27.0146694 C54.262234,27.0146694 54.712234,26.5646694 54.712234,26.0146694 L54.712234,10.0146694 C54.712234,9.46466935 54.262234,9.01466935 53.712234,9.01466935 L41.712234,9.01466935 Z M27.212234,9.01466935 C27.212234,9.01466935 27.212234,15.0146694 27.212234,27.0146694 L40.212234,27.0146694 L40.212234,9.01466935 C31.5455673,9.01466935 27.212234,9.01466935 27.212234,9.01466935 Z M13.712234,9.01466935 C13.162234,9.01466935 12.712234,9.46466935 12.712234,10.0146694 L12.712234,26.0146694 C12.712234,26.5646694 13.162234,27.0146694 13.712234,27.0146694 L25.712234,27.0146694 L25.712234,9.01466935 L13.712234,9.01466935 Z" id="columns_real" fill="#000000" fill-rule="nonzero"></path>
        </g>
    </g>
</svg>
        </div>
        <div style="font-family: 'IBM Plex Mono', monospace, courier; color: black; font-size: 10px; display: inline-block; vertical-align: middle;">
            <div>col_schema_match()</div>
        </div>
        
        </td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">&mdash;</td>
    <td style="height: 40px; color: black;font-family: IBM Plex Mono;font-size: 11px; border-left: 1px dashed #E5E5E5; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">SCHEMA</td>
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
    <td class="gt_sourcenote" colspan="14" style="text-align: left;"><div style='margin-top: 5px; margin-bottom: 5px;'><span style='background-color: #FFF; color: #444; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin-left: 10px; margin-right: 5px; border: solid 1px #999999; font-variant-numeric: tabular-nums; border-radius: 0; padding: 2px 10px 2px 10px;'>2026-03-13 19:11:23 UTC</span><span style='background-color: #FFF; color: #444; padding: 0.5em 0.5em; position: inherit; margin-right: 5px; border: solid 1px #999999; font-variant-numeric: tabular-nums; border-radius: 0; padding: 2px 10px 2px 10px;'>< 1 s</span><span style='background-color: #FFF; color: #444; padding: 0.5em 0.5em; position: inherit; text-transform: uppercase; margin: 5px 1px 5px -1px; border: solid 1px #999999; font-variant-numeric: tabular-nums; border-radius: 0; padding: 2px 10px 2px 10px;'>2026-03-13 19:11:23 UTC</span></div></td>
  </tr>


  <tr>
    <td class="gt_sourcenote" colspan="14" style="text-align: left;"><hr style='border: none; border-top-width: 1px; border-top-style: dotted; border-top-color: #B5B5B5; margin-top: -3px; margin-bottom: 3px;'>
<strong>Notes</strong>
<p><span style='font-variant: small-caps; font-weight: bold; font-size: smaller; text-transform: uppercase; color: #333333;'>Step 5</span> <span style='font-family: "IBM Plex Mono", monospace; font-size: smaller;'>(schema_check)</span> <span style="color:#4CA64C;">✓</span> Schema validation <strong>passed</strong>.</p>
<details style="margin-top: 2px; margin-bottom: 8px; font-size: 12px; text-indent: 12px;">
<summary style="cursor: pointer; font-weight: bold; color: #555; margin-bottom: -5px;">Schema Comparison</summary>
<div style="margin-top: 6px; padding-left: 15px; padding-right: 15px;">
<div id="pb_step_tbl" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono&display=swap');
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
#pb_step_tbl table {
          font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }
<p>#pb_step_tbl thead, tbody, tfoot, tr, td, th { border-style: none; }
tr { background-color: transparent; }
#pb_step_tbl p { margin: 0; padding: 0; }
#pb_step_tbl .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
#pb_step_tbl .gt_caption { padding-top: 4px; padding-bottom: 4px; }
#pb_step_tbl .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
#pb_step_tbl .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
#pb_step_tbl .gt_heading { background-color: #FFFFFF; text-align: left; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
#pb_step_tbl .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
#pb_step_tbl .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
#pb_step_tbl .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
#pb_step_tbl .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
#pb_step_tbl .gt_column_spanner_outer:first-child { padding-left: 0; }
#pb_step_tbl .gt_column_spanner_outer:last-child { padding-right: 0; }
#pb_step_tbl .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
#pb_step_tbl .gt_spanner_row { border-bottom-style: hidden; }
#pb_step_tbl .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
#pb_step_tbl .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
#pb_step_tbl .gt_from_md&gt; :first-child { margin-top: 0; }
#pb_step_tbl .gt_from_md&gt; :last-child { margin-bottom: 0; }
#pb_step_tbl .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
#pb_step_tbl .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
#pb_step_tbl .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
#pb_step_tbl .gt_row_group_first td { border-top-width: 2px; }
#pb_step_tbl .gt_row_group_first th { border-top-width: 2px; }
#pb_step_tbl .gt_striped { color: #333333; background-color: #F4F4F4; }
#pb_step_tbl .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
#pb_step_tbl .gt_grand_summary_row { color: #333333; background-color: #FFFFFF; text-transform: inherit; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; }
#pb_step_tbl .gt_first_grand_summary_row_bottom { border-top-style: double; border-top-width: 6px; border-top-color: #D3D3D3; }
#pb_step_tbl .gt_last_grand_summary_row_top { border-bottom-style: double; border-bottom-width: 6px; border-bottom-color: #D3D3D3; }
#pb_step_tbl .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
#pb_step_tbl .gt_sourcenote { font-size: 12px; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
#pb_step_tbl .gt_left { text-align: left; }
#pb_step_tbl .gt_center { text-align: center; }
#pb_step_tbl .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
#pb_step_tbl .gt_font_normal { font-weight: normal; }
#pb_step_tbl .gt_font_bold { font-weight: bold; }
#pb_step_tbl .gt_font_italic { font-style: italic; }
#pb_step_tbl .gt_super { font-size: 65%; }
#pb_step_tbl .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
#pb_step_tbl .gt_asterisk { font-size: 100%; vertical-align: 0; }</p>
</style>
<table style="table-layout: fixed;; width: 0px" class="gt_table" data-quarto-disable-processing="true" data-quarto-bootstrap="false">
<colgroup>
  <col style="width:40px;"/>
  <col style="width:190px;"/>
  <col style="width:190px;"/>
  <col style="width:40px;"/>
  <col style="width:190px;"/>
  <col style="width:30px;"/>
  <col style="width:190px;"/>
  <col style="width:30px;"/>
</colgroup>
<thead>
<tr class="gt_col_headings gt_spanner_row">
  <th class="gt_center gt_columns_top_border gt_column_spanner_outer" rowspan="1" colspan="3" scope="colgroup" id="pb_step_tbl-TARGET">
    <span class="gt_column_spanner">TARGET</span>
  </th>
  <th class="gt_center gt_columns_top_border gt_column_spanner_outer" rowspan="1" colspan="5" scope="colgroup" id="pb_step_tbl-EXPECTED">
    <span class="gt_column_spanner">EXPECTED</span>
  </th>
</tr>
<tr class="gt_col_headings">
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="pb_step_tbl-index_target"></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="pb_step_tbl-col_name_target">COLUMN</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="pb_step_tbl-dtype_target">DATA TYPE</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_right" rowspan="1" colspan="1" scope="col" id="pb_step_tbl-index_exp"></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="pb_step_tbl-col_name_exp">COLUMN</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="pb_step_tbl-col_name_exp_correct"></th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="pb_step_tbl-dtype_exp">DATA TYPE</th>
  <th class="gt_col_heading gt_columns_bottom_border gt_left" rowspan="1" colspan="1" scope="col" id="pb_step_tbl-dtype_exp_correct"></th>
</tr>
</thead>
<tbody class="gt_table_body">
  <tr>
    <td style="font-size: 13px;" class="gt_row gt_right">1</td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">user_id</td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">Int64</td>
    <td style="font-size: 13px; border-left: 3px double #E5E5E5;" class="gt_row gt_right">1</td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">user_id</td>
    <td class="gt_row gt_left"><span style='color: #4CA64C;'>✓</span></td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">Int64</td>
    <td class="gt_row gt_left"><span style='color: #4CA64C;'>✓</span></td>
  </tr>
  <tr>
    <td style="font-size: 13px;" class="gt_row gt_right">2</td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">age</td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">Int64</td>
    <td style="font-size: 13px; border-left: 3px double #E5E5E5;" class="gt_row gt_right">2</td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">age</td>
    <td class="gt_row gt_left"><span style='color: #4CA64C;'>✓</span></td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">Int64</td>
    <td class="gt_row gt_left"><span style='color: #4CA64C;'>✓</span></td>
  </tr>
  <tr>
    <td style="font-size: 13px;" class="gt_row gt_right">3</td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">email</td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">String</td>
    <td style="font-size: 13px; border-left: 3px double #E5E5E5;" class="gt_row gt_right">3</td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">email</td>
    <td class="gt_row gt_left"><span style='color: #4CA64C;'>✓</span></td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">String</td>
    <td class="gt_row gt_left"><span style='color: #4CA64C;'>✓</span></td>
  </tr>
  <tr>
    <td style="font-size: 13px;" class="gt_row gt_right">4</td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">score</td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">Float64</td>
    <td style="font-size: 13px; border-left: 3px double #E5E5E5;" class="gt_row gt_right">4</td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">score</td>
    <td class="gt_row gt_left"><span style='color: #4CA64C;'>✓</span></td>
    <td style="color: black;font-family: IBM Plex Mono;font-size: 13px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden;" class="gt_row gt_left">Float64</td>
    <td class="gt_row gt_left"><span style='color: #4CA64C;'>✓</span></td>
  </tr>
</tbody>
  <tfoot class="gt_sourcenotes">
  <tr>
    <td class="gt_sourcenote" colspan="8"><div style='padding-bottom: 2px;'>Supplied Column Schema:</div><div style='border-style: solid; border-width: thin; border-color: lightblue; padding-left: 2px; padding-right: 2px; padding-bottom: 3px;'><code style='color: #303030; font-family: monospace; font-size: 8px;'>[('user_id', 'Int64'), ('age', 'Int64'), ('email', 'String'), ('score', 'Float64')]</code></div></td>
  </tr>
  <tr>
    <td class="gt_sourcenote" colspan="8">
<div style='padding-bottom: 2px;'>Schema Match Settings</div>
<div style='padding-bottom: 4px;'><div style="display: flex; font-size: 13.7px; padding-top: 2px;"><div style="border-style: solid; border-width: 1px; border-color: #87CEFA; border-radius: 5px; background-color: #F0F8FF; font-size: x-small; padding-left: 4px; padding-right: 4px; margin-left: 5px; margin-right: 5px;  margin-top: 2px; ">COMPLETE</div><div style="border-style: solid; border-width: 1px; border-color: #87CEFA; border-radius: 5px; background-color: #F0F8FF; font-size: x-small; padding-left: 4px; padding-right: 4px; margin-left: 5px; margin-right: 5px;  margin-top: 2px; ">IN ORDER</div><div style="border-style: solid; border-width: 1px; border-color: #A9A9A9; border-radius: 5px; background-color: #F5F5F5; font-size: x-small; padding-left: 4px; padding-right: 4px; margin-left: 5px; margin-right: 5px;  margin-top: 2px; ">COLUMN &ne; column</div><div style="border-style: solid; border-width: 1px; border-color: #A9A9A9; border-radius: 5px; background-color: #F5F5F5; font-size: x-small; padding-left: 4px; padding-right: 4px; margin-left: 5px; margin-right: 5px;  margin-top: 2px; ">DTYPE &ne; dtype</div><div style="border-style: solid; border-width: 1px; border-color: #A9A9A9; border-radius: 5px; background-color: #F5F5F5; font-size: x-small; padding-left: 4px; padding-right: 4px; margin-left: 5px; margin-right: 5px;  margin-top: 2px; ">float &ne; float64</div></div></div>
</td>
  </tr>
</tfoot>
</table>
</div>
</div>
</details>
</td>
  </tr>

</tfoot>

</table>

</div>

This example demonstrates Pointblank's chainable validation approach where each validation step is
clearly defined and can be configured with different threshold levels. The resulting validation
object provides rich, interactive reporting that shows not just what passed or failed, but detailed
statistics about the validation process. The threshold system allows for nuanced responses to data
quality issues.

### Comparisons

Unlike Pandera's schema-first approach, Pointblank focuses on step-by-step validation with detailed
reporting and flexible failure thresholds that can be set at both the global and individual
validation step level. Both Pointblank and Validoopsie use numeric threshold values for granular
control over acceptable failure rates, but they differ in their primary focus: Pointblank emphasizes
comprehensive reporting and stakeholder communication, while Validoopsie prioritizes operational
resilience through its impact level system (low/medium/high) that controls whether threshold
breaches are logged, reported, or raise exceptions.

While both libraries support custom validation logic, Pointblank's `specially()` method integrates
seamlessly with its reporting system, whereas Validoopsie provides a structured framework for
creating custom validation classes that fit into its modular validation catalog.

### Unique Strengths and When to Use

- beautiful, interactive HTML reports perfect for sharing with stakeholders
- threshold-based alerting system with configurable actions
- segmented validation for analyzing subsets of data
- LLM-powered validation suggestions via `DraftValidation`
- comprehensive data inspection tools and summary tables
- step-by-step validation reporting with detailed failure analysis (via `.get_step_report()`)

Data practitioners might want to choose Pointblank when stakeholder communication and comprehensive
data quality reporting are priorities. Because of the reporting tables it can generate, it's
well-suited for data teams that need to regularly report on data quality to relevant stakeholders.
Pointblank also excels in production data monitoring scenarios, data observability workflows, and
situations where understanding the nuances of data quality issues matters more than simple pass/fail
validation.

## 4. Validoopsie: Composable Checks with Smart Failure Handling

Validoopsie is built around composable validation principles, providing a toolkit for creating
reusable validation functions organized into logical modules. Drawing inspiration from Great
Expectations but with a much lighter footprint, Validoopsie emphasizes building validation logic
from modular, testable components that can be combined in flexible ways to create complex validation
workflows. The library had Polars support from its very first release (early-2025).

What sets Validoopsie apart is its sophisticated approach to handling validation failures through
*impact levels* and *threshold tolerances*. These features that give you fine-grained control over
how your validation pipeline behaves when things go wrong.

### Example

``` python
from validoopsie import Validate
from narwhals.dtypes import Int64, Float64, String

# Composable validation checks with impact levels and thresholds
validation = (
    Validate(user_data)
    .ValuesValidation.ColumnValuesToBeBetween(
        column="user_id",
        min_value=0,
        impact="high"  # Critical - will raise exception
    )
    .ValuesValidation.ColumnValuesToBeBetween(
        column="age",
        min_value=18,
        max_value=80,
        threshold=0.1,  # Allow 10% failures
        impact="medium"  # Important but not critical
    )
    .StringValidation.PatternMatch(
        column="email",
        pattern=r"^[^@]+@[^@]+\.[^@]+$",
        threshold=0.05,  # Allow 5% malformed emails
        impact="low"  # Record but don't interrupt
    )
    .ValuesValidation.ColumnValuesToBeBetween(
        column="score",
        min_value=0,
        max_value=100,
        impact="medium"
    )
    .TypeValidation.TypeCheck(
        frame_schema_definition={
            "user_id": Int64,
            "age": Int64,
            "email": String,
            "score": Float64
        },
        impact="high"  # Schema compliance is critical
    )
)

# Get validation results
validation.validate()

# Access detailed results for analysis
print("Validation results:", validation.results)
```

<pre><span class="ansi-green-fg">2026-03-13 12:11:23.468</span> | <span class="ansi-bold">INFO    </span> | <span class="ansi-cyan-fg">validoopsie.validate</span>:<span class="ansi-cyan-fg">validate</span>:<span class="ansi-cyan-fg">414</span> - <span class="ansi-bold">Passed validation: {'validation': 'ColumnValuesToBeBetween', 'impact': 'high', 'timestamp': '2026-03-13T12:11:23.435459-07:00', 'column': 'user_id', 'result': {'status': 'Success', 'threshold_pass': True, 'message': 'All items passed the validation.', 'frame_row_number': 5, 'threshold': 0.0}}</span>

<span class="ansi-green-fg">2026-03-13 12:11:23.469</span> | <span class="ansi-red-fg ansi-bold">ERROR   </span> | <span class="ansi-cyan-fg">validoopsie.validate</span>:<span class="ansi-cyan-fg">validate</span>:<span class="ansi-cyan-fg">406</span> - <span class="ansi-red-fg ansi-bold">Failed validation: ColumnValuesToBeBetween_age - The column 'age' has values that are not between 18 and 80.</span>

<span class="ansi-green-fg">2026-03-13 12:11:23.469</span> | <span class="ansi-yellow-fg ansi-bold">WARNING </span> | <span class="ansi-cyan-fg">validoopsie.validate</span>:<span class="ansi-cyan-fg">validate</span>:<span class="ansi-cyan-fg">408</span> - <span class="ansi-yellow-fg ansi-bold">Failed validation: PatternMatch_email - The column 'email' has entries that do not match the pattern '^[^@]+@[^@]+\.[^@]+$'.</span>

<span class="ansi-green-fg">2026-03-13 12:11:23.469</span> | <span class="ansi-bold">INFO    </span> | <span class="ansi-cyan-fg">validoopsie.validate</span>:<span class="ansi-cyan-fg">validate</span>:<span class="ansi-cyan-fg">414</span> - <span class="ansi-bold">Passed validation: {'validation': 'ColumnValuesToBeBetween', 'impact': 'medium', 'timestamp': '2026-03-13T12:11:23.438392-07:00', 'column': 'score', 'result': {'status': 'Success', 'threshold_pass': True, 'message': 'All items passed the validation.', 'frame_row_number': 5, 'threshold': 0.0}}</span>

<span class="ansi-green-fg">2026-03-13 12:11:23.469</span> | <span class="ansi-bold">INFO    </span> | <span class="ansi-cyan-fg">validoopsie.validate</span>:<span class="ansi-cyan-fg">validate</span>:<span class="ansi-cyan-fg">414</span> - <span class="ansi-bold">Passed validation: {'validation': 'TypeCheck', 'impact': 'high', 'timestamp': '2026-03-13T12:11:23.438814-07:00', 'column': 'DataTypeColumnValidation', 'result': {'status': 'Success', 'threshold_pass': True, 'message': 'All items passed the validation.', 'frame_row_number': 4, 'threshold': 0.0}}</span>
</pre>

    Validation results: {'Summary': {'passed': False, 'validations': ['ColumnValuesToBeBetween_user_id', 'ColumnValuesToBeBetween_age', 'PatternMatch_email', 'ColumnValuesToBeBetween_score', 'TypeCheck_DataTypeColumnValidation'], 'failed_validation': ['ColumnValuesToBeBetween_age', 'PatternMatch_email']}, 'ColumnValuesToBeBetween_user_id': {'validation': 'ColumnValuesToBeBetween', 'impact': 'high', 'timestamp': '2026-03-13T12:11:23.435459-07:00', 'column': 'user_id', 'result': {'status': 'Success', 'threshold_pass': True, 'message': 'All items passed the validation.', 'frame_row_number': 5, 'threshold': 0.0}}, 'ColumnValuesToBeBetween_age': {'validation': 'ColumnValuesToBeBetween', 'impact': 'medium', 'timestamp': '2026-03-13T12:11:23.437027-07:00', 'column': 'age', 'result': {'status': 'Fail', 'threshold_pass': False, 'message': "The column 'age' has values that are not between 18 and 80.", 'failing_items': [95], 'failed_number': 1, 'frame_row_number': 5, 'threshold': 0.1, 'failed_percentage': 0.2}}, 'PatternMatch_email': {'validation': 'PatternMatch', 'impact': 'low', 'timestamp': '2026-03-13T12:11:23.437565-07:00', 'column': 'email', 'result': {'status': 'Fail', 'threshold_pass': False, 'message': "The column 'email' has entries that do not match the pattern '^[^@]+@[^@]+\\.[^@]+$'.", 'failing_items': ['invalid-email'], 'failed_number': 1, 'frame_row_number': 5, 'threshold': 0.05, 'failed_percentage': 0.2}}, 'ColumnValuesToBeBetween_score': {'validation': 'ColumnValuesToBeBetween', 'impact': 'medium', 'timestamp': '2026-03-13T12:11:23.438392-07:00', 'column': 'score', 'result': {'status': 'Success', 'threshold_pass': True, 'message': 'All items passed the validation.', 'frame_row_number': 5, 'threshold': 0.0}}, 'TypeCheck_DataTypeColumnValidation': {'validation': 'TypeCheck', 'impact': 'high', 'timestamp': '2026-03-13T12:11:23.438814-07:00', 'column': 'DataTypeColumnValidation', 'result': {'status': 'Success', 'threshold_pass': True, 'message': 'All items passed the validation.', 'frame_row_number': 4, 'threshold': 0.0}}}

This example showcases Validoopsie's key differentiators: modular validation categories
(`ValuesValidation`, `StringValidation`, `TypeValidation`) combined with *impact levels* that
control failure behavior and *thresholds* that allow controlled tolerance for data quality issues.
Unlike other libraries that treat all validation failures equally, Validoopsie lets you specify
which validations are critical ("high" impact raises exceptions) versus informational ("low" impact
just logs results).

Validoopsie's most powerful feature is its three-tier `impact=` system combined with `threshold=`
tolerance:

``` python
# Example showing sophisticated failure handling
validation = (
    Validate(user_data)
    # Critical validation - no tolerance
    .NullValidation.ColumnNotBeNull(
        column="user_id",
        impact="high"    # Will raise an exception if any Null values found
    )
    # Important validation with tolerance
    .StringValidation.PatternMatch(
        column="email",
        pattern=r"^[^@]+@[^@]+\.[^@]+$",
        threshold=0.15,  # Allow up to 15% malformed emails
        impact="medium"  # Log failures but don't stop processing
    )
    # Informational validation
    .ValuesValidation.ColumnValuesToBeBetween(
        column="score",
        min_value=90,
        max_value=100,
        threshold=0.8,  # Allow 80% to be outside "excellent" range
        impact="low"    # Just track high performers
    )
)

validation.validate()
```

<pre><span class="ansi-green-fg">2026-03-13 12:11:23.476</span> | <span class="ansi-bold">INFO    </span> | <span class="ansi-cyan-fg">validoopsie.validate</span>:<span class="ansi-cyan-fg">validate</span>:<span class="ansi-cyan-fg">414</span> - <span class="ansi-bold">Passed validation: {'validation': 'ColumnNotBeNull', 'impact': 'high', 'timestamp': '2026-03-13T12:11:23.474893-07:00', 'column': 'user_id', 'result': {'status': 'Success', 'threshold_pass': True, 'message': 'All items passed the validation.', 'frame_row_number': 5, 'threshold': 0.0}}</span>

<span class="ansi-green-fg">2026-03-13 12:11:23.477</span> | <span class="ansi-red-fg ansi-bold">ERROR   </span> | <span class="ansi-cyan-fg">validoopsie.validate</span>:<span class="ansi-cyan-fg">validate</span>:<span class="ansi-cyan-fg">406</span> - <span class="ansi-red-fg ansi-bold">Failed validation: PatternMatch_email - The column 'email' has entries that do not match the pattern '^[^@]+@[^@]+\.[^@]+$'.</span>

<span class="ansi-green-fg">2026-03-13 12:11:23.477</span> | <span class="ansi-bold">INFO    </span> | <span class="ansi-cyan-fg">validoopsie.validate</span>:<span class="ansi-cyan-fg">validate</span>:<span class="ansi-cyan-fg">414</span> - <span class="ansi-bold">Passed validation: {'validation': 'ColumnValuesToBeBetween', 'impact': 'low', 'timestamp': '2026-03-13T12:11:23.476300-07:00', 'column': 'score', 'result': {'status': 'Success', 'threshold_pass': True, 'message': "The column 'score' has values that are not between 90 and 100.", 'failing_items': [78.3, 85.5, 88.7], 'failed_number': 3, 'frame_row_number': 5, 'threshold': 0.8, 'failed_percentage': 0.6}}</span>
</pre>

Validoopsie strikes a unique balance between operational flexibility and production reliability,
making it an excellent choice for teams that need sophisticated failure handling without the
complexity of larger validation frameworks.

### Comparisons

Validoopsie's functional approach contrasts with Pandera's schema-centric methodology and Patito's
object-oriented models. While Pandera focuses on statistical validation and Patito emphasizes
Pydantic integration, Validoopsie prioritizes flexibility and operational robustness.

Compared to Pointblank, both libraries offer sophisticated threshold-based failure handling using
numeric values (e.g., 0.1 for 10% tolerance), but they differ in their architectural approach:
Validoopsie combines numeric thresholds with impact levels (low/medium/high) that control the
behavioral response to threshold breaches, while Pointblank integrates thresholds directly into its
comprehensive reporting and alerting system. Both support custom validation, but Validoopsie uses a
modular validation catalog approach while Pointblank's `specially()` method integrates seamlessly
with its step-by-step reporting workflow.

Validoopsie is the only library in this survey that provides built-in logging capabilities, making
it particularly valuable for production environments where validation events need to be tracked and
monitored.

The library's Great Expectations inspiration is evident in its modular design, but Validoopsie
delivers this functionality with a much lighter dependency footprint and simpler API. Teams
familiar with Great Expectations will find Validoopsie's approach familiar but more streamlined.

### Unique Strengths and When to Use

Validoopsie's standout features include:

- graduated failure handling through impact levels (low/medium/high) combined with numeric
  thresholds that control both tolerance levels and behavioral responses to failures
- numeric threshold tolerance allowing controlled acceptance of data quality issues (e.g., "allow
  10% email format failures" with `threshold=0.1`)
- built-in structured logging using loguru allows for automatic logging of validation results,
  failures, and performance metrics (unique among these libraries)
- being a lightweight Great Expectations alternative with similar composability but minimal
  dependencies
- an extensive validation catalog organized into logical namespaces (Date, String, Null, Values,
  etc.)
- custom validation framework with consistent patterns for creating domain-specific rules

Choose Validoopsie when you need:

- operational resilience in production pipelines where partial data quality issues shouldn't
  stop processing
- comprehensive validation logging and monitoring for observability in production environments
- fine-grained control over validation failure behavior with different criticality levels
- lightweight Great Expectations functionality without the complexity and dependencies
- custom validation development with a clear, consistent framework
- modular validation design that promotes reusability across projects

Validoopsie is particularly well-suited for data engineering teams building robust production
pipelines where data quality monitoring is important but pipeline availability is critical. Its
impact/threshold system makes it uniquely powerful for environments where you need to distinguish
between "nice to have" and "must have" data quality requirements.

## 5. Dataframely: Type-Safe Schema Validation with Advanced Features

Dataframely is a comprehensive data validation framework that brings type-safe schema validation to
Polars DataFrames with some of the most advanced features in the ecosystem. The library focuses on
providing both runtime validation and static type checking, with particular strengths in
collection validation for related DataFrames and extensive integration capabilities with external
tools.

Dataframely launched in early 2025 with native Polars support as a core feature, built specifically
for the modern data ecosystem with first-class support for complex validation scenarios.

### Example

``` python
import polars as pl
import dataframely as dy

class UserSchema(dy.Schema):
    user_id = dy.Int64(primary_key=True, min=1, nullable=False)
    age = dy.Int64(nullable=False)
    email = dy.String(nullable=False, regex=r"^[^@]+@[^@]+\.[^@]+$")
    score = dy.Float64(nullable=False, min=0.0, max=100.0)

    # Use @dy.rule() for age range validation
    @dy.rule()
    def age_in_range(cls) -> pl.Expr:
        return pl.col("age").is_between(18, 80, closed="both")

# Validate using the schema
try:
    validated_data = UserSchema.validate(user_data, cast=True)
    print("Validation successful!")
    print(validated_data)
except Exception as e:
    print(f"Validation failed: {e}")
```

This example showcases Dataframely's class-based schema approach with several notable features:
primary key constraints, comprehensive type validation with bounds, regex pattern matching, and
custom validation rules using the `@dy.rule()` decorator (used here for age range checking).

The `cast=True` parameter automatically coerces column types to match the schema definitions. This
is really useful when working with data from external sources where column types might not exactly
match your schema expectations (e.g., integers loaded as strings from CSV files).

Dataframely features soft validation and failure introspection. As one of Dataframely's standout
features, it brings a fairly sophisticated approach to validation failures. Rather than just raising
exceptions, it provides detailed failure analysis:

``` python
# Soft validation: separate valid and invalid rows
good_data, failure_info = UserSchema.filter(user_data, cast=True)

print("Valid rows:", len(good_data))
print("Failure counts:", failure_info.counts())
print("Co-occurrence analysis:", failure_info.cooccurrence_counts())

# Inspect the actual failed rows
failed_rows = failure_info.invalid()
print("Failed data:", failed_rows)
```

### Comparisons

While both Dataframely and Pandera offer schema-centric validation approaches, they serve different
validation philosophies. Pandera excels in statistical validation with hypothesis testing and
distribution checks, making it ideal for data science workflows where statistical properties matter.
Dataframely, by contrast, emphasizes relational data integrity and type safety, providing more
sophisticated failure analysis and collection-level validation capabilities that Pandera doesn't
offer.

The relationship between Dataframely and Patito is particularly interesting since both use
class-based schema definitions. However, Dataframely extends far beyond Patito's Pydantic-focused
approach. Where Patito provides clean, simple validation with excellent Pydantic integration,
Dataframely offers advanced features like collection validation, group rules, and comprehensive
failure introspection. Teams already invested in Pydantic workflows might prefer Patito's
simplicity, while those building complex data systems will appreciate Dataframely's feature set.

Dataframely and Pointblank represent two different approaches to comprehensive data validation.
Pointblank shines in stakeholder communication with its beautiful interactive reports and
threshold-based alerting systems, making it perfect for data quality reporting. Dataframely focuses
instead on type safety and complex validation logic, with unique collection validation capabilities
that no other library in this survey provides. The choice between these two will comes down to
whether your priority is communicating validation results or ensuring complex data relationships
remain consistent.

When compared to Validoopsie's method chaining approach, Dataframely offers a more structured,
schema-centric methodology with advanced type safety features that Validoopsie doesn't provide.
While Validoopsie excels in operational flexibility and lightweight design for building reusable
validation components, Dataframely's strength lies in its comprehensive type system integration,
collection validation capabilities, and sophisticated failure analysis. And that makes it ideal for
complex data engineering workflows where relationships between multiple DataFrames matter as much as
individual DataFrame validation.

### Unique Strengths and When to Use

Dataframely's standout features include:

- advanced type safety with full mypy integration and generic DataFrame types
- collection validation for ensuring consistency across related DataFrames
- group-based validation rules using `@dy.rule(group_by=[...])` for aggregate constraints
- schema inheritance for reducing code duplication in related schemas
- production-ready soft validation that separates valid and invalid data

One might choose Dataframely when building complex data systems where:

- type safety and static analysis are critical for code quality
- you need to validate relationships between multiple related DataFrames
- you're working with production pipelines that need to handle partial data quality issues
  gracefully
- schema reuse and inheritance would benefit your codebase organization

Dataframely is particularly well-suited for data engineering teams building robust, type-safe data
pipelines where the relationships between different data entities are as important as the validation
of individual DataFrames. Its collection validation capabilities make it uniquely powerful for
ensuring referential integrity in complex data workflows.

## Choosing the Right Library

With five solid validation libraries to choose from, the decision often comes down to your team's
specific workflow, existing tech stack, and validation requirements. Here are some practical
considerations to help guide your choice:

*Start with your existing tools*

If you're already using Pydantic extensively, Patito will feel natural. Teams that are heavily
invested in type checking and statistical analysis should probably gravitate toward Pandera. If
you're building data products that need stakeholder buy-in, Pointblank's reporting capabilities
become incredibly useful in that context. For teams already committed to strong typing and static
analysis workflows, Dataframely's advanced type safety features will feel like a natural extension
of your existing practices.

*Consider your validation complexity*

For straightforward schema validation and type checking, any of these libraries will work well. But
if you need statistical hypothesis testing, Pandera is your best bet. For highly custom validation
logic that needs to be composed and reused, Validoopsie shines. When validation results need to be
communicated to non-technical stakeholders, Pointblank's interactive reports are basically
unmatched. If you're dealing with complex relational data where multiple DataFrames need to maintain
consistency with each other, Dataframely's collection validation capabilities are unique in the
ecosystem.

*Think about failure tolerance requirements*

One of the most important architectural differences among these libraries is how they handle
validation failures. Only Pointblank and Validoopsie offer numeric threshold-based failure
tolerance. This is the ability to accept a controlled percentage of validation failures without
treating the entire validation as failed.

This distinction can be crucial for production environments where some level of data quality issues
is acceptable and you need fine-grained control over when validations should fail versus warn. In
many real-world scenarios, poor data quality is a given reality, and the goal becomes gradually
improving quality over time rather than enforcing perfection. Thresholds can then be seen not as
simple failure tolerances but more like data quality metrics and improvement goals (e.g., you might
start with `threshold=0.15` for email validation and progressively tighten to `0.05` as upstream
systems improve).

*Think about your team's preferences*

There's a human dimension here. Some data teams might prefer the declarative, schema-first approach
of Pandera, Patito, and Dataframely, whereas others like the step-by-step, method-chaining style of
Pointblank and Validoopsie. There's really no right or wrong choice here. It's all about what feels
right and most natural for your team's coding style and mental model.

*Don't feel locked into one choice*

My hunch is that many teams already successfully use different libraries for different parts of
their data pipeline. They're leveraging each tool's strengths where they matter most. So you could
conceivably use Patito for Pydantic-style validation, Pandera for statistical checks in your
analysis pipeline, Pointblank for generating stakeholder reports, and Dataframely for complex data
engineering workflows (use 'em all!). This multi-library approach can be particularly effective in
larger organizations with diverse validation needs.

I suppose the key is to start with one library that fits your immediate needs, learn it well, and
then consider expanding your toolkit as your validation requirements evolve.

## Summary and Wrapping Up

The Python ecosystem offers truly excellent options for validating Polars DataFrames! Choosing is
always tough but this is how one could make the decision based on specific needs:

- for type-safe pipelines, **Pandera**, **Dataframely**, or **Patito** are ideal
- for stakeholder reporting, **Pointblank** is a great choice
- for row-level object modeling, go with **Patito**
- for statistical validation, **Pandera** is perfect
- for data quality improvement, **Pointblank** or **Validoopsie** fit well

Each library has evolved to serve different aspects of the data validation ecosystem. Try them all
and, with a little understanding of their strengths, you'll get good at picking the right data
validation tool for your specific use case.

This survey represents our understanding of these libraries as of mid-2025. Given the rapid pace of
development in the Python data ecosystem, some details may become outdated or contain inaccuracies
(we may have even gotten things wrong at the outset). If you notice any errors or have updates to
share, we'd love to hear from you! Please reach out through:

- [GitHub Issues](https://github.com/posit-dev/pointblank/issues)
- [GitHub Discussions](https://github.com/posit-dev/pointblank/discussions)
- Our [Discord Server](https://discord.com/invite/YH7CybCNCQ)

Any feedback you provide helps keep this resource accurate and useful for the community!
