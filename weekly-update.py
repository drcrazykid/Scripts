#!/usr/bin/python3
# Last updated: 14 Feb 2021
# Author: CJ

import os,sys,subprocess, platform, getpass
from subprocess import Popen, PIPE
from datetime import datetime as dt


def osCheck():
    # Function to determine the OS version running this script. Returns True if running on linux and will exit the script if
    # on Windows. 
    if platform.platform().__contains__('linux') or platform.platform().__contains__('Linux'):
        return True
    else:
        print("[-] The OS is Windows and the script is not designed for Windows OS.\nExiting...")
        sys.exit()



def moduleCheck(isLinux):
    if isLinux:
        try:
            import distro
        except:
            
            print("[+] Installing python3 'Distro' module...")
            subprocess.call(["python3", "-m", "pip", "install", "distro"])
            import distro
            currentDistro = distro.linux_distribution()[0].lower()

        finally:
            pass
            # print("[+] Installing python3 'Distro' module...")
            # subprocess.call(["python3", "pip", "-m", "pip", "install", "distro"])
            # currentDistro = distro.linux_distribution()[0].lower() 

        return currentDistro




class DistroVersion():
    def __init___(self, distro='debian'):
        
        self.distroList = ['debian', 'arch', 'centos', 'raspbian']
        
        for dis in self.distroList:

            if dis.__contains__(distro):
                self.distro = dis
                break

        # To hold the generated tuples list    
        self.tuple_list =[]

        # Following variables for holding the outputs and errors of running the commands
        self.outputList = []
        self.errList = []
    
    def piHoleCheck(self):
        num, result = subprocess.getstatusoutput('pihole')
        if num == 0:
            return True
        else:
            return False

    def generateTuples(self):
        
        if self.distro == 'debian' or 'raspbian':
            self.tuple_list.append(('sudo', 'apt', 'update'))
            self.tuple_list.append(('sudo','apt','upgrade','-y'))
            self.tuple_list.append(('sudo','apt','full-upgrade','-y'))

        elif self.distro == 'arch':
            self.tuple_list.append(('sudo', 'pacman', '-Syu','--noconfirm'))
        
        elif self.distro == 'centos':
            self.tuple_list.append(('sudo', 'dnf', 'upgrade','-y'))

        else:
            print("[-] Was unable to determine the distribution. Exiting...")
            print("[-] The determined distribution was: '" + self.distro + "'.")
            print("[-] You must modify the script in order for it to function.")
            print("[-] Exiting...")
            sys.exit()
        
        if self.piHoleCheck():
            self.tuple_list.append(('sudo','pihole','-up'))

    def runTuples(self):
        self.outputList = []
        self.errList = []

        for tup in self.tuple_list:
            proc = Popen(tup,stdin=PIPE, stout=PIPE, stderr=PIPE)
            output, err = proc.communicate()

            self.outputList.append({str(tup).replace("'","").replace(",",""):output.decode('utf-8')})
            self.errList.append(err)
            #transcripe main p#s 
            pass

    def createLogFile(self):
        # creates a log file
        
        # Gets user running the script
        user = getpass.getuser()
        # Path to where the log files will be saved
        log_path = "/home/" + user + "/Documents/update_logs"
        
        # Gets the current date and time for logging the data
        currentTime = dt.now()
        currentDate = dt.date(dt.now())
        
        try:
            os.chdir(log_path)

        except FileNotFoundError as e:
            os.mkdir(log_path)
            os.chdir(log_path)

        with open('Log: {}'.format(str(currentDate)),'w') as f:
            
            f.write('Conducted upgrade check on '+str(currentTime)+'\n')
            
            for output in self.outputList:
                for command, log in output.items():
                    f.write("Command run:", command + "\n")
                    f.write(log)

def old():

    currentTime = dt.now()
    currentDate = dt.date(dt.now())

    #thisDistro.runTuples()

    update_tuple = ('sudo', 'apt', 'update')
    upgrade_tuple = ('sudo','apt','upgrade','-y')
    fullUpgrade_tuple = ('sudo','apt','full-upgrade','-y')

    # For Updating pihole
    if piHoleCheck():
        piHole_tuple = ('sudo','pihole','-up')


    p1 = Popen(update_tuple,stdin=PIPE,stdout=PIPE,stderr=PIPE)
    output1, err1 = p1.communicate()

    p2 = Popen(upgrade_tuple,stdin=PIPE,stdout=PIPE,stderr=PIPE)
    output2, err2 = p2.communicate()

    p3 = Popen(fullUpgrade_tuple,stdin=PIPE,stdout=PIPE,stderr=PIPE)
    output3, err3 = p3.communicate()

    # For updating pihole
    if piHoleCheck():
        p4 = Popen(piHole_tuple,stdin=PIPE,stdout=PIPE,stderr=PIPE)
        output4, err4 = p4.communicate()

    user = getpass.getuser()
    log_path = "/home/" + user + "/Documents/update_logs"

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
        if piHoleCheck():
            f.write('\n\nPihole Upadte/Upgrade Output\n' + '='*50+'\n')
            f.write(output4.decode('utf-8'))

def main():


    osResult = osCheck()

    linux_distro = moduleCheck(osResult)



    thisDistro = DistroVersion(linux_distro)
    
    thisDistro.generateTuples()

    thisDistro.runTuples()

    thisDistro.createLogFile()
    

if __name__ == "__main__":
    main()

