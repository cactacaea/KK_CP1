# KK 2nd Rock, Paper, Scissors Practice

start = '\033[1m'
end = '\033[0m'

print("Greetings.\nType 'q' to stop playing")
choice_list = ["rock","paper","scissors"]
computer_points = 0
player_points = 0

while True:
    choice = input(f"\n{start}Rock: 'r'\nPaper: 'p'\nScissors: 's'{end}\nWhat would you like to play?:\n").strip().lower()
    if choice == "q":
        print("\nThanks for playing!")
        break
    elif choice == "r":
        print()
    elif choice == "p":
        print()
    elif choice == "s":
        print()
    else:
        print("\nInvalid choice! Please try again")