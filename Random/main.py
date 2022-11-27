from pynput.keyboard import Key, Listener
from character import Character

def on_press(key):
        print('{0} pressed'.format(key))

def on_release(key):
        if key == Key.esc:
            return False

def main():
    

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()