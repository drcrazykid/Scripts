import os, json, shutil


# Configuration
SCAN_DIR = "/home/drcrazykid/jellyfinHDD/AudioBooks"
BACKUP_DIR = "/home/drcrazykid/4tb/audiobook_library"
TRACK_FILE = "/home/drcrazykid/.tracked_file.json"

def load_tracked_files():
    # Loads the previously tracked files from the json file.
    if os.path.exists(TRACK_FILE):
        with open(TRACK_FILE,"r") as f:
            return set(json.load(f))
    return set()

def save_tracked_files(tracked_files):
    with open(TRACK_FILE, "w") as f:
        json.dump(list(tracked_files), f, indent=4)

def scan_directory(directory):
    items = set()
    for root, dirs, files in os.walk(directory):
        for name in dirs + files:
            items.add(os.path.relpath(os.path.join(root,name),directory))
    return items

def copy_new_items(new_items, source, destination):
    for item in new_items:
        src_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
        else:
            os.makedirs(os.path.dirname(dest_path),exist_ok=True)
            shutil.copy2(src_path, dest_path)

def main():
    tracked_files = load_tracked_files()

    current_files = scan_directory(SCAN_DIR)

    new_files = current_files - tracked_files

    if new_files:
        print(f"New items detected:")
        for file in new_files:
            print(f"{file}")

    else:
        print("No new files detected")

if __name__ == "__main__":
    main()