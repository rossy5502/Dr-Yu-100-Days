from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()  # Create an instance of the Scoreboard class and attach it to the screen
new_game = Snake()     # Create an instance of the Snake class
food = Food()

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.2)
    new_game.move()
    screen.listen()
    screen.onkey(new_game.up, "Up")   #snake cannot move in the opposite direction it will hit itself
    screen.onkey(new_game.down, "Down") # snake cannot move in the opposite direction it will hit itself
    screen.onkey(new_game.left, "Left") # snake cannot move in the opposite direction it will hit itself
    screen.onkey(new_game.right, "Right")  # snake cannot move in the opposite direction it will hit itself
    # Detect collision with wall or self
    result=new_game.bounderies()
    if result == "game_over":
        scoreboard.game_over()    # Call the game_over method to display "GAME OVER" message
        game_over = True  # ends the while loop

    elif result:
        print(f"Tries left: {new_game.tries}")
    # Detect collision with food
    elif new_game.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        new_game.extend()

screen.update()
screen.exitonclick()

