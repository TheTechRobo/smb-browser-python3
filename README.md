# smb-browser-python3

Designed and tested on Elive.

GTK+ app (PyGObject) that allows you to mount Samba shares.

# Instructions
There's three ways

## Installing the .deb (debian)
Go to this link. https://github.com/TheTechRobo/smb-browser-python3/releases. Install the deb file.

## Building a .deb file from source
```zsh
make deb
cd build
sudo apt install ./youtube-dl-gui.deb
```
If on an old version of Debian, you may need to replace `apt` with `apt-get` - try that if `apt` returns "command not found".


## Manual
Copy the files inside `tree/usr` into your `/usr/` folder. Making sure it doesn't overwrite anything.

I'd really appreciate build instructions for other distros!
