# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY

def add(a, b):
    return a + b

print(add(1, 3))

def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
        print(total)
    return total

print(multiply(1, 2, 3))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Reece", "Tunesi")
print("")

def print_address(**kwargs):
    for value in kwargs.values():
        print(value)

print_address(street="Test Street", 
              city="London", 
              county="Surrey", 
              postcode="LA12 1PL")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="Test Street", 
              city="London", 
              county="Surrey", 
              postcode="LA12 1PL") 