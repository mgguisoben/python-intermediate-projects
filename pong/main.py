from time import sleep
from turtle import Screen

from ball import Ball
from paddle import Paddle
from score import ScoreBoard

score_board = ScoreBoard()

ball = Ball()

paddle1 = Paddle((-460, 0))
paddle2 = Paddle((460, 0))

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("gray")
screen.tracer(0)
screen.listen()
screen.onkeypress(paddle1.move_up, 'w')
screen.onkeypress(paddle1.move_down, 's')
screen.onkeypress(paddle2.move_up, 'Up')
screen.onkeypress(paddle2.move_down, 'Down')

game = True
while game:
    screen.update()
    sleep(ball.move_speed)

    ball.move()

    # Detect wall collision
    if ball.ycor() > 279 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect paddle collision
    if (ball.distance(paddle1) < 50 and ball.xcor() < -430) or (ball.distance(paddle2) < 50 and ball.xcor() > 430):
        ball.bounce_x()

    # Detect if paddle1 misses
    if ball.xcor() < - 490:
        ball.reset_position()
        score_board.p1_miss()

    # Detect if paddle2 misses
    if ball.xcor() > 490:
        ball.reset_position()
        score_board.p2_miss()

screen.exitonclick()
