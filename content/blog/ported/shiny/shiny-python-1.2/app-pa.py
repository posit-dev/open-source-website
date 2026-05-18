import great_tables as gt
import pyarrow as pa

from shiny.express import render, ui

pa_data = pa.Table.from_pandas(gt.data.sp500)

ui.h3("S&P 500 (PyArrow)")


@render.data_frame
def pa_df():
    return pa_data
