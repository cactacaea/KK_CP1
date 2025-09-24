# KK 2nd User Sign In Practice

# user = input("Please choose a username:\n")
# password = input("Please choose a password:\n")
# users = [["LaRose","abcd"],["cactus","password"],[["cactacaea"],["123"]]]

# while True:
#     user_checker = input("Please re-enter a username:\n")
#     if user_checker in users or user:
#         password_checker = input("Please re-enter the password:\n")
#         if password_checker in users or password:
#             print(f"Welcome, {user}!\n")
#             continue
#         else:
#             print("Password is invalid; please try again\n")
#     else:
#         print("Username is invalid; please try again")

user = input("Please choose a username:\n")
password = input("Please choose a password:\n")
print("Thank you.")
usr_checker = input("Re-enter your username to sign in:\n")
if usr_checker == user:
    pass_checker = input("Re-enter your password to sign in:\n")
    if pass_checker == password:
        print(f"Welcome, {user}!")
    else:
        print("Incorrect password, please try again.")
else:
    print("Incorrect username, please try again.")