
# Retreive local SSID and Password from Windows Machine

import subprocess, re


# Runs windows command to gather all profiles saved on machine
command_output = subprocess.run(["netsh","wlan","show","profiles"], capture_output=True).stdout.decode()


profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

wifi_list = list()

wifi_past_dict = dict()


if profile_names != 0:
    for name in profile_names:
        #print("netsh","wlan","show","profile",name,"key=clear")
        second_command = subprocess.run(["netsh","wlan","show","profile",name,"key=clear"],capture_output=True).stdout.decode()
        
        password = (re.findall("Key Content            : (.*)\r",second_command))
        if len(password) == 0:
            pass
        else:
            wifi_past_dict[name] = password[0]

for x,y in wifi_past_dict.items():
    print(x+":",y)