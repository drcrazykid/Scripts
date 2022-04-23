#!/bin/bash

# This is a script to turn the Raspberry pi into a  Wireless Access Point. 

# The URL with the guide is located here: https://thepi.io/how-to-use-your-raspberry-pi-as-a-wireless-access-point/


sudo apt-get update && sudo apt-get upgrade -y

SEP="*********************************************************************************"
# Install the necessary applications 
echo "Installing hostapd and dnsmasq..."
sudo apt-get install hostapd -y
sudo apt-get install dnsmasq -y

# Stop services before modifying files
echo "Stopping 2 services: hostapd and dnsmasq..."
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq


# Configure a static IP for the wlan0 interface
echo "Configure a static IP for the wlan0 interface"
echo "Enter in the following command: sudo nano etc/dhcpd.conf"
echo "Add the following lines:"
echo "interface wlan0"
echo "static ip_address='CHOOSE IP_ADDRESS'"
echo "denyinterfaces eth0"
echo "denyinterfaces wlan0"
echo "$SEP"
# Configure the DHCP server (dnsmasq)
echo "Backup the current file"
echo "sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.bak"
echo "sudo nano /etc/dnsmasq.conf"
echo "interface=wlan0"
echo "  dhcp-range=ENTER_IP_STARTING,ENTER_IP_ENDING,SUBNET,LEASE_TIME ('24h')"
echo "$SEP"
# resume at step 5
echo "Configure the access point host software (hostapd)"
echo "sudo nano /etc/hostapd/hostapd.conf"
#resume step 5
