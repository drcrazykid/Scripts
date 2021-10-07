#!/usr/bin/bash


# Script will be used to install and configure my common linux add-ins
# In order to run the user will have to have sudo permissions

# Programs to install

sudo apt update
sudo apt upgrade -y
sudo apt install terminator git zsh curl



cd ~/Documents
git clone https://www.github.com/drcrazykid/Scripts
$FOLDER=~/Documents/Scripts/

# zsh customization
bash $FOLDER/install_Ohmyzsh.sh

sudo echo '
if [ -d "$HOME/.bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi' >> /etc/zsh/zprofile

git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k

echo "# Added custom theme to ohmyzsh" >> ~/.zshrc
echo "ZSH_THEME=\"powerlevel9k/powerlevel9k\"" >> ~/.zshrc

#need to add zsh-autosuggestions and zsh-syntax-highlighting repos!!!!!

echo "plugins=(git zsh-autosuggestions zsh-syntax-highlighting)" >> ~/.zshrc

cp ./.zsh_aliases ~/.zsh_aliases

bash ./mod-vimrc.sh

mkdir ~/.bin
cp $FOLDER/weekly-update.py ~/.bin/weekly-update.py
cp $FOLDER/update-all

cd ~/Downloads
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb ~/Downloads/google.deb
