# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It's hot outside")
    print("It's sunny.")
elif temp <= 0 and is_sunny:
    print("It's cold outside")
    print("It's sunny.")
elif 28 > temp > 0 and is_sunny:
    print("It's warm outside")
    print("It's sunny.")
else:
    print("It's cold outside")
    print("It's cloudy.")