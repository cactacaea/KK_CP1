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
    # draw a finish line around 0,0
    drawer = turtle.Turtle()
    drawer.speed(10)
    drawer.color("#292929")
    drawer.pensize(8)
    drawer.left(90)
    drawer.forward(800)
    drawer.backward(800)
    drawer.backward(800)
    # penup
    drawer.penup()
    # start turtles on the same x coordinate (-850,y)
    gary.penup()
    gary.speed(13)
    gary.goto(-850, 400)
    gary.color("#C50303")
    gary.pensize(6)
    gary.pendown()

    tim.penup()
    tim.speed(13)
    tim.goto(-850, 200)
    tim.color("#97D161")
    tim.pensize(6)

    boris.penup()
    boris.speed(13)
    boris.goto(-850, 0)
    boris.color("#E4760F")
    boris.pensize(6)

    maurice.penup()
    maurice.speed(13)
    maurice.goto(-850, -200)
    maurice.color("#618ED1")
    maurice.pensize(6)

    albert.penup()
    albert.speed(13)
    albert.goto(-850, -400)
    albert.color("#DC91FA")
    albert.pensize(6)
    
    time.sleep(3)
# moveTurtle FUNCTION with parameters for each turtle

    # determine random integer # of steps
# win FUNCTION with parameters for each turtle, conditionals to check each turtle, parameter of the user's bet
    # if user's bet is the same as the turtle that won, display a positive message


raceSetup()
random_step = random.randint(50)

points = [gary.position(), tim.position(), boris.position(), maurice.position(), albert.position()]
wanted_x = 0
for point in points:
    if point[0] == wanted_x:
        x_coor = 0
# while true loop until a turtle reaches a coordinate
while True:
    for step in range(850):
        gary.forward(random_step)
        tim.forward(random_step)
        boris.forward(random_step)
        maurice.forward(random_step)
        albert.forward(random_step)
    if gary.position() or tim.position() or boris.position() or maurice.position() or albert.position() == x_coor:
        break