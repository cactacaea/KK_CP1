import turtle

nested_list = [[1, 2, 3], ['a', 'b'], [True, False, None]]

for sublist in nested_list:
    for item in sublist:
        turtle.forward(20)
        turtle.backward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.left(90)