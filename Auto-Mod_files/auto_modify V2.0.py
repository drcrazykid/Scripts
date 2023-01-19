#!/usr/bin/python
import os, csv, pandas, re
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


# Functions
def getfilepath(directory):
    if os.path.isdir(directory):

        dir = os.listdir(directory)
        return dir

def add_orig_files_to_dict(directory):
    for f in directory:
        data_dict['Original_File'].append(f)

def remove_text(text_to_remove,original_string):
    return original_string.replace(text_to_remove,'')


def create_txt_file(directory_list):
    with open('directory_listing.txt','w') as f:
        for file in directory_list:
            f.writelines(f'{file}\n')




def main():
    file_list = getfilepath(os.getcwd())
    add_orig_files_to_dict(file_list)
    
    for file in os.listdir():
        for text_num in range(len(remove_text_list)):
            match = re.search(re_compiled[text_num], file)
            if match:
                print(re_compiled[text_num])
                # file = remove_text(re_compiled[text_num],file)
                print(f'found {file}')
    


main()
# Whereever there are periods change to spaces except for the last period located in the file name

