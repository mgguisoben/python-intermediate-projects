from turtle import Turtle

FONT = ('Arial', 50, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.p1_score = 0
        self.p2_score = 0

        self.penup()
        self.hideturtle()
        self.goto(0, 220)
        self.update_scoreboard()

    def p1_miss(self):
        self.p2_score += 1
        self.clear()
        self.update_scoreboard()

    def p2_miss(self):
        self.p1_score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.p1_score}\t{self.p2_score}", align='center', font=FONT)
