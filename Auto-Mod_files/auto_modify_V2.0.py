#!/usr/bin/python


def install_modules():
    if subprocess.call(['sudo','pip','install','re','pandas']):
        print('[+] Successfully installed modules!')

try:
    import os, subprocess, csv, pandas, re
except:
    print("[-] One of the required modules is not installed: pandas/re")
    
    install_modules()

from file_handling import FileHandler




# Variables

data_dict = {
    'Original_File' : [],
    'Is Directory' : 'Y or N',
    'New_File' : []
}


# list of things to remove example 'axxo'
remove_text_list = ['appletv','yify','-','\d\d\dp','1080','1080p','bluray','x264','sparks',
    '\s{2,}','ps3', 'publichd','dvdrip','axxo', 'xvid', 'tots','1337x','bdrip','ac3']

# remove later
remove_text_list.append('\.py')

# Use re module to compile the text in re_remove_list to produce
re_compiled = [re.compile(item_to_exclude, re.IGNORECASE) for item_to_exclude in remove_text_list]


# get the folder location to do the automatic name changes

original_file_count = 0
# Functions
def getfilepath(directory):
    if os.path.isdir(directory):

        dir = os.listdir(directory)
        # print(dir)
        return dir
    else:
        print(f"[-] The provide path '{directory}' does not exist")
        exit()

def add_orig_files_to_dict(directory):
    global original_file_count
    for f in directory:
        original_file_count +=1
        data_dict['Original_File'].append(f)

def remove_text(text_to_remove,original_string):
    return original_string.replace(text_to_remove,'')


def create_txt_file(directory_list):
    with open('directory_listing.txt','w') as f:
        for file in directory_list:
            f.writelines(f'{file}\n')




def main():
    abs_path = input("Please input absolute path: ")
    file_list = getfilepath(abs_path)
    
    add_orig_files_to_dict(file_list)
    print(f"[+] There are {original_file_count} files.")
    for file in file_list:
        pass
        # print(file)
        # for text_num in range(len(remove_text_list)):
        #     match = re.search(re_compiled[text_num], file)
        #     if match:
        #         print(re_compiled[text_num])
        #         # file = remove_text(re_compiled[text_num],file)
        #         print(f'found {file}')
    print(data_dict["Original_File"])


main()
# Whereever there are periods change to spaces except for the last period located in the file name

