# Exercise 10: Random Number Guessing Game

import random

computer_number = random.randint(1, 100)
user_guess = 0
guess_count = 0 

print("Welcome to my python: random number guessing program.")

while True:
    if user_guess != computer_number:
        print("Please enter a number between 1-100")
        user_guess = int(input(">: "))
        if user_guess > computer_number:
            print("The number is lower, try again.")
            guess_count += 1
        else:
            print("The number is higher, try again.")
            guess_count += 1
    else:
        print(f"Correct! The generated number was {computer_number}")
        print(f"Your total number of guesses was: {guess_count}")
        break