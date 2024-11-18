# while loop = A statement that will execute it's block of code
#              as long as it's condition remains true.

name = ""

while len(name) == 0:
    name = input("Please enter your name. \n>: ")

print(f"Hello {name}")

# Another way to code the above is found below
# name = None
# while not name:
#   name = input()