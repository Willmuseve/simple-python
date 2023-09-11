# A python program that counts the number of elements in a list with value greater that 4
#  List contains numbers only

# Method 1
print("Method 1:")
MyList = [2, 6, 1, 4, 7, 9]  # initilize the list
counter = 0 # variable counter to countthe number greater than 4

for i in range(len(MyList)): # Loop through the elements in the list to count numbers greater than f4
    if MyList[i] > 4:
        counter +=1
print(counter)