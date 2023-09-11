# A python program that counts the number of repeated characters in a string
# the program also prints a message displayin the repeated characters sorted alphabetically and separated by space
# If there are no repeated characters, print 0 as the total and none on the next line

# Method 1
print("Method 1")

s = "Helloohho" # initialize the string

repearted_count = 0 # a variable to count the number of characters that are repeated
repearted_char = [] # a list that stores the repearted characters

for char in s: # using a for loop to loop through every character in the string
    if (s.count(char) > 1) and (char not in repearted_char): # the count method is used to determine if the char appears more
        #than once in string s and if that character is not in the list repearted_char then count will be increased by one
        # and the character will be added to the list
        repearted_count += 1
        repearted_char.append(char)
print(repearted_count)

if len(repearted_char) > 0:
    for char in sorted (repearted_char):
        print(char, end=' ')
else:
    print("None")