from turtle import Turtle

FONT = ('Arial', 15, 'normal')


class Level(Turtle):

    def __init__(self):
        super().__init__()

        self.level = 1
        self.car_speed = 0.15
        self.penup()
        self.hideturtle()
        self.goto(-220, 220)
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.car_speed *= 0.9
        self.clear()
        self.update_level()

    def update_level(self):
        self.write(f"LEVEL: {self.level}", align='left', font=FONT)
