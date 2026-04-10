import requests, gitlab, os, json
from dotenv import load_dotenv



def preload():
    load_dotenv()
    TOKEN = os.getenv("GITLAB_TOKEN")
    HEADERS = {"PRIVATE-TOKEN": TOKEN}
    return TOKEN


def main():
    t = preload()

    gl = gitlab.Gitlab(url="https://code.levelup.cce.af.mil",private_token=t,ssl_verify=False)


    groups = gl.groups.list(all=True)

    ACCESS_LEVELS = {
    10: "Guest",
    20: "Reporter",
    30: "Developer",
    40: "Maintainer",
    50: "Owner"
}
    group_data = []

    for g in groups:
        # print(f"Group: {g.name} (ID: {g.id})")
        group_dict = {
            "name": g.name,
            "id": g.id,
            "members": []
        }
        try:
            members = g.members.list(all=True)
            for m in members:
                # print(f" - Member: {m.username} (Access Level: {m.access_level})")
                group_dict["members"].append({
                    "username": m.name,
                    "access_level": ACCESS_LEVELS.get(m.access_level, "Unknown")
                })
            group_data.append(group_dict)

            
        except gitlab.exceptions.GitlabGetError as e:
            if e.response_code == 403:
                print(f"Insufficient permissions to access members of group: {g.name} (ID: {g.id})")
                group_dict["members_accessible"] = False
            else:
                raise
        with open("group_membership_original.json", "a") as f:
            json.dump(group_data, f, indent=4, sort_keys=True)

if __name__ == "__main__":
    main()