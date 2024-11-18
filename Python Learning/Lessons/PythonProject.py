# Goal: Find out if an array has a duplicate value.
# Return TRUE if it does, FALSE if it doesn't.

import random

# Creating the varibles
r_list = []
total = 10

duplicates = []
seen = set()

# Generate a random list
for i in range(total):
    r_list.append(random.randint(1, 9))
    
print(r_list)

# Check if the list has duplicates
for item in r_list:
    if item in seen:
        duplicates.append(item)
    else:
        seen.add(item)

print(duplicates)