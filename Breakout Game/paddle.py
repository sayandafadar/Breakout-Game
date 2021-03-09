from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color('pink')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.penup()
        self.goto(position, -260)

