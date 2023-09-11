# A python program that prints the elements of a list followed by their indices
# Each element and it's corresponding indices must be on the same line separated by space
# Prints empty if list is empty

# Method 1
print("Method 1:")
MyList = [2, 3, 0, 21, 12, 11]


if len(MyList) == 0:
    print("List is empty")
else:
    for i, j in enumerate( MyList):
        print(j, i)

print("\n")

#Method 2
print("Method 2:")
MyList2 = [1, 5, 78, 103, 2]

if not MyList2:
    print("List is empty")
else:
    for j in range(len(MyList2)):
        print(MyList2[j], j)