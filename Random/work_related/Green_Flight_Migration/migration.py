import requests, json, os, pandas as pd
from dotenv import load_dotenv
# Script designed to migrate issues from one project to another.

# High-level migration flow
# 1. get the source issue
# 2. creat a new issue in the destination project
# 3. copy over:
#     labels
#     comments
#     close the original issues

TOKEN = os.getenv("GITLAB_TOKEN")
PROJ_ID = #####
HEADERS = {"PRIVATE-TOKEN": TOKEN}
GITLAB_URL = "https://gitlab.com/drcrazykid_projects/sample_green_project/"


# Issue url https://gitlab.com/drcrazykid_projects/sample_green_project/-/issues/1

response = requests.get(f"https://gitlab.com/drcrazykid_projects/api/v4/issues?scope=all",headers={"PRIVATE-TOKEN:":TOKEN},verify=False)

if response == 200:
    issues = response.json()

for i in issues:
    print(i)
