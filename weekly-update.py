#!/usr/bin/python3

# 
# Updating Debian Based Linux
import os,sys,subprocess, platform, getpass
from subprocess import Popen, PIPE
from datetime import datetime as dt


def osCheck():
    if platform.platform().__contains__('linux'):
        return True
    else:
        print("Script not designed for Windows OS.\nExiting...")
        sys.exit()



def moduleCheck(isLinux):
    if isLinux:
        try:
            import distro
        except ModuleNotFoundError:
            
            subprocess.call(["python3", "pip", "-m", "pip", "install", "distro"])
            currentDistro = distro.linux_distribution()[0]
        finally:
            subprocess.call(["python3", "pip", "-m", "pip", "install", "distro"])
            currentDistro = distro.linux_distribution()[0].lower() 

        return currentDistro

def piHoleCheck():

    num, result = subprocess.getstatusoutput('pihole')
    if num == 0:
        return True
    else:
        return False



class DistroVersion():
    def __init___(self, distro='debian'):
        
        self.distroList = ['debian', 'arch', 'centos', 'raspbian']
        
        for dis in self.distroList:

            if dis.__contains__(distro):
                self.distro = dis
                break
            
        self.tuple_list =[]
    
    def generateTuples(self):
        
        if self.distro == 'debian' or 'raspbian':
            self.tuple_list.append(('sudo', 'apt', 'update'))
            self.tuple_list.append(('sudo','apt','upgrade','-y'))
            self.tuple_list.append(('sudo','apt','full-upgrade','-y'))

        
        elif self.distro == 'arch':
            self.tuple_list.append(('sudo', 'pacman', '-Syu'))
        
        elif self.distro == 'centos':
            self.tuple_list.append(('sudo', 'dnf', 'upgrade'))

        
        else:
            print("Was unable to determing the distribution. Exiting...")
            sys.exit()

    def runTuples(self):

        

        #conditional if debian run three tuples
        #conditional if arch run one tuple
        #if redhat-based run # tuples
        # or
        for tup in self.tuple_list:
            #transcripe main p#s 
            pass
        pass

# Add in support to handle different managers: apt, pacman, yum, dnf, etc.

def main():

    osResult = osCheck()

    linux_distro = moduleCheck(osResult)

    # print(piHoleCheck)

    thisDistro = DistroVersion(linux_distro)
    
    thisDistro.generateTuples()
    
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

if __name__ == "__main__":
    main()

