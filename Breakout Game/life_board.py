from turtle import Turtle


class Lifekeeper(Turtle):

    def __init__(self):
        super().__init__()
        self.live = 5
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_life()

    def update_life(self):
        self.clear()
        self.goto(200, 260)
        self.write('Lives:', align='center', font=('Courier', 25, 'bold'))
        self.goto(280, 260)
        self.write(self.live, align='center', font=('Courier', 25, 'bold'))

    def decrease_life(self):
        if self.live == 1:
            self.clear()
            self.goto(0, 0)
            self.write('You Lost', align='center', font=('Courier', 45, 'bold'))
        else:
            self.live -= 1
            self.update_life()







