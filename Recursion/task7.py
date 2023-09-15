# A program that checks if a string is a palindrome 
# Case insensitive
# prints true if is a palindrome, else false

def palindrome(s):
    s = s.lower()

    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])
    
print(palindrome("hola"))