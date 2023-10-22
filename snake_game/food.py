from random import randrange
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('yellow')
        self.speed('fastest')

        self.refresh()

    def refresh(self):
        x, y = randrange(-260, 260, 20), randrange(-260, 260, 20)
        self.goto(x, y)
