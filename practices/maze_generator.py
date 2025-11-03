# KK 2nd Maze Generator Pracice

# turtle and random imports
import turtle
import random
import time

# 2 nested list maze grid variable w/ 6 lists inside one list and 6 more lists inside each list
column_grid = [[True,True,True,True,True,True],
               [True,True,True,True,True,True],
               [[],[],[],[],[],[]],
               [[],[],[],[],[],[]],
               [[],[],[],[],[],[]],
               [[],[],[],[],[],[]]]

row_grid = [[[],[],[],[],[],[]],
            [[],[],[],[],[],[]],
            [[],[],[],[],[],[]],
            [[],[],[],[],[],[]],
            [[],[],[],[],[],[]],
            [[],[],[],[],[],[]]]

# setup FUNCTION
def setup():
    # screen title/setup
    window = turtle.Screen()
    window.setup(1500,1500)
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
    # draws 20 pixels for every slot in the grid
    turtle.forward(720)
    time.sleep(1)
    turtle.right(90)
    turtle.forward(720)
    turtle.right(90)
    turtle.forward(720)
    time.sleep(1)
    turtle.right(90)
    turtle.forward(720)

# drawing/generating the actual maze FUNCTION
# def drawMaze():

# check for solvable maze FUNCTION


setup()
mazeWall()