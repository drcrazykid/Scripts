import pandas as pd
import uuid

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
    print("Saved CSV")
    return pd.read_csv(file)


def main():
    file = "C:/Users/CJ/Documents/GitHub/Scripts/Random/tournament/tourney_data.csv"
    data = get_data(file)

    print(data)

    data = mass_id_gen(data)
    print(data)
    update_csv(file=file,dataframe=data)
    # fn = data.iloc[:, [0,1]]

    # print(data['First Name'])


if __name__ == "__main__":
    main()