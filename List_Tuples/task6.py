# A python program that removes an element from a list
# Output is the new list without the removed element
# If the element is not found in the list then the output  should be not found
# If the list is empty should print empty list

#Method 1
print("Method 1:")
MyList = [1, 2, 3, 4, 5] # initialize the list
rem = 4 # Element to be removed

if len(MyList) == 0: # check if the list is empty
    print("List is empty")
elif MyList.count(rem) == 0: # Check of the list has the number to be removed
    print("Number not found")
else:
    for i in range(MyList.count(rem)): # checks the number of occurencec of the number to be removed and removes
        MyList.remove(rem)

print(MyList)

print("\n")


