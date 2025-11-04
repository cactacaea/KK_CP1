# KK 2nd Maze Generator Pracice

# turtle and random imports
import turtle
import random
import time

# 2 nested list maze grid variable w/ 6 lists inside one list and 6 more lists inside each list
column_grid = [[True,True,False,True,True,False],
               [True,False,True,True,True,True],
               [True,True,True,True,True,True],
               [True,True,True,True,True,True],
               [True,True,True,True,True,True],
               [True,True,True,True,True,True]]

row_grid = [[True,True,True,True,True,True],
            [True,True,True,True,True,True],
            [True,True,True,True,True,True],
            [True,True,True,True,True,True],
            [True,True,True,True,True,True],
            [True,True,True,True,True,True]]

# setup FUNCTION
def setup():
    # screen title/setup
    window = turtle.Screen()
    window.setup(1500,1500) # 900,900 / 1500,1500
    window.title("Maze Generator")
    # turtle setups
    turtle.pensize(4)
    turtle.speed(6)
    turtle.shape("turtle")
    
# maze wall drawing FUNCTION
def mazeWall():
    # TOP LINE
    # turtle starts in the 2nd quadrant
    turtle.penup()
    turtle.goto(-360,360)
    turtle.pendown()
    # 120 pixels for each slot in the grid
    turtle.forward(720)
    time.sleep(.5)
    turtle.right(90)
    turtle.forward(720)
    turtle.right(90)
    turtle.forward(720)
    time.sleep(.5)
    turtle.right(90)
    turtle.forward(720)
    turtle
    # TURTLE STOPS WITH ITS PEN BACK UP AND TURNED DIRECTLY TO THE RIGHT
    turtle.penup()
    turtle.right(90)

# drawing/generating the actual maze FUNCTION
def drawMaze():
    for unit in column_grid:
        for value in unit:
            if value == True:
                turtle.pendown()
                turtle.forward(120)
                turtle.penup()
            else:
                turtle.penup()
                turtle.forward(120)
    # for unit in row_grid:
    #     for value in unit:
    #         if value == True:
    #             turtle.pendown()
    #             turtle.forward(120)

# check for solvable maze FUNCTION


setup()
mazeWall()
drawMaze()