-- Escape Hugo shortcodes inside code blocks
-- Converts {{< shortcode >}} to {{</* shortcode */>}}
-- so Hugo displays them as literal text instead of parsing them

function CodeBlock(el)
  -- Escape shortcodes in fenced code blocks
  el.text = el.text:gsub("{{<", "{{</*")
  el.text = el.text:gsub(">}}", "*/>}}")
  return el
end

function Code(el)
  -- Escape shortcodes in inline code
  el.text = el.text:gsub("{{<", "{{</*")
  el.text = el.text:gsub(">}}", "*/>}}")
  return el
end
