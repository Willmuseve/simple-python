# A python progtam that prints a string s withount character n
# If string n is out of range or s is empty it will print s 

s = "HelloWorld"
n = 0

if (len(s) == 0) or (n >= len(s)):
    print(s)
else:
    new_String = ""
    for i in range(len(s)):
        if i != n:
            new_String += s[i]
    print(new_String) 