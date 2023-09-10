# A python program that prints the string s without the characters located at even indices
# If the string is empty or contains one character print it inract

s = "HelloWorld"
new_string = ""

for j in range(len(s)):
    if j % 2 != 0:
        new_string += s[j]
print(new_string)