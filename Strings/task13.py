# A python program thatr checks if the string s ends with a specific sequence denoted by the variable suffix
# If it does it prints True Else it prints false
# Case sensitive
# If the length of the suffix is greater than the string print false

# Method 1 string slicing
print("Method 1:")
s = "Helloworld"
suffix = "world"

print(s[-len(suffix):] == suffix)
# Returns true

s = "Helloworld"
suffix = "World"

print(s[-len(suffix):] == suffix)
# Returns false because the suffix contains an uppercase letter not in the s string

s = "Helloworld"
suffix = "planet"

print(s[-len(suffix):] == suffix)
# Returns false because there is no match

print('\n')

# Method 2 using a builtin method --endswith
print("Method 2:")
s = "Helloworld"
suffix = "world"

print(s.endswith(suffix))