from turtle import  Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid = 1, stretch_len = 1)
        self.goto(x=0,y=0)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def r_movement(self):
        y_cor = self.ycor() + self.y_move
        x_cor = self.xcor() + self. x_move
        self.goto(x=x_cor, y=y_cor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()