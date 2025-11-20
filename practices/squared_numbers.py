# KK 2nd, Squared Numbers // Practice

# list for numbers to square
numbers = [2,3,4,5,9,10,16,20,25,30,50,65,70,85,90,105,110,125,130,190,200]

# lambda function giving a num variable that gets squared taking numbers from a list with map
squared_nums = list(map(lambda num: num**2, numbers))

# for loop w/ enumerate so index/values to be taken
for i,num in enumerate(numbers):
    print(f"{num} squared is: {squared_nums[i]}")