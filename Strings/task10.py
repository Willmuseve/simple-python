# A python script that checks if the string contains all the letters of the alphabet
# Letters should be case insensitive
# If it contain all letters it retursn true else it returns false

import string
from string import ascii_lowercase

s = "The quick brown fox jumps over the lazy dog"
SPACE = " "
is_pangram = True

# set_string = set(s.lower())
# if SPACE in s:
#     set_string.remove(" ")
# print(set_string == set(string.ascii_lowercase))


for i in string.ascii_lowercase:
    if i not in s.lower():
        is_pangram = False
        break
print(is_pangram)