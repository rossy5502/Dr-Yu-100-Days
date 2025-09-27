from turtle import *

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)
        self.speed("fastest")
        self.moving_up = False
        self.moving_down = False
        self.move_speed = 20

    def start_moving_up(self):
        self.moving_up = True
        
    def stop_moving_up(self):
        self.moving_up = False
        
    def start_moving_down(self):
        self.moving_down = True
        
    def stop_moving_down(self):
        self.moving_down = False
        
    def move(self):
        if self.moving_up and self.ycor() < 250:
            new_y = self.ycor() + self.move_speed
            self.goto(self.xcor(), new_y)
        if self.moving_down and self.ycor() > -240:
            new_y = self.ycor() - self.move_speed
            self.goto(self.xcor(), new_y)
