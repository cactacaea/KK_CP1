# KK 2nd Tic Tac Toe Practice

# import random module

# nested list variable for tic tac toe board (board = [[0,1,2],
#                                                      [0,1,2],
#                                                      [0,1,2]])

# display greeting

# main game loop
# while True
    # slot input asking what spot the player wants to play in
    # check for x or o in nested list
    # if the slot is open(doesn't have x or o)
        # player input asking for x, converting to lowercase
        # computer uses random.choice() inside each list to pick one spot
        # numbers are replaced using .replace() (function) with player and computer inputs
    # else/otherwise
        # ask user to choose a different spot until they enter something valid

    # WINNING CONDITIONS
    # if each x value in each list aligns vertically; board[1][1]
        # display win for user
    # otherwise if each x value aligns horizontally
        # display win for user
    # otherwise if each x value aligns any other way/diagonally
        # display user win
    # otherwise if each x value aligns in another diagonal
    # SAME THING FOR COMPUTER WINS
    # otherwise each o value in each list aligns vertically; board[1][1]
        # display win for computer
    # otherwise if each o value aligns horizontally
        # display win for computer
    # otherwise if each o value aligns any other way/diagonally
        # display computer win
    # otherwise if each o value aligns in another diagonal
    # TIE
    # otherwise the board fills up (is replaced with Xs/Os)
        #display tie
    # ELSE continue the code which asks for slot inputs



