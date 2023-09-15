# A program that rrads a text file and saves it's contents line by line to a list called file_content
# List contains strings that represent each line of a text

file_path = "../file/file1.txt"

list_file = []

with open(file_path) as file:
    for line in file:
        list_file.append(line)

print(list_file)