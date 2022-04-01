#Pong Game following a tutorial
# https://youtu.be/XGf2GcyHPhc "Learn Python by Building Five Games - Full Course" 
# by freeCodeCamp and TokyoEdTech

import turtle 

#Score variables
score_1 = 0
score_2 = 0

#Screen
wn = turtle.Screen()
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Player 1
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.shape("square")
player_1.color("white")
player_1.penup()
player_1.goto(-350, 0)

#Player 2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.shape("square")
player_2.color("white")
player_2.penup()
player_2.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

#Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0".format(score_1, score_2) , align="center", font=("Courier", 24, "normal"))

#Game over pen
gameover = turtle.Turtle()
gameover.speed(0)
gameover.color("red")
gameover.penup()
gameover.hideturtle()
gameover.goto(0, 0)

#Moving player 1 up
def player_1_up():
    y = player_1.ycor()
    y += 20
    player_1.sety(y)

#Moving player 1 down
def player_1_down():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)

#Moving player 2 up
def player_2_up():
    y = player_2.ycor()
    y += 20
    player_2.sety(y)

#Moving player 2 down
def player_2_down():
    y = player_2.ycor()
    y -= 20
    player_2.sety(y)

# Keyboard input listening
wn.listen()
wn.onkeypress(player_1_up, "w")
wn.onkeypress(player_1_down, "s")
wn.onkeypress(player_2_up, "8")
wn.onkeypress(player_2_down, "5")

#Game loop
while True:
    wn.update()

    #Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checker
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= 1
        #increases player 1 score
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2) , align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        #increases player 2 score
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2) , align="center", font=("Courier", 24, "normal"))

    #Player - Ball Collisions
    #Trying to add ball speed up after it hits player but not sure how to reset speed after point is scored
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_2.ycor() + 40 and ball.ycor() > player_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        #this speeds up the ball after each collision
        #ball.dx *= -1.10
        #ball.dy *= -1.10

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_1.ycor() + 40 and ball.ycor() > player_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        #this speeds up the ball after each collision
        #ball.dx *= -1.10
        #ball.dy *= -1.10

    #Game over message
    if score_1 == 10:
        gameover.write("GAME OVER PLAYER ONE HAS WON", align="center", font=("Courier", 30, "normal"))

    elif score_2 == 10: 
        gameover.write("GAME OVER PLAYER TWO HAS WON", align="center", font=("Courier", 30, "normal"))