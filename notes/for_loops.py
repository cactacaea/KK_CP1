# KK 2nd For Loops Notes

import time

nums = [6,51,61,94,351,946,5489,4,654,684]

for num in nums:
    div = num/2
    if div > 100:
        print(f"{div} is half of {num}, and it's still a large number!")
    else:
        print(num)
print("We completed all of the numbers.")
time.sleep(3)

print("Counting from 1 to 9 inclusive:")
for x in range(1,10):
    print(x)
    time.sleep(1)
time.sleep(3)

print("Counting by 2s:")
for x in range(2,11,2):
    print(x)
    time.sleep(1)
time.sleep(3)

print("Counting down:")
for x in range(10,0,-1):
    print(x)
    time.sleep(1)
time.sleep(1)
print("Finished Running.")