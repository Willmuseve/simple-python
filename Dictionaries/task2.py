# A python program that adds a new key-value pair to a dictionary only of it doesnt exist


months = {"January" : 1, "February" : 2, "March" : 3, "April" : 4} # initialize the dictionary

new_key = "May" 
new_value = "5"
 
if new_key not in months: # check if the new key and value is in the dictionary if not add it to the dict
    months[new_key] = new_value
print(months)