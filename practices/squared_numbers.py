# KK 2nd, Squared Numbers // Practice

import math

# list for numbers to square
numbers = [2,3,4,5,9,10,16,20,25,30,50,65,70,85,90,105,110,125,130,190,200]
# lambda function giving a num variable that gets squared taking numbers from a list with map
squared_nums = list(map(lambda num: {pow(num,2)}), numbers)
print(squared_nums)