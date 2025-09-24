from turtle import Turtle, Screen
import turtle as t
from random import choice, randint

screen = Screen()
screen.bgcolor("white")
dash_turtle = Turtle()
t.colormode(255)

dash_turtle.width(2)
dash_turtle.speed(2)

def random_color():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    return (r,g,b)

def circles(size_of_gap=10):
    circle_amount=360/size_of_gap
    for _ in range(int(circle_amount)):
        dash_turtle.speed(520)
        dash_turtle.color(random_color())
        dash_turtle.circle(100)
        dash_turtle.setheading(dash_turtle.heading() + size_of_gap)
    screen.exitonclick()
circles()
