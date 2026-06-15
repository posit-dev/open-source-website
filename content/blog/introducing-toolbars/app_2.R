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
            id = "region_filter",
            label = "Region",
            choices = c("All", "North", "South", "East", "West"),
            icon = icon("filter")
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
        p("Footer content here.")
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
  # Handle save button click
  observeEvent(input$save_btn, {
    # Change icon to checkmark and show notification
    update_toolbar_input_button(
      "save_btn",
      icon = icon("check"),
      label = "Saved",
      session = session
    )
    showNotification("Saving", type = "message")
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

  # Filtered sales data based on region filter
  filtered_data <- reactive({
    data <- sales_data()

    if (input$region_filter != "All") {
      data <- data[data$Region == input$region_filter, ]
    }

    data
  })

  # Render the table
  output$sales_table <- renderTable({
    data <- filtered_data()
    data$Sales <- paste0("$", format(data$Sales, big.mark = ",", trim = TRUE))
    data
  })
}

shinyApp(ui, server)
