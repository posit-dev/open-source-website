library(ggplot2)

token_types <- c("Output", "Input", "Cached input")

token_colors <- c(
  "Output" = "#cc79a7",
  "Input" = "#e69f00",
  "Cached input" = "#009e73"
)

token_prices <- c("Output" = 10, "Input" = 1, "Cached input" = 0.05)

request_tokens <- function(
  request,
  output = 0,
  input = 0,
  cached = 0,
  label = paste("Request", request),
  scenario = NULL,
  messages = NULL
) {
  n <- length(request)
  long <- data.frame(
    request = request,
    label = label,
    type = factor(
      rep(token_types, each = length(request)),
      levels = token_types
    ),
    tokens = c(rep_len(output, n), rep_len(input, n), rep_len(cached, n))
  )
  long$cost <- long$tokens * token_prices[as.character(long$type)] / 1e6
  # Optional facet row; plot_requests() stacks scenarios as rows.
  if (!is.null(scenario)) {
    long$scenario <- scenario
  }
  if (!is.null(messages)) {
    text <- messages[as.character(long$type)]
    text[is.na(text)] <- ""
    long$tooltip <- ifelse(
      long$tokens > 0,
      paste0(
        "<b>",
        htmltools::htmlEscape(paste(long$label, long$type, sep = " — ")),
        "</b><br>",
        scales::comma(long$tokens),
        " tokens<br><br>",
        gsub("\n", "<br>", htmltools::htmlEscape(text), fixed = TRUE)
      ),
      ""
    )
  }
  long
}

theme_hud <- function() {
  theme_minimal(base_size = 12) +
    theme(
      panel.grid.major.x = element_blank(),
      panel.grid.minor = element_blank(),
      panel.grid.major.y = element_line(color = "#e8e8e8"),
      axis.text = element_text(color = "#6b6b6b"),
      axis.title.x = element_blank(),
      axis.title.y = element_text(color = "#6b6b6b"),
      legend.position = "bottom",
      legend.title = element_blank(),
      legend.text = element_text(color = "#6b6b6b"),
      plot.title = element_text(color = "#333333", size = 12),
      strip.text = element_text(color = "#333333", hjust = 0)
    )
}

plot_requests <- function(
  data,
  y = c("tokens", "cost"),
  n_slots = 6,
  x_labels = FALSE,
  show_total = FALSE
) {
  y <- match.arg(y)

  labels <- if (y == "tokens") {
    scales::label_comma()
  } else {
    scales::label_number(prefix = "$", accuracy = NULL)
  }

  present <- levels(droplevels(data$type[data[[y]] > 0]))

  slots <- unique(data[c("request", "label")])
  slots <- slots[!duplicated(slots$request), ]
  x_breaks <- if (x_labels) slots$request else NULL

  facet <- if ("scenario" %in% names(data)) {
    facet_wrap(vars(scenario), ncol = 1)
  }

  tooltip <- if ("tooltip" %in% names(data)) aes(text = tooltip)

  total <- if (show_total) {
    by <- if ("scenario" %in% names(data)) "scenario" else NULL
    totals <- aggregate(data["cost"], data[by], sum)
    totals$request <- n_slots + 0.5
    y_max <- max(aggregate(data[y], data[c(by, "request")], sum)[[y]])
    breaks <- scales::extended_breaks()(c(0, y_max))
    gaps <- (head(breaks, -1) + tail(breaks, -1)) / 2
    totals$annotation_y <- gaps[which.min(abs(gaps - y_max / 2))]
    geom_label(
      aes(
        x = request,
        y = annotation_y,
        label = paste(
          "Conversation cost:",
          scales::label_number(prefix = "$", accuracy = NULL)(signif(cost, 2))
        )
      ),
      data = totals,
      inherit.aes = FALSE,
      hjust = 1,
      vjust = 0.5,
      color = "#8c8c8c",
      linewidth = 0,
      label.padding = grid::unit(0.1, "lines"),
      size = 3.5
    )
  }

  ggplot(data, aes(x = request, y = .data[[y]], fill = type)) +
    tooltip +
    geom_col(aes(group = type), width = 0.8) +
    total +
    scale_x_continuous(
      limits = c(0.5, n_slots + 0.5),
      breaks = x_breaks,
      labels = if (x_labels) slots$label
    ) +
    scale_y_continuous(
      labels = labels,
      expand = expansion(mult = c(0, 0.05))
    ) +
    scale_fill_manual(
      values = token_colors,
      breaks = rev(present),
      drop = TRUE,
      name = NULL
    ) +
    facet +
    labs(y = if (y == "tokens") "Tokens" else "Cost (USD)") +
    theme_hud()
}

request_widget <- function(plot) {
  plotly::ggplotly(plot, tooltip = "text") |>
    plotly::layout(
      margin = list(t = 60),
      hovermode = "closest",
      dragmode = FALSE,
      xaxis = list(fixedrange = TRUE),
      yaxis = list(fixedrange = TRUE),
      hoverlabel = list(
        bgcolor = "white",
        bordercolor = "#d9d9d9",
        font = list(color = "#333333", size = 12)
      )
    ) |>
    plotly::config(
      displayModeBar = FALSE,
      scrollZoom = FALSE,
      doubleClick = FALSE
    ) |>
    htmlwidgets::onRender(
      "function(el) {
        el.on('plotly_hover', function() {
          // Keep callouts from competing with the tooltip while hovering.
          el.querySelectorAll('.annotation').forEach(function(annotation) {
            annotation.style.visibility = 'hidden';
          });
          window.requestAnimationFrame(function() {
            var layer = el.querySelector('.hoverlayer');
            if (!layer) return;
            layer.removeAttribute('transform');
            var frame = el.getBoundingClientRect();
            var box = layer.getBoundingClientRect();
            var dx = Math.max(0, frame.left + 8 - box.left) -
              Math.max(0, box.right - frame.right + 8);
            var dy = Math.max(0, frame.top + 8 - box.top) -
              Math.max(0, box.bottom - frame.bottom + 8);
            layer.setAttribute('transform', 'translate(' + dx + ',' + dy + ')');
          });
        });
        el.on('plotly_unhover', function() {
          el.querySelectorAll('.annotation').forEach(function(annotation) {
            annotation.style.removeProperty('visibility');
          });
          var layer = el.querySelector('.hoverlayer');
          if (layer) layer.removeAttribute('transform');
        });
      }"
    )
}
