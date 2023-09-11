# A python program that creates and prints a dictionary that maps each element in a list to it's corresponding frequency
# Case sensitive

MyList = ["a", "c", "c", "d", "a"]

Mydict = {}

for i in MyList:
    if i not in Mydict:
        Mydict[i] = 1
    else:
        Mydict[i] += 1
print(Mydict)