# KK 2nd Multiplication Table Practice

import time

base = int(input("What base would you like to use for your multiplication table? Ex; 12:\n"))
print(f"Multiplication Chart: {base}x{base}\n")
time.sleep(1)

for num in range(1,base+1):
    for another in range(1,base+1):
        print(f"{num*another}".center(4), end="\t")
    print()
