# function = A block of reusable code
#            place () after the function name to invoke it

def happy_birthday(name):
    print(f"Happy birthday to {name}!")
    print("You are old!")
    print("Happy birthday to you!")

happy_birthday("Reece")
happy_birthday("Steve")
happy_birthday("Sergei")

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of £{amount:.2f} is due: {due_date}")

display_invoice("Reece", 45.99, "01/11/2024")

# return = statement used to end a function
#          send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(4, 2))
print(multiply(4, 9))
print(divide(9, 3))