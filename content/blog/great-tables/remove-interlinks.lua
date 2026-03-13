Link = function(link)
  if not link.target:match("%%60") then
        return link
  end
  return pandoc.Inlines(link.content)
end