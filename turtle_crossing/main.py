from time import sleep
from turtle import Screen

from cars import Cars
from player import Player
from level import Level

player = Player()
cars = Cars()
level = Level()

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor('gray')
screen.tracer(0)
screen.listen()
screen.onkeypress(player.move_up, 'Up')
screen.onkeypress(player.move_down, 'Down')
screen.onkeypress(player.move_left, 'Left')
screen.onkeypress(player.move_right, 'Right')

game = True
while game:
    screen.update()
    sleep(0.2)

    cars.create_cars()
    cars.move()

    # Detect if player is at finish line
    if player.ycor() > 240:
        player.reset_position()

    # Detect collision with car object
    for car in cars.cars_list:
        pass

screen.exitonclick()
