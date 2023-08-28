#!/usr/bin/python


# Goal of this script is to great my data of people
# Fields: First Name, Last name, Age, occupation, marital status, salary, kids (under 18), more to come
import pandas as pd
import numpy as np
from random import randint

data_points = 200
ages_numpy = np.random.randint(18,70,data_points)
ages_series = pd.Series(data=ages_numpy,name='Ages')



def create_marriage_data(size=200):
    marital_status_choices = ["S","M","D"]
    marital_status_data = []
    x = 0
    data = []
    while x < size:
        choice = randint(0,2)
        data.append(marital_status_choices[choice])
        x+=1

    return data    

m_data = create_marriage_data()
marital_status_series = pd.Series(data=m_data,name="Marital Status")

print(ages_series)
print(marital_status_series)