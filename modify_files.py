#!/usr/bin/python3.7

import os, subprocess, sys, re, threading, platform
from argparse import ArgumentParser


# Global Variables
working_directory = ''
new_dir = ''
file_list = []
move_files_list = []
run_script = 1
user_safe_input = ["y","n","exit","quit"]
global_new_filename_list = []

def isPath(directory):
    if os.path.exists(directory):
        return directory
    else:
        return 
def setup():
    ''' First function to setup important variables for the remainder of the program. '''
    # Setup Parser
    parser = ArgumentParser()
    parser.add_argument('-d','--working-dir',dest='working_directory',help="enter in the directory to start with. Ex: ~/plex_server/Organize/Converted Movies")
    parser.add_argument('-n','--post-dir',dest='new_dir',help="direcotry to store file after modifying the file\nEx: ~/plex_server/Movies/")
    opt = parser.parse_args()
    
    # Changes scope of variables
    global working_directory, file_list, new_dir

    if len(sys.argv) <= 1:
        print("[-] You need to supply a working directory and destination directory to begin. Use '-h' for help.")
        continue_response = input("Continue anyway? (y or n)")
        if continue_response in user_safe_input:
            if continue_response == user_safe_input[0]:
                pass                
        else:
            sys.exit()
    else:
        working_directory = os.path.abspath(opt.working_directory)
        new_dir = os.path.abspath(opt.new_dir) + '/'
        Log.logger("[+] Working with the \'" + working_directory + "\' directory.")
        Log.logger("[+] Files will be placed in \'" + new_dir + "\' directory.")
        Log.logger("[+] Options:")
        for item in user_safe_input:
            Log.logger("\t[*] " + item)
    if new_dir == '':
        new_dir = working_directory
    
    file_list = sorted(os.listdir(working_directory))
    os.chdir(working_directory)

def findText(textToLookFor):
    ''' '''
    global file_list
    x=0
    searchList = []
    if textToLookFor == '':
        for item in file_list:
            if re.search('^\.',item):
                Log.logger("Removed: '"+ item +"'")
                file_list.remove(item)
        searchList = file_list
        Log.logger("There are " + str(len(searchList)) + " files in the current directory.")

    else:
        for item in file_list:
            if re.search('^\.',item):
                Log.logger("Removed: '"+ item +"'")
                file_list.remove(item)
            if re.search(textToLookFor,item,re.IGNORECASE):
                x+=1
                searchList.append(item)
    Log.logger("Found: "+ str(x) +" files matching your criteria.(" + str(len(file_list))+") files.")
    Log.logger("-------------------Matching List-------------------\n")
    
    if len(searchList) < 15:
        for item in searchList:
            Log.logger(item)
    else:
        for x in range(10):
            Log.logger(searchList[x])
        Log.logger(str(len(searchList) - 10) + ' item(s) also meet search criteria')
    return searchList

def modifyFile(files_list, textToremove):
    global global_new_filename_list
    # use os.path.splitext to separate name and file extension
    # filename_without_ext = os.path.splitext(filename)[0]
    # use os.rename to modify name
    for fileToModify in files_list:
        
        skip_it = prompt("Selected File: "+ fileToModify + "\nSkip it? (y/n) ")
        if skip_it == user_safe_input[0]:
            pass
        else:
            old_file_ext = os.path.splitext(working_directory + fileToModify)[1]
            new_filename = prompt("Change it to: ")
            confirmChange = prompt("'Is this correct '"+new_filename+"'? (y/n) ")
            if confirmChange == user_safe_input[0]:
                os.rename(fileToModify, new_filename + old_file_ext)
                Log.logger("Old: "+ str(fileToModify) + "\nNew: "+ new_filename + old_file_ext + '\n')
                move_files_list.append(working_directory + '/' + new_filename+old_file_ext)
                global_new_filename_list.append(new_filename + old_file_ext)
            else:
                new_filename = prompt("Change it to: ")
                confirmChange = prompt("'Is this correct '" + new_filename + "'? (y/n) ")
                if confirmChange == user_safe_input[0]:
                    os.rename(fileToModify, new_filename + old_file_ext)
                    Log.logger("Old: " + fileToModify + "\nNew: " + new_filename + old_file_ext + '\n')
                    move_files_list.append(working_directory + '/' + new_filename+old_file_ext)
                    global_new_filename_list.append(new_filename + old_file_ext)
                    
                else:
                    Log.logger("Moving on...")
            if prompt("Do you want to continue? ") == user_safe_input[1]:
                move_files(move_files_list)
                break

def prompt(message):
    global run_script

    user_response = input(message)
    if user_response == user_safe_input[2] or user_response == user_safe_input[3]:
        Log.logger('met quitting criteria')
        run_script = 0
        sys.exit()

    return user_response

def move_files(alist):
    
    temp_dict= {}
    x = 0
    for file in alist:
        temp_dict[x] = file
        x +=1
    Log.logger("Moving " + str(x) + " file(s) to '" + new_dir + "'")
   
    Log.logger("Sample")
    for filename_no in range(len(global_new_filename_list)):
        old_file = temp_dict[filename_no]
        Log.logger("Old location: " + temp_dict[filename_no])
        new_file = new_dir + global_new_filename_list[filename_no]
        Log.logger("New location: " + new_file)
        os.rename(old_file, new_file)
        Log.logger("Move Complete!")
            

def main():

    setup()

    while run_script == 1:

        textToLookFor = prompt("What are you looking for? ")
        search_files_list = findText(textToLookFor)

        modify_prompt = prompt("Do you want to modify the file(s)? (y or n)")
        if modify_prompt == user_safe_input[0]:
            modifyFile(search_files_list,textToLookFor)
        elif modify_prompt == user_safe_input[1]:
            pass
    
        elif modify_prompt == user_safe_input[2] or modify_prompt == user_safe_input[3]:
            Log.logger("You are exiting the script now. Goodbye!")
            run_script = 0

if __name__ == "__main__":
    main()