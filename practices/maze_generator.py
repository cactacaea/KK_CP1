# KK 2nd Maze Generator Pracice

# turtle and random imports
import turtle
import random

# nested list maze grid variable w/ 6 lists inside one list and 6 more lists inside each list
grid = [[[],[],[],[],[],[]],
        [[],[],[],[],[],[]],
        [[],[],[],[],[],[]],
        [[],[],[],[],[],[]],
        [[],[],[],[],[],[]],
        [[],[],[],[],[],[]]]

# setup FUNCTION
def setup():
    # screen title/setup
    window = turtle.Screen()
    window.setup(600,600)
    window.title("Maze Generator")
    # turtle setups
    turtle.goto(200,200)
    turtle.speed(8)
    turtle.shape("turtle")
    turtle.pensize(8)

# maze wall drawing FUNCTION
#def mazeWall():

# right vertical line
    turtle.left(90)
# for loop iterating over each list in the maze list
    for list in grid:
    # nested for loop iterating over each first list in the previous lists
        for nested_list in list[0]:
            turtle.forward(20)

# left vertical line
# for loop iterating over each list in the maze list
    # nested for loop iterating over the last index of each previous list

# bottom line
# for loop iterating over the last list in the first maze list
    # nested for loop drawing a line to the right for each list in the last list

# top line
# for loop taking the first list in the initial entire list
    # nested for loop drawing a line to the right for every list

# drawing/generating the actual maze FUNCTION