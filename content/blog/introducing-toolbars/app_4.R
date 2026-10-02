library(shiny)
library(bslib)

ui <- page_fluid(
  h2("Example App"),
  layout_columns(
    card(
      card_header(
        "Sales Data",
        toolbar(
          align = "right",
          toolbar_input_select(
            id = "data_filter",
            label = "Region",
            choices = c("All", "North", "South", "East", "West"),
            icon = icon("filter"),
            tooltip = "Region"
          ),
          toolbar_input_button(
            id = "toggle_filter",
            label = "Switch to Product",
            icon = icon("right-left"),
            tooltip = "Switch to filtering by Product"
          ),
          toolbar_divider(),
          toolbar_input_button(
            id = "save_btn",
            label = "Save",
            icon = icon("floppy-disk")
          )
        )
      ),
      card_body(
        tableOutput("sales_table")
      )
    ),
    card(
      card_header(
        "Toolbar in header, footer, label"
      ),
      card_body(
        p("More placeholder text.")
      ),
      card_footer(
        toolbar(
          align = "right",
          toolbar_input_button(
            id = "share_btn",
            label = "Share",
            icon = icon("share-nodes"),
            show_label = TRUE
          ),
          toolbar_input_button(
            id = "export_btn",
            label = "Export",
            icon = icon("download")
          )
        )
      )
    ),
    col_widths = c(6, 6)
  ),
  card(
    card_header(
      "Toolbar in Text Input Submit Area: Message Composer"
    ),
    card_body(
      layout_columns(
        p("Placeholder for an input"),
        div(
          p("Placeholder for outputs")
        ),
        col_widths = c(6, 6)
      )
    )
  )
)

server <- function(input, output, session) {
  # Track current filter mode

  filter_mode <- reactiveVal("Region")

  # Handle save button click
  observeEvent(input$save_btn, {
    update_toolbar_input_button(
      "save_btn",
      icon = icon("check"),
      label = "Saved"
    )
    showNotification("Saving", type = "message")
  })

  # Handle toggle filter button click
  observeEvent(input$toggle_filter, {
    if (filter_mode() == "Region") {
      filter_mode("Product")
      update_toolbar_input_select(
        "data_filter",
        label = "Product",
        choices = c("All", "Widget A", "Widget B", "Widget C", "Widget D"),
        selected = "All"
      )
      update_toolbar_input_button(
        "toggle_filter",
        label = "Switch to Region"
      )
      update_tooltip("toggle_filter_tooltip", "Switch to filtering by Region")
      update_tooltip("data_filter_tooltip", "Product")
    } else {
      filter_mode("Region")
      update_toolbar_input_select(
        "data_filter",
        label = "Region",
        choices = c("All", "North", "South", "East", "West"),
        selected = "All"
      )
      update_toolbar_input_button(
        "toggle_filter",
        label = "Switch to Product"
      )
      update_tooltip("toggle_filter_tooltip", "Switch to filtering by Product")
      update_tooltip("data_filter_tooltip", "Region")
    }
  })

  # Sample sales data
  sales_data <- reactive({
    data.frame(
      Product = c("Widget A", "Widget B", "Widget C", "Widget D"),
      Region = c("North", "South", "East", "West"),
      Sales = c(1200, 850, 1450, 920),
      stringsAsFactors = FALSE
    )
  })

  # Filtered sales data based on current filter
  filtered_data <- reactive({
    data <- sales_data()

    if (input$data_filter != "All") {
      if (filter_mode() == "Region") {
        data <- data[data$Region == input$data_filter, ]
      } else {
        data <- data[data$Product == input$data_filter, ]
      }
    }

    data
  })

  # Render the table
  output$sales_table <- renderTable({
    data <- filtered_data()
    if (nrow(data) > 0) {
      data$Sales <- paste0("$", format(data$Sales, big.mark = ",", trim = TRUE))
    }
    data
  })
}

shinyApp(ui, server)
