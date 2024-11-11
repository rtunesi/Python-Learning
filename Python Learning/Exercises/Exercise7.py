# Exercise 7: Shopping Cart Program

foods = []
prices = []
total = 0

print("Welcome to the shopping cart program.")

while True:
    food = input("Enter a food item you would like to buy. (q to quit). \n>: ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"Enter the price of {food}. \n>: "))
        prices.append(price)

print("---- YOUR SHOPPING CART ----")
for food in foods:
    print(food)

for price in prices:
    total += price

print(f"Your total bill is: £{total}.")