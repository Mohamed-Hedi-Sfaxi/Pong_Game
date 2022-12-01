

import turtle

import winsound

wn = turtle.Screen()
wn.title("Pong By @Mohamed-Hedi-Sfaxi")
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.tracer(0)


# Score
score_a = 0
score_b = 0



# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=8, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-600, 0)


# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=8, stretch_len=1)
paddle_b.penup()
paddle_b.goto(600, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(1.5,1.5)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "bold"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Bindings
wn.listen()
wn.onkeypress(paddle_a_up, "z")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()

    # Move The Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border cheking
    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy *= -1
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)

    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy *= -1
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)

    if ball.xcor() > 620:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)

    if ball.xcor() < -620:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)


    #paddle and ball collisions
    if (ball.xcor() > 590 and ball.xcor() < 600) and (ball.ycor() < paddle_b.ycor() + 70 and ball.ycor() > paddle_b.ycor() - 70):
        ball.setx(590)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -590 and ball.xcor() > -600) and (ball.ycor() < paddle_a.ycor() + 70 and ball.ycor() > paddle_a.ycor() - 70):
        ball.setx(-590)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)