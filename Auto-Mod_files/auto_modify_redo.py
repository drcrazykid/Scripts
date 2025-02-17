#!/usr/bin/python3

import os,re,json

#for test path: C:\Users\CJ\iCloudDrive\GitHub\Scripts-2\Auto-Mod_files

exclude_text = [
    r'\bAAC\b', r'\bappletv\b', r'\byify\b', r'-', r'\b\d{2,4}p\b', r'\b1080\b', r'\b1080p\b', 
    r'\bbluray\b', r'\bBRRip\b', r'\bx264\b', r'\bDTSJYK\b', r'\bsparks\b', r'\bps3\b', 
    r'\bpublichd\b', r'\[publichd\]', r'\bdvdrip\b', r'\baxxo\b', r'\bxvid\b', 
    r'\bExtraTorrentRG\b', r'\btots\b', r'\b1337x\b', r'\bbdrip\b', r'\bac3\b', r'\bKLAXXON\b'
]
print(os.path.abspath("."))
# with open("C:/Users/CJ/iCloudDrive/GitHub/Scripts-2/Auto-Mod_files/list_of_movies.txt","r") as f:
    # file_list = f.readlines()

re_compiled = [re.compile(text_to_exclude,re.IGNORECASE) for text_to_exclude in exclude_text]


# for every file in a directory grab the file, regex the exclude text
# then remove the 'text to remove'
def remove_text(text_to_remove,original_string) -> str:
    
    return original_string.replace(text_to_remove,"")


# change the periods to spaces except for the last one
def remove_periods(original_string) -> str:
    period_count = original_string.count(".")
    new_string = original_string.replace("."," ", period_count-1)
    new_string = new_string.replace(" .",".")
    return new_string

def sample_output(input_list):
    x = 0
    new_output = []
    for f in input_list:
        
        for r in range(len(exclude_text)):
            if re.search(re_compiled[r],f):
                # print(f)
                # print(re.search(re_compiled[r],f))
                f = remove_text(re.search(re_compiled[r],f)[0],f)

        f = remove_periods(f)
        f = " ".join(f.split())
        new_output.append(f)
    return new_output


def process_it_all(directory):
    dir_list = [os.listdir(directory)]
    file_dict = {}
       
    for x in range(len(dir_list)):
        file_dict[x]= {dir_list[x]:sample_output(dir_list)[x]}
    
    for k,v in file_dict.items():
        print(k,v)
    
    with open("movie_data.json","w") as json_file:
        json.dump(file_dict,json_file,indent=4)


def main():
    working_dir = input("Please provide the absolute directory to begin the process: ")
    print(os.listdir(working_dir))

    if os.path.isdir(working_dir):
        os.chdir(working_dir)
    for file in os.listdir(working_dir):
        if os.path.isfile(file):
            for r in range(len(exclude_text)):
                if re.search(re_compiled[r],file):
                    file = remove_text(re.search(re_compiled[r],file)[0],file)
        file = remove_periods(file)
        file = ' '.join(file.split())
        print(f"Changed to: {file}")

if __name__ == "__main__":
    main()