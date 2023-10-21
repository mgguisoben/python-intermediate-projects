import turtle as t


def move_fd(): turtle.forward(move_dist)
def move_bw(): turtle.backward(move_dist)
def turn_right(): turtle.right(10)
def turn_left():  turtle.left(10)
def clear(): turtle.reset()


move_dist = 5
turtle = t.Turtle()
screen = t.Screen()

screen.setup(width=600, height=600)
screen.listen()

screen.onkeypress(move_fd, 'w')
screen.onkeypress(turn_right, 'd')
screen.onkeypress(turn_left, 'a')
screen.onkeypress(move_bw, 's')
screen.onkeypress(clear, 'c')

screen.mainloop()
