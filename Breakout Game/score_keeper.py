from turtle import Turtle
import time

class Scorekeeper(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-300, 260)
        self.write('Score:', align='center', font=('Courier', 25, 'bold'))
        self.goto(-220, 260)
        self.write(self.score, align='center', font=('Courier', 25, 'bold'))

    def increase_point(self):
        if self.score == 80:
            self.clear()
            self.goto(0, 0)
            self.write('You Won', align='center', font=('Courier', 45, 'bold'))
        else:
            self.score += 1
            self.update_score()




