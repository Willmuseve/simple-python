# A Python program that prints a "flattened" version of a list that contains nested lists
# prints an empty list if the list is empty

MyList  = [2, [3, 5, 7], [9, 7, 0], 3, 5]

f_list = []

for element in MyList:
    if isinstance(element, list):
        for nested_element in element:
            f_list.append(nested_element)
    else:
        f_list.append(element)

print(f_list)