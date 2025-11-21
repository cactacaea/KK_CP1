# KK 2nd

import turtle

def drawBranch(length):
    if length > 5:
        for i in range(3):
            turtle.forward(length)
            drawBranch(length/3)
            turtle.backward(length)
            turtle.right(60)

turtle.shape = "turtle"
turtle.speed(10)
turtle.color("#77CFDF")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()

for i in range(6):
    drawBranch(100)
    turtle.right(60)

turtle.hideturtle()
turtle.done()