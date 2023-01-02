import os, re
class MyFile:
    def __init__(self,name):
        self.name = name
        self.badcharacterlist =[
            'appletv','yify','-','\d\d\dp',
            '1080','1080p','bluray','x264','sparks',
            '\s{2,}','ps3', 'publichd','dvdrip','axxo', 
            'xvid', 'tots','1337x','bdrip','ac3'

        ]
    
    def changeName(self,):
        self




class FileHandler:
    def __init__(self,directory = []):
        self.filelist = directory
        for file in self.filelist:
            pass


    def show_filelist(self):
        print(self.filelist)