#!/usr/bin/python3
import os,sys,subprocess
from subprocess import Popen, PIPE
from datetime import datetime as dt

currentTime = dt.now()
currentDate = dt.date(dt.now())
update_tuple = ('sudo', 'apt', 'update')
upgrade_tuple = ('sudo','apt','upgrade','-y')
fullUpgrade_tuple = ('sudo','apt','full-upgrade','-y')
#subprocess.call(update_tuple)
#subprocess.call(upgrade_tuple)
#subprocess.call(fullUpgrade_tuple)

p1 = Popen(update_tuple,stdin=PIPE,stdout=PIPE,stderr=PIPE)
output1, err1 = p1.communicate()

p2 = Popen(upgrade_tuple,stdin=PIPE,stdout=PIPE,stderr=PIPE)
output2, err2 = p2.communicate()

p3 = Popen(fullUpgrade_tuple,stdin=PIPE,stdout=PIPE,stderr=PIPE)
output3, err3 = p3.communicate()

os.chdir('/home/pi/Documents/update_logs')
with open('Log: {}'.format(str(currentDate)),'w') as f:
    f.write('Conducted update, upgrade and full-upgrade check on '+str(currentTime)+'\n')
    f.write('\n\nUpdate Output\n'+'='*50+'\n')
    f.write(output1.decode('utf-8'))
    f.write('\n\nUpgrade Output\n'+'='*50+'\n')
    f.write(output2.decode('utf-8'))
    f.write('\n\nFull-Upgrade Output\n'+'='*50+'\n')
    f.write(output3.decode('utf-8'))