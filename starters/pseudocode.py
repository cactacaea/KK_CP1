# KK 2nd Pseudocode Splitup

import random

while True:
    board = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    print(board, end=" ")
    comp_choice = random.randint(1,9)
    player_choice = int(input("\nPlease choose a number open on the board:\n"))
    