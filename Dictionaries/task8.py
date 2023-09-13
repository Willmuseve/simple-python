# A py program tht creates a dictionary from nested list
# Each nested list has he format [value1, value2]
# The dictionary takes value 1 as the key and value 2 as it's corresponsing value
# Prints an empty list if the dictionary is empty

MyList = [["a", 1], ["b", 2], ["c", 3], ["d", 4], ["e", 5]]
MyDict = {}

if not MyList:
    print("The list is empty")
else:
    for nested_list in MyList:
        key = nested_list[0]
        value  = nested_list[1]
        MyDict[key] = value

    print(MyDict)