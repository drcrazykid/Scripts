#!/usr/bin/bash

# URL 
$dir = "/home/$(whoami)/Downloads/Documtents/"

if [ -d "$dir" ]; then
	cd $dir
else
	cd "/home/$(whoami)/Downloads/"
fi

# download necessary files from git
git clone https://aur.archlinux.org/snapd.git
cd snapd
makepkg -si

#enable the service to allow the socket
sudo systemctl enable --now snapd.socket

# Install odrive-unofficial
sudo snap install odrive-unofficial
