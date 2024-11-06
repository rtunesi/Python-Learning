# Exercise 5: Temperature Conversion

print("Welcome to my python temperature conversion program.")

unit = input("Is this temperaturein Celsius or Fahrenheit (C/F)? \n>: ")
unit = unit.upper()
temp = float(input("Enter the temperature. \n>: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}")
else:
    print(f"{unit} is an invalid unit of measurement.")