import os, re
class MyFile:
    def __init__(self,absolute_filename):
        self.name = absolute_filename
        
    
    def show_filename(self):
        print(self.name)
    def changeName(self,):
        self




class FileHandler:
    def __init__(self,directory = []):
        
        '''Input the absolute directory path you want to modify'''
        self.filelist = directory
        self.badcharacterlist =[
            'appletv','yify','-','\d\d\dp',
            '1080','1080p','bluray','x264','sparks',
            '\s{2,}','ps3', 'publichd','dvdrip','axxo', 
            'xvid', 'tots','1337x','bdrip','ac3'
        ]

        self.file_objects = []
        for file in self.filelist:
            file_obj = MyFile(file)
            self.file_objects.append(file_obj)


    def show_filelist(self):
        print(self.filelist)
    
    def show_file_objects(self):
        for f_obj in self.file_objects:
            print(f_obj.show_filename())