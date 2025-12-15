import requests, re, json, os, pandas as pd
from dotenv import load_dotenv
# Script designed to migrate issues from one project to another.

# High-level migration flow
# 1. get the source issue
# 2. creat a new issue in the destination project
# 3. copy over:
#     labels
#     comments
#     close the original issues
load_dotenv()

TOKEN = os.getenv("GITLAB_TOKEN")
PROJ_ID = 77104649
HEADERS = {"PRIVATE-TOKEN": TOKEN}
GITLAB_URL = f"https://gitlab.com/api/v4/projects/{PROJ_ID}"
GITLAB_URL = f"https://gitlab.com/api/v4/projects/{PROJ_ID}/issues?scope=all"
# projects/{PROJ_ID}
# Issue url https://gitlab.com/drcrazykid_projects/sample_green_project/-/issues/1

# This is will be the actual URL GITLAB_URL = "https://code.levelup.cce.af.mil/api/v4"


response = requests.get(url=GITLAB_URL,headers=HEADERS)#,verify=False)
issues = response.json()
print(response.status_code)
if response.status_code == 200:
    for i in issues:
        print(f"ID: {i["id"]}")
        print(f"Title: {i["title"]}")
        print(f"Description: {i["description"]}")
        print(f"Labels: {i["labels"]}")

def sanitize_description(description: str) -> str:
    '''
    Remove any PII found in the description block of the issue such as cell and email
    '''
    if not description:
        return ""
    
    # find replace the email
    description = re.sub(r"^[\w\.-]+@[\w\.-]+\.\w+$","[Removed_email]", description, flags=re.MULTILINE)
    
    # find replace phone number
    description = re.sub(r"^\+?\d[\d\-\(\) ]{7,}\d$","[Removed_phone_number]",description, flags=re.MULTILINE)

def create_new_issue(dest_proj_id, title, description, labels=None, assignee_ids=None):
    url = f"https://gitlab.com/api/v4/projects/{dest_proj_id}/issues"

    payload = {
        "title": title,
        "description": description
    }   
    if labels:
        payload["labels"] = ",".join(labels)
    if assignee_ids:
        payload["assignee_ids"] = ",".join(assignee_ids)
    
    response = requests.post(url, headers=HEADERS, data=payload)
    response.raise_for_status()
    return response.json()

