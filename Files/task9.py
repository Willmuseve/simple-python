# A program that checks if a file exists 
# If file eixst print the file (file name) exists esle
# print the file(file name) doesn't exist

import os.path

my_file = "../file/file8.txt"

if os.path.isfile(my_file):
    print(f"The file{my_file} exits")
else:
    print(f"The file {my_file} doesn't exist")