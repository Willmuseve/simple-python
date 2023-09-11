# A python program thatchecks if the string s starts with a sequence of characters denoted by the variable prefix
# If it does print True Else print False
# Case sensitive
# If the length of the prefix is greater than the string then print False

# Method 1 string slicing

s = "Helloworld"
prefix = "Hello"
print(s[:len(prefix)] == prefix)
# Returns true

s = "Hello"
prefix = "Helloworld"
print(s[:len(prefix)] == prefix)
# Returns false


# Method 2 Builtin method startswith
s = "Helloworld"
prefix = "Hello"

print(s.startswith(prefix))
#Returns  true

s = "world"
prefix = "Hello"

print(s.startswith(prefix))
#Returns false

