#IMPORTING STUFF
from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screenturtle = Turtle()
screen = Screen()

#SCREEN SETUP
screen.setup(height=600, width=800)
screen.title("PONG GAME")
screen.bgcolor('black')
screen.tracer(0)

#SELECTING THE GAME MODE
while True:
    mode = screen.textinput(
        "Game Mode",
        "Choose a game mode:\n1 - First to 5 points wins\n2 - AI Opponent (vs Computer)\n3 - Infinite / Casual\n\nEnter 1, 2, or 3:"
    )

    if mode not in ("1", "2", "3"):
        print("Please select from the given list")
    else:
        break

#SETTING UP THE SCORE BOARD AND THE SCREEN
scoreboard = ScoreBoard()
screenturtle.penup()
screenturtle.goto(0,-300)
screenturtle.setheading(90)
screenturtle.pensize(10)
screenturtle.pencolor('white')
for x in range(20):
    screenturtle.pendown()
    screenturtle.forward(20)
    screenturtle.penup()
    screenturtle.forward(20)

#SETTING UP PADDLES AND THE BALL
ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# CONTROLS
screen.listen()
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

if mode != "2": 
    screen.onkeypress(r_paddle.move_up, key="Up")
    screen.onkeypress(r_paddle.move_down, key="Down")

WIN_SCORE = 5
AI_SPEED = 4
game_running = True
while game_running:
    screen.update()
    ball.move()

    # AI MODE
    if mode == "2":
        if ball.ycor() > r_paddle.ycor() + AI_SPEED:
            r_paddle.sety(r_paddle.ycor() + AI_SPEED)
        elif ball.ycor() < r_paddle.ycor() - AI_SPEED:
            r_paddle.sety(r_paddle.ycor() - AI_SPEED)

    # COLLISION WITH TOP AND BOTTOM EDGES
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.change_y()

    # COLLISION WITH PADDLES
    if ball.distance(r_paddle) < 60 and ball.xcor() > 340 or ball.distance(l_paddle) < 60 and ball.xcor() < -340:
        ball.change_x()
        ball.increase_speed()

    # BALL PAST R_PADDLE
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.refresh()
        ball.reset_speed()

    # BALL PAST L_PADDLE
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.refresh()
        ball.reset_speed()

    # WIN FOR MODE 1
    if mode == "1":
        if scoreboard.l_score >= WIN_SCORE:
            scoreboard.show_winner("Left Player")
            game_running = False

        elif scoreboard.r_score >= WIN_SCORE:
            winner = "Computer" if mode == "2" else "Right Player"
            scoreboard.show_winner(winner)
            game_running = False

screen.exitonclick()
