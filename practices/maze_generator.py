# KK 2nd Maze Generator Pracice

# turtle and random imports
import turtle
import random
import time

# 2 nested list maze grid variable w/ 6 lists inside one list and 6 more lists inside each list
column_grid = [[[],[],[],[],[],[]],
               [[],[],[],[],[],[]],
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
    turtle.penup()
    turtle.goto(-400,400)
    turtle.pendown()
    
# maze wall drawing function(?)
#def mazeWall():

# right vertical line
# for loop iterating over each list in the column grid list
turtle.right(90)
for list in column_grid:
    # nested for loop iterating over each first list in the previous lists
    for nested_list in list:
        turtle.forward(20)

# left vertical line

# turtle.penup()
# turtle.goto(400,400)
# turtle.pendown()

# for loop iterating over each list in the maze list
for list in column_grid:
    # nested for loop iterating over the last index of each previous list
    for nested_list in list:
        turtle.forward(20)

# bottom line
# for loop iterating over the last list in the first maze list
    # nested for loop drawing a line to the right for each list in the last list

# top line
# for loop taking the first list in the initial entire list
    # nested for loop drawing a line to the right for every list

# drawing/generating the actual maze FUNCTION

setup()