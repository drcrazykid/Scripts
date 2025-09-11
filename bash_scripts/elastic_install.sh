#!/usr/bin/bash

sudo apt update

sudo apt install apt-transport-https openjdk-11-jdk -y

java -version

export JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"

wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list

sudo apt-get update

sudo apt-get install elasticsearch

sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch

sudo systemctl status elasticsearch