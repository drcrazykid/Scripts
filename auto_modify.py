#!/usr/bin/python3.7
import os, re, argparse, getpass
#from modify_files import *

working_dir = ''
test_op = False
user = getpass.getuser()

def is_path(value):
    global working_dir
    if os.path.isdir(value):
        working_dir = args.directory
    else:
        print('[-] Please input valid directory.')
        exit()

def test_operations(v):
    global test_op
    if isinstance(v,bool):
        return v
    if v.lower() in ('y','true','t','1'):
        test_op = True
        return True
    else:
        test_op = False
        return False

# setup arguments
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--test', help='activate TEST mode', type=test_operations,nargs='?', const=False, default=False)
parser.add_argument('-d','--directory',help='directory to auto-correct files',type=is_path, required=False)
args = parser.parse_args()


if test_op == True:
    filename = '/home/'+user+'/Documents/sample_movie_list.txt'
    with open(filename,'r') as f:
        movie_list= f.readlines()
    print(movie_list)
else:
    os.chdir(working_dir)
    movie_list = sorted(os.listdir())
changed_list = []
year_search = re.compile('\d\d\d\d')

exclude_text = ['appletv','-','\d\d\dp','1080','1080p','bluray','x264','sparks','\s{2,}','publichd','dvdrip']
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
    
    for file in movie_list:
        
        remove_period(file)

        for text_to_exclude in range(len(exclude_text)):
            if re.search(re_compiled[text_to_exclude], file):
                # print(file)
                file = remove_text(re.search(re_compiled[text_to_exclude], file)[0], file)
                # print(file)
        file = file.replace(" .", ".")
        print(file)
        changed_list.append(file)

    print('Old File name \t\t\tNew File name')
    print('*'*50)
    for x in range(len(movie_list)):
        print(movie_list[x], '\t', changed_list[x])
        
if __name__ == "__main__":
    main()
