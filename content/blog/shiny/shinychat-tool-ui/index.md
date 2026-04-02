---
title: Tool Calling UI in shinychat
description: Rich tool calling displays are now available in shinychat!
people:
  - Garrick Aden-Buie
  - Carson Sievert
  - Barret Schloerke
date: '2025-11-20'
image: feature.png
ported_from: shiny
port_status: in-progress
software:
  - shinychat
  - shiny-python
languages:
  - Python
categories:
  - Interactive Apps
tags:
  - Shiny
---


<link href="index_files/libs/shinychat-0.3.0/chat/chat.css" rel="stylesheet" />
<link href="index_files/libs/shinychat-0.3.0/markdown-stream/markdown-stream.css" rel="stylesheet" />
<script src="index_files/libs/shinychat-0.3.0/chat/chat.js" type="module"></script>
<script src="index_files/libs/shinychat-0.3.0/markdown-stream/markdown-stream.js" type="module"></script>


<style>
.highlight-line {
  font-weight: bold;
}
body:not(.modal-open) div.sourceCode pre code.has-line-highlights> span:not(.highlight-line) {
  opacity: 0.6;
}
body:not(.modal-open) div.sourceCode:hover pre code.has-line-highlights> span:not(.highlight-line) {
  opacity: 0.8;
}
.card-header {
  --bs-card-cap-bg: transparent;
}
.shiny-tool-card {
  margin-bottom: 1rem !important;
}
.code-copy-button> .bi::after {
  display: none;
}
</style>

We're jazzed to announce that [shinychat](https://posit-dev.github.io/shinychat) now includes rich UI for tool calls!
shinychat makes it easy to build LLM-powered chat interfaces in Shiny apps, and with tool calling UI, your users can see which tools are being executed and their outcomes.
This feature is available in [shinychat for R](https://posit-dev.github.io/shinychat/r) (v0.3.0) and [shinychat for Python](https://posit-dev.github.io/shinychat/py/) (v0.2.0 or later).

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-1" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-1-1">R</a></li>
<li><a href="#tabset-1-2">Python</a></li>
</ul>
<div id="tabset-1-1">

``` r
install.packages("shinychat")
```

</div>
<div id="tabset-1-2">

``` bash
pip install shinychat
```

</div>
</div>

This release brings tool call displays that work with [ellmer](https://ellmer.tidyverse.org) (R) and [chatlas](https://github.com/posit-dev/chatlas) (Python).
When the LLM calls a tool, shinychat automatically displays the request and result in a collapsible card interface.

In this post we'll cover the new [Tool calling UI](#tool-calling-ui) features, how to set them up in your apps, and ways to customize the display.
We'll also highlight some [chat bookmarking support](#bookmarking-support) and [other improvements in shinychat for R v0.3.0](#other-improvements-in-r-v0.3.0).
As always, you can find the full list of changes in the [R release notes](https://posit-dev.github.io/shinychat/r/news/index.html#shinychat-030) and [Python release notes](https://github.com/posit-dev/shinychat/blob/main/pkg-py/CHANGELOG.md).

## Tool calling UI

Tool calling lets you extend an LLM's capabilities by giving it access to functions you define.
When you provide a tool to the LLM, you're telling it "here's a function you can call if you need it."
The key thing to understand is that the tool runs on *your machine* (or wherever your Shiny app is running) --- the LLM doesn't directly run the tool itself.
Instead, it asks *you* to run the function and return the result.

Both ellmer and chatlas make it easy to define tools and register them with your chat client[^1], and they also handle the back-and-forth of tool calls by receiving requests from the LLM, executing the tool, and sending the results back.
This means you can focus on what you do best: writing code to solve problems.

Any problem you can solve with a function can become a tool for an LLM!
You can give the LLM access to live data, APIs, databases, or any other resources your app can reach.

<div class="callout callout-tip" role="note" aria-label="Tip">
<div class="callout-header">
<span class="callout-title">Tip</span>
</div>
<div class="callout-body">

If you're working in R, [btw](https://posit-dev.github.io/btw) is a complete toolkit to help LLMs work better with R.
Whether you're copy-pasting to ChatGPT, chatting with an AI assistant in your IDE, or building LLM-powered apps with shinychat, btw makes it easy to give LLMs the context they need.

And, most importantly, btw provides a full suite of tools for gathering context from R sessions, including tools to: read help pages and vignettes, describe data frames, search for packages on CRAN, read web pages, and more.

Learn more at [posit-dev.github.io/btw](https://posit-dev.github.io/btw)!

</div>
</div>

When the LLM decides to call a tool, shinychat displays the request and result in the chat interface.
Users can see which tools are being invoked, what arguments are being passed, and what data is being returned.
The tool display is designed to be customizable, so shinychat developers can customize the appearance and display of tool calls to best serve their users.

### Basic tool display

Let's start by creating a simple weather forecasting tool that fetches a weather data (in the United States) for a given latitude and longitude.

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-2" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-2-1">R</a></li>
<li><a href="#tabset-2-2">Python</a></li>
</ul>
<div id="tabset-2-1">

``` r
library(shinychat)
library(ellmer)
library(weathR)

get_weather_forecast <- tool(
  function(lat, lon) {
    point_tomorrow(lat, lon, short = FALSE)
  },
  name = "get_weather_forecast",
  description = "Get the weather forecast for a location.",
  arguments = list(
    lat = type_number("Latitude"),
    lon = type_number("Longitude")
  )
)

# Register the tool with your chat client
chat <- ellmer::chat("openai/gpt-4.1-nano")
chat$register_tool(get_weather_forecast)
```

</div>
<div id="tabset-2-2">

``` python
from chatlas import ChatOpenAI
import requests

def get_weather_forecast(lat: float, lon: float) -> dict:
    """Get the weather forecast for a location."""
    lat_lng = f"latitude={lat}&longitude={lon}"
    url = f"https://api.open-meteo.com/v1/forecast?{lat_lng}&current=temperature_2m,wind_speed_10m"
    response = requests.get(url)
    return response.json()["current"]

# Register the tool with your chat client
chat = ChatOpenAI(model="gpt-4.1-nano")
chat.register_tool(get_weather_forecast)
```

</div>
</div>

With this tool registered, when you ask a weather-related question, the LLM might decide to call the `get_weather_forecast()` tool to get the latest weather.

In a chat conversation in your R console with ellmer, this might look like the following.

``` r
chat$chat("Will I need an umbrella for my walk to the T?")
#> ◯ [tool call] get_weather_forecast(lat = 42.3515, lon = -71.0552)
#> ● #> [{"time":"2025-11-20 16:00:00 EST","temp":42,"dewpoint":0,"humidity":67,"p_rain":1,"wi…
#>
#> Based on the weather forecast, there is a chance of rain around 4 to 5 PM,
#> with mostly cloudy to partly sunny skies. It seems there might be some rain
#> during this time, so carrying an umbrella could be a good idea if you plan
#> to go out around that time. Otherwise, the weather looks relatively clear
#> in the evening.
```

Notice that I didn't provide many context clues, but the model correctly guessed that I'm walking to the MBTA in Boston, MA and picked [the latitude and longitude for Boston's South Station](https://www.openstreetmap.org/?mlat=42.35150&mlon=-71.05520#map=16/42.35150/-71.05520&layers=P).

In shinychat, when the LLM calls the tool, shinychat automatically displays the tool request in a collapsed card:

    OpenTelemetry error: there is no package called 'otelsdk'

<shiny-tool-request request-id="tool_call_001" tool-name="get_weather_forecast" arguments="{&quot;lat&quot;:42.3515,&quot;lon&quot;:-71.0552}"></shiny-tool-request>

Expanding the card shows the arguments passed to the tool.
When the tool completes, shinychat replaces the request with a card containing the result:

<shiny-tool-result request-id="tool_call_002" tool-name="get_weather_forecast" request-call="get_weather_forecast(lat = 42.3515, lon = -71.0552)" status="success" show-request value="[&#10;  {&#10;    &quot;time&quot;: &quot;2026-04-02 18:00:00 EDT&quot;,&#10;    &quot;temp&quot;: 38,&#10;    &quot;dewpoint&quot;: 1.1111,&#10;    &quot;humidity&quot;: 85,&#10;    &quot;p_rain&quot;: 13,&#10;    &quot;wind_speed&quot;: 12,&#10;    &quot;wind_dir&quot;: &quot;NE&quot;,&#10;    &quot;skies&quot;: &quot;Patchy Fog&quot;,&#10;    &quot;geometry&quot;: {&#10;      &quot;type&quot;: &quot;Point&quot;,&#10;      &quot;coordinates&quot;: [-71.0589, 42.3601]&#10;    }&#10;  },&#10;  {&#10;    &quot;time&quot;: &quot;2026-04-02 19:00:00 EDT&quot;,&#10;    &quot;temp&quot;: 38,&#10;    &quot;dewpoint&quot;: 1.1111,&#10;    &quot;humidity&quot;: 85,&#10;    &quot;p_rain&quot;: 12,&#10;    &quot;wind_speed&quot;: 12,&#10;    &quot;wind_dir&quot;: &quot;NE&quot;,&#10;    &quot;skies&quot;: &quot;Patchy Fog&quot;,&#10;    &quot;geometry&quot;: {&#10;      &quot;type&quot;: &quot;Point&quot;,&#10;      &quot;coordinates&quot;: [-71.0589, 42.3601]&#10;    }&#10;  },&#10;  {&#10;    &quot;time&quot;: &quot;2026-04-02 20:00:00 EDT&quot;,&#10;    &quot;temp&quot;: 38,&#10;    &quot;dewpoint&quot;: 1.1111,&#10;    &quot;humidity&quot;: 85,&#10;    &quot;p_rain&quot;: 10,&#10;    &quot;wind_speed&quot;: 10,&#10;    &quot;wind_dir&quot;: &quot;NE&quot;,&#10;    &quot;skies&quot;: &quot;Patchy Fog&quot;,&#10;    &quot;geometry&quot;: {&#10;      &quot;type&quot;: &quot;Point&quot;,&#10;      &quot;coordinates&quot;: [-71.0589, 42.3601]&#10;    }&#10;  },&#10;  {&#10;    &quot;time&quot;: &quot;2026-04-02 21:00:00 EDT&quot;,&#10;    &quot;temp&quot;: 38,&#10;    &quot;dewpoint&quot;: 1.1111,&#10;    &quot;humidity&quot;: 85,&#10;    &quot;p_rain&quot;: 10,&#10;    &quot;wind_speed&quot;: 9,&#10;    &quot;wind_dir&quot;: &quot;NE&quot;,&#10;    &quot;skies&quot;: &quot;Patchy Fog&quot;,&#10;    &quot;geometry&quot;: {&#10;      &quot;type&quot;: &quot;Point&quot;,&#10;      &quot;coordinates&quot;: [-71.0589, 42.3601]&#10;    }&#10;  },&#10;  {&#10;    &quot;time&quot;: &quot;2026-04-02 22:00:00 EDT&quot;,&#10;    &quot;temp&quot;: 38,&#10;    &quot;dewpoint&quot;: 0.5556,&#10;    &quot;humidity&quot;: 82,&#10;    &quot;p_rain&quot;: 11,&#10;    &quot;wind_speed&quot;: 8,&#10;    &quot;wind_dir&quot;: &quot;E&quot;,&#10;    &quot;skies&quot;: &quot;Cloudy&quot;,&#10;    &quot;geometry&quot;: {&#10;      &quot;type&quot;: &quot;Point&quot;,&#10;      &quot;coordinates&quot;: [-71.0589, 42.3601]&#10;    }&#10;  },&#10;  {&#10;    &quot;time&quot;: &quot;2026-04-02 23:00:00 EDT&quot;,&#10;    &quot;temp&quot;: 38,&#10;    &quot;dewpoint&quot;: 0.5556,&#10;    &quot;humidity&quot;: 82,&#10;    &quot;p_rain&quot;: 11,&#10;    &quot;wind_speed&quot;: 7,&#10;    &quot;wind_dir&quot;: &quot;E&quot;,&#10;    &quot;skies&quot;: &quot;Cloudy&quot;,&#10;    &quot;geometry&quot;: {&#10;      &quot;type&quot;: &quot;Point&quot;,&#10;      &quot;coordinates&quot;: [-71.0589, 42.3601]&#10;    }&#10;  }&#10;]" value-type="code"></shiny-tool-result>

If the tool throws an error, the error is captured and the error message is shown to the LLM.
Typically this happens when the model makes a mistake in calling the tool and often the error message is instructive.

shinychat updates the card to show the error message:

<shiny-tool-result request-id="tool_call_001c" tool-name="get_weather_forecast" request-call="get_weather_forecast(lat = 42.3515, lon = -71.0552)" status="error" show-request value="object of type &#39;closure&#39; is not subsettable" value-type="code"></shiny-tool-result>

### Setting up streaming

To enable tool UI in your apps, you need to ensure that tool requests and results are streamed to shinychat:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-3" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-3-1">R</a></li>
<li><a href="#tabset-3-2">Python</a></li>
</ul>
<div id="tabset-3-1">

You don't need to do anything if you're using `chat_app()` or the chat module via `chat_mod_ui()` and `chat_mod_server()`; tool UI is enabled automatically.

If you're using `chat_ui()` with `chat_append()`, set `stream = "content"` when calling `$stream_async()`:

``` r
server <- function(input, output, session) {
  client <- ellmer::chat("openai/gpt-4.1-nano")
  client$register_tool(get_weather_forecast)

  observeEvent(input$chat_user_input, {
    stream <- client$stream_async(input$chat_user_input, stream = "content")
    chat_append("chat", stream)
  })
}
```

</div>
<div id="tabset-3-2">

In Python with Shiny Express, use `content="all"` when calling `stream_async()`:

**app.py**

``` python
from chatlas import ChatOpenAI
from shiny.express import ui
from shinychat.express import Chat

client = ChatOpenAI(model="gpt-4.1-nano")
client.register_tool(get_weather_forecast)

chat = Chat(id="chat")
chat.ui()

@chat.on_user_submit
async def handle_user_input(user_input: str):
    response = await client.stream_async(user_input, content="all")
    await chat.append_message_stream(response)
```

For Shiny Core mode:

**app.py**

``` python
from chatlas import ChatOpenAI
from shiny import App, ui
from shinychat import Chat

client = ChatOpenAI(model="gpt-4.1-nano")
client.register_tool(get_weather_forecast)

app_ui = ui.page_fluid(
    Chat(id="chat").ui()
)

def server(input, output, session):
    chat = Chat(id="chat")

    @chat.on_user_submit
    async def handle_user_input(user_input: str):
        response = await client.stream_async(user_input, content="all")
        await chat.append_message_stream(response)

app = App(app_ui, server)
```

</div>
</div>

### Customizing tool title and icon

You can enhance the visual presentation of tool requests and results by adding custom titles and icons to your tools.
This helps users quickly identify which tools are being called.

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-4" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-4-1">R</a></li>
<li><a href="#tabset-4-2">Python</a></li>
</ul>
<div id="tabset-4-1">

Use `tool_annotations()` to add a title and icon:

``` r
get_weather_forecast <- tool(
  function(lat, lon) {
    point_tomorrow(lat, lon, short = FALSE)
  },
  name = "get_weather_forecast",
  description = "Get the weather forecast for a location.",
  arguments = list(
    lat = type_number("Latitude"),
    lon = type_number("Longitude")
  ),
  annotations = tool_annotations(
    title = "Weather Forecast",
    icon = bsicons::bs_icon("cloud-sun")
  )
)
```

</div>
<div id="tabset-4-2">

With chatlas, you can customize the tool display in two ways:

1.  Use the `._display` attribute to customize the tool display:

    ``` python
    import faicons

    def get_weather_forecast(lat: float, lon: float) -> dict:
        """Get the weather forecast for a location."""
        # ... implementation ...

    get_weather_forecast._display = {
        "title": "Weather Forecast",
        "icon": faicons.icon_svg("cloud-sun")
    }
    ```

    This approach sets the title and icon for all calls to this tool, so it's ideal for predefined tools or tools that are bundled in a Python module or package.

2.  Set the tool annotations at registration time:

    ``` python
    chat.register_tool(
        get_weather_forecast,
        annotations={
            "title": "Weather Forecast",
            "icon": faicons.icon_svg("cloud-sun")
        }
    )
    ```

    This approach allows you to customize the display for a specific chat client or application without modifying the tool function itself.

</div>
</div>

Now the tool card shows your custom title and icon:

<shiny-tool-result request-id="tool_call_004" tool-name="get_weather_forecast" request-call="get_weather_forecast(lat = 42.3515, lon = -71.0552)" status="success" tool-title="Weather Forecast" icon="&lt;svg xmlns=&quot;http://www.w3.org/2000/svg&quot; viewBox=&quot;0 0 16 16&quot; class=&quot;bi bi-cloud-sun &quot; style=&quot;height:1em;width:1em;fill:currentColor;vertical-align:-0.125em;&quot; aria-hidden=&quot;true&quot; role=&quot;img&quot; &gt;&lt;path d=&quot;M7 8a3.5 3.5 0 0 1 3.5 3.555.5.5 0 0 0 .624.492A1.503 1.503 0 0 1 13 13.5a1.5 1.5 0 0 1-1.5 1.5H3a2 2 0 1 1 .1-3.998.5.5 0 0 0 .51-.375A3.502 3.502 0 0 1 7 8zm4.473 3a4.5 4.5 0 0 0-8.72-.99A3 3 0 0 0 3 16h8.5a2.5 2.5 0 0 0 0-5h-.027z&quot;&gt;&lt;/path&gt;&#10;&lt;path d=&quot;M10.5 1.5a.5.5 0 0 0-1 0v1a.5.5 0 0 0 1 0v-1zm3.743 1.964a.5.5 0 1 0-.707-.707l-.708.707a.5.5 0 0 0 .708.708l.707-.708zm-7.779-.707a.5.5 0 0 0-.707.707l.707.708a.5.5 0 1 0 .708-.708l-.708-.707zm1.734 3.374a2 2 0 1 1 3.296 2.198c.199.281.372.582.516.898a3 3 0 1 0-4.84-3.225c.352.011.696.055 1.028.129zm4.484 4.074c.6.215 1.125.59 1.522 1.072a.5.5 0 0 0 .039-.742l-.707-.707a.5.5 0 0 0-.854.377zM14.5 6.5a.5.5 0 0 0 0 1h1a.5.5 0 0 0 0-1h-1z&quot;&gt;&lt;/path&gt;&lt;/svg&gt;" show-request value="[&#10;  {&#10;    &quot;time&quot;: &quot;2026-04-02 18:00:00 EDT&quot;,&#10;    &quot;temp&quot;: 38,&#10;    &quot;dewpoint&quot;: 1.1111,&#10;    &quot;humidity&quot;: 85,&#10;    &quot;p_rain&quot;: 13,&#10;    &quot;wind_speed&quot;: 12,&#10;    &quot;wind_dir&quot;: &quot;NE&quot;,&#10;    &quot;skies&quot;: &quot;Patchy Fog&quot;,&#10;    &quot;geometry&quot;: {&#10;      &quot;type&quot;: &quot;Point&quot;,&#10;      &quot;coordinates&quot;: [-71.0589, 42.3601]&#10;    }&#10;  },&#10;  {&#10;    &quot;time&quot;: &quot;2026-04-02 19:00:00 EDT&quot;,&#10;    &quot;temp&quot;: 38,&#10;    &quot;dewpoint&quot;: 1.1111,&#10;    &quot;humidity&quot;: 85,&#10;    &quot;p_rain&quot;: 12,&#10;    &quot;wind_speed&quot;: 12,&#10;    &quot;wind_dir&quot;: &quot;NE&quot;,&#10;    &quot;skies&quot;: &quot;Patchy Fog&quot;,&#10;    &quot;geometry&quot;: {&#10;      &quot;type&quot;: &quot;Point&quot;,&#10;      &quot;coordinates&quot;: [-71.0589, 42.3601]&#10;    }&#10;  },&#10;  {&#10;    &quot;time&quot;: &quot;2026-04-02 20:00:00 EDT&quot;,&#10;    &quot;temp&quot;: 38,&#10;    &quot;dewpoint&quot;: 1.1111,&#10;    &quot;humidity&quot;: 85,&#10;    &quot;p_rain&quot;: 10,&#10;    &quot;wind_speed&quot;: 10,&#10;    &quot;wind_dir&quot;: &quot;NE&quot;,&#10;    &quot;skies&quot;: &quot;Patchy Fog&quot;,&#10;    &quot;geometry&quot;: {&#10;      &quot;type&quot;: &quot;Point&quot;,&#10;      &quot;coordinates&quot;: [-71.0589, 42.3601]&#10;    }&#10;  },&#10;  {&#10;    &quot;time&quot;: &quot;2026-04-02 21:00:00 EDT&quot;,&#10;    &quot;temp&quot;: 38,&#10;    &quot;dewpoint&quot;: 1.1111,&#10;    &quot;humidity&quot;: 85,&#10;    &quot;p_rain&quot;: 10,&#10;    &quot;wind_speed&quot;: 9,&#10;    &quot;wind_dir&quot;: &quot;NE&quot;,&#10;    &quot;skies&quot;: &quot;Patchy Fog&quot;,&#10;    &quot;geometry&quot;: {&#10;      &quot;type&quot;: &quot;Point&quot;,&#10;      &quot;coordinates&quot;: [-71.0589, 42.3601]&#10;    }&#10;  },&#10;  {&#10;    &quot;time&quot;: &quot;2026-04-02 22:00:00 EDT&quot;,&#10;    &quot;temp&quot;: 38,&#10;    &quot;dewpoint&quot;: 0.5556,&#10;    &quot;humidity&quot;: 82,&#10;    &quot;p_rain&quot;: 11,&#10;    &quot;wind_speed&quot;: 8,&#10;    &quot;wind_dir&quot;: &quot;E&quot;,&#10;    &quot;skies&quot;: &quot;Cloudy&quot;,&#10;    &quot;geometry&quot;: {&#10;      &quot;type&quot;: &quot;Point&quot;,&#10;      &quot;coordinates&quot;: [-71.0589, 42.3601]&#10;    }&#10;  },&#10;  {&#10;    &quot;time&quot;: &quot;2026-04-02 23:00:00 EDT&quot;,&#10;    &quot;temp&quot;: 38,&#10;    &quot;dewpoint&quot;: 0.5556,&#10;    &quot;humidity&quot;: 82,&#10;    &quot;p_rain&quot;: 11,&#10;    &quot;wind_speed&quot;: 7,&#10;    &quot;wind_dir&quot;: &quot;E&quot;,&#10;    &quot;skies&quot;: &quot;Cloudy&quot;,&#10;    &quot;geometry&quot;: {&#10;      &quot;type&quot;: &quot;Point&quot;,&#10;      &quot;coordinates&quot;: [-71.0589, 42.3601]&#10;    }&#10;  }&#10;]" value-type="code"></shiny-tool-result>

### Custom display content

By default, shinychat shows the raw tool result value as a code block.
But often you'll want to present data to users in a more polished format---like a formatted table or a summary.

You can customize the display by returning alternative content:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-5" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-5-1">R</a></li>
<li><a href="#tabset-5-2">Python</a></li>
</ul>
<div id="tabset-5-1">

Return a `ContentToolResult` with `extra$display` containing alternative content:

``` r
get_weather_forecast <- tool(
  function(lat, lon, location_name) {
    forecast_data <- point_tomorrow(lat, lon, short = FALSE)
    forecast_table <- gt::as_raw_html(gt::gt(forecast_data))

    ContentToolResult(
      forecast_data,  # This is what the LLM sees
      extra = list(
        display = list(
          html = forecast_table,  # This is what users see
          title = paste("Weather Forecast for", location_name)
        )
      )
    )
  },
  name = "get_weather_forecast",
  description = "Get the weather forecast for a location.",
  arguments = list(
    lat = type_number("Latitude"),
    lon = type_number("Longitude"),
    location_name = type_string("Name of the location")
  ),
  annotations = tool_annotations(
    title = "Weather Forecast",
    icon = bsicons::bs_icon("cloud-sun")
  )
)
```

</div>
<div id="tabset-5-2">

Return a `ToolResult` with display options:

``` python
from chatlas import ToolResult
import pandas as pd

def get_weather_forecast(lat: float, lon: float, location_name: str):
    """Get the weather forecast for a location."""
    # Get forecast data
    data = fetch_weather_data(lat, lon)

    # Create a DataFrame for the LLM
    forecast_df = pd.DataFrame(data)

    # Create HTML table for users
    forecast_table = forecast_df.to_html(index=False)

    return ToolResult(
        value=forecast_df.to_dict(),  # LLM sees this
        display={
            "html": forecast_table,  # Users see this
            "title": f"Weather Forecast for {location_name}"
        }
    )
```

</div>
</div>

The `display` options support three content types (in order of preference):

1.  **`html`**: HTML content from packages like `{gt}`, `{reactable}`, or `{htmlwidgets}` (R), or Pandas/HTML strings (Python)
2.  **`markdown`**: Markdown text that's automatically rendered
3.  **`text`**: Plain text without code formatting

Here's what a formatted table looks like in the tool result:

<shiny-tool-result request-id="tool_call_007" tool-name="get_weather_forecast" request-call="get_weather_forecast(lat = 42.3515, lon = -71.0552, location_name = &quot;South Station in Boston, MA&quot;)" status="success" tool-title="Weather Forecast for South Station in Boston, MA" icon="&lt;svg xmlns=&quot;http://www.w3.org/2000/svg&quot; viewBox=&quot;0 0 16 16&quot; class=&quot;bi bi-cloud-sun &quot; style=&quot;height:1em;width:1em;fill:currentColor;vertical-align:-0.125em;&quot; aria-hidden=&quot;true&quot; role=&quot;img&quot; &gt;&lt;path d=&quot;M7 8a3.5 3.5 0 0 1 3.5 3.555.5.5 0 0 0 .624.492A1.503 1.503 0 0 1 13 13.5a1.5 1.5 0 0 1-1.5 1.5H3a2 2 0 1 1 .1-3.998.5.5 0 0 0 .51-.375A3.502 3.502 0 0 1 7 8zm4.473 3a4.5 4.5 0 0 0-8.72-.99A3 3 0 0 0 3 16h8.5a2.5 2.5 0 0 0 0-5h-.027z&quot;&gt;&lt;/path&gt;&#10;&lt;path d=&quot;M10.5 1.5a.5.5 0 0 0-1 0v1a.5.5 0 0 0 1 0v-1zm3.743 1.964a.5.5 0 1 0-.707-.707l-.708.707a.5.5 0 0 0 .708.708l.707-.708zm-7.779-.707a.5.5 0 0 0-.707.707l.707.708a.5.5 0 1 0 .708-.708l-.708-.707zm1.734 3.374a2 2 0 1 1 3.296 2.198c.199.281.372.582.516.898a3 3 0 1 0-4.84-3.225c.352.011.696.055 1.028.129zm4.484 4.074c.6.215 1.125.59 1.522 1.072a.5.5 0 0 0 .039-.742l-.707-.707a.5.5 0 0 0-.854.377zM14.5 6.5a.5.5 0 0 0 0 1h1a.5.5 0 0 0 0-1h-1z&quot;&gt;&lt;/path&gt;&lt;/svg&gt;" show-request value="&lt;div id=&quot;jreiujlmyq&quot; style=&quot;padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;&quot;&gt;&#10;  &#10;  &lt;table class=&quot;gt_table&quot; data-quarto-disable-processing=&quot;false&quot; data-quarto-bootstrap=&quot;false&quot; style=&quot;-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; font-family: system-ui, &#39;Segoe UI&#39;, Roboto, Helvetica, Arial, sans-serif, &#39;Apple Color Emoji&#39;, &#39;Segoe UI Emoji&#39;, &#39;Segoe UI Symbol&#39;, &#39;Noto Color Emoji&#39;; display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3;&quot; bgcolor=&quot;#FFFFFF&quot;&gt;&#10;  &lt;thead style=&quot;border-style: none;&quot;&gt;&#10;    &lt;tr class=&quot;gt_col_headings&quot; style=&quot;border-style: none; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3;&quot;&gt;&#10;      &lt;th class=&quot;gt_col_heading gt_columns_bottom_border gt_left&quot; rowspan=&quot;1&quot; colspan=&quot;1&quot; scope=&quot;col&quot; id=&quot;time&quot; style=&quot;border-style: none; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; text-align: left;&quot; bgcolor=&quot;#FFFFFF&quot; valign=&quot;bottom&quot; align=&quot;left&quot;&gt;time&lt;/th&gt;&#10;      &lt;th class=&quot;gt_col_heading gt_columns_bottom_border gt_right&quot; rowspan=&quot;1&quot; colspan=&quot;1&quot; scope=&quot;col&quot; id=&quot;temp&quot; style=&quot;border-style: none; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; bgcolor=&quot;#FFFFFF&quot; valign=&quot;bottom&quot; align=&quot;right&quot;&gt;temp&lt;/th&gt;&#10;      &lt;th class=&quot;gt_col_heading gt_columns_bottom_border gt_right&quot; rowspan=&quot;1&quot; colspan=&quot;1&quot; scope=&quot;col&quot; id=&quot;dewpoint&quot; style=&quot;border-style: none; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; bgcolor=&quot;#FFFFFF&quot; valign=&quot;bottom&quot; align=&quot;right&quot;&gt;dewpoint&lt;/th&gt;&#10;      &lt;th class=&quot;gt_col_heading gt_columns_bottom_border gt_right&quot; rowspan=&quot;1&quot; colspan=&quot;1&quot; scope=&quot;col&quot; id=&quot;humidity&quot; style=&quot;border-style: none; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; bgcolor=&quot;#FFFFFF&quot; valign=&quot;bottom&quot; align=&quot;right&quot;&gt;humidity&lt;/th&gt;&#10;      &lt;th class=&quot;gt_col_heading gt_columns_bottom_border gt_right&quot; rowspan=&quot;1&quot; colspan=&quot;1&quot; scope=&quot;col&quot; id=&quot;p_rain&quot; style=&quot;border-style: none; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; bgcolor=&quot;#FFFFFF&quot; valign=&quot;bottom&quot; align=&quot;right&quot;&gt;p_rain&lt;/th&gt;&#10;      &lt;th class=&quot;gt_col_heading gt_columns_bottom_border gt_right&quot; rowspan=&quot;1&quot; colspan=&quot;1&quot; scope=&quot;col&quot; id=&quot;wind_speed&quot; style=&quot;border-style: none; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; bgcolor=&quot;#FFFFFF&quot; valign=&quot;bottom&quot; align=&quot;right&quot;&gt;wind_speed&lt;/th&gt;&#10;      &lt;th class=&quot;gt_col_heading gt_columns_bottom_border gt_left&quot; rowspan=&quot;1&quot; colspan=&quot;1&quot; scope=&quot;col&quot; id=&quot;wind_dir&quot; style=&quot;border-style: none; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; text-align: left;&quot; bgcolor=&quot;#FFFFFF&quot; valign=&quot;bottom&quot; align=&quot;left&quot;&gt;wind_dir&lt;/th&gt;&#10;      &lt;th class=&quot;gt_col_heading gt_columns_bottom_border gt_left&quot; rowspan=&quot;1&quot; colspan=&quot;1&quot; scope=&quot;col&quot; id=&quot;skies&quot; style=&quot;border-style: none; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; text-align: left;&quot; bgcolor=&quot;#FFFFFF&quot; valign=&quot;bottom&quot; align=&quot;left&quot;&gt;skies&lt;/th&gt;&#10;      &lt;th class=&quot;gt_col_heading gt_columns_bottom_border gt_center&quot; rowspan=&quot;1&quot; colspan=&quot;1&quot; scope=&quot;col&quot; id=&quot;geometry&quot; style=&quot;border-style: none; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 6px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; text-align: center;&quot; bgcolor=&quot;#FFFFFF&quot; valign=&quot;bottom&quot; align=&quot;center&quot;&gt;geometry&lt;/th&gt;&#10;    &lt;/tr&gt;&#10;  &lt;/thead&gt;&#10;  &lt;tbody class=&quot;gt_table_body&quot; style=&quot;border-style: none; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3;&quot;&gt;&#10;    &lt;tr style=&quot;border-style: none;&quot;&gt;&lt;td headers=&quot;time&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;2026-04-02 18:00:00 EDT&lt;/td&gt;&#10;&lt;td headers=&quot;temp&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;38&lt;/td&gt;&#10;&lt;td headers=&quot;dewpoint&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;1.666667&lt;/td&gt;&#10;&lt;td headers=&quot;humidity&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;89&lt;/td&gt;&#10;&lt;td headers=&quot;p_rain&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;13&lt;/td&gt;&#10;&lt;td headers=&quot;wind_speed&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;14&lt;/td&gt;&#10;&lt;td headers=&quot;wind_dir&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;NE&lt;/td&gt;&#10;&lt;td headers=&quot;skies&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;Patchy Fog&lt;/td&gt;&#10;&lt;td headers=&quot;geometry&quot; class=&quot;gt_row gt_center&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: center;&quot; valign=&quot;middle&quot; align=&quot;center&quot;&gt;c(-71.0552, 42.3515)&lt;/td&gt;&lt;/tr&gt;&#10;    &lt;tr style=&quot;border-style: none;&quot;&gt;&lt;td headers=&quot;time&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;2026-04-02 19:00:00 EDT&lt;/td&gt;&#10;&lt;td headers=&quot;temp&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;38&lt;/td&gt;&#10;&lt;td headers=&quot;dewpoint&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;1.666667&lt;/td&gt;&#10;&lt;td headers=&quot;humidity&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;89&lt;/td&gt;&#10;&lt;td headers=&quot;p_rain&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;12&lt;/td&gt;&#10;&lt;td headers=&quot;wind_speed&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;13&lt;/td&gt;&#10;&lt;td headers=&quot;wind_dir&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;NE&lt;/td&gt;&#10;&lt;td headers=&quot;skies&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;Patchy Fog&lt;/td&gt;&#10;&lt;td headers=&quot;geometry&quot; class=&quot;gt_row gt_center&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: center;&quot; valign=&quot;middle&quot; align=&quot;center&quot;&gt;c(-71.0552, 42.3515)&lt;/td&gt;&lt;/tr&gt;&#10;    &lt;tr style=&quot;border-style: none;&quot;&gt;&lt;td headers=&quot;time&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;2026-04-02 20:00:00 EDT&lt;/td&gt;&#10;&lt;td headers=&quot;temp&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;38&lt;/td&gt;&#10;&lt;td headers=&quot;dewpoint&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;1.666667&lt;/td&gt;&#10;&lt;td headers=&quot;humidity&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;89&lt;/td&gt;&#10;&lt;td headers=&quot;p_rain&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;10&lt;/td&gt;&#10;&lt;td headers=&quot;wind_speed&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;13&lt;/td&gt;&#10;&lt;td headers=&quot;wind_dir&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;NE&lt;/td&gt;&#10;&lt;td headers=&quot;skies&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;Patchy Fog&lt;/td&gt;&#10;&lt;td headers=&quot;geometry&quot; class=&quot;gt_row gt_center&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: center;&quot; valign=&quot;middle&quot; align=&quot;center&quot;&gt;c(-71.0552, 42.3515)&lt;/td&gt;&lt;/tr&gt;&#10;    &lt;tr style=&quot;border-style: none;&quot;&gt;&lt;td headers=&quot;time&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;2026-04-02 21:00:00 EDT&lt;/td&gt;&#10;&lt;td headers=&quot;temp&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;38&lt;/td&gt;&#10;&lt;td headers=&quot;dewpoint&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;1.666667&lt;/td&gt;&#10;&lt;td headers=&quot;humidity&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;89&lt;/td&gt;&#10;&lt;td headers=&quot;p_rain&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;10&lt;/td&gt;&#10;&lt;td headers=&quot;wind_speed&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;13&lt;/td&gt;&#10;&lt;td headers=&quot;wind_dir&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;E&lt;/td&gt;&#10;&lt;td headers=&quot;skies&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;Patchy Fog&lt;/td&gt;&#10;&lt;td headers=&quot;geometry&quot; class=&quot;gt_row gt_center&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: center;&quot; valign=&quot;middle&quot; align=&quot;center&quot;&gt;c(-71.0552, 42.3515)&lt;/td&gt;&lt;/tr&gt;&#10;    &lt;tr style=&quot;border-style: none;&quot;&gt;&lt;td headers=&quot;time&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;2026-04-02 22:00:00 EDT&lt;/td&gt;&#10;&lt;td headers=&quot;temp&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;38&lt;/td&gt;&#10;&lt;td headers=&quot;dewpoint&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;1.111111&lt;/td&gt;&#10;&lt;td headers=&quot;humidity&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;85&lt;/td&gt;&#10;&lt;td headers=&quot;p_rain&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;11&lt;/td&gt;&#10;&lt;td headers=&quot;wind_speed&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;12&lt;/td&gt;&#10;&lt;td headers=&quot;wind_dir&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;E&lt;/td&gt;&#10;&lt;td headers=&quot;skies&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;Patchy Fog&lt;/td&gt;&#10;&lt;td headers=&quot;geometry&quot; class=&quot;gt_row gt_center&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: center;&quot; valign=&quot;middle&quot; align=&quot;center&quot;&gt;c(-71.0552, 42.3515)&lt;/td&gt;&lt;/tr&gt;&#10;    &lt;tr style=&quot;border-style: none;&quot;&gt;&lt;td headers=&quot;time&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;2026-04-02 23:00:00 EDT&lt;/td&gt;&#10;&lt;td headers=&quot;temp&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;38&lt;/td&gt;&#10;&lt;td headers=&quot;dewpoint&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;1.111111&lt;/td&gt;&#10;&lt;td headers=&quot;humidity&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;85&lt;/td&gt;&#10;&lt;td headers=&quot;p_rain&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;11&lt;/td&gt;&#10;&lt;td headers=&quot;wind_speed&quot; class=&quot;gt_row gt_right&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: right; font-variant-numeric: tabular-nums;&quot; valign=&quot;middle&quot; align=&quot;right&quot;&gt;10&lt;/td&gt;&#10;&lt;td headers=&quot;wind_dir&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;E&lt;/td&gt;&#10;&lt;td headers=&quot;skies&quot; class=&quot;gt_row gt_left&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: left;&quot; valign=&quot;middle&quot; align=&quot;left&quot;&gt;Patchy Fog&lt;/td&gt;&#10;&lt;td headers=&quot;geometry&quot; class=&quot;gt_row gt_center&quot; style=&quot;border-style: none; padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; text-align: center;&quot; valign=&quot;middle&quot; align=&quot;center&quot;&gt;c(-71.0552, 42.3515)&lt;/td&gt;&lt;/tr&gt;&#10;  &lt;/tbody&gt;&#10;  &#10;&lt;/table&gt;&#10;&lt;/div&gt;" value-type="html"></shiny-tool-result>

### Additional display options

You can control how tool results are presented using additional display options:

- `show_request = FALSE`: Hide the tool call details when they're obvious from the display
- `open = TRUE`: Expand the result panel by default (useful for rich content like maps or charts)
- `title` and `icon`: Override the tool's default title and icon for this specific result

Another helpful feature is to include an `_intent` argument in your tool definition.
When present in the tool arguments, shinychat shows the `_intent` value in the tool card header, helping users understand why the LLM is calling the tool.

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-6" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-6-1">R</a></li>
<li><a href="#tabset-6-2">Python</a></li>
</ul>
<div id="tabset-6-1">

``` r
tool_with_intent <- tool(
  function(`_intent`) {
    runif(1)
  },
  name = "random_number",
  description = "Generate a random number.",
  arguments = list(
    `_intent` = type_string(
      "Explain why you're generating this number"
    )
  )
)
```

</div>
<div id="tabset-6-2">

``` python
def random_number(_intent: str) -> float:
    """Generate a random number.

    Args:
        _intent: Explain why you're generating this number
    """
    import random
    return random.random()
```

</div>
</div>

Notice that the tool function itself doesn't actually use the `_intent` argument, but its presence allows shinychat to give the user additional context about the tool call.

## Bookmarking support

When a Shiny app reloads, the app returns to its initial state, unless the URL includes [bookmarked state](https://shiny.posit.co/r/articles/build/bookmarking-state/).[^2]
Automatically updating the URL to include a bookmark of the chat state is a great way to help users return to their work if they accidentally refresh the page or unexpectedly lose their connection.

Both shinychat for R and Python provide helper functions that make it easy to restore conversations with bookmarks.
This means users can refresh the page or share a URL and pick up right where they left off.

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-7" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-7-1">R</a></li>
<li><a href="#tabset-7-2">Python</a></li>
</ul>
<div id="tabset-7-1">

In R, the `chat_restore()` function restores the message history from the bookmark when the app starts up *and* ensures that the chat client state is automatically bookmarked on user input and assistant responses.

``` r
library(shiny)
library(shinychat)

ui <- function(request) {
  page_fillable(
    chat_ui("chat")
  )
}

server <- function(input, output, session) {
  chat_client <- ellmer::chat_openai(model = "gpt-4o-mini")

  # Automatically save chat state on user input and responses
  chat_restore("chat", chat_client)

  observeEvent(input$chat_user_input, {
    stream <- chat_client$stream_async(input$chat_user_input)
    chat_append("chat", stream)
  })
}

# Enable URL-based bookmarking
shinyApp(ui, server, enableBookmarking = "url")
```

`enableBookmarking = "url"` stores the chat state in encoded data in the query string of the app's URL.
Because browsers have native limitations on the size of a URL, you should use `enableBookmarking = "server"` to store state server-side without URL size limitations for chatbots expected to have large conversation histories.

And if you're using `chat_app()` for quick prototypes, bookmarking is already enabled automatically.

</div>
<div id="tabset-7-2">

In Python, the `.enable_bookmarking()` method handles the where, when, and how of bookmarking chat state.

### Express mode

``` python
from chatlas import ChatOllama
from shiny.express import ui

chat_client = ChatOllama(model="llama3.2")

chat = ui.Chat(id="chat")
chat.ui(messages=["Welcome!"])

chat.enable_bookmarking(
    chat_client,
    bookmark_store="url", # or "server"
    bookmark_on="response", # or None
)
```

### Core mode

``` python
from chatlas import ChatOllama
from shiny import ui, App

app_ui = ui.page_fixed(
    ui.chat_ui(id="chat", messages=["Welcome!"])
)

def server(input):
    chat_client = ChatOllama(model="llama3.2")
    chat = ui.Chat(id="chat")

    chat.enable_bookmarking(
        chat_client,
        bookmark_on="response", # or None
    )

app = App(app_ui, server, bookmark_store="url")
```

### Configuration options

The `.enable_bookmarking()` method handles three aspects of bookmarking:

1.  **Where** (`bookmark_store`)
    - `"url"`: Store the state in the URL.
    - `"server"`: Store the state on the server. Consider this over `"url"` if you want to support a large amount of state, or have other bookmark state that can't be serialized to JSON.
2.  **When** (`bookmark_on`)
    - `"response"`: Triggers a bookmark when an `"assistant"` response is appended.
    - `None`: Don't trigger a bookmark automatically. This assumes you'll be triggering bookmarks through other means (e.g., a button).
3.  **How** is handled automatically by registering the relevant `on_bookmark` and `on_restore` callbacks.

When `.enable_bookmarking()` triggers a bookmark for you, it'll also update the URL query string to include the bookmark state.
This way, when the user unexpectedly loses connection, they can load the current URL to restore the chat state, or go back to the original URL to start over.

</div>
</div>

## Other improvements in shinychat for R

Beyond tool calling UI and bookmarking support, shinychat for R v0.3.0 includes several other enhancements.

### Better programmatic control

`chat_mod_server()` now returns a set of reactive values and functions for controlling the chat interface:

``` r
server <- function(input, output, session) {
  chat <- chat_mod_server("chat", ellmer::chat_openai())

  # React to user input
  observe({
    req(chat$last_input())
    print(paste("User said:", chat$last_input()))
  })

  # React to assistant responses
  observe({
    req(chat$last_turn())
    print("Assistant completed response")
  })

  # Programmatically control the chat
  observeEvent(input$suggest_question, {
    chat$update_user_input(
      value = "What's the weather like today?",
      submit = TRUE  # Automatically submit
    )
  })

  observeEvent(input$reset, {
    chat$clear()  # Clear history and UI
  })
}
```

The returned list includes:

- **`last_input`** and **`last_turn`** reactives for monitoring chat state
- **`update_user_input()`** for programmatically setting or submitting user input---great for suggested prompts or guided conversations
- **`append()`** for adding messages to the chat UI
- **`clear()`** for resetting the chat, with options to control how the client history is handled
- **`client`** for direct access to the ellmer chat client

There's also a standalone `update_chat_user_input()` function if you're using `chat_ui()` directly, which supports updating the placeholder text and moving focus to the input.

### Custom assistant icons

You can now customize the icon shown next to assistant messages to better match your application's branding or to distinguish between different assistants:

``` r
library(bsicons)

# Set a custom icon for a specific response
chat_append(
  "chat",
  "Here's some helpful information!",
  icon = bs_icon("lightbulb")
)

# Or set a default icon for all assistant messages
chat_ui("chat", icon_assistant = bs_icon("robot"))
```

This is especially useful when building multi-agent applications where different assistants might have different personalities or roles.

### Safer external links

External links in chat messages now open in a new tab with a confirmation dialog.
This prevents users from accidentally navigating away from the chat session and losing their conversation.
This is particularly helpful when LLMs include links in their responses, for example when shinychat is used in combination with Retrieval Augmented Generation via [ragnar](https://ragnar.tidyverse.org).

## Learn more

The tool calling UI opens up exciting possibilities for building transparent, user-friendly AI applications.
Whether you're fetching data, running calculations, or integrating with external services, users can now see exactly what's happening.

To dive deeper:

- Read the [tool calling UI article](https://posit-dev.github.io/shinychat/r/articles/tool-ui.html) for comprehensive examples in R
- Explore tool calling with [ellmer](https://ellmer.tidyverse.org/articles/tool-calling.html) (R) or [chatlas](https://posit-dev.github.io/chatlas/tool-calling/displays.html) (Python)

## Acknowledgements

A huge thank you to everyone who contributed to this release with bug reports, feature requests, and code contributions:

[@bianchenhao](https://github.com/bianchenhao), [@cboettig](https://github.com/cboettig), [@chendaniely](https://github.com/chendaniely), [@cpsievert](https://github.com/cpsievert), [@DavZim](https://github.com/DavZim), [@DeepanshKhurana](https://github.com/DeepanshKhurana), [@DivadNojnarg](https://github.com/DivadNojnarg), [@gadenbuie](https://github.com/gadenbuie), [@iainwallacebms](https://github.com/iainwallacebms), [@janlimbeck](https://github.com/janlimbeck), [@jcheng5](https://github.com/jcheng5), [@jimrothstein](https://github.com/jimrothstein), [@karangattu](https://github.com/karangattu), [@ManuelSpinola](https://github.com/ManuelSpinola), [@MohoWu](https://github.com/MohoWu), [@nissinbo](https://github.com/nissinbo), [@noamanemobidata](https://github.com/noamanemobidata), [@parmsam](https://github.com/parmsam), [@PaulC91](https://github.com/PaulC91), [@rkennedy01](https://github.com/rkennedy01), [@schloerke](https://github.com/schloerke), [@selesnow](https://github.com/selesnow), [@simonpcouch](https://github.com/simonpcouch), [@skaltman](https://github.com/skaltman), [@stefanlinner](https://github.com/stefanlinner), [@t-kalinowski](https://github.com/t-kalinowski), [@thendrix-trlm](https://github.com/thendrix-trlm), [@wch](https://github.com/wch), [@wlandau](https://github.com/wlandau), and [@Yousuf28](https://github.com/Yousuf28).

[^1]: See the [ellmer tool calling documentation](https://ellmer.tidyverse.org/articles/tool-calling.html) for R and the [chatlas tool calling documentation](https://posit-dev.github.io/chatlas/tool-calling/how-it-works.html) for Python for more details on defining and registering tools.

[^2]: This can be especially frustrating behavior since hosted apps, by default, will close an idle session after a certain ([configurable](https://docs.posit.co/shinyapps.io/guide/applications/#advanced-settings)) amount of time.
