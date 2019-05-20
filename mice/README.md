# Various mouse config files

![Mouse](../images/icons/mouse-crop.gif)

* `50-vmmouse.conf` - Saitek/Madcatz R.A.T.3.
* `52-logitechmarble.conf` - Logitech Marble trackball - left mini button scrolls, right mini button middle-clicks, emulate3 buttons enabled. 2D scrolling.

On Ubuntu/Raspbian these go in `/usr/share/X11/xorg.conf.d`.

* `fix_libinput.sh` - This shell script enforces settings from `52-logitechmarble.conf` which are mysteriously overridden on some distros with `libinput` e.g. Raspbian.  This needs to be run at every login by whichever method you prefer.

* `ubuntu-18.04-40-libinput.conf` - Settings for the Logitech Marble trackball to go into `/usr/share/X11/xorg.conf.d/40-libinput.conf` on Ubuntu 18.04 to achieve the same settings as the config file/fix script above.
