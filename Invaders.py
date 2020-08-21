import turtle
import time

wn = turtle.Screen()
wn.setup(width=600,height=600)
wn.bgcolor("black")

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

wn.mainloop()