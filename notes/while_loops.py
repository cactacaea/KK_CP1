# KK 2nd While Loops Notes

import time
import random

# infinite loop
num = 0
break_point = random.randint(1,30)
print(f"Breakpoint: {break_point}\n")
while num < 20:
    num += 1 # fixes the infinite loop!
    if num == break_point:
        break
    # even #s num%2 == 0
    elif num%2 != 0:
        continue
    print(num)
    time.sleep(.15)
    
else:
    print("The loop exited by meeting the condition.")

print("The loop is over.")