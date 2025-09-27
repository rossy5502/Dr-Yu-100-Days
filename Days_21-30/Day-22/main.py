from turtle import Turtle, Screen
from ball import Ball
from paddles import Paddle
import time
from score_board import ScoreBoard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
scoreboard=ScoreBoard()

#create paddles
right_paddle = Paddle((370, 0))
left_paddle = Paddle((-380, 0))
ball=Ball()
#keyboard bindings
screen.listen()
screen.onkeypress(right_paddle.start_moving_up, "Up")
screen.onkeyrelease(right_paddle.stop_moving_up, "Up")
screen.onkeypress(right_paddle.start_moving_down, "Down")
screen.onkeyrelease(right_paddle.stop_moving_down, "Down")
screen.onkeypress(left_paddle.start_moving_up, "w")
screen.onkeyrelease(left_paddle.stop_moving_up, "w")
screen.onkeypress(left_paddle.start_moving_down, "s")
screen.onkeyrelease(left_paddle.stop_moving_down, "s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    # Move paddles if their movement flags are set
    right_paddle.move()
    left_paddle.move()
    
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < -270:
       ball.bounce_y()
    if (ball.distance(right_paddle) < 40 and  ball.xcor()>340 or
          ball.distance(left_paddle) < 40 and ball.xcor() < -340) :
        ball.bounce_x()
    if ball.xcor() > 380:
        scoreboard.left_score()
        ball.reset_position()
    if ball.xcor() < -380:
        scoreboard.right_score()
        ball.reset_position()







screen.exitonclick()