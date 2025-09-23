# KK 2nd User Sign In Practice

while True:
    user = input("Please choose a username:\n")
    password = input("Please choose a password:\n")
    users = [["LaRose","programmer246"],["cactus","18passwords"],[["cactacaea"],["123"]]]

    user_checker = input("Please re-enter a username:\n")
    if user_checker in users:
        continue
    else:
        print("Username is invalid; please try again\n")
    password_checker = input("Please re-enter the password:\n")
    if password_checker in users:
        print(f"Welcome, {user}!\n")
    else:
        print("Password is invalid; please try again")