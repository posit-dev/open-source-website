-- callout filter for Hugo
-- Transforms .callout-* divs into styled HTML wrappers before Quarto
-- converts them to plain blockquotes in hugo-md output.
-- Body content is kept as Pandoc AST so it renders as markdown, not HTML.

-- Icons are handled purely in CSS via ::before pseudo-elements on .callout-header,
-- using mask-image to reference SVGs from /icons/. No icon markup in the HTML.
local callout_types = {
  ["callout-note"]      = { label = "Note" },
  ["callout-tip"]       = { label = "Tip" },
  ["callout-warning"]   = { label = "Warning" },
  ["callout-caution"]   = { label = "Caution" },
  ["callout-important"] = { label = "Important" },
}

-- Detect which callout type a div is, if any
local function get_callout_type(div)
  for cls, info in pairs(callout_types) do
    if div.classes:includes(cls) then
      return cls, info
    end
  end
  return nil, nil
end

-- Extract title from the first header in the div, if present
local function extract_title(div)
  local title_inlines = nil
  local body_content = pandoc.List()

  for _, el in ipairs(div.content) do
    if el.t == "Header" and title_inlines == nil then
      title_inlines = el.content
    else
      body_content:insert(el)
    end
  end

  return title_inlines, body_content
end

-- Render pandoc inlines to HTML string
local function inlines_to_html(inlines)
  local html = pandoc.write(pandoc.Pandoc({pandoc.Plain(inlines)}), "html")
  return html:gsub("^%s*<p>", ""):gsub("</p>%s*$", "")
end

function Div(div)
  if not quarto.doc.is_format("hugo-md") then
    return div
  end

  local cls, info = get_callout_type(div)
  if cls == nil then
    return div
  end

  local collapse = div.attributes["collapse"]
  local title_inlines, body_content = extract_title(div)

  -- Use default label if no title header was provided
  local title_html
  if title_inlines ~= nil then
    title_html = inlines_to_html(title_inlines)
  else
    title_html = info.label
  end

  local blocks = pandoc.List()

  -- aria-label preserves the callout type for screen readers even when
  -- the visible title is custom (e.g. "Watch out!" instead of "Warning")
  local aria = ' aria-label="' .. info.label .. '"'

  if collapse == "true" then
    -- Collapsible callout: opening <details>/<summary>
    blocks:insert(pandoc.RawBlock("html",
      '<details class="callout ' .. cls .. '" role="note"' .. aria .. '>\n' ..
      '<summary class="callout-header">\n' ..
      '<span class="callout-title">' .. title_html .. '</span>\n' ..
      '</summary>\n' ..
      '<div class="callout-body">'
    ))
    -- Body content as AST (renders to markdown)
    blocks:extend(body_content)
    -- Close
    blocks:insert(pandoc.RawBlock("html", '</div>\n</details>'))
  else
    -- Standard callout: opening wrapper + header
    blocks:insert(pandoc.RawBlock("html",
      '<div class="callout ' .. cls .. '" role="note"' .. aria .. '>\n' ..
      '<div class="callout-header">\n' ..
      '<span class="callout-title">' .. title_html .. '</span>\n' ..
      '</div>\n' ..
      '<div class="callout-body">'
    ))
    -- Body content as AST (renders to markdown)
    blocks:extend(body_content)
    -- Close
    blocks:insert(pandoc.RawBlock("html", '</div>\n</div>'))
  end

  return blocks
end
