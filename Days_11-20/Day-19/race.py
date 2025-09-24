import turtle, random
colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']
turtles=[]
screen = turtle.Screen()
screen.setup(500, 400)
is_race_on=False


for i in range(6):
   tim = turtle.Turtle(shape="turtle")
   turtles.append(tim)

user_bet=screen.textinput("Race", "Which color would you like to choose?")
for index, turtle in enumerate(turtles):
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(x=-230, y=-90 + index * 40)

if user_bet in colors:
    is_race_on=True
else:
    print("Please choose a valid color next time!")
    is_race_on=False
while is_race_on:
    for turtle in turtles:
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on=False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner!")

screen.exitonclick()


