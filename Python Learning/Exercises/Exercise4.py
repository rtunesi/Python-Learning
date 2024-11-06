# Exercise 4: Weight Convertor

print("Welcome to my python weight convertor program.")

weight = float(input("Enter your weight. \n>: "))
unit = input("Kilograms or Pounds? (K/P) \n>: ")
unit = unit.upper()

if unit == "K":
    converted = weight * 2.205
    unit = "Lbs."
elif unit =="P":
    converted = weight / 2.205
    unit = "Kgs."
else:
    print("Sorry I don't recognise the weight type.")

print(f"Your weight is: {converted} {unit}")