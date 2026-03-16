-- Strip Bootstrap classes from elements
-- These classes are designed for Bootstrap CSS and don't work with Tailwind

-- Classes that should cause the entire element to be removed
local remove_element_classes = {
  ["dark-content"] = true,  -- Dark mode images, we only show light versions
}

-- Bootstrap class patterns to strip
local bootstrap_patterns = {
  -- Buttons
  "^btn$", "^btn%-",
  -- Bootstrap Icons
  "^bi$", "^bi%-",
  -- Font Awesome
  "^fa$", "^fa%-", "^fas$", "^far$", "^fab$",
  -- Spacing utilities (margin/padding)
  "^m[xytblr]?%-", "^p[xytblr]?%-",
  -- Flexbox
  "^d%-flex$", "^d%-block$", "^d%-inline", "^d%-grid$", "^d%-none$",
  "^flex%-", "^align%-items%-", "^align%-self%-", "^justify%-content%-",
  -- Text utilities
  "^text%-muted$", "^text%-end$", "^text%-center$", "^text%-start$",
  "^fw%-", "^fs%-", "^fst%-",
  -- Images
  "^img%-fluid$", "^img%-shadow$", "^shadow$", "^lightbox$",
  -- Nav/tabs
  "^nav$", "^nav%-", "^tab%-",
  -- Visibility
  "^visually%-hidden$",
  -- Code highlighting (Jekyll artifact)
  "^language%-plaintext$", "^highlighter%-rouge$",
  -- Layout
  "^container$", "^container%-", "^row$", "^col$", "^col%-",
  -- Quarto-specific layout (won't work in Hugo)
  "^column%-page$", "^column%-body$", "^column%-margin$",
}

-- Check if a class should be stripped
local function should_strip(class)
  for _, pattern in ipairs(bootstrap_patterns) do
    if class:match(pattern) then
      return true
    end
  end
  return false
end

-- Filter classes, returning only non-Bootstrap ones
local function filter_classes(classes)
  local kept = {}
  for _, class in ipairs(classes) do
    if not should_strip(class) then
      table.insert(kept, class)
    end
  end
  return kept
end

-- Check if element should be removed entirely
local function should_remove_element(classes)
  for _, class in ipairs(classes) do
    if remove_element_classes[class] then
      return true
    end
  end
  return false
end

-- Process any element with classes
local function process_element(el)
  if el.classes and #el.classes > 0 then
    -- Check if element should be removed entirely
    if should_remove_element(el.classes) then
      return {}  -- Return empty list to remove element
    end
    el.classes = filter_classes(el.classes)
  end
  return el
end

-- Process class attribute in raw HTML string
local function process_raw_html(html)
  -- Find and process class="..." attributes
  local result = html:gsub('class="([^"]*)"', function(classes)
    local kept = {}
    for class in classes:gmatch("%S+") do
      if not should_strip(class) then
        table.insert(kept, class)
      end
    end
    if #kept == 0 then
      return ''  -- Remove empty class attribute entirely
    else
      return 'class="' .. table.concat(kept, " ") .. '"'
    end
  end)
  -- Clean up leftover spaces from removed attributes (e.g., '<code >' -> '<code>')
  result = result:gsub(' >', '>')
  result = result:gsub(' />', '/>')
  return result
end

-- Process raw HTML blocks and inlines
local function process_raw(el)
  if el.format == "html" then
    el.text = process_raw_html(el.text)
  end
  return el
end

return {
  Div = process_element,
  Span = process_element,
  Image = process_element,
  Link = process_element,
  Code = process_element,
  CodeBlock = process_element,
  RawInline = process_raw,
  RawBlock = process_raw,
}
