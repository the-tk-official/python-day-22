import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

ball = Ball()
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')

screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the ball
    if ball.ycor() > 270 or ball.ycor() < -270:
        # Need a bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 360:
        scoreboard.l_point()
        ball.reset_position()

    # Detect L paddle misses
    if ball.xcor() < -360:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()
