from turtle import Screen,colormode
import time
from random import randint
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
colormode(255)
# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)  # Turn off automatic screen updates

# Initialize game objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Keyboard bindings
screen.listen()
screen.onkeypress(player.Up, "Up")


# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    
    # Create new cars randomly
    if randint(1, 7) == 1:  # 1 in 6 chance to create a new car each frame
        car_manager.create_car()
    
    # Move all cars
    car_manager.move_cars()
    
    # Check for collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
        # Check if player reached the top
        elif player.ycor() > 280:
            player.reset_position()
            car_manager.increase_speed()
            scoreboard.increase_level()
    
    # Update the screen after all movements and checks
    screen.update()

screen.exitonclick()