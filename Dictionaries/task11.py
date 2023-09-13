# A python program that sorts the list contained as values in a dictionary in ascenfnding order
# The dictionary contains the key value pairs that match strings to the sorted list

myDict = {
    "a" : [2, 1, -4, 5, 0],
    "b" : [3, 10, 91, 80, 22],
    "c" : [1000, 987, 2087, 2100]
}

for list_value in myDict.values():
    list_value = list_value.sort()
print(myDict)