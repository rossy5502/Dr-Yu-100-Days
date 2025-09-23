from turtle import Turtle, Screen
from random import choice
turtle_colors = ["red", "blue", "yellow", "purple", "orange", "pink", "cyan", "magenta"]
screen = Screen()
screen.bgcolor("green")
dash_turtle = Turtle()
dash_turtle.color("white")
dash_turtle.width(5)
dash_turtle.speed(1)

def draw_sides(side_length):
    for num_sides in range(3, 11):
         angle = 360 / num_sides
         dash_turtle.color(choice(turtle_colors))
         for _ in range(num_sides):
            dash_turtle.forward(side_length)
            dash_turtle.right(angle)
    screen.exitonclick()

draw_sides(100)




