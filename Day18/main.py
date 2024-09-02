import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("arrow")


turtle.colormode(255)
tim.speed("fastest")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

def draw_circle(degree):
    for i in range(int(360/degree)):
        tim.color(random_color())
        tim.circle(100)
        tim.right(degree)

draw_circle(5)















screen = Screen()
screen.exitonclick()