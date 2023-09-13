# A python program that prints the largest sum of the values in a dict
# Values in the dict are lists or tuples

MyDict = {
    "a" : [2, 4, 6],
    "b" : [7, 6, -5],
    "c" : [9, 7, 10],
}

MaxSum = None

for list_values in MyDict.values():
    totalsum = sum(list_values)

    if MaxSum == None:
        MaxSum = totalsum
    else:
        if MaxSum < totalsum:
            MaxSum = totalsum
print(MaxSum)