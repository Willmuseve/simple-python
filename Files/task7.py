# A program that counts the number of characters in a file inc commas and quotes
# Doesn't count spaces and new line characters

file_path = "../file/file8.txt"

character_count = 0

with open(file_path) as file:
    for line in file:
        character_count += len(line.replace(" ", "").strip("\n"))