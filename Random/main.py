from character import Character
try:
     from pynput.keyboard import Key, Listener

except:
      print("Not running on pi")    


def on_press(key):
        print('{0} pressed'.format(key))

def on_release(key):
        if key == Key.esc:
            return False

def main():
    test = Character()

    # with Listener(on_press=on_press, on_release=on_release) as listener:
    #     listener.join()

if __name__ == "__main__":
    main()