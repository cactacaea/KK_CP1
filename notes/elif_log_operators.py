# KK 2nd Logical Operators and Elif Notes

homework = False
chores = True
room = True

# all conditions must be true for the condition to happen
if homework and chores and room:
    print("You can go to your friends house.")
# one condition must be true
elif not chores or not room:
    print("Do your chores and clean your room.")
else:
    print("Go do your homework!!")

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "LaRose":
    if password == "1234":
        print("Welcome, Ms. LaRose")
    else:
        print("Incorrect Login")
elif username == "cactacaea" and password == "Password":
    pass

elif username == "Andrew" and password == "orange":
    print("Welcome, Andrew")
else:
    print("Invalid sign-in")