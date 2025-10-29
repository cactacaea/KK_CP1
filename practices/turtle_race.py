# KK 2nd Turtle Race Practice

import turtle
import random
import time

# LATER INPUT FOR BETTING ON TURTLE

# 5 turtles named gary, tim, boris, maurice, and albert using turtle.Turtle()
turtle.shape("turtle")
gary = turtle.Turtle()
tim = turtle.Turtle()
boris = turtle.Turtle()
maurice = turtle.Turtle()
albert = turtle.Turtle()
# screen setup/pixels/title
screen = turtle.Screen()
screen.setup(2000,1100)
screen.title("Turtle Race")

# raceSetup FUNCTION
def raceSetup(gary, tim, boris, maurice, albert):
    # draw a finish line around 0,0
    turtle.color("#292929")
    turtle.pensize(8)
    turtle.left(90)
    turtle.forward(800)
    turtle.backward(800)
    turtle.backward(800)
    # penup
    turtle.penup()
    # start turtles on the same x coordinate (-850,y)
    turtle.pendown()
    gary.goto(-850, 400)
    gary.color("#D16262")
    gary.pensize(6)
    tim.goto(-850, 200)
    tim.color("#97D161")
    tim.pensize(6)
    boris.goto(-850, 0)
    boris.color("#E4760F")
    boris.pensize(6)
    maurice.goto(-850, -200)
    maurice.color("#618ED1")
    maurice.pensize(6)
    albert.goto(-850, -400)
    albert.color("#B61EF1")
    albert.pensize(6)
    time.sleep(10)
# moveTurtle FUNCTION with parameters for each turtle
    # determine random integer # of steps
# win FUNCTION with parameters for each turtle, conditionals to check each turtle, parameter of the user's bet
    # if user's bet is the same as the turtle that won, display a positive message


# while true loop until a turtle reaches a coordinate
raceSetup(gary,tim,boris,maurice,albert)
