#!/usr/bin/python
import os, os.path, platform
import datetime as dt
from tkinter import *

# Global Variables
LOG_BUFFER_STRINGS:list
if platform.system().contain
def get_dateandtime():
    
    now = dt.datetime.now()

    return now
def display_msg(msg:str,isGood=bool):
    if isGood == True:
        print(f"[+] {msg}")
    else:
        print(f"[-] {msg}")

def create_folder(folder_name:str):
    os.mkdir(path=folder_name)

def add_toLogBuffer(log_entry:str):
    global LOG_BUFFER_STRINGS

    LOG_BUFFER_STRINGS.append(log_entry)

    return LOG_BUFFER_STRINGS

def write_log(logFilePath:str):
    global LOG_BUFFER_STRINGS
    try:
        os.chdir(logFilePath)
    except FileNotFoundError:
        os.mkdir(logFilePath)
        os.chdir(logFilePath)
    finally:
        filename = f"Log: {dt.date(dt.now())}.log"

        if len(LOG_BUFFER_STRINGS) > 1:
            with open(filename,'w') as f:
                f.writelines(LOG_BUFFER_STRINGS)

def get_filepath_to_organize():
    pathToOrganzie = input("What is the absolute filepath you would like to use for the script? ")
    if os.path.exists(pathToOrganzie):
        os.chdir(pathToOrganzie)
        return pathToOrganzie
    else:
        display_msg("Using Downloads Folder")
