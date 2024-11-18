# 2D = A list made up of lists

fruits = ["apple", "orange", "pear"]
vegetables = ["lettuce", "potatoes", "carrots"]
meats = ["chicken", "fish", "beef"]

groceries = [fruits, vegetables, meats]

print(groceries)
print(groceries[0])             # Displays the first list within the list
print(groceries[0][0])          # Displays the first value in the first list within the list

geography = [["London", "Manchester", "Surrey"], 
             ["England", "Wales", "Scotland"],
             ["United Kingdom", "United States", "Japan"]]

print(geography)

for lst in geography:
    for value in lst:
        print(value, end=" ")
    print()