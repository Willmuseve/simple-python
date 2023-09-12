# A python program that prints the smallest value in a list
# Prints none if the dictionary is empty

MyDict = {"a" : 3, "b" : 9, "c" : 15}

if MyDict:
    min_value = min(set(MyDict.values())) # the values() method returns all values whci are cast into a set and then the min function extracts the minimum value
    print(min_value)
else:
    print("None")