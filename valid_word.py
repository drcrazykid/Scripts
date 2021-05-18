import enchant, itertools,os,sys
from threading import Thread


class MyThread (Thread):
    pass


class MyProgram():
    def __init__(self):
        self.d = enchant.Dict("en_US")

        self.listOfLetters = []

    def CreateFilename(self):
        temp = input("What is the name of this file (without the extension)? ")
        filename = temp + ".txt"
        print("Here is your filename:",filename)
        return filename

    def CreateListOfLetters(self, theInput):
        letters = []
        for l in theInput:
            letters.append(l)
        return letters

    def CheckForFile(self, theFilename):
        if (os.path.exists(theFilename)):
            theFilename = theFilename.replace(".","-01.")
            return theFilename
        else:
            return theFilename


    def CreatePossibleWords(self, listOfLetters,filename):
        x = 2
        listOfWords = []
        while x < len(listOfLetters):
            print("Creating",x,"letter words")
            tempList = [''.join(comb) for comb in itertools.product(listOfLetters, repeat=x)]
            
            # Create a text file with all possible words
            for word in tempList:
                if self.d.check(word):
                    with open(filename,'a+') as f:
                        f.writelines(word+"\n")

            listOfWords += tempList
            x +=1    
            
        return listOfWords

    def ReadFromFile(self, filename):
        listOfWords = []
        with open(filename,'r') as f:
            listOfWords = f.readlines()
        x = 0
        while (x < len(listOfWords)):
            listOfWords[x] = listOfWords[x].replace('\n','')
            x +=1
        return listOfWords

    def CheckIfValid(self, word):

        if(self.d.check(word)):
            print(word)

    def CheckListForValid(self, wordList):
        count = 0
        for word in wordList:
            if(self.d.check(word)):
                count +=1
                print(word)
        print(count,"valid words")
#CreatePossibleWords(listOfLetters,"Test File.txt")

theInput = input("Please type the letters with no spaces: ")
prog = MyProgram()

filename = prog.CreateFilename()

listOfLetters = prog.CreateListOfLetters(theInput)

prog.CreatePossibleWords(listOfLetters,filename)

possibleWords = prog.ReadFromFile(filename)

print(possibleWords)
print("Complete")

