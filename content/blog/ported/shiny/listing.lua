--[[
listing.lua

Minimal stand-in for Quarto's listings feature, applied at qmd→md render.
Reads the document `listing:` metadata, loads the referenced YAML file, and
replaces the Div whose `id` matches with rendered Blocks — one section per
item.

Schema (under document `listing:`):
  listing:
    - id: <div-id>
      contents: <yml-path-relative-to-source>

Per-item fields (all optional except title):
  title         heading text
  conf_link     primary link → titled "Conf talk page" in the footer
  scipy_link    primary link → titled "SciPy talk page" in the footer
  *_link        any other "<x>_link" → titled "Talk page"
  speaker       meta row "Speaker"
  track         meta row "Track"
  date_display  meta row "When" (joined with `time`)
  time          meta row "When"
  room          meta row "Room"
  slides_link   footer link "Slides"
  abstract      markdown paragraphs after the meta line

Output per item is plain markdown (heading + meta line + links line + optional
abstract). No Bootstrap markup, so strip-bootstrap has nothing to do.
]]--

local function read_yaml(path)
  -- pandoc.pipe runs the command and returns stdout; YAML→JSON via python3.
  local script = "import yaml, json, sys; print(json.dumps(yaml.safe_load(open(sys.argv[1]))))"
  local out = pandoc.pipe("python3", { "-c", script, path }, "")
  return pandoc.json.decode(out)
end

local function input_dir()
  local input = quarto and quarto.doc and quarto.doc.input_file
    or PANDOC_STATE.input_files[1]
  if not input then return "." end
  return input:match("(.*)/") or "."
end

local function present(v)
  return type(v) == "string" and v ~= "" and v ~= "~"
end

local PRIMARY_LINK_LABELS = {
  video_link = "Video",
  conf_link = "Conf talk page",
  scipy_link = "SciPy talk page",
}

local function primary_link(talk)
  -- Deterministic order: prefer the named ones, then fall back to any *_link.
  for _, k in ipairs({ "video_link", "conf_link", "scipy_link" }) do
    if present(talk[k]) then
      return talk[k], PRIMARY_LINK_LABELS[k]
    end
  end
  for k, v in pairs(talk) do
    if type(k) == "string" and k:match("_link$") and k ~= "slides_link" and present(v) then
      return v, "Talk page"
    end
  end
  return nil, nil
end

local function meta_line(talk)
  local parts = {}
  if present(talk.speaker) then
    table.insert(parts, "**Speaker:** " .. talk.speaker)
  end
  if present(talk.track) then
    table.insert(parts, "**Track:** " .. talk.track)
  end
  local when = {}
  for _, k in ipairs({ "date_display", "time" }) do
    if present(talk[k]) then table.insert(when, talk[k]) end
  end
  if #when > 0 then
    table.insert(parts, "**When:** " .. table.concat(when, " "))
  end
  if present(talk.room) then
    table.insert(parts, "**Room:** " .. talk.room)
  end
  return table.concat(parts, " · ")
end

local function render_talk_md(talk)
  local lines = {}
  local title = talk.title or "(untitled)"
  local link, link_label = primary_link(talk)
  table.insert(lines, "### " .. title)
  table.insert(lines, "")

  local meta = meta_line(talk)
  if meta ~= "" then
    table.insert(lines, meta)
    table.insert(lines, "")
  end

  local footer = {}
  if link then
    table.insert(footer, string.format("[%s](%s)", link_label, link))
  end
  if present(talk.slides_link) then
    table.insert(footer, string.format("[Slides](%s)", talk.slides_link))
  end
  if #footer > 0 then
    table.insert(lines, table.concat(footer, " · "))
    table.insert(lines, "")
  end

  if present(talk.abstract) then
    table.insert(lines, talk.abstract)
    table.insert(lines, "")
  end

  return table.concat(lines, "\n")
end

local function blocks_from_items(items)
  local md = {}
  for _, talk in ipairs(items) do
    table.insert(md, render_talk_md(talk))
  end
  local doc = pandoc.read(table.concat(md, "\n"), "markdown")
  return doc.blocks
end

local listings_by_id = {}

return {
  -- Pass 1: read meta, load each referenced YAML, build replacement blocks.
  {
    Pandoc = function(doc)
      local listings = doc.meta.listing
      if not listings then return nil end

      local base = input_dir()
      for _, entry in ipairs(listings) do
        local id = pandoc.utils.stringify(entry.id)
        local contents = pandoc.utils.stringify(entry.contents)
        local path = base .. "/" .. contents
        local items = read_yaml(path)
        listings_by_id[id] = blocks_from_items(items)
      end

      -- Drop `listing` from meta so it doesn't leak into the rendered .md
      -- frontmatter (Hugo would just ignore it, but it's noise).
      doc.meta.listing = nil
      return doc
    end,
  },
  -- Pass 2: drop the rendered blocks into any Div whose id matches.
  {
    Div = function(div)
      local replacement = listings_by_id[div.identifier]
      if replacement then
        div.content = replacement
        return div
      end
    end,
  },
}
