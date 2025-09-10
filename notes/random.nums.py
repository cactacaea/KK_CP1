# KK 2nd Random Numbers Notes

import random

# random number examples
print(random.random()) # floats between 0 and 1
print(random.randint(0,100)) # integers between the stated arguments (0 and 100 inclusive in this case)

name = input("What's your name?:\n").strip().title()

# random D&D statistic creator
stat_one = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_two = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_three = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_four = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_five = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_six = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_seven = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

print(f"Your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")
strength = int(input("What stat are you making your strength?:\n")) + 2
