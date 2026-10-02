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
      card_header("Toolbar in Input Label"),
      card_body(
        numericInput(
          "quantity",
          label = toolbar(
            "Quantity:",
            toolbar_spacer(),
            toolbar_input_button(
              id = "btn_preset_10",
              label = "10",
              show_label = TRUE,
              tooltip = "Set to 10"
            ),
            toolbar_input_button(
              id = "btn_preset_50",
              label = "50",
              show_label = TRUE,
              tooltip = "Set to 50"
            ),
            toolbar_input_button(
              id = "btn_preset_100",
              label = "100",
              show_label = TRUE,
              tooltip = "Set to 100"
            ),
            toolbar_divider(),
            toolbar_input_button(
              id = "btn_reset",
              label = "Reset",
              icon = icon("rotate-left"),
              tooltip = "Reset to 1"
            ),
            align = "right"
          ),
          value = 1,
          min = 1,
          max = 1000
        ),
        textOutput("quantity_output")
      )
    ),
    col_widths = c(6, 6)
  ),
  card(
    card_header("Toolbar in Text Input Submit Area: Message Composer"),
    card_body(
      layout_columns(
        input_submit_textarea(
          id = "message",
          label = "Your message",
          placeholder = "Type your message here...",
          toolbar = toolbar(
            align = "left",
            toolbar_input_button(
              id = "attach_file",
              label = "Attach",
              icon = icon("paperclip")
            ),
            toolbar_input_select(
              id = "priority",
              label = "Priority",
              choices = c("Low", "Medium", "High", "Urgent"),
              icon = icon("flag")
            ),
            toolbar_divider(),
            toolbar_input_button(
              id = "clear_message",
              label = "Clear",
              icon = icon("trash")
            )
          )
        ),
        div(
          h4("Message History"),
          uiOutput("message_history"),
          style = "max-height: 400px; overflow-y: auto;"
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

  # Handle numeric input preset buttons
  observeEvent(input$btn_preset_10, {
    updateNumericInput(session, "quantity", value = 10)
  })

  observeEvent(input$btn_preset_50, {
    updateNumericInput(session, "quantity", value = 50)
  })

  observeEvent(input$btn_preset_100, {
    updateNumericInput(session, "quantity", value = 100)
  })

  observeEvent(input$btn_reset, {
    updateNumericInput(session, "quantity", value = 1)
  })

  output$quantity_output <- renderText({
    paste("Current quantity:", input$quantity)
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

  # Handle message input with toolbar
  messages <- reactiveVal(character(0))

  observeEvent(input$message, {
    new_message <- paste0(
      "[", input$priority, "] ",
      input$message
    )
    messages(c(messages(), new_message))
  })

  observeEvent(input$attach_file, {
    showNotification("File attachment feature clicked", type = "message")
  })

  observeEvent(input$clear_message, {
    updateTextAreaInput(session, "message", value = "")
  })

  output$message_history <- renderUI({
    if (length(messages()) == 0) {
      p("No messages yet")
    } else {
      tagList(
        lapply(messages(), function(msg) {
          div(
            msg,
            class = "mb-2",
            style = "background-color: #e9ecef; padding: 10px 15px; border-radius: 8px;"
          )
        })
      )
    }
  })
}

shinyApp(ui, server)
