# A python program that returns a copy of the string s without any spaces

s = "python is almost as good as c"
new_string = ""
SPACE = " "

# for i in s:
#     if i != " ":
#         new_string += i
# print(new_string)

print(s.replace(" ", ""))