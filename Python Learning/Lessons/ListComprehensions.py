# list comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [Expression for value in iterable if condition]

doubles = []
for x in range(1, 11):
    doubles.append(x)

print(doubles)

doubles = [x * 2 for x in range(1, 11)]
print(doubles)
triples = [y * 3 for y in range(1, 11)]
print(triples)
squares = [z * z for z in range(1,11)]
print(squares)

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)
first_letter = [fruit[0] for fruit in fruits]
print(first_letter)

numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)
negative_nums = [num for num in numbers if num < 0]
print(negative_nums)
even_nums = [num for num in numbers ]