-- layout filter for Hugo
-- Transforms layout-ncol / layout / layout-nrow divs into CSS grid HTML.
-- Uses the HTML+AST sandwich pattern so cell content (code blocks, images,
-- markdown) is kept as Pandoc AST and rendered correctly by Goldmark.
-- Mirrors the Tailwind classes used by layouts/shortcodes/columns.html.

-- Collect cells from a layout div.
-- If any direct children are Div elements, each Div is one cell.
-- Otherwise, each top-level block is one cell (common for bare image grids).
local function collect_cells(div)
  local cells = pandoc.List()
  local has_divs = false

  for _, el in ipairs(div.content) do
    if el.t == "Div" then
      has_divs = true
      break
    end
  end

  if has_divs then
    for _, el in ipairs(div.content) do
      if el.t == "Div" then
        cells:insert(el.content)
      end
    end
  else
    for _, el in ipairs(div.content) do
      local cell = pandoc.List()
      cell:insert(el)
      cells:insert(cell)
    end
  end

  return cells
end

-- Parse a layout weight string like "[70,30]" or "[[3,1]]" into a list of
-- weight strings, handling both single-row shorthand and explicit multi-row.
-- Returns two values: rows (list of lists of weight strings), is_multi_row.
local function parse_layout_string(layout)
  -- Multi-row: "[[r1c1,r1c2],[r2c1,...]]"
  local is_multi = layout:match("^%[%[")
  if is_multi then
    local rows = pandoc.List()
    -- Extract each [...] group inside the outer [[...]]
    for row_str in layout:gmatch("%[([^%[%]]+)%]") do
      local weights = pandoc.List()
      for w in row_str:gmatch("[^,]+") do
        weights:insert(w:match("^%s*(.-)%s*$"))  -- trim
      end
      rows:insert(weights)
    end
    return rows, true
  else
    -- Single-row shorthand: "[70,30]"
    local inner = layout:match("%[(.-)%]")
    if not inner then return pandoc.List(), false end
    local weights = pandoc.List()
    for w in inner:gmatch("[^,]+") do
      weights:insert(w:match("^%s*(.-)%s*$"))
    end
    local rows = pandoc.List()
    rows:insert(weights)
    return rows, false
  end
end

-- Build the Tailwind grid-cols class for a list of weight strings.
local function weights_to_grid_class(weights)
  -- Check if all weights are equal (emit md:grid-cols-N for cleaner output)
  local first = weights[1]
  local all_equal = true
  for _, w in ipairs(weights) do
    if w ~= first then all_equal = false; break end
  end
  if all_equal then
    return "md:grid-cols-" .. #weights
  end
  -- Proportional: md:grid-cols-[70fr_30fr]
  local parts = pandoc.List()
  for _, w in ipairs(weights) do
    parts:insert(w .. "fr")
  end
  return "md:grid-cols-[" .. table.concat(parts, "_") .. "]"
end

-- Emit one grid row as a list of Pandoc blocks (HTML+AST sandwich).
local function render_row(cells, grid_class, align_class, extra_classes)
  local blocks = pandoc.List()
  local classes = "grid gap-12 " .. align_class .. " mt-12 " .. grid_class
  if extra_classes ~= "" then
    classes = classes .. " " .. extra_classes
  end
  blocks:insert(pandoc.RawBlock("html", '<div class="' .. classes .. '">'))
  for _, cell in ipairs(cells) do
    blocks:insert(pandoc.RawBlock("html", '<div class="prose max-w-none">'))
    blocks:extend(cell)
    blocks:insert(pandoc.RawBlock("html", "</div>"))
  end
  blocks:insert(pandoc.RawBlock("html", "</div>"))
  return blocks
end

function Div(div)
  if not quarto.doc.is_format("hugo-md") then
    return div
  end

  local ncol   = div.attributes["layout-ncol"]
  local layout = div.attributes["layout"]

  -- Only act on divs that carry a layout attribute
  if not ncol and not layout then
    return div
  end

  local valign = div.attributes["layout-valign"]
  local align_class = (valign == "center") and "items-center" or "items-start"

  -- Pass through any non-layout classes on the outer div
  -- (e.g. column-body-outset-right), but strip Quarto's own layout classes.
  local layout_class_prefixes = {
    "column%-", "layout%-"
  }
  local extra_parts = pandoc.List()
  for _, cls in ipairs(div.classes) do
    local skip = false
    for _, prefix in ipairs(layout_class_prefixes) do
      if cls:match("^" .. prefix) then skip = true; break end
    end
    if not skip then
      extra_parts:insert(cls)
    end
  end
  local extra_classes = table.concat(extra_parts, " ")

  local blocks = pandoc.List()

  if layout then
    -- layout="[W1,W2]" or layout="[[R1C1,R1C2],[R2C1]]"
    local rows, is_multi = parse_layout_string(layout)

    if is_multi then
      -- Multiple rows: each row gets its own grid div.
      -- We need to split cells across rows according to the row widths.
      local all_cells = collect_cells(div)
      local cell_idx = 1
      for _, weights in ipairs(rows) do
        local ncols_in_row = #weights
        local row_cells = pandoc.List()
        for _ = 1, ncols_in_row do
          if all_cells[cell_idx] then
            row_cells:insert(all_cells[cell_idx])
            cell_idx = cell_idx + 1
          end
        end
        local gcls = weights_to_grid_class(weights)
        blocks:extend(render_row(row_cells, gcls, align_class, extra_classes))
        -- Only apply extra_classes (like column-body-outset-right) to the first row
        extra_classes = ""
      end
    else
      local weights = rows[1]
      local gcls = weights_to_grid_class(weights)
      local cells = collect_cells(div)
      blocks:extend(render_row(cells, gcls, align_class, extra_classes))
    end

  else
    -- layout-ncol=N: equal-width columns
    local weights = pandoc.List()
    local n = tonumber(ncol) or 2
    for _ = 1, n do weights:insert("1") end
    local gcls = "md:grid-cols-" .. n
    local cells = collect_cells(div)
    blocks:extend(render_row(cells, gcls, align_class, extra_classes))
  end

  return blocks
end
