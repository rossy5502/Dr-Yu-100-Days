import turtle
import random

turtle.colormode(255)
screen = turtle.Screen()
tim = turtle.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_hirst_grid(rows, cols, dot_size, spacing):
    start_x = -cols * spacing // 2
    start_y = -rows * spacing // 2
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * spacing
            y = start_y + row * spacing
            tim.goto(x, y)
            tim.dot(dot_size, random_color())

draw_hirst_grid(10, 10, 20, 50)
screen.exitonclick()
