# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

first_name = "Reece"                        # String Variable
print(first_name)

number = 80                                 # Integer Variable
print(number)

flo = 3.5                                   # Float Variable
print(flo)

statement = True                            # Boolean Variable
print(statement)

last_name = "Tunesi"
print(f"My last name is {last_name}")       # Format printing

# Personal project
# 

user_name = "rTunesi"
passcode = 4329
score = 50.5
is_admin = True

print(f"Welcome to the program, your username is {user_name} and your passcode is {passcode}")
print(f"You managed to score a {score} on our system")

if is_admin == True:
    print("You have now been granted admin access.")
else:
    print("Unfortunately due to your low score you haven't been granted admin access.")