# KK 2nd Libraries & Built-in Functions Notes

import random
import turtle
num = random.randint(100,500)

turtle.shape("turtle")
turtle.color("#68C496")
turtle.pensize(10)
turtle.fillcolor("black")
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(0,400)
turtle.pendown()
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)
    turtle.right(90)
turtle.end_fill()

turtle.done()