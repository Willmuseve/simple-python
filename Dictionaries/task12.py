# A python program that takes the contents of a dictionay and converts it into a nested list
# The nested list contains the key as the first element and value as the second

person = {
    "Name" : "Allan",
    "Age" : 23,
    "Profession" :[" Designer", "ux", "researcher"]
}
new = []

for key, value in person.items():
    new.append([key, value])
print(new)