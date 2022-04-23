#!/usr/bin/python3

from multiprocessing.spawn import old_main_modules
import os, sys, subprocess, apt, getpass


# Installation of terminator
cache = apt.Cache()

cache.open()
if(cache["terminator"]):
    print("[+] Terminator is installed.")
else:
    subprocess.call(["sudo","apt","install","terminator","-y"])


# Kill any open Terminator processes... Just in case
subprocess.call(["killall","-9","terminator",">/dev/null", "2>&1"])

terminator_config_path = "/home/{}/.config/terminator/".format(getpass.getuser())
new_config = "/home/{}/.config/terminator/config".format(getpass.getuser())

created_config = False

if(os.path.isdir(terminator_config_path)):
    print("[+] File Path exists!")

else:

    print("[-] File path does not exist (%s)"%terminator_config_path)
    
    # Create the directory...
    #subprocess.call(["mkdir",terminator_config_path])  <---- not working for some reason!
    os.mkdir(terminator_config_path)

    
    # Create the empty config file
    subprocess.call(["touch", "/home/{}/.config/terminator/config".format(getpass.getuser())])

    print("[+] Created file path and file")
    created_config = True


t_configs = '''[global_config]
  title_transmit_bg_color = "#204a87"
  title_inactive_bg_color = "#729fcf"
  suppress_multiple_term_dialog = True
  title_use_system_font = False
  title_font = Sans 12
[keybindings]
[profiles]
  [[default]]
    background_darkness = 0.76
    background_type = transparent
    cursor_color = "#aaaaaa"
    font = Monospace 12
    use_system_font = False
[layouts]
  [[default]]
    [[[window0]]]
      type = Window
      parent = ""
    [[[child1]]]
      type = Terminal
      parent = window0
[plugins]'''

def write_configs():
    try:
        with open(new_config,"w") as f:
            f.write(t_configs)
    except:
        print("[-] Unable to write ne configs.")
    else:
        print("[+] Successfully wrote new configs!")

if (created_config):

    write_configs()
    
else:

    try:
        with open(terminator_config_path+"config",'r+') as f:
            # Will read old config
            old_config = f.read()
            print(old_config)
            
        #prompts user to replace old configs
        response = input("Would you like to replace the configs? (y/n)\n")
            
        if response == "y":
            write_configs()

            write_configs()
        else:
            print("[*] Exiting...")
            sys.exit()

    except FileNotFoundError:
        print("[-] The terminator file was not found.")
    else:
        print("[+] Successfully ran script. Good-bye!")
