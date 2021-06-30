import turtle


# Window
window = turtle.Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.title("PONG")
window.tracer(0)

# Left rocket
leftRocket = turtle.Turtle()
leftRocket.speed(0)
leftRocket.shape("square")
leftRocket.shapesize(stretch_wid=5, stretch_len=1)
leftRocket.color("green")
leftRocket.penup()
leftRocket.goto(-350,0)

# Right rocket
rightRocket = turtle.Turtle()
rightRocket.speed(0)
rightRocket.shape("square")
rightRocket.shapesize(stretch_wid=5, stretch_len=1)
rightRocket.color("blue")
rightRocket.penup()
rightRocket.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.shapesize(0.5, 0.5)
ball.penup()
ball.speed(0)
ballspeed = 0
ball.dx = 0.10
ball.dy = 0.10

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align='center', font=('Courier', 24, 'bold'))
pen.hideturtle()

# Score
score_a = 0
score_b = 0

def leftRocket_up():
    y = leftRocket.ycor()
    y += 20
    leftRocket.sety(y)

def rightRocket_up():
    y = rightRocket.ycor()
    y += 20
    rightRocket.sety(y)

def leftRocket_down():
    y = leftRocket.ycor()
    y += -20
    leftRocket.sety(y)

def rightRocket_down():
    y = rightRocket.ycor()
    y += -20
    rightRocket.sety(y)

# Keyboard binding
window.listen()
window.onkeypress(leftRocket_up, 'w')
window.onkeypress(leftRocket_down, 's')
window.onkeypress(rightRocket_up, 'Up')
window.onkeypress(rightRocket_down, 'Down')

# Main game loop
while True:
    window.update()

     # Moving Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290 or ball.ycor() < -290: 
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))

    if ball.xcor() < -390:
        ball.goto(0, 0)

        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))

    # Rocket and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < rightRocket.ycor() + 60 and ball.ycor() > rightRocket.ycor() -60):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < leftRocket.ycor() + 60 and ball.ycor() > leftRocket.ycor() -60):
        ball.setx(-340)
        ball.dx *= -1