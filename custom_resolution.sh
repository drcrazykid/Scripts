#/bin/bash
# XRANDR custom screen resolution

# First we need to get the modeline string for xrandr
# Luckily, the tool "gtf" will help you calculate it.
# All you have to do is to pass the resolution & the-
# refresh-rate as the command parameters:
gtf 2560 1440 120

# In this case, the horizontal resolution is 1920px the
# vertical resolution is 1080px & refresh-rate is 60Hz.
# IMPORTANT: BE SURE THE MONITOR SUPPORTS THE RESOLUTION

# Typically, it outputs a line starting with "Modeline"
# e.g. "1920x1080_60.00"  172.80  1920 2040 2248 2576  1080 1081 1084 1118  -HSync +Vsync
# Copy this entire string (except for the starting "Modeline")

# Now, use "xrandr" to make the system recognize a new
# display mode. Pass the copied string as the parameter
# to the --newmode option:
xrandr --newmode "2560x1440"  311.83  2560 2744 3024 3488  1440 1441 1444 1490  -HSync +Vsync

# Well, the string within the quotes is the nick/alias
# of the display mode - you can as well pass something
# as "MyAwesomeHDResolution". But, careful! :-|

# Then all you have to do is to add the new mode to the
# display you want to apply, like this:
xrandr --addmode VGA1 "2560x1440_60.00"

# VGA1 is the display name, it might differ for you.
# Run "xrandr" without any parameters to be sure.
# The last parameter is the mode-alias/name which
# you've set in the previous command (--newmode)

# It should add the new mode to the display & apply it.
# Usually unlikely, but if it doesn't apply automatically
# then force it with this command:
xrandr --output VGA1 --mode "2560x1440_60.00"