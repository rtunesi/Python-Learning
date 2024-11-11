# Excerise 9: Concession Stand Program

menu = {"popcorn": 1.00,
        "hot dog": 2.00,
        "pretzel": 2.50,
        "haribos": 1.50,
        "drink": 1.00,
        "water": 0.50}

cart = []
total = 0

print("Welcome to my python: concession stand program")

print("Please find all available items below")
print("-------- MENU --------")
for key, value in menu.items():
    print(f"{key:10}: £{value}")
print("----------------------")

while True:
    food = input("Select an item from the menu above (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total purchase amounts to: £{total}")