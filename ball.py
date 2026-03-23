from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(1.1,1.1)
        self.turtlesize(1.1,1.1)
        self.penup()
        self.ymovement = 0.1
        self.xmovement = 0.1
    
    def move(self):
        new_x = self.xcor() + self.xmovement
        new_y = self.ycor() + self.ymovement

        self.goto(new_x, new_y)

    def change_y(self):
        
        self.ymovement = -(self.ymovement)

    def change_x(self):

        self.xmovement = -(self.xmovement)

    def refresh(self):
        self.goto(0,0)

    def increase_speed(self):
        if self.xmovement < 0:
            self.xmovement -= 0.01
        else:
            self.xmovement += 0.01

        if self.ymovement < 0:
            self.ymovement -= 0.01
        else:
            self.ymovement += 0.01

    def reset_speed(self):
        if self.xmovement < 0:
            self.xmovement = 0.1
        else:
            self.xmovement = 0.1

        if self.ymovement < 0:
            self.ymovement = 0.1
        else:
            self.ymovement = 0.1