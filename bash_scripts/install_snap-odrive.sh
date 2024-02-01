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

echo "You will need to logout or restart your computer before running the following command"
wait 3
echo "sudo snap install odrive-unofficial"
wait 5

# Install odrive-unofficial
#sudo snap install odrive-unofficial
