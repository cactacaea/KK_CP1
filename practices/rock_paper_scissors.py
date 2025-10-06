# KK 2nd Rock, Paper, Scissors Practice

import random

start = '\033[1m'
end = '\033[0m'

print("Greetings.\nType 'q' to stop playing, and 'score' to show game points.\n\nRock: 'rock'\nPaper: 'paper'\nScissors: 'scissors'")
choice_list = ["rock","paper","scissors"]
aligned_choices = [1,2,3]
computer_points = 0
player_points = 0
total_score = (f"{start}PLAYER SCORE: {player_points}\nCOMPUTER SCORE: {computer_points}{end}")
# combine = list(zip(choice_list, aligned_choices))
# print(combine)

while True:
    computer_choice = random.choice(choice_list)
    choice = input(f"\nWhat would you like to play?:\n").strip().lower()
    if choice == "q":
        print("\nThanks for playing!")
        break
    elif choice == "score":
        print(f"\n{total_score}")
    # ROCK
    elif choice == "rock":
        if computer_choice == "rock":
            print(f"\nThe computer played {computer_choice}! {start}Tie.{end}")

        elif computer_choice == "paper":
            print(f"\nThe computer played {computer_choice}! {start}Paper covers rock; you lost..{end}")
            computer_points +=1

        elif computer_choice == "scissors":
            print(f"\nThe computer played {computer_choice}! {start}Rock crushes scissors! You won!{end}")
            player_points += 1

    # PAPER
    elif choice == "paper":
        if computer_choice == "rock":
            print(f"\nThe computer played {computer_choice}! {start}You won!{end}")
            player_points += 1
            
        elif computer_choice == "paper":
            print(f"\nThe computer played {computer_choice}! {start}Tie.{end}")

        elif computer_choice == "scissors":
            print(f"\nThe computer played {computer_choice}! {start}Scissors cuts paper; you lost..{end}")
            computer_points += 1
    
    # SCISSORS
    elif choice == "scissors":
        if computer_choice == "rock":
            print(f"\nThe computer played {computer_choice}! {start}Rock broke scissors; you lost.{end}")
            computer_points += 1

        elif computer_choice == "paper":
            print(f"\nThe computer played {computer_choice}! {start}Scissors cuts paper; you won!{end}")
            player_points +=1

        elif computer_choice == "scissors":
            print(f"\nThe computer played {computer_choice}! {start}Tie.{end}")
    # other choices
    else:
        print("\nInvalid choice! Please try again")