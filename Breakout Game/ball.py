from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('cyan')
        self.shape('circle')
        self.penup()
        self.goto(0, -200)
        self.x_move = randint(14, 22)
        self.y_move = randint(14, 22)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def x_bounce(self):
        self.x_move *= -1

    def y_bounce(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, -200)
        self.y_bounce()
