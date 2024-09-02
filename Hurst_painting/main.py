import turtle as t
import  random

t.colormode(255)
rgb_colors = [(28, 108, 162), (191, 40, 81), (233, 160, 57), (233, 214, 89), (220, 137, 175), (141, 108, 58), (107, 193, 215), (21, 57, 131), (202, 165, 33), (210, 73, 94), (236, 90, 56), (142, 29, 72), (119, 191, 142), (142, 208, 227), (9, 184, 170), (106, 107, 196), (7, 158, 86), (97, 51, 37), (22, 160, 206), (232, 166, 185), (85, 46, 34)]
total_dots = 100
tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for dot_count in range(1,total_dots + 1):
    tim.dot(15,random.choice(rgb_colors))
    tim.forward(50)
    if dot_count %10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = t.Screen()
screen.exitonclick()