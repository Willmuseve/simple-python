# A python program that prints the largets value in a dictionary
# If the dictionary is empty print none

MyDict = {"a" : 3, "b" : 9, "c" : 15}

if MyDict:
    max_value = max(set(MyDict.values()))
    print(max_value)
else:
    print("None")