# Exercise 6: Validate User Inputs

# 1. Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

print("Welcome to my python: validate user inputs program")

username = input("Please enter your username. \n>: ")

leng = len(username)
nodigits = username.isalpha()
nospaces = username.find(" ")

if leng <= 12 and nodigits and nospaces <= 0:
    print(f"The username: {username} is valid.")
else:
    print(f"The username: {username} isn't valid")