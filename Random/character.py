import pandas

class Character():
    
    walk_amount = 5
    run_amount = walk_amount * 2

    energy = 100
    food = 100
    
    name = ""
    
    def __init__(self,name = ""):
        if name == "":
            name = self.pull_random_name()
        else:
            self.name = name

    def pull_random_name(self):
        data = pandas.read_csv('C:/Users/CJ/iCloudDrive/GitHub/Scripts/Random/names_list.csv')
        data_dict = data.to_dict()
        
        print(data_dict['year'].keys())
        #print(data_dict['name'])
        print(data_dict[1])

    def display(self):
        print(self.name,"\n",self.energy,"\n",self.food)

    def walk(self):
        print(self.name, "walked")
        self.minus_energy(self.walk_amount)
        
    def run(self):
        self.minus_energy(self.run_amount)

    def minus_energy(self,num=int):
        self.energy -= num
        self.display()
    
    def minus_food(self,num=int):
        self.food -= num
        self.display()

    def add_energy(self,num=int):
        self.energy += num
        self.display()
    
    def add_food(self,num=int):
        self.food += num
        self.display()

def main():
    test = Character()
    
if __name__ == "__main__":
    main()