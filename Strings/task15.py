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
print(repearted_char) # print the repeated characters but as elements of a list

if len(repearted_char) > 0:
    for char in sorted (repearted_char): # returns  sorted  
        print(char, end=' ')
else:
    print("None")


print("\n")


# E2
print("Example 2")
st = "goodieevening"

r_count = 0
r_char = []

for s in st:
    if (st.count(s) > 1) and (s not in r_char):
        r_count += 1
        r_char.append(s)
print(r_count)
print(r_char)

if len(r_char) > 0:
    for x in sorted (r_char):
        print(x, end=" ")
else:
    print("None")

print("\n")
#Method 2
print("Method 2:")

nstr = "bonsoirmademoiselle"

ct = 0
ch = []

for s in nstr:
    if (nstr.count(s) > 1) and (nstr not in ch):
        ct += 1
        ch.append(s)
print(ct)
print(ch)

if ch: #checks the list and returns true if not empty and false if empty
    print(*sorted(ch), sep=" ") # the asterics delists the items in the list and sorts them alphabetically
else:
    print("None")


print("\n")
#Method 3: We remove the variable to count the repeated characters
print("Method 3:")

strng = "hollaamego"
r_ch = []

for s in strng:
    if (strng.count(s) > 1) and (s not in r_ch):
        r_ch.append(s)
print(r_ch)

if r_ch:
    print(*sorted(r_ch), sep = " ")
else:
    print("None")
