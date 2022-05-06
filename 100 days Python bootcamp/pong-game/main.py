from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))

ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_direction_wall()

    if (ball.xcor() > 350) or (ball.xcor() < -350): # and ball.distance(r_paddle) < 50) or (ball.xcor() < -330 and ball.distance(l_paddle) < 50):
        print(f"ball.distance(r_paddle): {ball.distance(r_paddle)}, ball.distance(l_paddle): {ball.distance(l_paddle)}")

        ball_coord = (ball.xcor(),ball.ycor())
        r_paddle_coord = (r_paddle.xcor(),r_paddle.ycor())
        l_paddle_coord = (l_paddle.xcor(),l_paddle.ycor())
        print(f"ball: {ball_coord}, r_paddle: {r_paddle_coord}, l_paddle: {l_paddle_coord}")

        #print("ball: (" + str(ball.xcor()) + "," + str(ball.ycor()) + "), rpaddle: (" + str(r_paddle.xcor()) + "," + str(r_paddle.ycor()) + "), lpaddle: (" + str(l_paddle.xcor()) + "," + str(l_paddle.ycor()) + ")")
        ball.change_direction_paddle()



screen.exitonclick()