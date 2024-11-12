# Exercise 11: Rock Paper Scissors Game

import random

print("Welcome to my python: rock, paper, scissors program.")

options = ("rock", "paper", "scissors")
score = 0
running = True

while running:

    player = None
    computer_choice = random.choice(options)
    print(computer_choice)

    while player not in options:
        player = input("Please choose your option rock paper or scissors. \n>: ").lower()
        
    print(f"Player: {player}")
    print(f"Computer: {computer_choice}")

    if player == computer_choice:
        print("It's a tie!")
    elif player == "rock" and computer_choice == "scissors":
        print("You win!")
        score += 1
    elif player == "paper" and computer_choice == "rock":
        print("You win!")
        score += 1
    elif player == "scissors" and computer_choice == "paper":
        print("You win!")
        score += 1
    else:
        print("You lose")

    play_again = input("Play again? (y,n). \n>: ").lower()
    if play_again == "n":
        break


print(f"Your final score was: {score}")
    
