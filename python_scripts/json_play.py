import json
from random import randint

def create_id() -> str:
    return str(randint(10000000, 99999999))

def random_name() -> str:
    names = ["Peter", "susan","michele","taylor","michael","charlie","rebecca"]
    x = randint(0,len(names)-1)
    return names[x]

person = {
    "ID": "46111234",
    "name": "John",
    "height": 66,
    "weight": 185
}

x = 0
people = {}
while x < 100:
    id = create_id()
    name = random_name()
    
    h = randint(60,70)
    w = randint(150,200)
    person["ID"] = id
    person["name"] = name
    person["height"] = h
    person["weight"] = w
    new_person = person
    people[id] = new_person

    x += 1

print(json.dumps(people,indent=4))