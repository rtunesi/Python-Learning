# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates.

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow",
            "England": "London"}

print(capitals.get("USA"))                  # Prints value assigned to the KEY (USA)
print(capitals.get("India"))

if capitals.get("Japan"):                   # Checks to see if the KEY exists
    print("That capital exists")
else:
    print("That capital doesn't exist")

if capitals.get("Russia"):
    print("That capital does exist")
else:
    print("That captial doesn't exist")

capitals.update({"Japan": "Tokyo"})         # Inserts/Updates a key value pair
capitals.update({"USA": "Detroit"})
print(capitals)

capitals.pop("China")                       # Removes the selected key value pair
capitals.popitem                            # Removes the latest key value pair
print(capitals)

keys = capitals.keys()                      # Gets all the keys within the dictionary
print(keys)

for key in capitals.keys():
    print(key)

values = capitals.values()                  # Gets all the values within the dictionary
print(values)

for value in capitals.values():
    print(value)

items = capitals.items()
print(items)
for key, value in capitals.items():
    print(f"{key}: {value}")

capitals.clear()                            # Clears the dictionary
print(capitals)