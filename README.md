# youtube-dl-gui
A small GUI frontend for youtube-dl designed for Elive Linux

# Requirements
This has only been tested on Debian/Elive Linux, and will NEVER work on Windows unless there is  some major refactoring or you use Git Bash.

You will need the following package  `mpg321` and also `python3-tk`. 

# Credits
## Code
See inside of source code, there's stuff scattered around.
## Song
Pandemic by CHRISRGMFB  
https://chrisrgmfb.com  
Promoted by Royalty Free Planet: https://royaltyfreeplanet.com  
Creative Commons Attribution 3.0

# Instructions
There's three ways

## Installing the .deb (debian)
Go to this link. https://github.com/TheTechRobo/youtube-dl-gui/releases. Install the deb file.

## Building a .deb file from source
```zsh
make deb
cd build
sudo apt install ./youtube-dl-gui.deb
```

## Manual
Copy the files inside `usr` into your `/usr/` folder. Making sure it doesn't overwrite anything.
