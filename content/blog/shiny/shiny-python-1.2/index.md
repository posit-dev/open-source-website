---
title: Shiny for Python 1.2.0
description: >-
  Shiny's `@render.data_frame` has a new integration with `narwhals`, gaining
  support for multiple data frame types!
people:
  - Shiny Team
date: '2024-10-31'
image: shinyforpython-120.jpg
image-alt: Shiny for Python 1.2.0
ported_from: shiny
port_status: in-progress
---


Shiny for Python `v1.2.0` is here! To celebrate, let's highlight a big new feature of this release: integration with [`narwhals`](https://narwhals-dev.github.io/narwhals/) for `@render.data_frame`! 🐳🦄

In a follow up post, we'll also highlight another new exciting feature: integration with brand new [`brand-yml`](https://github.com/posit-dev/brand-yml) package for theming.

For a full list of all the changes in this release, check out the [CHANGELOG](https://github.com/posit-dev/py-shiny/blob/main/CHANGELOG.md#120---2024-10-29).

> **What is Shiny for Python?**
>
> Shiny for Python is a framework that makes it easy to build interactive web applications using Python ([Quick Start](https://shiny.posit.co/py/docs/)). You can create web applications directly from your Python code without needing to know any Javascript. Shiny is built on a [reactive programming model](https://shiny.posit.co/py/docs/reactive-foundations.html), meaning that Shiny automatically figures out the relationships between different components in your application. When a user interacts with your application, Shiny will only update the necessary parts. This ensures that your applications stay fast and responsive even as they grow in size and complexity.

------------------------------------------------------------------------

## `narwhals` integration

In the Shiny `v1.0.0` release, `@render.data_frame` added support for [Polars](https://docs.pola.rs/) data frames (in addition to the existing support for [pandas](https://pandas.pydata.org/) data frames). This was performed through custom inspection and handling for the two supported data frame types. While this worked, it was not ideal for users who wanted use a *new* data frame type. This would require Shiny to implement custom code for each new data frame type of which we are not experts. This approach does not scale well!

In Shiny `v1.2.0`, `@render.data_frame` integrated with [narwhals](https://narwhals-dev.github.io/narwhals/) better data frame support! 🥳🥳

![](narwhals_w_shiny.jpeg)

`narwhals` describes itself as an *"Extremely lightweight and extensible compatibility layer between dataframe libraries!"* that can *"Seamlessly support all, without depending on any!"*. `narwhals` (as of this blog post) has full API support for eager data frames such as [cuDF](https://docs.rapids.ai/api/cudf/stable/), [Modin](https://modin.readthedocs.io/en/stable/), [pandas](https://pandas.pydata.org/), [Polars](https://docs.pola.rs/), and [PyArrow](https://arrow.apache.org/docs/python/). This means that you can immediately use any of these data frame libraries (even `narwhals` itself) within Shiny's `@render.data_frame` without any updates to Shiny or forcing you to export your data to pandas or Polars. Additionally, as `narwhals` (who is rapidly improving by the day) adds support for new data frame libraries, Shiny will automatically support them as well! As `narwhals` improves, so does Shiny! 🚀

> **Additional Narwhals data frame types**
>
> Narwhals also supports other styles of data frames such as [Dask](https://docs.dask.org/en/stable/) (Lazy-only) and [Ibis](https://docs.ibis-project.org/) and [Vaex](https://vaex.io/docs/index.html) through the DataFrame Interchange Protocol. However, these data frame types are not directly supported within Shiny as they are not *eager* data frames.
>
> Please convert your lazy or interchange data to an eager data frame before returning it within `@render.data_frame`.

Let's look at an example that uses a PyArrow Table (which has never been directly implemented by Shiny) displaying `great_tables`'s S&P 500 data:

**app.py**

``` python
import great_tables as gt
import pyarrow as pa
from shiny.express import render, ui

pa_data = pa.Table.from_pandas(gt.data.sp500)

ui.h3("S&P 500 (PyArrow)")

@render.data_frame
def pa_df():
    return pa_data
```

<figure>
<img src="pa-sp500.gif" class="w-100" alt="PyArrow Table; 16,607 rows" />
<figcaption aria-hidden="true">PyArrow Table; 16,607 rows</figcaption>
</figure>

For a quick demo, Barret Schloerke will talk about the example above and more!

<https://youtu.be/W-_0rkcuB_8>

------------------------------------------------------------------------

## New methods for `@render.data_frame`

In addition to the integration of `narwhals`, we have added new instance methods to `@render.data_frame` objects to make it easier to work with data frames.

- `.update_data(data)`
  - Updates the `.data()` data frame with a new value.
  - The user's sorting and filtering will not be reset. However, all `.cell_patches()` patches (user edits) will be removed.
- `.update_cell_value(value, *, row, col)`
  - Updates a single value of a cell in the data frame.
  - `.cell_patches()` patches which are used to create `.data_patched()` from `.data()`.
- `.data_patched()`
  - Reactive calculation of the `.data()` data frame value with all `.cell_patches()` patches applied.
  - Unlike `.data_view()`, `.data_patched()` will not be affected by user sorting, filtering, or row selections.
  - The new data set can be of completely different types and shape. For typing purposes, it is strongly recommended to use the same type as the original data set.

### Learn more

For a comprehensive overview of new and old data frame features, see the updated articles on [DataGrid](https://shiny.posit.co/py/components/outputs/data-grid/) and [DataTable](https://shiny.posit.co/py/components/outputs/data-table/).

------------------------------------------------------------------------

We're thrilled to bring you these new features and improvements in Shiny for Python 1.2.0. As always, if you have any questions or feedback, please [join us on Discord](https://discord.gg/yMGCamUMnS) or [open an issue on GitHub](https://github.com/posit-dev/py-shiny/issues/new). Happy Shiny-ing!
