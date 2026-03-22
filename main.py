from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard

turtle = Turtle()
screen = Screen()
scoreboard = ScoreBoard()

#SCREEN SETUP
screen.setup(height=600, width=800)
screen.title("PONG GAME")
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

ball = Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

#CONTROLS
#l_paddle

screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

#r_paddle
screen.onkeypress(r_paddle.move_up, key="Up")
screen.onkeypress(r_paddle.move_down, key="Down")


game_running = True
while game_running:
    screen.update()
    ball.move()

    #Checks collisions with edges of the screen
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.change_y()

    #Checks collision with paddles
    if ball.distance(r_paddle) < 60 and ball.xcor() > 340 or ball.distance(l_paddle) < 60 and ball.xcor() < -340:
        ball.change_x()
    
    #checks if ball has gone past the screen
    #r_paddle
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.refresh()

    #l_paddle
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.refresh()



screen.exitonclick()

print("Hello world")