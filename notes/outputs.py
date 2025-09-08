# KK 2nd Formatting Outputs Notes

name = ("Bobby")
age = 21
grade = .75
money = 25

#print(f"Hello {name}! Nice to meet you; {age} is really old!")
print("Hello {}! Nice to meet you; {:b} is really old! You have a {:%} in this class. You also have ${:.2f}, that's a lot of money!".format(name, age, grade, money))

print(f"Hello {name}! Nice to meet you; {age:b} is really old! You have a {grade:%} in this class. You also have ${money:.2f}, that's a lot of money!")




