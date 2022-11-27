
class Character():
    
    walk_amount = 5
    run_amount = walk_amount * 2

    energy = 100
    food = 100
    
    name = ""

    def __init__(self,name):
        self.name = name

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

