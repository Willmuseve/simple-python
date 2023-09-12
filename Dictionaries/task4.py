# A python program that checks if all the values in a dictionary are equal
# If equal prints true else false
# If the dictionary is empty print empty

MyDict = {"a" : 7, "b" : 7, "c" : 5, "d" : 5, "e" : 4, "f" : 4}

uniq_values = len(set(MyDict.values()))

if uniq_values == 0:
    print("Empty")
elif uniq_values > 0:
    print("True")
else:
    print("False")
