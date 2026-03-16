library(asciicast)

# You might need to adjust the version number...
chromote::chrome_versions_remove("134.0.6998.88", "chrome")
chromote::chrome_versions_remove("134.0.6998.88", "chrome-headless-shell")

cast <- asciicast::record(
  r"(
library(chromote)

# Use the latest stable version of Chrome
local_chrome_version("latest-stable")

# Now `ChromoteSession` uses this version of Chrome...
chrome <- ChromoteSession$new()
chrome$Browser$getVersion()$product

# Switch to the latest stable version of chrome-headless-shell
local_chrome_version("latest-stable", binary = "chrome-headless-shell")

# Now ChromoteSession uses `chrome-headless-shell`...
chs <- ChromoteSession$new()
chs$Browser$getVersion()$product
  )"
)

theme <- default_theme()
theme$green <- c(60, 140, 0) # rgb(61, 140, 0)
theme$background = c(245, 245, 245) #F5F5F5
theme$bold = c(0, 0, 0) # rgb(0, 0, 0)
theme$cursor = c(0, 40, 200)
theme$text = c(50, 50, 50) #rgb(50, 50, 50)

asciicast::write_svg(cast, "chromote-demo.svg", theme = theme, cols = 80)
