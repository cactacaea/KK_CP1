# KK 2nd Maze Generator Pracice

# turtle and random imports
import turtle
import random
import time

# 2 nested list maze grid variable w/ 6 lists inside one list and 6 more lists inside each list, randomizing the choices
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


turtle.hideturtle()
# setup FUNCTION
def setup():
    # screen title/setup
    window = turtle.Screen()
    window.setup(900,900) # 900,900 / 1500,1500
    window.title("Maze Generator")
    # turtle setups
    turtle.pensize(2)
    turtle.speed(6)
    turtle.shape("turtle")

# randomized grid drawing FUNCTION
def drawGrids(row_grid,column_grid):
    turtle.goto(-360,240)
    # for LOOP iterating over each list in the row list, drawing a line to the right if it's true/false
    for unit in row_grid:
        for value in unit:
            if value == True:
                turtle.pendown()
                turtle.forward(120)
                turtle.penup()
            # lift pen if false and continue drawing
            else:
                turtle.penup()
                turtle.forward(120)
        current_y = turtle.ycor()
        turtle.goto(-360,(current_y-120))
    turtle.right(90)
        
    turtle.penup()
    turtle.goto(-240,360)
    turtle.pendown()
    # for LOOP iterating over each list in the column list, drawing a line to the right if it's true/false
    for unit in column_grid:
        for value in unit:
            if value == True:
                turtle.pendown()
                turtle.forward(120)
                turtle.penup()
            # lift pen if false and continue drawing
            else:
                turtle.penup()
                turtle.forward(120)
        current_x = turtle.xcor()
        turtle.goto((current_x+120),360)

setup()

# # check for solvable maze FUNCTION
# def solvableMaze(row_grid,column_grid):
#     visited_cells = []
#     def search(rows, columns):
#         if rows == 5 and columns == 5:
#             return True
#         visited_cells[rows][columns] = True

# setup()
# solvable = False
# # CALLING FUNCTIONS AND DRAWING WALLS

# # while loop checking for valid row/column grids
# while solvable == False:


# if maze is solvable
    # draw walls

    # turtle starts in the 2nd quadrant
turtle.penup()
turtle.goto(-360,360)
turtle.pendown()
# 120 pixels for each slot in the grid, for LOOP to draw square/walls
for x in range(4):
    turtle.forward(720)
    turtle.right(90)
drawGrids(row_grid,column_grid)

    # draw grid function is called w/ parameters
    # drawGrids(row_grid,column_grid)
