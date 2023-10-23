from random import choice, randrange
from turtle import Turtle

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']


class Cars():

    def __init__(self):

        self.cars_list = []

    def create_cars(self):
        rand_y = randrange(-180, 200, 60)
        self.car = Turtle('square')
        self.car.penup()
        self.car.shapesize(stretch_wid=1, stretch_len=2)
        self.car.setheading(180)
        self.car.color(choice(COLORS))
        self.car.goto(220, rand_y)
        self.cars_list.append(self.car)

    def move(self):
        for car in self.cars_list:
            car.forward(20)

            # Delete car object that reached the end of the screen
            if car.xcor() < -260:
                self.cars_list.pop(self.cars_list.index(car))
