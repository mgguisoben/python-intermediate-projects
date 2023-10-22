from time import sleep
from turtle import Screen

from food import Food
from score import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.title("SNEK")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game = True
while game:
    screen.update()
    sleep(.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score_board.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        game = False
        score_board.game_over()

    # Detect collision with tail
    for body in snake.snake[1:]:
        if snake.head.distance(body) < 10:
            game = False
            score_board.game_over()

screen.exitonclick()
