#!/usr/bin/env bash

# OK, we can't actually fix libinput because it's terrible.  But this should
# un-break a logitech trackball using the accompanying 52-logitechmarble.conf
# if you are as profoundly unlucky as to have a machine with libinput.  You
# will have to change the button number if you aren't using button 8.

# Owain Kenway

scroll_button=8

# Get the device ID as this could change.
id_temp=$(xinput list | grep "Logitech USB Trackball" | awk '{print $6}')
id=${id_temp:3}

# Turn on three button emulation
xinput set-prop ${id} "libinput Middle Emulation Enabled" 1

# Set the scroll button to the value of scroll_button
xinput set-prop ${id} "libinput Button Scrolling Button" ${scroll_button}
