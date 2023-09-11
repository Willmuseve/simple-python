# A python program that converts a string s to lower case, sort the lowercase in an alpha numerical order and print the resulting string
# The string contins letters and spaces to separate the words
# The final strng must hve original spaces

st = "Hello World" # initialize the list
new_st = ""

st_list = st.split(" ") # split the string into a list where there is space
print(st_list)
for s in st_list: # loop through the list created above
    lower_case = s.lower() #converting to lower
    sorted_c = "".join(sorted(lower_case)) #sortin the letters using join method to a string
    new_st += sorted_c + " " # adding the new list to new_st with a space as a separator

new_st = new_st.rstrip()
print(new_st) 


#Method 2
print("\n")
print("Method 2:")

st_r = "Hello Again World"
new_l = ""

n_list = st_r.split(" ")

for s in n_list:
    new_l += "".join(sorted(s.lower())) + " "
print(new_l)