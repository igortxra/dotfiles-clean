#!/bin/sh

# Enable numlock
numlockx on &

# Remaps caps to super
setxkbmap -option caps:super

# Load wallpaper
$HOME/.fehbg &

# Greenclip Daemon (for clipboard manager)
greenclip daemon &

# Notification Daemon
dunst &

# Compositor
picom &

# Auto detect screen profile
autorandr --change &
