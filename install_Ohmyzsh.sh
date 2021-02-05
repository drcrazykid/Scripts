#!/bin/bash

sudo apt update && sudo apt install zsh

chsh -s /usr/bin/zsh $(whoami)
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
