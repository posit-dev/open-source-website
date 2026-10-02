# Social Media Posts — Shiny for Python 1.6

## Blue Sky

> 300 character limit per post

Shiny for Python 1.6 is out! Two big additions: toolbar components for compact, modern UIs (thank you, @enelson5.bsky.social!) and built-in OpenTelemetry support for production observability. Zero Shiny changes required w/ usual OTel config.

`pip install -U shiny`

🔗: https://shiny.posit.co/blog/posts/shiny-python-1.6/

---

## LinkedIn

Shiny for Python 1.6 is now available on PyPI!

This release ships two major additions:

**Toolbars** — A new family of compact components (`ui.toolbar()`, `ui.toolbar_input_button()`, `ui.toolbar_input_select()`) designed to fit controls into tight spaces. Place them in card headers and footers, inline with input labels, or directly inside `input_submit_textarea()` for AI chat interfaces. The same toolbar components are also available in bslib for R.

**OpenTelemetry** — Built-in observability support with zero changes to your app code. Set a single environment variable (`SHINY_OTEL_COLLECT=reactivity`), point Shiny at any OTLP-compatible backend, and get full traces of session lifecycles, reactive update cascades, and individual reactive expressions. This is particularly useful for GenAI apps where you need to understand whether slowdowns are in model calls, tool execution, or downstream reactive calculations.

Upgrade today:

```
pip install -U shiny
```

Full release notes and examples: https://shiny.posit.co/blog/posts/shiny-python-1.6/
