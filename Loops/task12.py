# A program that prints a string reversed in the same line

strings = "HelloWorld"
strings2 = "Konichiwa"

for char in strings[::-1]:
    print(char, end = ",")

print("")
for char in reversed(strings2):
    print(char, end = " ")