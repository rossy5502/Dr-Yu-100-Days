from turtle import Turtle
from random import choice

POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0
list_of_directions=[UP,DOWN,LEFT,RIGHT]

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.turtles_list = []
        self.create_snake()
        self.segments = self.turtles_list
        self.head = self.segments[0]
        self.tries = 3

    def create_snake(self):

        for index in range(3):
            turtle = Turtle()
            turtle.shape("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x=POSITIONS[index], y=0)
            self.turtles_list.append(turtle)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def extend(self):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        self.turtles_list.append(new_segment)
        new_segment.goto(self.segments[-1].position())



    def bounderies(self):
        # Check for wall collision
        if (self.head.xcor() > 290 or self.head.xcor() < -290 or
                self.head.ycor() > 290 or self.head.ycor() < -290):
            self.head.goto(0, 0)
            self.head.setheading(choice(list_of_directions)) #random direction for the 3 tries instead of one
            self.tries -= 1
            if self.tries <= 0:
                return "game_over"
            return True
            
        # Check for self collision (skip the head)
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                self.head.goto(0, 0)
                self.head.setheading(UP)
                self.tries -= 1
                if self.tries <= 0:
                    return "game_over"
                return True
                
        return False
