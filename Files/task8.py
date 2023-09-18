# A program that copies the contents of a file to another file
# if the file doesnt exist it reates one

file_path = "../file/file8.txt"
copy_path = "../file/file8copy.txt"


with open(file_path) as file, open(copy_path, "w") as copy:
    for line in file:
        copy.write(line)

