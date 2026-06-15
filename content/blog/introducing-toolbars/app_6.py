import pandas as pd
from faicons import icon_svg

from shiny import App, Inputs, Outputs, Session, reactive, render, ui

app_ui = ui.page_fluid(
    ui.h2("Example App"),
    ui.layout_columns(
        ui.card(
            ui.card_header(
                "Sales Data",
                ui.toolbar(
                    ui.toolbar_input_select(
                        id="data_filter",
                        label="Region",
                        choices=["All", "North", "South", "East", "West"],
                        icon=icon_svg("filter"),
                        tooltip="Region",
                    ),
                    ui.toolbar_input_button(
                        id="toggle_filter",
                        label="Switch to Product",
                        icon=icon_svg("right-left"),
                        tooltip="Switch to filtering by Product",
                    ),
                    ui.toolbar_divider(),
                    ui.toolbar_input_button(
                        id="save_btn",
                        label="Save",
                        icon=icon_svg("floppy-disk"),
                    ),
                    align="right",
                ),
            ),
            ui.card_body(ui.output_table("sales_table")),
        ),
        ui.card(
            ui.card_header("Toolbar in Input Label"),
            ui.card_body(
                ui.input_numeric(
                    "quantity",
                    label=ui.toolbar(
                        "Quantity:",
                        ui.toolbar_spacer(),
                        ui.toolbar_input_button(
                            "btn_preset_10",
                            label="10",
                            show_label=True,
                            tooltip="Set to 10",
                        ),
                        ui.toolbar_input_button(
                            "btn_preset_50",
                            label="50",
                            show_label=True,
                            tooltip="Set to 50",
                        ),
                        ui.toolbar_input_button(
                            "btn_preset_100",
                            label="100",
                            show_label=True,
                            tooltip="Set to 100",
                        ),
                        ui.toolbar_divider(),
                        ui.toolbar_input_button(
                            "btn_reset",
                            label="Reset",
                            icon=icon_svg("rotate-left"),
                            tooltip="Reset to 1",
                        ),
                        align="right",
                    ),
                    value=1,
                    min=1,
                    max=1000,
                ),
                ui.output_text("quantity_output"),
            ),
        ),
        col_widths=[6, 6],
    ),
    ui.card(
        ui.card_header("Toolbar in Text Input Submit Area: Message Composer"),
        ui.card_body(
            ui.layout_columns(
                ui.input_submit_textarea(
                    id="message",
                    label="Your message",
                    placeholder="Type your message here...",
                    toolbar=ui.toolbar(
                        ui.toolbar_input_button(
                            id="attach_file",
                            label="Attach",
                            icon=icon_svg("paperclip"),
                        ),
                        ui.toolbar_input_select(
                            id="priority",
                            label="Priority",
                            choices=["Low", "Medium", "High", "Urgent"],
                            icon=icon_svg("flag"),
                        ),
                        ui.toolbar_divider(),
                        ui.toolbar_input_button(
                            id="clear_message",
                            label="Clear",
                            icon=icon_svg("trash"),
                        ),
                        align="left",
                    ),
                ),
                ui.div(
                    ui.h4("Message History"),
                    ui.output_ui("message_history"),
                    style="max-height: 400px; overflow-y: auto;",
                ),
                col_widths=[6, 6],
            ),
        ),
    ),
)


def server(input: Inputs, output: Outputs, session: Session) -> None:
    # Track current filter mode
    filter_mode = reactive.value("Region")

    @reactive.effect
    @reactive.event(input.save_btn)
    def _():
        ui.update_toolbar_input_button(
            "save_btn",
            icon=icon_svg("check"),
            label="Saved",
        )
        ui.notification_show("Saving", type="message")

    # Handle toggle filter button click
    @reactive.effect
    @reactive.event(input.toggle_filter)
    def _():
        if filter_mode() == "Region":
            filter_mode.set("Product")
            ui.update_toolbar_input_select(
                "data_filter",
                label="Product",
                choices=["All", "Widget A", "Widget B", "Widget C", "Widget D"],
                selected="All"
            )
            ui.update_toolbar_input_button(
                "toggle_filter",
                label="Switch to Region",
            )
            ui.update_tooltip("toggle_filter_tooltip", "Switch to filtering by Region")
            ui.update_tooltip("data_filter_tooltip", "Product")
        else:
            filter_mode.set("Region")
            ui.update_toolbar_input_select(
                "data_filter",
                label="Region",
                choices=["All", "North", "South", "East", "West"],
                selected="All"
            )
            ui.update_toolbar_input_button(
                "toggle_filter",
                label="Switch to Product",
            )
            ui.update_tooltip("toggle_filter_tooltip", "Switch to filtering by Product")
            ui.update_tooltip("data_filter_tooltip", "Region")

    # Handle numeric input preset buttons
    @reactive.effect
    @reactive.event(input.btn_preset_10)
    def _():
        ui.update_numeric("quantity", value=10)

    @reactive.effect
    @reactive.event(input.btn_preset_50)
    def _():
        ui.update_numeric("quantity", value=50)

    @reactive.effect
    @reactive.event(input.btn_preset_100)
    def _():
        ui.update_numeric("quantity", value=100)

    @reactive.effect
    @reactive.event(input.btn_reset)
    def _():
        ui.update_numeric("quantity", value=1)

    @render.text
    def quantity_output():
        return f"Current quantity: {input.quantity()}"

    # Sample sales data
    @reactive.calc
    def sales_data():
        return pd.DataFrame(
            {
                "Product": ["Widget A", "Widget B", "Widget C", "Widget D"],
                "Region": ["North", "South", "East", "West"],
                "Sales": [1200, 850, 1450, 920],
            }
        )

    # Filtered sales data based on current filter
    @reactive.calc
    def filtered_data():
        data = sales_data()

        if input.data_filter() != "All":
            if filter_mode() == "Region":
                data = data[data["Region"] == input.data_filter()]
            else:
                data = data[data["Product"] == input.data_filter()]

        return data

    # Render the table
    @render.table
    def sales_table():
        return (
            filtered_data()
            .style.hide(axis="index")
            .format({"Sales": "${:,.0f}"})
            .set_table_styles([
                {"selector": "th", "props": [
                    ("border-bottom", "1px solid black"),
                    ("padding", "8px 6px"),
                    ("text-align", "left"),
                ]},
                {"selector": "td", "props": [
                    ("padding", "6px"),
                ]},
            ])
        )

    # Handle message input with toolbar
    messages = reactive.value([])

    @reactive.effect
    @reactive.event(input.message)
    def _():
        new_message = f"[{input.priority()}] {input.message()}"
        messages.set(messages.get() + [new_message])

    @reactive.effect
    @reactive.event(input.attach_file)
    def _():
        ui.notification_show("File attachment feature clicked", type="message")

    @reactive.effect
    @reactive.event(input.clear_message)
    def _():
        ui.update_text_area("message", value="")

    @render.ui
    def message_history():
        if len(messages.get()) == 0:
            return ui.p("No messages yet")
        else:
            return ui.TagList([
                ui.div(
                    msg,
                    class_="mb-2",
                    style="background-color: #e9ecef; padding: 10px 15px; border-radius: 8px;"
                )
                for msg in messages.get()
            ])


app = App(app_ui, server)
