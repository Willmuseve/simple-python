# A program that reads a text file and prints the first n lines of the file

file_path = "../file/file3.txt"

n = (int(input("Please enter the number of files: ")))

with open(file_path) as file:
    lines = file.readlines()
    nums = len(lines)

if nums < n:
    print(f"Invalid! The file has {nums} lines.")
else:
    for i in range(n):
        print(lines[i].strip("\n"))