# if = Do some code only IF some condition is True.
#      Else do something else.

age = int(input("Enter your age. \n>: "))

if age >= 18:
    print("You can apply for a credit card.")
else:
    print("Sorry but you cannot apply for a credit card.")

response = input("Are you hungry? (Y/N) \n>: ")
response = response.upper()

if response == "Y":
    print("Please get some food.")
elif response == "N":
    print("I'm glad you're satisfied.")
else:
    print("Sorry I didn't understand your input.")

for_sale = True

if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")