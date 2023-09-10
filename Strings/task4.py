# A python program that prints the first and the last three characters of a string
# If the atring has less than 6 characters it returns an empty strings

s = "Hellowor"

if len(s) < 10:
    print("")
else:
    new_string = s[:3] + s[len(s) -3:]
    print(new_string)