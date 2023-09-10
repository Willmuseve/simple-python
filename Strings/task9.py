# A python program that prints a version of a string where all commas are replaced by fullstop

string = "Hello, World"
new_string = ""

fullstop = "."
comma = ","

# for i  in string:
#     if i  == comma:
#         new_string += fullstop
#     else:
#         new_string += i
# print(new_string)

print(string.replace(comma, fullstop))