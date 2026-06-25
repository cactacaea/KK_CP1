# num = int(input("Pick an integer: "))

# board = []
# for i in range(num):
#     board.append([])
#     for x in range(num):
#         board[i].append((i + x) % 2)
#     print(board[-1])

num = 5

board = []
for i in range(num):
    board.append([])
    for x in range(num):
        board[i].append("x")
    print(board[-1])