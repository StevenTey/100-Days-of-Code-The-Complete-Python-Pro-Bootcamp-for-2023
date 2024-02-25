from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

TIMESLEEP = 0.1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.tracer(0)

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(TIMESLEEP)
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
        TIMESLEEP *= 0.9
        
    if ball.xcor() > 380: 
        ball.reset_position()
        scoreboard.l_scored()
        
        
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_scored()
    
    screen.update()

screen.exitonclick()