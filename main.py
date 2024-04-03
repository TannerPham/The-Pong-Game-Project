from turtle import Turtle, Screen
import random
import time

# import paddle
from gamedisplay import Mainscreen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
display = Mainscreen()

screen.setup(width=800, height=650)
screen.bgcolor("black")
screen.title("Pong Pong Pong")
screen.tracer(0)

display.draw_border()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
l_score = Scoreboard((-60,260))
r_score = Scoreboard((60,260))
# paddle.create_lpaddle()
ball = Ball()


screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
#screen.onkey(paddle.p2_up,"Up")
#screen.onkey(paddle.p2_down,"Down")
game_is_on = True


while game_is_on:
    sleeptime = ball.ball_speed
    time.sleep(sleeptime)

    screen.update()
    ball.move_ball()
    # if r_paddle.distance(ball) < 10:
    #     angle += 125
    #     ball.move_ball(angle)
    if ball.ycor() > 300 or ball.ycor() < -300 :
        ball.wall_bounce()
    if ball.xcor() > 330 and r_paddle.distance(ball)< 40:
        ball.paddle_bounce()
    elif ball.xcor() < -330 and l_paddle.distance(ball) < 40:
        ball.paddle_bounce()



    if ball.xcor() > 400:
        l_score.increase_score()
        ball.reset_ball()
        sleeptime *= 0.99
        r_paddle.goto(350,0)
        l_paddle.goto(-350,0)
    elif ball.xcor() < -410:
        r_score.increase_score()
        ball.reset_ball()
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)
screen.exitonclick()