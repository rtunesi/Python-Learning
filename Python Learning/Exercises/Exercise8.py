# Excerise 8: Quiz Game

questions = ("What is the capital of France?: ",
             "What is 2 + 2?: ",
             "What color are bananas?: ",
             "How many days are in a week?: ",
             "What is the largest planet in our solar system?: ")

options = (("A. Paris", "B. London", "C. Dublin"), 
           ("A. 5", "B. 3", "C. 4"), 
           ("A. Orange", "B. Yellow", "C. Red"), 
           ("A. 7", "B. 6", "C. 5"), 
           ("A. Jupiter", "B. Mars", "C. Earth"))

answers = ("A", "C", "B", "A", "A")
guesses = []
score = 0
question_num = 0

print("Welcome to my python: quiz game program")

for question in questions:
    print("-----------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("You have completed the quiz.")
print(f"Your final score is: {score}")