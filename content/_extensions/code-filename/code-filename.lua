-- code-filename filter for Hugo
-- Converts Quarto's filename attribute on non-executable code blocks
-- into Goldmark-compatible fenced code with { filename="..." } attribute,
-- so Hugo's render-codeblock hook can render a styled filename label.
--
-- Without this filter, Quarto renders filename as bold text above the block.

-- Only run for hugo-md format
if not quarto.doc.is_format("hugo-md") and not quarto.doc.is_format("gfm") then
  return {}
end

function CodeBlock(el)
  local filename = el.attributes["filename"]
  if not filename then
    return nil
  end

  -- Remove filename from attributes so Quarto doesn't also render it as bold
  el.attributes["filename"] = nil

  -- Build the Goldmark-compatible fenced code block
  -- Hugo expects: ``` lang { filename="value" }
  local lang = ""
  if #el.classes > 0 then
    lang = " " .. el.classes[1]
  end

  -- Ensure text ends with a newline before the closing fence
  local text = el.text
  if text:sub(-1) ~= "\n" then
    text = text .. "\n"
  end

  -- Use an outer fence longer than any run of backticks inside the code, so
  -- nested ``` fences (e.g. example blocks showing code chunks) don't close it
  -- early. This mirrors CommonMark's own rule for nesting fenced code.
  local max_ticks = 0
  for ticks in text:gmatch("`+") do
    if #ticks > max_ticks then
      max_ticks = #ticks
    end
  end
  local fence = string.rep("`", math.max(3, max_ticks + 1))

  -- Leading newline ensures a blank line before the fence, which Goldmark
  -- requires when the preceding block is raw HTML (e.g. a callout closing tag).
  -- Extra blank lines are harmless in Markdown.
  local raw = "\n" .. fence .. lang .. " { filename=\"" .. filename .. "\" }\n"
    .. text
    .. fence .. "\n"

  return pandoc.RawBlock("markdown", raw)
end
