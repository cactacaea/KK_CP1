# KK 2nd, Mapping // Notes

numbers = [832,40,8234,324,8,2749,82,1,929,80,3,1,]
"""divided = []

for num in numbers:
    divided.append(num/2)"""

# def divide(number):
#     return number/2

divided = list(map(lambda num: num/2, numbers))

print(divided)

for i,num in enumerate(numbers):
    print(f"{num} divided by 2 is {divided[i]}")