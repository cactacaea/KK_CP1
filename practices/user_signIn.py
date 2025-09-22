# KK 2nd User Sign In Practice

users = [["LaRose","programmer246"],["cactus","18passwords"]]
while True:
    user = input("Please choose a new username:\n")
    password = input("Please choose a password:\n")
    saved_users = []
    saved_passwords = []
    saved_users.append(user)
    saved_passwords.append(password)

    user_checker = input("Please re-enter your username:\n")
    if user_checker in saved_users:
        continue
    else:
        print("Username is invalid; please try again\n")
    password_checker = input("Please re-enter your password:\n")
    if password_checker in saved_passwords:
        print(f"Welcome, {user}!\n")
    else:
        print("Password is invalid; please try again")