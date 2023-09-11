# A python program that checks if the list is empty
# If the list is not empty prints empty, else print not empty


# Method 1
print("Method 1:")
MyList = [1, 2, 3, 4, 5, 10]

if MyList:
    print("Not empty")
else:
    print("Empty")

print("\n")

 #Method 2
print("Method 2:")
MyList2 = [3, 4, 5]

if len(MyList2) == 0:
    print("Empty")
else:
    print("Not empty")

print("\n")

# Method 3
print("Method 3:")
MyList3 = []

if not MyList3:
    print("List 3 is Empty")
else:
    print("List 3 not Empty")
