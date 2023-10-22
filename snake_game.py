import turtle as t

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("SNEK")

coords = [(0, 0), (-20, 0), (-40, 0),]
snake = []

for coord in coords:
    body = t.Turtle(shape='square')
    body.color("white")
    body.penup()
    body.goto(coord)
    snake.append(body)

screen.exitonclick()
