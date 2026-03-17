-- Video embed filter - intercepts Quarto video shortcodes and outputs Hugo shortcodes
-- Runs at pre-quarto stage to intercept before Quarto processes them
-- Only active for hugo-md format

function Pandoc(doc)
  -- Only run for hugo-md format
  if not quarto.doc.is_format("hugo-md") then
    return doc
  end

  local node_data = quarto._quarto.ast.custom_node_data

  -- Build a map of video shortcode IDs to their params
  local video_data = {}
  for id, data in pairs(node_data) do
    if data.name == "video" and data.params then
      local params = {}
      for _, param in ipairs(data.params) do
        if param.type == "param" then
          -- Positional param is the src
          params.src = param.value
        elseif param.key then
          -- Named param
          params[param.key] = param.value
        end
      end
      if params.src then
        video_data[tostring(id)] = params
      end
    end
  end

  -- Skip walk if no video shortcodes
  if not next(video_data) then
    return doc
  end

  -- Walk the document and replace video shortcode paragraphs with Hugo shortcodes
  local modified = doc:walk({
    Para = function(el)
      -- Check if paragraph contains a single video shortcode span
      if #el.content == 1 and el.content[1].t == "Span" then
        local span = el.content[1]
        if span.attributes["__quarto_custom_type"] == "Shortcode" then
          local id = span.attributes["__quarto_custom_id"]
          local params = video_data[id]

          if params and params.src then
            -- Build shortcode with all params
            local parts = { string.format('src="%s"', params.src) }
            for key, value in pairs(params) do
              if key ~= "src" then
                table.insert(parts, string.format('%s="%s"', key, value))
              end
            end
            local shortcode = '{{{< video ' .. table.concat(parts, ' ') .. ' >}}}'
            return pandoc.RawBlock("markdown", shortcode)
          end
        end
      end
      return nil
    end
  })

  return modified
end
