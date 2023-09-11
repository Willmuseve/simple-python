# A python program that prints the second largest value in a list
# prints none if the list is empty or has only one element


#Method 1
print("Method 1:")
MyList = [1, 2, 3, 4, 5, 6] #initialize the list

if len(MyList) > 1:
    MyList_sorted = sorted(MyList)
else:
    print("None")

print(MyList_sorted[-2])
print("\n")

