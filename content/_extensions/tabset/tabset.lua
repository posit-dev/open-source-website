-- tabset filter for Hugo
-- Transforms .panel-tabset divs into HTML that works with Tabby.js

local tabset_counter = 0

-- Render pandoc inlines to HTML
local function inlines_to_html(inlines)
  local html = pandoc.write(pandoc.Pandoc({pandoc.Plain(inlines)}), "html")
  -- Strip wrapping <p> tags
  return html:gsub("^%s*<p>", ""):gsub("</p>%s*$", "")
end

-- Parse tabset: extract headers as tab titles, group following content
local function parse_tabset(div)
  -- Find first header to determine the tab heading level
  local level = nil
  for _, el in ipairs(div.content) do
    if el.t == "Header" then
      level = el.level
      break
    end
  end

  if level == nil then
    return nil
  end

  -- Group content by headers at this level
  local tabs = {}
  local current_tab = nil

  for _, el in ipairs(div.content) do
    if el.t == "Header" and el.level == level then
      current_tab = {
        title = el.content,
        content = pandoc.List(),
        active = el.classes:includes("active")
      }
      table.insert(tabs, current_tab)
    elseif current_tab ~= nil then
      current_tab.content:insert(el)
    end
  end

  return tabs
end

-- Build blocks for Tabby.js tabset
-- Returns a list of Pandoc blocks with HTML wrappers but AST content
local function render_tabset(tabs, tabset_id)
  local blocks = pandoc.List()

  -- Default first tab to active if none specified
  local has_active = false
  for _, tab in ipairs(tabs) do
    if tab.active then has_active = true; break end
  end
  if not has_active and #tabs > 0 then
    tabs[1].active = true
  end

  -- Opening container and tab navigation
  local nav_html = {'<div class="panel-tabset">'}
  table.insert(nav_html, '<ul id="' .. tabset_id .. '" class="panel-tabset-tabby">')
  for i, tab in ipairs(tabs) do
    local panel_id = tabset_id .. "-" .. i
    local default_attr = tab.active and 'data-tabby-default ' or ''
    local title = inlines_to_html(tab.title)
    table.insert(nav_html, '<li><a ' .. default_attr .. 'href="#' .. panel_id .. '">' .. title .. '</a></li>')
  end
  table.insert(nav_html, '</ul>')
  blocks:insert(pandoc.RawBlock("html", table.concat(nav_html, "\n")))

  -- Tab panels with AST content (not converted to HTML)
  for i, tab in ipairs(tabs) do
    local panel_id = tabset_id .. "-" .. i
    blocks:insert(pandoc.RawBlock("html", '<div id="' .. panel_id .. '">'))
    blocks:extend(tab.content)
    blocks:insert(pandoc.RawBlock("html", '</div>'))
  end

  -- Close container
  blocks:insert(pandoc.RawBlock("html", '</div>'))

  return blocks
end

-- Main filter
function Div(div)
  if not quarto.doc.is_format("hugo-md") then
    return div
  end

  if not div.classes:includes("panel-tabset") then
    return div
  end

  local tabs = parse_tabset(div)
  if tabs == nil or #tabs == 0 then
    return div
  end

  tabset_counter = tabset_counter + 1
  local tabset_id = "tabset-" .. tabset_counter

  return render_tabset(tabs, tabset_id)
end
