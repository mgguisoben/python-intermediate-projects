import turtle as t
from random import choice
# import colorgram

# extract colors from image into an RGB tuple
# colors = colorgram.extract('image.jpg', 25)
# color_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

COLORS = [(31, 102, 156), (149, 23, 55), (224, 158, 51), (165, 64, 109), (217, 212, 49), (170, 72, 47),
          (234, 206, 216), (42, 104, 61), (204, 223, 229), (205, 137, 175), (95, 170, 115), (55, 37, 44),
          (39, 54, 121), (34, 36, 72), (22, 68, 58), (231, 188, 21), (56, 80, 48), (233, 241, 237), (210, 100, 48),
          (244, 218, 7), (162, 100, 154), (47, 149, 185), (128, 160, 186), (216, 177, 190)]

scrn_size = 500
dot_gap = 50
dot_size = 15

INITIAL_GOTO = int((scrn_size / 2) - 50)
DOTS = int((scrn_size - 100) / dot_gap)

turtle = t.Turtle()
turtle.penup()
screen = t.Screen()
screen.setup(scrn_size, scrn_size, )
screen.colormode(255)
# screen.bgcolor('black')

turtle.goto(INITIAL_GOTO, -INITIAL_GOTO)

for _ in range(DOTS + 1):
    turtle.left(180)

    for _ in range(DOTS):
        dot_color = choice(COLORS)
        turtle.dot(dot_size, dot_color)
        turtle.forward(dot_gap)
        turtle.dot(dot_size, dot_color)

    turtle.right(90)
    turtle.forward(dot_gap)
    turtle.right(90)
    turtle.forward(scrn_size - 100)


turtle.hideturtle()

t.mainloop()
