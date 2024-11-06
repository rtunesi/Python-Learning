# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

num = -1
print("Positive" if num > 0 else "Negative")

num = 6
result = "Even" if num % 2 == 0 else "Odd"
print(result)

a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)

age = 25
status = "Adult" if age >= 18 else "Child"
print(status)

user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)