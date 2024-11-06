# Exercise 2: Shopping Cart Program

print("Welcome to the shopping cart program")

item = input("What item would you like to purchase? \n>: ")
price = float(input("What is the price of the item? \n>: "))
quantity = int(input("How many of this item would you like to purchase? \n>: "))

total_amount = price * quantity

print(f"You have brought {quantity} x {item}")
print(f"The total amount for this purchase is: £{total_amount}")