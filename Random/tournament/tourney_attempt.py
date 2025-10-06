import pandas as pd
import uuid, random
from player import Player

def id_gen():
    i = uuid.uuid4().hex[:7].upper()
    return i


def mass_id_gen(dataframe):
    if not "ID" in dataframe.columns:
        print("Generating IDs...")
        dataframe["ID"] = [id_gen() for p in range(len(dataframe))]
        return dataframe
    else:
        print("IDs already exist")
        return dataframe

def update_csv(file,dataframe):
    dataframe.to_csv(file,index=False)

def get_data(file):
    return pd.read_csv(file)

def load_players(dataframe):
    players = [Player(first=row.first_name,last=row.last_name, dupr=row.rating, phone=row.phone, player_id=row.unique_id) for _, row in dataframe.iterrows()]

    return players

def create_bracket(players):
    random.shuffle(players)
    print(players)
    if len(players) % 2 !=0:
        print(f"{players[-1].full_name()} gets a bye this round")
        players = players[:-1]
    
    matchups = [(players[i], players[i+1]) for i in range(0, len(players), 2)]
    return matchups

def main():
    file = "C:/Users/CJ/Documents/GitHub/Scripts/Random/tournament/tourney_data.csv"
    data = get_data(file)

    # print(data)

    # data = mass_id_gen(data)
    # print(data)
    # update_csv(file=file,dataframe=data)
    # fn = data.iloc[:, [0,1]]

    # print(data['First Name'])
    
    players = load_players(data)

    matchups = create_bracket(players)
    for i, (p1, p2) in enumerate(matchups, start =1):
        print(f"Match {i}: {p1.full_name()} ({p1.record()}) vs {p2.full_name()} ({p2.record()})")
    

if __name__ == "__main__":
    main()