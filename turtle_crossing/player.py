from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.shape('turtle')
        self.color('white')
        self.setheading(90)
        self.reset_position()

    def reset_position(self):
        self.goto(0, -220)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)

    def move_left(self):
        x = self.xcor() - 10
        self.goto(x, self.ycor())

    def move_right(self):
        x = self.xcor() + 10
        self.goto(x, self.ycor())
