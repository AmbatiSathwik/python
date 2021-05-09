import turtle

win = turtle.Screen()
win.title("Ping Pong")
win.bgcolor("Black")
win.setup(width = 800, height = 600)
win.tracer(0)


#paddle_a

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5 ,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle_b

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5 ,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#score
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align = "center", font = ("Lucid",24,"normal"))

def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 25
    paddle_a.goto(-350, y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 25
    paddle_a.goto(-350, y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 25
    paddle_b.goto(350, y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 25
    paddle_b.goto(350, y)

#keyboard
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

count = 0

while True:
    win.update()

    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #boarder
    if ball.ycor() > 280:
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.dy *= -1

    if ball.xcor() > 390:
        score_a += 1
        ball.goto(0, 0)
        ball.dy = ball.dx
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align = "center", font = ("Lucid",24,"normal"))

    if ball.xcor() < -390:
        score_b += 1
        ball.goto(0, 0)
        ball.dy = ball.dx
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align = "center", font = ("Lucid",24,"normal"))

    if ball.xcor() > 330 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        if ball.ycor() > paddle_b.ycor() + 10 or ball.ycor() < paddle_b.ycor() - 10:
                ball.setx(330)
                ball.dx *= -1
                if ball.dy < 0.5:
                    ball.dy *= 2
                else:
                    ball.dy -= 0.5
        if ball.ycor() < paddle_b.ycor() +10 and ball.ycor() > paddle_b.ycor() - 10:
            ball.setx(330)
            ball.dx *= -1
    if ball.xcor() < -330 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        if ball.ycor() > paddle_a.ycor() + 10 or ball.ycor() < paddle_a.ycor() - 10:
            ball.setx(-330)
            ball.dx *= -1
            if ball.dy < 0.5:
                ball.dy *= 2
            else:
                ball.dy -= 0.5
        if ball.ycor() < paddle_a.ycor() +10 and ball.ycor() > paddle_a.ycor() - 10:
            ball.setx(-330)
            ball.dx *= -1