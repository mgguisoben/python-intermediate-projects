from time import sleep
from turtle import Screen

from cars import Cars
from level import Level
from player import Player

player = Player()
cars = Cars()
level = Level()

screen = Screen()
screen.setup(width=500, height=500)
screen.title("Turtle Crossing")
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
    sleep(level.car_speed)

    cars.create_cars()
    cars.move()

    # Detect if player is at finish line
    if player.ycor() > 240:
        player.reset_position()
        level.level_up()

    # Detect collision with car object
    for car in cars.cars_list:
        if player.distance(car) < 15:
            game = False
            level.game_over()

screen.exitonclick()
