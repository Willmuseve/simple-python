# A python program that prints the frequency of each value in a dictionary
# The programs output is a new dictionary with the value as it's key and te frequency as it'svalue


MyDict = {"a" : 6, "b" : 3, "c" : 4, "d" : 4, "e" : 6, "f" : 4}

NewDict = {}

for value in MyDict.values(): # Using a forloop toloop through each value with the values method
    if value in NewDict:
        NewDict[value] +=1 # if the value is already in the new dict, increment it's frequency by one
    else:
        NewDict[value] = 1 # else it's initialised to one
print(NewDict)