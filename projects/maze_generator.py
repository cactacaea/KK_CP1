# KK 2nd Maze Generator Pracice

# turtle and random imports
import turtle
import random
import time

# 2 nested list maze grid variable w/ 6 lists inside one list and 6 more lists inside each list
column_grid = [[(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False]))],
               [(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False]))],
               [(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False]))],
               [(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False]))],
               [(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False]))],
               [(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False]))]]

row_grid = [[(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False]))],
            [(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False]))],
            [(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False]))],
            [(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False]))],
            [(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False]))],
            [(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False])),(random.choice([True,False]))]]



# setup FUNCTION
def setup():
    # screen title/setup
    window = turtle.Screen()
    window.setup(1500,1500) # 900,900 / 1500,1500
    window.title("Maze Generator")
    # turtle setups
    turtle.pensize(2)
    turtle.speed(6)
    turtle.shape("turtle")
    
# maze wall drawing FUNCTION
#def mazeWall():
    
# drawing/generating the actual maze FUNCTION

# check for solvable maze FUNCTION

setup()
# turtle starts in the 2nd quadrant
turtle.penup()
turtle.goto(-360,360)
turtle.pendown()
# 120 pixels for each slot in the grid, for LOOP to draw square/walls
for x in range(4):
    turtle.forward(720)
    turtle.right(90)

 

turtle.goto(-360,240)
for unit in row_grid:
    for value in unit:
        if value == True:
            turtle.pendown()
            turtle.forward(120)
            turtle.penup()
        else:
            turtle.penup()
            turtle.forward(120)
    current_y = turtle.ycor()
    turtle.goto(-360,(current_y-120))
    
turtle.goto(-240,360)
turtle.right(90)
for unit in column_grid:
    for value in unit:
        if value == True:
            turtle.pendown()
            turtle.forward(120)
            turtle.penup()
        else:
            turtle.penup()
            turtle.forward(120)
    current_x = turtle.xcor()
    turtle.goto(-240,(current_x+120))
    