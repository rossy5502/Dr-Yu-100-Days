from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
CAR_WIDTH = 40  # Approximate width of a car (20 * stretch_len=2)
CAR_HEIGHT = 20  # Approximate height of a car (20 * stretch_wid=1)

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def is_too_close(self, new_car):
        for car in self.all_cars:
            if car.distance(new_car) < CAR_WIDTH:  # If cars are too close
                return True
        return False

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(randint(0, 255), randint(0, 255), randint(0, 255))
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        
        # Try to find a valid y-position that's not too close to other cars
        max_attempts = 10
        for _ in range(max_attempts):
            y_pos = randint(-250, 250)
            new_car.goto(300, y_pos)
            
            # Check if this position is too close to other cars
            if not self.is_too_close(new_car):
                self.all_cars.append(new_car)
                return
        
        # If we couldn't find a good position, don't add the car
        new_car.hideturtle()

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            # Remove cars that are off-screen to save memory
            if car.xcor() < -320:
                car.hideturtle()
                self.all_cars.remove(car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
