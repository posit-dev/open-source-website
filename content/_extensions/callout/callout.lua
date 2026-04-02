-- callout filter for Hugo
-- Transforms .callout-* divs into styled HTML wrappers before Quarto
-- converts them to plain blockquotes in hugo-md output.
-- Body content is kept as Pandoc AST so it renders as markdown, not HTML.

local callout_types = {
  ["callout-note"]      = { label = "Note",      icon = "info-circle" },
  ["callout-tip"]       = { label = "Tip",        icon = "lightbulb" },
  ["callout-warning"]   = { label = "Warning",    icon = "alert-triangle" },
  ["callout-caution"]   = { label = "Caution",    icon = "alert-octagon" },
  ["callout-important"] = { label = "Important",  icon = "alert-circle" },
}

-- SVG icons (tabler-icons style, decorative)
local icons = {
  ["info-circle"] = '<svg class="callout-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>',
  ["lightbulb"] = '<svg class="callout-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2a7 7 0 0 0 -4 12.9l0 .1v1h8v-1l0 -.1a7 7 0 0 0 -4 -12.9"/></svg>',
  ["alert-triangle"] = '<svg class="callout-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 9v4"/><path d="M10.363 3.591l-8.106 13.534a1.914 1.914 0 0 0 1.636 2.871h16.214a1.914 1.914 0 0 0 1.636 -2.87l-8.106 -13.536a1.914 1.914 0 0 0 -3.274 0z"/><path d="M12 16h.01"/></svg>',
  ["alert-octagon"] = '<svg class="callout-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 9v4"/><path d="M7.86 2h8.28l5.86 5.86v8.28l-5.86 5.86h-8.28l-5.86 -5.86v-8.28z"/><path d="M12 16h.01"/></svg>',
  ["alert-circle"] = '<svg class="callout-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>',
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

  local icon_html = icons[info.icon] or ""
  local blocks = pandoc.List()

  if collapse == "true" then
    -- Collapsible callout: opening <details>/<summary>
    blocks:insert(pandoc.RawBlock("html",
      '<details class="callout ' .. cls .. '" role="note">\n' ..
      '<summary class="callout-header">\n' ..
      icon_html .. '\n' ..
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
      '<div class="callout ' .. cls .. '" role="note">\n' ..
      '<div class="callout-header">\n' ..
      icon_html .. '\n' ..
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
