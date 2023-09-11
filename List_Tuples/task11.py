# A python program that prints a list with elelents that listA and listB have in common
# prints an empty list if they dont have anything in common

listA = [1, 2, 3, 4, 5]
listB = [3, 4, 5, 6]

c_elements = []

for i in listA:
    if i in listB:
        c_elements.append(i)
print(c_elements)