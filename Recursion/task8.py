# A  program that counts the number of vowels in a string recursively
# Prints 0 if string is empty or has one constant

def vowels(s):
    s = s.lower()

    if not s:
        return 0
    elif s[0] in ("a", "e", "i", "o", "u"):
        return 1 + vowels(s[1:])
    else:
        return vowels(s[1:])
    
print(vowels("The quick brown fox"))