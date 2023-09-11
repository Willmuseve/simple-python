# A python program that removes duplicate elements from a list only keeping one occurence of the elements
# Original list is modified
# Final version of the list is printed

#Method 1
print("Method 1:")

MyList = [1, 1, 2, 3, 4, 5 ,3, 5, 6, 6] # initialize the list
rem_duplicate = list(set(MyList))# the set data structure removes duplicates in Mylist and then passes it to list function which turns it to a list
print(rem_duplicate)
print("\n")

# Method 2
print("Method 2:")
MyList2 = [1, 2, 1, 3, 3, 4, 5, 6, 6, 7, ] # initialize the list
rem_duplicate2 = list(dict.fromkeys(MyList2)) # unlike set the dict function keeps the order of the list but as a dictionary then it passes it to list fucntion which turns it into a list
print(rem_duplicate2)