# nested loops = The "inner loop" will finish all of it's iterations before
#                finishing one iteration of the "outer loop"

rows = int(input("Enter the number of rows. \n>: "))
columns = int(input("Enter the number of columns. \n>: "))
symbol = input("Enter a symbol to use. \n>: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()