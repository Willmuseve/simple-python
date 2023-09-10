# a python script that prints a character at index j in string s
# If the index is out of range, the program should print "j is out of range"
# If the string is empty the program should print "empty string"

s = "HelloWorld"
j = 20

if len(s) == 0:
    print("Empty string")
elif j < len(s):
    print(s[j])
else:
    print("j is out of range") 