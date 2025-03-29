import pandas as pd 
import time, itertools, requests, json
from random import randint



# create csv with Last, First, Rank
def create_csv():
    first = ["John", "Peter", "Suzy", "Becky","Rebecca","Samantha","Walter","Chad","Brian"]
    last = ["White","Brown", "Sanchez","Sandberg","Witherspoon","Jolie","Smithers"]
    rank = ["Amn","A1C","SrA","SSgt","TSgt","MSgt","2LT","1LT","Capt","Maj"]
    combined = [(f"{l}, {f}", {r}) for f,l,r in itertools.product(first,last, rank)]

    df = pd.DataFrame(combined, columns=["Name","Rank"])    
    df.to_csv("people.csv", index=False)

    print("[+] File created")

# git lab information
gitlab_url = "https://gitlab.com/api/v4/projects"
token = ""

# get project ID
def get_project_id(project_name) -> int:
    headers = {"PRIVATE-TOKEN": token}

    response = requests.get(gitlab_url,headers=headers,params={"search":project_name})

    if response.status_code == 200:
        projects = response.json()
        print("Projects found:")
        # print(json.dumps(projects, indent=4))
        # df = pd.DataFrame(projects)
        # df.to_json("gitlab_projects.json",orient="records", indent=4)
        print(projects[0])
    else:
        print(f"Failed to fetch projects: {response.status_code}, {response.text}")


#task completed
# create_csv()

get_project_id("restructure")