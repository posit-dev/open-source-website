#!/bin/sh -xe
ffmpeg -i "$1" -b:v 0 -crf 30 -pass 1 -an -f webm -y /dev/null
ffmpeg -i "$1" -b:v 0 -crf 30 -pass 2 "${1%.mp4}.webm"
