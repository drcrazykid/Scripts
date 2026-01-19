import requests, re, gitlab, json, os, pandas as pd
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
PROJ_ID = 23035
DEST_PROJ_ID = 42518
HEADERS = {"PRIVATE-TOKEN": TOKEN}
GITLAB_URL = f"https://gitlab.com/api/v4/projects/{PROJ_ID}"
GITLAB_URL = f"https://gitlab.com/api/v4/projects/{PROJ_ID}/issues?scope=all"
# projects/{PROJ_ID}
# Issue url https://gitlab.com/drcrazykid_projects/sample_green_project/-/issues/1

# This is will be the actual URL GITLAB_URL = "https://code.levelup.cce.af.mil/api/v4"
source_gitlab = f"https://code.levelup.cce.af.mil/api/v4/projects/{PROJ_ID}/issues?scope=all"

# response = requests.get(url=source_gitlab,headers=HEADERS,verify=False)
# issues = response.json()
# print(response.status_code)
# if response.status_code == 200:
#     for i in issues:
#         print(f"ID: {i["id"]}")
#         print(f"Title: {i["title"]}")
#         # print(f"Description: {i["description"]}")
#         print(f"Labels: {i["labels"]}")

def sanitize_description(description: str, show_all=False) -> str:
    '''
    Remove any PII found in the description block of the issue such as cell and email
    '''
    if not description:
        return ""
    original_description = description
    
    # find replace phone number
    phone_re = re.compile(r"^.*\b(?=(?:.*\d){7,})\+?[\d\s\-\(\)]+\b.*$")

    # find replace the email
    email_re = re.compile( r"^.*\b[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}\b.*$")
    sanitized_lines = []

    for line in description.splitlines():
        if email_re.search(line):
            sanitized_lines.append("[REDACTED_EMAIL]")
        elif phone_re.search(line):
            sanitized_lines.append("[REDACTED_PHONE]")
        else:
            sanitized_lines.append(line)

    sanitized_description = "\n".join(sanitized_lines)        
    
    if show_all:
        print(f"Original Description:\n{original_description}\n\nNew Description: \n{sanitized_description}")

    return sanitized_description
    
def create_new_issue(dest_proj_id, title, description, labels=None, assignee_ids=None):
    url = f"https://code.levelup.cce.af.mil/api/v4/projects/{dest_proj_id}/issues"

    payload = {
        "title": title,
        "description": description
    }   
    if labels:
        payload["labels"] = ",".join(labels)
    if assignee_ids:
        payload["assignee_ids"] = ",".join(assignee_ids)
    
    response = requests.post(url, headers=HEADERS, data=payload,verify=False)
    response.raise_for_status()
    return response.json()

# for i in issues:
#     san_desc = sanitize_description(description=i["description"],show_all=True)
#     labels = i.get("labels",[])
#     assignees = [a["id"] for a in i.get("assignees",[])] if i.get("assignees") else None

#     new_issue = create_new_issue(
#         dest_proj_id=DEST_PROJ_ID,
#         title=i["title"],
#         description=san_desc,
#         labels=labels,
#         assignee_ids=assignees)

#     print(f"Migrated: {i['title']}")

response = requests.get(url=source_gitlab,headers=HEADERS,verify=False)

if response.status_code == 200:
    issues = response.json()
    for i in issues:
        print(i["title"])
        print(i["labels"])