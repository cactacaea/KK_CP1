# KK 2nd Fix the Game Practice

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    # not major but the user should know the input should be an integer
    print("I'm thinking of an integer between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        # LOGIC, input must be coverted to a number (one way or another)
        guess = int(input("Enter your guess: "))
        # LOGIC, the attempt number isn't counted
        attempts += 1
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        # LOGIC, it would print when the condition is met but also print whether or not the number was higher/lower
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        # continue isn't necessary is a while loop
        
    print("Game Over. Thanks for playing!")
start_game()