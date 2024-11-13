# iterables = An object/collection that can return its elements one at a time
#             allowing it to be iterated over in a loop.

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

for item in reversed(numbers):
    print(item, end=" - ")

numbers = (1, 2, 3, 4, 5)

for num in numbers:
    print(num)

fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit)

name = "oniJal"

for character in name:
    print(character, end=" ")
print("")

my_dictionary = {"A": 1,
                 "B": 2,
                 "C": 3,}

for key in my_dictionary:
    print(key)

for value in my_dictionary.values():
    print(value)

for key, value in my_dictionary.items():
    print(key, value)