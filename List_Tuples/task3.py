# A python script that prints the largest and smallest elements in a list on the same line
# the largest and smallest line should be separated on the same line and separated by commas
# All the elements are numeric
# Largest element should appear first then smallst last
# Prints none when the script is empty

MyList = [] # define a list

if MyList: # condition to check if the list is empty
    print(max(MyList), min(MyList))
else:
    print("None")