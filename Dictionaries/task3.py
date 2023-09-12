# A python progrm that mmerges two dictionaries

dict1 = {'a' : 1, "c" : 3, "f" : 6, "g" : 7}  # inititalize the dictionaries
dict2 = {"b" : 2, "d" : 4, "e" : 5, "g" : 4}

newDict = dict1 | dict2 # use the vertical bar which is a python operator that merges the dictionary

print(newDict)