# Simple pong in python 3 for beginner
# Tutorial by @TokyoEdTech
# Editing by little-bear-creator
# Part 1 : getting started

#import basic game's graphics for beginners
import turtle 

#Initialization of screen
wn = turtle.Screen()
wn.title("Pong by little-bear-creator")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# Allow the game to display on screen faster
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)               # set the speed to the maximum speed possible (on screen)
paddle_a.shape("square")        # default shape 20px by 20px
paddle_a.color("white")
# Changing shape
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)               # set the speed to the maximum speed possible (on screen)
paddle_b.shape("square")        # default shape 20px by 20px
paddle_b.color("white")
# Changing shape
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)               # set the speed to the maximum speed possible (on screen)
ball.shape("square")        # default shape 20px by 20px
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1               # define speed, can be different between computers
ball.dy = -0.1


# ------ Functions to move paddles and ball ------
# paddle_a
def paddle_a_up():
    y = paddle_a.ycor()     # get coordinate
    y += 20
    paddle_a.sety(y)        # set coordinate

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# paddle_b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# ------ Keyboard binding ------
wn.listen()
# When user push "z" on keyboard, paddle_a_up() is called
# paddle_a
wn.onkeypress(paddle_a_up, "z")
wn.onkeypress(paddle_a_down, "s")
# paddle_b
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top and bottom border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collision
    # Boucing with right paddle
    # /!\ info : le paddle fait 20 px de large, sa coordonée 350 divise le paddle en 2 paddle de 10 px de largeur
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() <  paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() <  paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1



