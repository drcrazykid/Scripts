#!/usr/bin/python3
# Last updated: 14 Feb 2021
# Author: CJ

import os,sys,subprocess, platform, getpass, time
from subprocess import Popen, PIPE
from datetime import datetime as dt


def osCheck():
    # Function to determine the OS version running this script. Returns True if running on linux and will exit the script if
    # on Windows. 
    if platform.platform().__contains__('linux') or platform.platform().__contains__('Linux'):
        print("[+] Running on Linux...")
        return True
    else:
        print("[-] The OS is Windows and the script is not designed for Windows OS.\nExiting...")
        sys.exit()



def moduleCheck(isLinux):
    if isLinux:
        try:
            import distro
        except:
            
            print("[-] Missing the necessary module. Install python3 'Distro' module...")
            sys.exit()    

        finally:
            print("[+] Python has the required modules...")
            currentDistro = distro.linux_distribution()[0].lower()
            print("[+] Script running on {}".format(currentDistro))
            # print("[+] Installing python3 'Distro' module...")
            # subprocess.call(["python3", "pip", "-m", "pip", "install", "distro"])
            # currentDistro = distro.linux_distribution()[0].lower() 

        return currentDistro




class DistroVersion:
    def __init__(self, selectedDistro):
        
        self.specificDistro = selectedDistro
        self.distroList = ['debian', 'arch', 'garuda', 'centos', 'raspbian']
        
        for dis in self.distroList:

            if selectedDistro.lower().__contains__(dis):
                self.specificDistro = dis
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
        
        if self.specificDistro == 'debian' or self.specificDistro == 'raspbian':
            self.tuple_list.append(('sudo', 'apt', 'update'))
            self.tuple_list.append(('sudo','apt','upgrade','-y'))
            self.tuple_list.append(('sudo','apt','full-upgrade','-y'))

        elif self.specificDistro == 'arch' or self.specificDistro == 'garuda':
            self.tuple_list.append(('sudo', 'pacman', '-Syu','--noconfirm'))
        
        elif self.specificDistro == 'centos':
            self.tuple_list.append(('sudo', 'dnf', 'upgrade','-y'))

        else:
            print("[-] Was unable to determine the distribution.")
            print("[-] The determined distribution was: '" + self.specificDistro + "'.")
            print("[-] You must modify the script in order for it to function.")
            print("[-] Exiting...")
            sys.exit()
        
        
        if self.piHoleCheck():
            self.tuple_list.append(('sudo','pihole','-up'))

        print("[+] Generating the necessary tuples...")
        for tup in self.tuple_list:
            print(str(tup).replace(",",""))

    def runTuples(self):
        self.outputList = []
        self.errList = []

        # There is an issue when the user needs to enter their password. may need to not "background" the subprocesses
        print("[+] Running the generated commands")
        for tup in self.tuple_list:
            proc = Popen(tup,stdin=PIPE, stdout=PIPE, stderr=PIPE)
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

        except FileNotFoundError:
            os.mkdir(log_path)
            os.chdir(log_path)

        try:
            with open('Log: {}'.format(str(currentDate)),'w') as f:
                
                f.write('Conducted upgrade check on '+str(currentTime)+'\n')
                
                for output in self.outputList:
                    for command, log in output.items():
                        f.write("Command run: "+
                        
                        command + "\n")
                        f.write(log)
        except:
            print("[-] Cannont generate log output")
            sys.exit()        



def main():
    osResult = osCheck()

    linux_distro = moduleCheck(osResult)


    thisDistro = DistroVersion(linux_distro)
    
    thisDistro.generateTuples()

    thisDistro.runTuples()

    thisDistro.createLogFile()
    

if __name__ == "__main__":
    main()

