#!/bin/zsh

utils_root_dir="$HOME/Scripts/utils"
chosen=$(find $utils_root_dir -type f | rofi -dmenu -p "Utils Scripts")

if [[ $chosen = "" ]]; then
  exit 1;
fi

. $chosen
