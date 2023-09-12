# A python program that prints the second smallest value in a list
# Prints none if the list ios empty

MyList = [21, 9, 21, 10, 27]

if len(MyList) > 1:
    MyList_sorted = sorted(MyList)
    print(MyList_sorted[1])


