from random import randint

global currentCost

currentCost = 10

def increaseCost():
    global currentCost
    
    currentCost = currentCost + 10
    

class Dice():
    def __init__(self,cost):
        self.cost = cost
        self.level = 1
        
        self.typeDict = {1 : 'Water', 2 : 'Fire', 3 : 'Earth', 4 : 'Ice', 5 : 'Wind', 6 : 'Ice'}
        self.type = self.typeDict[randint(1,6)]

        self.showDice()

    
    def increaseLevel(self):
        if self.level < 7:
            self.level = self.level + 1

    def showDice(self):
        # print("Name:",self.type,"\nLevel:",self.level,"\nCost:",self.cost)
        tempDice = self.__dict__
        tempDice.pop('typeDict')
        print(tempDice)
        


x = 0
dieDict = {}

for x in range(10):
    dieDict[x] = Dice(currentCost)

    increaseCost()
    #print(randint(1,7))
    x += 1


