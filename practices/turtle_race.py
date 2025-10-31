# KK 2nd Turtle Race Practice

import turtle
import random
import time

# LATER INPUT FOR BETTING ON TURTLE

# 5 turtles named gary, tim, boris, maurice, and albert using turtle.Turtle()
gary = turtle.Turtle()
tim = turtle.Turtle()
boris = turtle.Turtle()
maurice = turtle.Turtle()
albert = turtle.Turtle()
# screen setup/pixels/title
screen = turtle.Screen()
screen.setup(2000,1100)
screen.title("Turtle Race")

gary.shape('turtle')
tim.shape("turtle")
boris.shape("turtle")
maurice.shape("turtle")
albert.shape("turtle")
# raceSetup FUNCTION
def raceSetup():
    # draw a finish line after 0,0
    drawer = turtle.Turtle()
    drawer.speed(10)
    drawer.color("#292929")
    drawer.pensize(10)
    drawer.penup()
    drawer.forward(700)
    drawer.pendown()
    drawer.left(90)
    drawer.forward(800)
    drawer.backward(800)
    drawer.backward(800)
    # penup
    drawer.penup()
    # start turtles on the same x coordinate (-850,y)
    gary.penup()
    gary.speed(10)
    gary.goto(-850, 400)
    gary.color("#C50303")
    gary.pensize(6)
    gary.pendown()

    tim.penup()
    tim.speed(10)
    tim.goto(-850, 200)
    tim.color("#97D161")
    tim.pensize(6)
    tim.pendown()

    boris.penup()
    boris.speed(10)
    boris.goto(-850, 0)
    boris.color("#E4760F")
    boris.pensize(6)
    boris.pendown()

    maurice.penup()
    maurice.speed(10)
    maurice.goto(-850, -200)
    maurice.color("#618ED1")
    maurice.pensize(6)
    maurice.pendown()

    albert.penup()
    albert.speed(10)
    albert.goto(-850, -400)
    albert.color("#DC91FA")
    albert.pensize(6)
    albert.pendown()
    
    time.sleep(1)

    gary.speed(4)
    tim.speed(4)
    boris.speed(4)
    maurice.speed(4)
    albert.speed(4)
# moveTurtle FUNCTION with parameters for each turtle

raceSetup()
# determine random integer number of steps
random_step = random.randint(0,50)

game = True
# while true loop until a turtle reaches a coordinate for win "function"
while game:
    for step in range(850):
        gary.forward(random_step)
        if gary.xcor()>= 700:
            print("Gary won")
            game = False
            break
        tim.forward(random_step)
        boris.forward(random_step)
        maurice.forward(random_step)
        albert.forward(random_step)

    # points = [gary.position(), tim.position(), boris.position(), maurice.position(), albert.position()]
    # wanted_x = 0
    # for point in points:
    #     if point[0] == wanted_x:
    #         print("a turtle won")
    #         break
    # if gary.position() or tim.position() or boris.position() or maurice.position() or albert.position() == x_coor:
    #     break