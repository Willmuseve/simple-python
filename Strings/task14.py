# A python program that reverses the individual letters in a string and changes their capitalization.
# Uppercase letters should be changed to lower and lower to upper
# String contains letters only and spaces separates the letters 

s = "Hello World"


word_list = s.split(" ")
#splits the string at spaces to form individual words as a list and save to the variable word_list

new_string = ""
# a new list 

for word in word_list: # use a for loop to iterate the different elements of a list to get the reversed version of the word
    reversed_word = "".join(reversed(word)) # the reversed_word variable stores a reversed version of a word in the list 
    swappedCase = reversed_word.swapcase() # the swapcase method swaps the case of the word from uppercase to lower and vice versa
    new_string += swappedCase + " " # the swapped word is added to the new_string variable with " " representing a space after the word

new_string = new_string.rstrip () # returns a copy of the string with trailing whitespaces removed
print(new_string)


st = "Meet me at midnight by Taylor Swift"
new_ss = ""

s_list = st.split(" ")
print(s_list)

for w in s_list:
    reverse_s = "".join(reversed(w))
    sw = reverse_s.swapcase()
    new_ss += sw +" "

new_ss = new_ss.rstrip()
print(new_ss)