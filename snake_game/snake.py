from turtle import Turtle

COORDS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[len(self.snake) - 1]

    def create_snake(self):
        for coord in COORDS:
            self.add_body(coord)

    def move(self):
        for i in range((len(self.snake) - 1), 0, -1):
            x, y = self.snake[i - 1].xcor(), self.snake[i - 1].ycor()
            self.snake[i].goto(x, y)

        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_body(self, coord):
        body = Turtle(shape='square')
        body.color("white")
        body.penup()
        body.goto(coord)
        self.snake.append(body)

    def extend(self):
        coord = (self.tail.xcor(), self.tail.ycor())
        self.add_body(coord)
