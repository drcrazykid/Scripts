#!/bin/bash

# Adds Balena Etcher's Repo to apt
echo "deb https://deb.etcher.io stable etcher" | sudo tee /etc/apt/sources.list.d/balena-etcher.list

# Imports the key
sudo apt-key adv --keyserver hkps://keyserver.ubuntu.com:443 --recv-keys 379CE192D401AB61


# Updates and Installs
sudo apt update && sudo apt install balena-etcher-electron
