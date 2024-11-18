# collections = single "Variable" used to store multiple values.
# list        = [] ordered and changeable. Duplicates OK.
# Set         = {} Unordered and immutable, but Add/Remove OK. NO duplicates.
# Tuple       = () Ordered and unchangeable. Duplicates OK. FASTER.

fruits = ["apple", "orange", "pear"]

print(fruits)
print(fruits[1])
print(fruits[:3])
print(fruits[::-1])             # Reverses the list
print(len(fruits))              # Prints length of the list
print("apple" in fruits)        # Find if a value is in the list

for fruit in fruits:
    print(fruit)

fruits[0] = "pineapple"         # Changes the first value in the list
print(fruits)

fruits.append("apple")          # Adds an element to the END of the list
print(fruits)

fruits.remove("apple")          # Removes the selected element
print(fruits)

fruits.insert(0, "apple")       # Adds an element to the selected order of the list
fruits.sort()                   # Sorts the list in alphebetical order
fruits.reverse()                # Reverses the list
print(fruits.index("apple"))    # Prints the index of the desired element  
print(fruits.count("apple"))    # Prints how much of the element are in the list         
fruits.clear()                  # Clears the list
