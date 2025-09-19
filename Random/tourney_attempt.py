import pandas as pd


data = pd.read_csv("C:/Users/CJ/Documents/GitHub/Scripts/Random/tourney_data.csv")

print(data)

fn = data.iloc[:, [0,1]]

print(data['First Name'])