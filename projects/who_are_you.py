# KK 2nd Who Are You

saved_names=[]
name = input("What's your name?:\n\n").capitalize().strip()
age = input("How old are you?:\n")
color = input("Lastly, what's your favourite color?:\n")
if name in saved_names:
   print(f"Welcome back, {name}!")
else:
    print(f"You are {age} years old and your favourite color is {color}, {name}!")
saved_names.append(name)
    









