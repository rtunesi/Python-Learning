# Exercise 3: Python Calculator

print("Welcome to my python calculator program.")

operator = input("Please enter the operator you would like to use (+, -, *, /) \n>: ")
num1 = float(input("Please enter your first value. \n>: "))
num2 = float(input("Please enter your second value. \n>: "))

if operator == "+":
    total = num1 + num2
    print(f"Your final calculation was: {total}")
elif operator == "-":
    total = num1 - num2
    print(f"Your final calculation was: {total}")
elif operator == "*":
    total = num1 * num2
    print(f"Your final calculation was: {total}")
elif operator == "/":
    total = num1 / num2
    print(f"Your final calculation was: {total}")
else:
    print("Sorry I don't recognise the operator you inputed")