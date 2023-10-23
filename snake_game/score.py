from turtle import Turtle

with open('highscore.txt', 'r') as hs:
    high_score = hs.read()

ALIGNMENT = 'center'
FONT = ('Arial', 18, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}\tHigh Score: {high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
        if self.score > int(high_score):
            current_highscore = str(self.score)

            with open('highscore.txt', 'w') as hs:
                hs.write(current_highscore)
