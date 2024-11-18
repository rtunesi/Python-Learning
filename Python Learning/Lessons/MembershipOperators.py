# membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set or dictionary)
#                        1. in 2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word. \n>: ").upper()

if letter in word:
    print(f"There is a {letter} in the secret word.")
else:
    print(f"{letter} was not found.")

if letter not in word:
    print(f"{letter} was not found.")
else:
    print(f"There is a {letter} in the secret word.")


students = {"Reece", "Sergei", "Laura"}

student = input("Please enter the name of a student. \n>: ")

if student in students:
    print(f"{student} is in the set.")
else:
    print(f"{student} was not found.")

grades = {"Reece": "B",
          "Laura": "A",
          "Sergei": "B"}

student = input("Please enter the name of a student. \n>: ")

if student in grades:
    print(f"{student}'s grade is: {grades[student]}")
else:
    print(f"{student} was not found.")