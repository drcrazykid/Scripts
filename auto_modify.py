#!/usr/bin/python3.7

# Last Updated: 1 Sept 2021

import sys, os, re, argparse, getpass
#from modify_files import *

working_dir = ''
test_op = False
user = getpass.getuser()
movie_list = []

def is_path(value):
    global working_dir
    if os.path.isdir(value):
        working_dir = args.directory
    else:
        print('[-] Please input valid directory.')
        exit()


# need to add in a way for user to input sample file
def test_operations(v,):
    global test_op
    global movie_list
    test_op = True
    if os.path.isfile(v):
        try:
            filename = v #'/home/'+user+'/Documents/sample_movie_list.txt'
            with open(filename,'r') as f:
                movie_list= f.readlines()
                
                #print(movie_list)
            # Creating a temp list to remove the '\n' from the text file
            temp = []
            for movie in movie_list:
                temp.append(movie.replace('\n',''))
                movie.replace('.','',)
            movie_list = temp    
        except FileNotFoundError:
            print("[-] Sample file not found\nExiting...")
            sys.exit()
    else:
        print("[-] Sample file not found\nExiting...")
        sys.exit()
   

# setup arguments
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--test', help='activate TEST mode. give absolute path to sample file', type=test_operations,nargs='?', const=False, default=False)
parser.add_argument('-d','--directory',help='directory to auto-correct files',type=is_path, required=False)
args = parser.parse_args()


if test_op == False:
    os.chdir(working_dir)
    movie_list = sorted(os.listdir())

changed_list = []
# Unused
year_search = re.compile('\d\d\d\d')

exclude_text = ['appletv','yify','-','\d\d\dp','1080','1080p','bluray','x264','sparks','\s{2,}','ps3', 'publichd','dvdrip','axxo', 'xvid', 'tots','1337x','bdrip','ac3']
re_compiled = []

for item_to_exclude in exclude_text:
    re_compiled.append(re.compile(item_to_exclude, re.IGNORECASE))

def remove_text(text_to_remove,original_string):
    return original_string.replace(text_to_remove,'')

def remove_period(file):
    count_dot = file.count('.')
    file = file.replace('.', ' ', count_dot - 1)
    return file

def main():
    
    for movie_file in movie_list:
        
        file = remove_period(movie_file)

        for text_to_exclude in range(len(exclude_text)):
            if re.search(re_compiled[text_to_exclude], file):

                file = remove_text(re.search(re_compiled[text_to_exclude], file)[0], file)

        file = file.replace(" .", ".")

        movie_file = file
        
        changed_list.append(file)

    print('Old File name \t\t\tNew File name')
    print('*'*100)
    for x in range(len(movie_list)):
        #print(movie_list[x],'\t\t', changed_list[x])
        print(f"{movie_list[x]}{changed_list[x]:>8}")

if __name__ == "__main__":
    main()
