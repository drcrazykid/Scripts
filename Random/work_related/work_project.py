import pandas as pd 
import time, itertools, requests, json, sys
from random import randint
import certifi


# create csv with Last, First, Rank - only for test purposes
def create_csv():
    first = ["John", "Peter", "Suzy", "Becky","Rebecca","Samantha","Walter","Chad","Brian"]
    last = ["White","Brown", "Sanchez","Sandberg","Witherspoon","Jolie","Smithers"]
    rank = ["Amn","A1C","SrA","SSgt","TSgt","MSgt","2LT","1LT","Capt","Maj"]
    combined = [(f"{l}, {f}", r) for f,l,r in itertools.product(first, last, rank)]

    df = pd.DataFrame(combined, columns=["Name","Rank"])    
    df.to_csv("people.csv", index=False)

    print("[+] File created")

def list_of_users(filename):
    df = pd.read_csv(filename)
    users = df.to_dict(orient="records")
    complete_list = []
    for u in users:
        complete_list.append(f"{u['Rank']} {u['Name']}")
    print(complete_list[:10])
    
    return complete_list
# git lab information

def fill_master_issue(username,default_body_text,labels):

    master_issue_data = {
        "title": f"{username} Master File",
        "description": f"{default_body_text}",
        "labels": f"{labels}",
        "assignee_id": None,
        "confidential": True
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
def get_project_id(gitlab_url, header, project_name=""):
    ca_cert_path = "C:/Users/CJ/Documents/GitHub/Scripts/Random/work_related/wildcard2-com-h2.cce.af.mil.crt"
    # response = requests.get(f"{gitlab_url}/projects",headers=header,verify=False)
    response = requests.get(f"{gitlab_url}/projects",headers=header,params={"search":project_name},verify=ca_cert_path)

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
    # GITLAB_URL = "https://gitlab.com/api/v4/"
    GITLAB_URL = "https://code.levelup.cce.af.mil/api/v4/"
    TOKEN = ""

    HEADERS = {"PRIVATE-TOKEN": TOKEN}
    
    # PROJ_ID = 68482389
    PROJ_ID = 0

    if TOKEN == "":
        print("[-] Token is incorrect. Exiting...")
        sys.exit()

    default_body_text = '''This is the template file for the acocunts. (Include logs, screenshots, or any relevant details.)'''
    default_labels_string = "auto-created, masterfile"


    usersfile = "C:/Users/CJ/Documents/GitHub/Scripts/Random/work_related/people.csv"
    users = list_of_users(usersfile)
    x = 0

    while x < len(users):
        # issue_data = fill_master_issue(users[x],default_body_text,default_labels_string)
        
        # submit_issue(GITLAB_URL,HEADERS,PROJ_ID,issue_data)

        # time.sleep(1)
        x += 1
    proj_test = get_project_id(GITLAB_URL,HEADERS, "gitlab_restructure")
    




if __name__ == "__main__":
    main()