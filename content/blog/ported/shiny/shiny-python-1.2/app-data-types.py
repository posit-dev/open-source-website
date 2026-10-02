import great_tables as gt
import narwhals.stable.v1 as nw
import polars as pl
import pyarrow as pa

from shiny.express import render, ui

pd_data = gt.data.sp500
pl_data = pl.from_pandas(pd_data)
nw_data = nw.from_native(pd_data, eager_only=True)
pa_data = pa.Table.from_pandas(pd_data)

ui.h3("S&P 500")

with ui.navset_card_tab():
    with ui.nav_panel("Pandas"):

        @render.data_frame
        def pd_df():
            return pd_data

    with ui.nav_panel("Polars"):

        @render.data_frame
        def pl_df():
            return pl_data

    with ui.nav_panel("PyArrow"):

        @render.data_frame
        def pa_df():
            return pa_data

    with ui.nav_panel("Narwhals"):

        @render.data_frame
        def nw_df():
            return nw_data
