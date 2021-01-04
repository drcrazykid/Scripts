#!/usr/bin/python3

import os,subprocess,sys
from argparse import ArgumentParser as AP

# Setup Parser
#parser = ArgumentParser()
#parser.add_argument('-A','--allfonts',dest='working_directory',help="install ClearType fonts and TrueType fonts")
#parser.add_argument('-n','--post-dir',dest='new_dir',help="direcotry to store file after modifying the file\nEx: ~/plex_server/Movies/")
#opt = parser.parse_args()



os.system('sudo apt install ttf-mscorefonts-installer')

os.system('mkdir ~/.fonts')
os.system('wget -qO- http://plasmasturm.org/code/vistafonts-installer/vistafonts-installer | bash')


os.system('echo "Complete"')