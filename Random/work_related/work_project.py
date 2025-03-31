import pandas as pd 
import time, itertools, requests, json
from random import randint



# create csv with Last, First, Rank - only for test purposes
def create_csv():
    first = ["John", "Peter", "Suzy", "Becky","Rebecca","Samantha","Walter","Chad","Brian"]
    last = ["White","Brown", "Sanchez","Sandberg","Witherspoon","Jolie","Smithers"]
    rank = ["Amn","A1C","SrA","SSgt","TSgt","MSgt","2LT","1LT","Capt","Maj"]
    combined = [(f"{l}, {f}", {r}) for f,l,r in itertools.product(first,last, rank)]

    df = pd.DataFrame(combined, columns=["Name","Rank"])    
    df.to_csv("people.csv", index=False)

    print("[+] File created")

def list_of_users(filename):
    df = pd.read_csv(filename)
    users = df.to_dict(orient="records")
    print(users[1:10])

    return df
# git lab information

def fill_master_issue(username,default_body_text,labels):

    master_issue_data = {
        "title": f"{username} Master File",
        "description": f"{default_body_text}",
        "labels": f"{labels}",
        "assignee_id": None
    }
    return master_issue_data

def submit_issue(gitlab_url,header,proj_id,issue_data):
    url = f"{gitlab_url}/projects/{proj_id}/issues"

    response = requests.post(url,headers=header,data=issue_data)
    if response.status_code == 200:
        print(f"[+] Created issue for {issue_data['title']}")
    else:
        print(f"[-] Could not create issue for {issue_data['title']}")

# Run this to get the project ID use project name as a 'search'
def get_project_id(gitlab_url, header, project_name):
    
    response = requests.get(f"{gitlab_url}/projects",headers=header,params={"search":project_name})

    if response.status_code == 200:
        projects = response.json()
        print("Projects found:")
        # print(json.dumps(projects, indent=4))
        # df = pd.DataFrame(projects)
        # df.to_json("gitlab_projects.json",orient="records", indent=4)
        for p in projects[:5]:
            print(f"- {p['name']} (ID: {p['id']})")
        return projects
    else:
        print(f"Failed to fetch projects: {response.status_code}, {response.text}")


#task completed
# create_csv()
#

def main():
    GITLAB_URL = "https://gitlab.com/api/v4/"
    TOKEN = ""

    HEADERS = {"PRIVATE-TOKEN": TOKEN}
    default_body_text = "This is the default text that will go into the description. perhaps this could just be in a file by its self, if it is long."
    default_labels_string = "auto-created, masterfile"

    usersfile = "C:/User/CJ/Documents/GitHub/Scripts/Random/work_related/people.csv"
    list_of_users(usersfile)

    # proj_test = get_project_id(GITLAB_URL,HEADERS, "gitlab_restructure")
    PROJ_ID = 68482389




if __name__ == "__main__":
    main()