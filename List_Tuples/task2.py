# python program that prints the elements of a list on the same line without a comm
# Elements should be separated by space and not comma
# Output should not include opening and closing [] brackets


#Method 1
print("Method 1:")
MyList = [1, 2, 3, 4, 5] # Initialize the list

for i in MyList: # Looop through the list to get individual elements and print them with space as the EOF character
    print(i, end= " " )

print("\n") # new line

#Method 2:
print("Methos 2:")

MyList2 = [6, 7, 8, 9, 10] # initialize the list
print(*MyList2, sep = " ")
