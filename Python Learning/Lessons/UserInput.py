# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("Please enter your name \n>: ")                # Getting the users input
age = int(input("Please enter your age \n>: "))             # Change input data type to Int 

age += 1

print(f"So your name is: {name}")
print(f"And if you added one to your age you'd be: {age}")