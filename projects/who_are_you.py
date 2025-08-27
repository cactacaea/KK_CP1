# KK 2nd Who Are You

while True:
    saved_names=[]
    name = input("What's your name?:\n").capitalize().strip()
    
    if name in saved_names:
        print(f"Welcome back, {name}!")
    else:
        age = input("How old are you?:\n")
        color = input("Lastly, what's your favourite color?:\n")
        print(f"You are {age} years old and your favourite color is {color}, {name}!")
    saved_names.append(name)

    cont = input("\nWould you like to continue?:\n")
    if cont != "yes":
        break
