#!/usr/bin/python3

# Updating Debian Based Linux
import os,sys,subprocess
from subprocess import Popen, PIPE
from datetime import datetime as dt


# Add in support to handle different managers: apt, pacman, yum, dnf, etc.

currentTime = dt.now()
currentDate = dt.date(dt.now())
update_tuple = ('sudo', 'apt', 'update')
upgrade_tuple = ('sudo','apt','upgrade','-y')
fullUpgrade_tuple = ('sudo','apt','full-upgrade','-y')

# Add in conditional statement, read '/etc/*-release
# For Updating pihole
piHole_tuple = ('sudo','pihole','-up')


p1 = Popen(update_tuple,stdin=PIPE,stdout=PIPE,stderr=PIPE)
output1, err1 = p1.communicate()

p2 = Popen(upgrade_tuple,stdin=PIPE,stdout=PIPE,stderr=PIPE)
output2, err2 = p2.communicate()

p3 = Popen(fullUpgrade_tuple,stdin=PIPE,stdout=PIPE,stderr=PIPE)
output3, err3 = p3.communicate()

# For updating pihole
p4 = Popen(piHole_tuple,stdin=PIPE,stdout=PIPE,stderr=PIPE)
output4, err4 = p4.communicate()


log_path = '/home/pi/Documents/update_logs'

try:
    os.chdir(log_path)

except FileNotFoundError as e:
    os.mkdir(log_path)
    os.chdir(log_path)

with open('Log: {}'.format(str(currentDate)),'w') as f:
    f.write('Conducted update, upgrade and full-upgrade check on '+str(currentTime)+'\n')
    
    f.write('\n\nUpdate Output\n'+'='*50+'\n')
    f.write(output1.decode('utf-8'))
    
    f.write('\n\nUpgrade Output\n'+'='*50+'\n')
    f.write(output2.decode('utf-8'))
    
    f.write('\n\nFull-Upgrade Output\n'+'='*50+'\n')
    f.write(output3.decode('utf-8'))

    # For updating pihole
    f.write('\n\nPihole Upadte/Upgrade Output\n' + '='*50+'\n')
    f.write(output4.decode('utf-8'))