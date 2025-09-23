from turtle import Turtle, Screen
from random import choice
turtle_colors = ["red", "blue", "yellow", "purple", "orange", "pink", "cyan", "magenta"]
screen = Screen()
screen.bgcolor("white")
dash_turtle = Turtle()
dash_turtle.color("green")
dash_turtle.width(10)
dash_turtle.speed(2)

def random_walk(steps, step_length):
    directions = [0, 90, 180, 270]
    for _ in range(steps):
        dash_turtle.color(choice(turtle_colors))
        dash_turtle.setheading(choice(directions))
        dash_turtle.forward(step_length)
    screen.exitonclick()
random_walk(100, 20)