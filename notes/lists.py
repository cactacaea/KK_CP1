# KK 2nd Lists Notes

import random

names = ["Alex", "Katie", "Cora", "Andrew", "Jake", "Erika", 3.14, 5, "stuff"]
print(names)
print(names[3]) # andrew
print(names[random.randint(1,len(names))])
print(random.choice(names))
names[-1] = "Xavier"
names.extend(["Treyson", "Tia"])
names += ["Bobby", "Vienna","Zee"]
names.remove(3.14)
names.pop(6)
print(names)
names.insert(3, "Kris")

print(names)

board = [[1,2,3],
         [4,5,6],
         [7,8,9]]
board[1][1] = "x"
print(board)
# List // Changable, ordered
# Tuple // Unchangable, ordered
classes = ("Bard", "Monk", "Barbarian", "Paladdin")
# Set // Changable, unordered
fruits = {"Apple", "Orange", "Strawberry", "Kiwi"}
print(fruits)
