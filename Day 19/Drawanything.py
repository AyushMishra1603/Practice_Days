from turtle import  Turtle, Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def clockwise():
    tim.right(10)

def Counterclockwise():
    tim.left(10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key = "w", fun= forward)
screen.onkey(key = "s", fun= backward)
screen.onkey(key = "a", fun= Counterclockwise)
screen.onkey(key = "d", fun= clockwise)
screen.onkey(key = "c", fun= clear_drawing)

screen.exitonclick()
