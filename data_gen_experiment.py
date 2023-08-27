#!/usr/bin/python


# Goal of this script is to great my data of people
# Fields: First Name, Last name, Age, occupation, marital status, salary, kids (under 18), more to come
import pandas as pd
import numpy as np


ages_numpy = np.random.randint(18,70,200)
ages_series = pd.Series(data=ages_numpy,name='Ages')


print(ages_series)
