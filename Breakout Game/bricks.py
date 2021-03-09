from turtle import Turtle
import randomcolor

rand_color = randomcolor.RandomColor()


class Bricks(Turtle):

    def __init__(self, x_position, y_position, width, height):
        super().__init__()
        self.shape('square')
        self.color(rand_color.generate())
        self.shapesize(stretch_wid=width, stretch_len=height)  # stretch_wid=1, stretch_len=3
        self.penup()
        self.goto(x_position, y_position)

    def destroy_bricks(self):
        self.goto(550, 660)
        self.hideturtle()

    def clear_screen(self):
        self.clear()



