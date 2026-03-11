#! /usr/local/bin/Rscript
library(readr)

filename <- "./index.md"
inputtext <- read_file(filename)
# text <- "xxx [text info](http://url) yyy [text info2](http://url2) zzz"

newtext <- gsub('\\[(.*?)\\]\\((.*?)\\)', '<a href="\\2" target="_blank" rel="noopener noreferrer">\\1</a>', inputtext)
write_file(newtext, "./newindex.Rmd")
