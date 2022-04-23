#!/bin/bash
# Auto-mount External Drives

echo "Starting Auto-mount script"

# Get variables drive count(qty) drive UUID(s)
read -p "Please enter in how many drives you would like to auto-mount: " qty


while (( qty != 0 ))
 do

  # Does the user need to create a mounting point?
  read -p "Do you need to create a mounting point? (y/n)" create
  
  if [ $create = "y" ] ;
  then
   echo "You entered in '$create'"
   
   # Create Mount Points for Drive(s)
   read -p "Please input your mounting point: " mnt_pt
   echo "You entered: $mnt_pt"
   echo " "
   # sudo mkdir -p $mnt_pt
   echo "Created mounting point"
   
  else
   read -p "What is your absolute mounting point? " mnt_pt
  fi
  
  
  
  echo "Now will modify fstab." 
  echo "[!] Please be sure to double check the UUID"
  
  # Modify /etc/fstab file with UUID=ENTER_UUID    ENTER_TYPE    defaults, automount     0 0
 qty=$((qty-1))
 echo "$qty"  
 done
echo "Running command 'sudo mount -a' to verify installation before reboot"
sleep 4

