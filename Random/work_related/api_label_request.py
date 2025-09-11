import requests, json, pandas as pd

# Script designed to simply query all known labels from a project

TOKEN = ""
PROJ_ID = 33855
HEADERS = {"PRIVATE-TOKEN": TOKEN}
GITLAB_URL = "https://code.levelup.cce.af.mil/api/v4"

# test = '''https://code.levelup.cce.af.mil/api/v4/projects/33855/labels?with_counts=true'''
# response = requests.get(test, headers=HEADERS,verify=False)


def get_labels(gitlab_url, header, proj_id):
    
    response = requests.get(f"{gitlab_url}/projects/{proj_id}/labels",headers=header,params={"with_counts":True},verify=False)

    if response.status_code == 200:
        labels = response.json()
        print(f"{len(labels)} Labels found:")
        # print(json.dumps(labels, indent=4))
        df = pd.DataFrame(labels)
        df.to_json("gitlab_projects.json",orient="records", indent=4)
        for l in labels[:5]:
            print(f"- {l['name']} (ID: {l['id']})")
        return labels
    else:
        print(f"Failed to fetch projects: {response.status_code}, {response.text}")


get_labels(gitlab_url=GITLAB_URL,header=HEADERS,proj_id=PROJ_ID)