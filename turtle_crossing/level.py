from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()

        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-220, 220)
        self.write(f"LEVEL: {self.level}", align='left', font=('Arial', 15, 'normal'))
