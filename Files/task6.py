# A program that writes the elements of a list to a file denoted by
# Each element written on separate lines
# Prints to a new file or updates an existing one

file_path = "../file/file7.txt"

MyList = [1, 2, 3, 4, 5]

with open(file_path, "w") as file:
    for i in MyList:
        file.write(str(i) + "\n")