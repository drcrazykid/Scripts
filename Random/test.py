from turtle import Turtle
from random import random


def setup():

    pass

def main():
    t = Turtle()
    t.hideturtle()
    for i in range(100):
        steps = int(random() * 100)
        angle = int(random() *360)
        t.right(angle)
        t.fd(steps)

    
    t.screen.mainloop()

if __name__ == "__main__":
    main()