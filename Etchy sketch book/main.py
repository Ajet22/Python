from turtle import Turtle, Screen

tom = Turtle()
tom.pensize(5)
def move_forwards():
    tom.forward(10)
def move_backwards():
    tom.backward(10)
def move_counterclock():
    tom.left(10)
def move_right():
    tom.right(10)
def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()
screen = Screen()
screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(move_right, 'a')
screen.onkey(move_right, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()