#!/usr/bin/bash


# Script will be used to install and configure my common linux add-ins
# In order to run the user will have to have sudo permissions

# Programs to install

sudo apt update
sudo apt upgrade -y
sudo apt install terminator git zsh



cd ~/Documents
git clone https://www.github.com/drcrazykid/Scripts
cd Scripts

# zsh customization
bash ./install_Ohmyzsh.sh
sudo echo '
if [ -d "$HOME/.bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi' >> /etc/zsh/zprofile


cp ./.zsh_aliases ~/.zsh_aliases

bash ./mod-vimrc.sh

mkdir ~/.bin
cp ./weekly-update.py ~/.bin/weekly-update.py
cp ./update-all

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
