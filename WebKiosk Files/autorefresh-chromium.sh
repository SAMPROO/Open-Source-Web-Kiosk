#!/bin/bash
#declare -i a #turn parameter to int
#a = $1
DISPLAY=:0 xdotool key "ctrl+F5"
export DISPLAY=:0

while true; #create an infinite loop
do
  xdotool key "ctrl+F5" &
  sleep $1 #refresh time in seconds
done
