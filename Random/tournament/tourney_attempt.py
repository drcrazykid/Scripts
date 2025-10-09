import pandas as pd
import uuid, random
from typing import List, Tuple
from player import Player

def id_gen():
    i = uuid.uuid4().hex[:7].upper()
    return i

# function may no longer be needed, since player.__init__() creates ID
def mass_id_gen(df, file=None):
    # if csv doesn't have ID column will create column and generate IDs
    if not "unique_id" in df.columns:
        print("Generating IDs...")
        df["unique_id"] = [id_gen() for p in range(len(df))]
        
    else:
        # will check and generate IDs for missing players
        print(df)
        print(pd.notna(df))
        df["unique_id"] = df["unique_id"].apply(lambda x: id_gen() if pd.isna(x) else x)
        
        update_csv(file, df=df)
        print(df)
def update_csv(file,df):
    df.to_csv(file,index=False)

def get_data(file):
    return pd.read_csv(file)


def load_players(dataframe):
    mass_id_gen(df=dataframe)

    players = [Player(first=row.first_name,last=row.last_name, dupr=row.rating, phone=row.phone, player_id=row.unique_id) for _, row in dataframe.iterrows()]

    return players

def create_bracket(players):
    random.shuffle(players)
    # print(players)
    if len(players) % 2 !=0:
        print(f"{players[-1].full_name()} gets a bye this round")
        players = players[:-1]
    
    matchups = [(players[i], players[i+1]) for i in range(0, len(players), 2)]
    return matchups

def play_round(matchups: List[Tuple[Player, Player]]):
    winners = []
    losers = []
    for p1, p2 in matchups:
        # random choice for now
        winner = random.choice([p1,p2])
        loser = p1 if winner == p2 else p2
        
        print(f"{p1.full_name()} vs {p2.full_name()} -> Winner: {winner.full_name()}")
        
        # update players records
        winner.update_record(1)
        loser.update_record(-1)

        winners.append(winner)
        losers.append(loser)

    return winners, losers

def run_tournament(players:List[Player]):
    round_num = 1
    all_losers = []

    while len(players) > 1:
        print(f"--- Round {round_num} ---")

        matchups = create_bracket(players)

        winners, losers = play_round(matchups=matchups)
        all_losers.extend(losers)

        players = winners

        round_num += 1

def add_players() -> List[Player]:
    #     All player fields:
    # first_name
    # last_name
    # rating
    # phone
    # unique_id


    return

def main():
    def working():
        # main program loop
        title = "Riverstone Pickleball Tournament"
        while True:
            
            print("*"*15 + f" {title} " + "*"*15)
            
            load_in_file = input("Would you like to load in a (1) CSV or (2) type in player info?\n")
            if load_in_file == str(1):
                file = "C:/Users/CJ/Documents/GitHub/Scripts/Random/tournament/tourney_data.csv"
                data = get_data(file)
                players = load_players(data)
            else:
                add_players()
                first = input("Please input first name: ")
                last = input("Please input last name: ")
                r = float(input("Please input rating, if known: "))
    file = "C:/Users/CJ/Documents/GitHub/Scripts/Random/tournament/tourney_data.csv"
    data = get_data(file)
    players = load_players(data)
    mass_id_gen(data,file)
    # run_tournament(players=players)

if __name__ == "__main__":
    main()