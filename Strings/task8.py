# A python program that prints the string s with the character curr_char replaced by the character new_char
# curr_char and new_char are  strings that contain single characters
# Assume new chas isnt an empty string
# If no match is found print the empty string

# s =  "wubba"
# new_string = ""

# curr_char = "w"
# new_char = "l"

# for char in s:
#     if char == curr_char:
#         new_string += new_char
#     else:
#         new_string += char
# print(new_string)



# A built in method replace cab be used to replace the strings

s =  "wubba"
curr_char = "w"
new_char = "L"

print(s.replace(curr_char, new_char))