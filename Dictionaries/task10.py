# A python program that creates and displays a dictionary that maps each letter in a string to the number of
# times it occured in the string
# case insensitive
# the dictinary has letters only

s = "Hello world"  # Initialize the string
MyDict = {} #empty dictionary to add the char string

for char in s.lower():          #convert the characters to lower case
    if char.isalpha():          #remove special characters like comma, and space etc only remain with letters
        if char in MyDict:      #add the character to the dictionary as a key and it's frequency as value
            MyDict[char] += 1
        else:
            MyDict[char] = 1

print(MyDict) 