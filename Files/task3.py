# A program that prints the last n lines of a file in order

file_path = "../file/file4.txt"

n = int(input("Enter the last number of lines to read: "))

with open(file_path) as file:
    lines = file.readlines()
    line_list = len(lines)

# print(f"The file has {line_list} lines")

if line_list < n:
    print(f" The file has {line_list}")
else:
    for i in range(-n, 0):
        print(lines[i].strip("\n"))