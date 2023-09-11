# A python program that multiplies all items of a list by the value of the variable F
# prints the list as the output
# can multiply the value of F by a string is the list contains a string
# Value of f is a positive integer

#Method 1
print("Method 1:")

MyList = [2, 3, 4, 5] # initialize the list
f = 2

for i in range(len(MyList)): #loop throug the elements of the list
    MyList[i] *= f # multiply through each element by the value of f
print(MyList, "\n") 



#Method 2:
print("Method 2:")

MyList2 = ['a', 7, 8, 9]
g = 3

for i, it in enumerate(MyList2):
    MyList2[i] = it * g

print(MyList2)