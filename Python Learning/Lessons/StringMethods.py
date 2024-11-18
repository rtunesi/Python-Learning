name = input("Enter your full name. \n>: ")

name_length = len(name)                # Finds the length of the string
print(name_length)

spaces = name.find("e")                # Finds the first occurance
result = name.rfind("e")               # Finds the last occurance
print(spaces)

name = name.capitalize()               # Capitalises the first letter
print(name)

name = name.upper()                    # Capitalises the entire string
print(name)

name = name.lower()                    # Converts the entire string to lowercase
print(name)

result = name.isdigit()                # Sees if the entire string is digits
print(result)                          # If yes returns True else False

result = name.isalpha()                # Sees if the entire string only containes letters
print(result)                          # If yes returns True else False

