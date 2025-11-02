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
screen.setup(1800,900)
screen.title("Turtle Race")

gary.shape('turtle')
tim.shape("turtle")
boris.shape("turtle")
maurice.shape("turtle")
albert.shape("turtle")
# raceSetup FUNCTION
def raceSetup():
    # draw a finish line around x=700
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

raceSetup()

game = True

# while loop until a turtle reaches a coordinate for win "function"
while game:
    for step in range(100):
        
        gary.forward(random.randint(0,50))
        if gary.xcor() >= 700:
            print("Gary (red turtle) won!")
            game = False
            break
        tim.forward(random.randint(0,50))
        if tim.xcor() >= 700:
            print("Tim (green turtle) won!")
            game = False
            break
        boris.forward(random.randint(0,50))
        if boris.xcor() >= 700:
            print("Boris (orange turtle) won!")
            game = False
            break
        maurice.forward(random.randint(0,50))
        if maurice.xcor() >= 700:
            print("Maurice (blue turtle) won!")
            game = False
            break
        albert.forward(random.randint(0,50))
        if albert.xcor() >= 700:
            print("Albert (purple turtle) won!")
            game = False
            break