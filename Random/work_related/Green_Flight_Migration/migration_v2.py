import gitlab, os, re
from dotenv import load_dotenv

# Reference: https://python-gitlab.readthedocs.io/en/stable/gl_objects
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

def preload():
    load_dotenv()
    TOKEN = os.getenv("GITLAB_TOKEN")
    HEADERS = {"PRIVATE-TOKEN": TOKEN}
    return TOKEN
def main():
    t = preload()

    gl = gitlab.Gitlab(url="https://code.levelup.cce.af.mil",private_token=t,ssl_verify=False)

    # issues = gl.issues.list(get_all=True)

    # i = gl.issues.list(get_all=False)[0]
    # pro = gl.projects.get(i.project_id, lazy=True)
    source_proj_id = 23035
    dest_proj_id = 42518

    source_proj = gl.projects.get(source_proj_id)
    dest_proj = gl.projects.get(dest_proj_id)

    src_proj_issues = source_proj.issues.list(state="opened",all=True)
    
    
    for i in src_proj_issues:
        new_i = dest_proj.issues.create({
            "title": i.title,
            # NEED TO SANITIZE DESCRIPTION!
            "description": sanitize_description(i.description),
            "labels": i.labels,
            "assignee_ids": [a["id"] for a in i.assignees] if i.assignees else None

        })
        print(i.title)

    print(f"Total issues is: {len(src_proj_issues)}") 

if __name__ == "__main__":
    main()

