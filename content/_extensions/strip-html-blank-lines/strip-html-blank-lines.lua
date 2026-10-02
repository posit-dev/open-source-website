-- Collapse blank lines inside raw HTML blocks so Hugo's Goldmark parser keeps
-- the HTML block contiguous.
--
-- Background: Hugo's Goldmark closes a CommonMark "type 6" HTML block (one
-- opened by <div>, <table>, etc.) at the first blank line. Pointblank and
-- great-tables emit tables whose <div> wrappers contain blank lines, which
-- causes Goldmark to drop out of HTML mode mid-table and re-parse the rest as
-- markdown -- wrapping CSS in <p> tags and turning indented SVG payloads into
-- <pre><code> blocks. Stripping the blank lines keeps everything inside one
-- HTML block.

if not quarto.doc.is_format("hugo-md") and not quarto.doc.is_format("gfm") then
  return {}
end

local function collapse_blanks(text)
  local previous
  repeat
    previous = text
    text = text:gsub("\n[ \t]*\n", "\n")
  until text == previous
  return text
end

function RawBlock(el)
  if el.format == "html" then
    el.text = collapse_blanks(el.text)
    return el
  end
end
