import turtle as t
from random import randint

screen = t.Screen()
screen.setup(width=500, height=400)

user_choice = screen.textinput("Make a bet", "Who will win the race? Choose a color.")

color_list = ['red', 'blue', 'yellow', 'green', 'orange', 'violet']
y_coords = [25, -25, 75, -75, 125, -125]
turtle_list = []
winner = ''

for x in range(6):
    turtle = t.Turtle()
    turtle.penup()
    turtle.shape('turtle')
    turtle.color(color_list[x])
    turtle.goto(-230, y_coords[x])
    turtle_list.append(turtle)

race_on = True
while race_on:

    for turt in turtle_list:

        if turt.xcor() > 230:
            winner = turt.pencolor()
            race_on = False

        move_dist = randint(0, 10)
        turt.forward(move_dist)

if user_choice == winner:
    print("Your turtle won!")
else:
    print(f"The winner is {winner}. You lost.")

screen.mainloop()
