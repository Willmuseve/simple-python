# A program tht finds and created a frequency dictionary of words in a text file
# The words are the keys and the frequencies are the values


file_path = "../file/file6.txt"

words_dictionary = {}

with open(file_path) as file:
    for word in file:
        word = word.strip("\n")
        if word not in words_dictionary:
            words_dictionary[word] = 1
        else:
            words_dictionary[word] += 1

print(words_dictionary)