import enchant, itertools,os,sys
from threading import Thread


class MyThread (Thread):
    pass



d = enchant.Dict("en_US")

listOfLetters = []

def CreateFilename():
    temp = input("What is the name of this file (without the extension)? ")
    filename = temp + ".txt"
    print("Here is your filename:",filename)
    return filename

def CreateListOfLetters(theInput):
    letters = []
    for l in theInput:
        letters.append(l)
    return letters

def CheckForFile(theFilename):
    if (os.path.exists(theFilename)):
        theFilename = theFilename.replace(".","-01.")
        return theFilename
    else:
        return theFilename


def CreatePossibleWords(listOfLetters,filename):
    x = 2
    listOfWords = []
    while x < len(listOfLetters):
        print("Creating",x,"letter words")
        tempList = [''.join(comb) for comb in itertools.product(listOfLetters, repeat=x)]
        
        # Create a text file with all possible words
        for word in tempList:
            if d.check(word):
                with open(filename,'a+') as f:
                    f.writelines(word+"\n")

        listOfWords += tempList
        x +=1    
        
    return listOfWords

def ReadFromFile(filename):
    listOfWords = []
    with open(filename,'r') as f:
        listOfWords = f.readlines()
    x = 0
    while (x < len(listOfWords)):
        listOfWords[x] = listOfWords[x].replace('\n','')
        x +=1
    return listOfWords

def CheckIfValid(word):

    if(d.check(word)):
        print(word)

def CheckListForValid(wordList):
    count = 0
    for word in wordList:
        if(d.check(word)):
            count +=1
            print(word)
    print(count,"valid words")
#CreatePossibleWords(listOfLetters,"Test File.txt")

theInput = input("Please type the letters with no spaces: ")

filename = CreateFilename()

listOfLetters = CreateListOfLetters(theInput)

CreatePossibleWords(listOfLetters,filename)

possibleWords = ReadFromFile(filename)

print(possibleWords)
print("Complete")

