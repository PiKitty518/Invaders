import turtle
import time

wn = turtle.Screen()
wn.title("Shooter by PiKitty518")
wn.setup(width=600,height=600)
wn.bgcolor("black")
wn.tracer(0)

delay = 0.01

border = turtle.Turtle()
border.speed(0)
border.penup()
border.pencolor("white")
border.goto(300,300)
border.pendown()
border.goto(-300,300)
border.goto(-300,-300)
border.goto(300,-300)
border.goto(300,300)
border.penup()
border.goto(10000,10000)

player = turtle.Turtle()
player.penup()
player.speed(0)
player.color("blue")
player.shape("triangle")
player._rotate(90)
player.goto(0,-200)

def right():
    x=player.xcor()
    player.setx(x+40)
def left():
    x=player.xcor()
    player.setx(x-40)

wn.listen()
wn.onkeypress(right,"d")
wn.onkeypress(left,"a")

while True:
    time.sleep(delay)

    wn.update()
