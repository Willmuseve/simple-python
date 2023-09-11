# A pythonn program that prints the elements of List A that are not present in List B as a list(difference)
# prints empty list if the lists have the same elements
# prints empty list if list A has empty list

listA = [1, 2, 3, 4, 3]
listB = [1, 2]

diff = []

for i in listA:
    if i not in listB:
        diff.append(i)
print(diff)