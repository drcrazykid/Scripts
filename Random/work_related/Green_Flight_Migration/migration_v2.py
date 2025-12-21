import gitlab, os, re
from dotenv import load_dotenv



def main():
    load_dotenv()
    TOKEN = os.getenv("GITLAB_TOKEN")
    HEADERS = {"PRIVATE-TOKEN": TOKEN}
    

